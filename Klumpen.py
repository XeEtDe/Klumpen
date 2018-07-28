import random

print("Lädt...\n")

##Klassen und Karten##
Start_Lebewesen = []
Start_Lebensraum = []
Start_Elemente = []
Nur = [Start_Lebewesen, Start_Elemente]

Alle_Lebewesen = []
Alle_Lebensraum = []
Alle_Elemente = []
Alle_Verteilung = [Alle_Lebewesen, Alle_Lebensraum, Alle_Elemente]

Alle_Start_Karten = [Start_Lebewesen, Start_Lebensraum, Start_Elemente]
Alle_Karten = []

#Alle
class Karten:
    def __init__(self, Name, Beschreibung, Kombi = [], Start = False):
        self.Name = Name
        self.Beschreibung = Beschreibung
        self.Start = Start
        self.Kombi = Kombi #aus denen Karte entstehen kann
        Alle_Karten.append(self)
    
#Lebewesen
class Lebewesen(Karten):
    def __init__(self, Name, Beschreibung, Punkte, Angriff, Verteidigung, Lebensraum, Kombi = [], Start = False):
        Karten.__init__(self, Name, Beschreibung, Kombi, Start)
        self.Punkte = Punkte
        self.Angriff = Angriff
        self.Verteidigung = Verteidigung
        self.Lebensraum = Lebensraum
        if self.Start == True:
            Start_Lebewesen.append(self)
        Alle_Lebewesen.append(self)
        
    #für Punkte
    def __repr__(self):
        CDS = Counter_Dict[Spieler]
        MDS = Magisch_Dict[Spieler]
        SDS = Stärker_Dict[Spieler]
        Mod_Punkte = self.Punkte
        Mod_Lebensraum_ = []
        for LR in self.Lebensraum:
            if not LR == "Wonderland":
                Mod_Lebensraum_.append(LR)
        Mod_Lebensraum = ""
        for LR in Mod_Lebensraum_:
            Mod_Lebensraum = Mod_Lebensraum + LR + ", "
        Mod_Lebensraum = Mod_Lebensraum.strip(", ")
        if self in CDS:
            if CDS[self] == True:
                Verbesserung_Spieler = Verbesserung[Spieler]
                Verbesserung_Karte = Verbesserung_Spieler[self]
                Add_Punkte = Verbesserung_Karte["Punkte"]
                Mod_Punkte = self.Punkte + Add_Punkte
                if Mod_Punkte < 0:
                    Mod_Punkte = 0
                for LR in Verbesserung_Karte["Lebensräume"]:
                    if not LR in Mod_Lebensraum_:
                        Mod_Lebensraum_.append(LR)
                if "Alle" in Mod_Lebensraum_:
                    Mod_Lebensraum = "Alle"
                else:
                    Mod_Lebensraum = ""
                    for LR in Mod_Lebensraum_:
                        Mod_Lebensraum = Mod_Lebensraum + LR + ", "
                    Mod_Lebensraum = Mod_Lebensraum.strip(", ")
                CDS[self] = False
        if self in Magisch_Dict[Spieler]:
            if MDS[self] > 0:
                Mod_Punkte += 1
                MDS[self] -= 1
        if self in Stärker_Dict[Spieler]:
            if SDS[self] > 0:
                Mod_Punkte += 2
                SDS[self] -= 1
        return "{} (Lebewesen):\n{} - Punkte: {} - Lebensräume: {}".format(self.Name, self.Beschreibung, Mod_Punkte, Mod_Lebensraum)

    #für Kampf
    def __str__(self):
        CDS = Counter_Dict[Spieler]
        MDS = Magisch_Dict[Spieler]
        SDS = Stärker_Dict[Spieler]
        Mod_Angriff = self.Angriff
        Mod_Verteidigung = self.Verteidigung
        Mod_Lebensraum_ = []
        for LR in self.Lebensraum:
            if not LR == "Wonderland":
                Mod_Lebensraum_.append(LR)
        Mod_Lebensraum = ""
        for LR in Mod_Lebensraum_:
            Mod_Lebensraum = Mod_Lebensraum + LR + ", "
        Mod_Lebensraum = Mod_Lebensraum.strip(", ")
        if self in CDS:
            if CDS[self] == True:
                Verbesserung_Spieler = Verbesserung[Spieler]
                Verbesserung_Karte = Verbesserung_Spieler[self]
                Add_Angriff = Verbesserung_Karte["Angriff"]
                Mod_Angriff = self.Angriff + Add_Angriff
                if Mod_Angriff < 0:
                    Mod_Angriff = 0
                Add_Verteidigung = Verbesserung_Karte["Verteidigung"]
                Mod_Verteidigung = self.Verteidigung + Add_Verteidigung
                if Mod_Verteidigung < 0:
                    Mod_Verteidigung = 0
                for LR in Verbesserung_Karte["Lebensräume"]:
                    if not LR in Mod_Lebensraum_:
                        Mod_Lebensraum_.append(LR)
                if "Alle" in Mod_Lebensraum_:
                    Mod_Lebensraum = "Alle"
                else:
                    Mod_Lebensraum = ""
                    for LR in Mod_Lebensraum_:
                        Mod_Lebensraum = Mod_Lebensraum + LR + ", "
                    Mod_Lebensraum = Mod_Lebensraum.strip(", ")
                CDS[self] = False
        if self in Magisch_Dict[Spieler]:
            if MDS[self] > 0:
                Mod_Angriff += 1
                Mod_Verteidigung += 1
                MDS[self] -= 1
        if self in Stärker_Dict[Spieler]:
            if SDS[self] > 0:
                Mod_Angriff += 2
                Mod_Verteidigung += 2
                SDS[self] -= 1
        return "{} (Lebewesen):\n{} - Angriff: {} - Verteidigung: {} - Lebensräume: {}".format(self.Name, self.Beschreibung, Mod_Angriff, Mod_Verteidigung, Mod_Lebensraum)

#Vordruck
# = Lebewesen("", "", P, A, V, ["L"], ["K"])

#Gummikrieger
Gummikrieger = Lebewesen("Gummikrieger", "Einst zum Schutz der königlichen Familie erschaffen, lebt nun aber frei in den Wäldern von Klumpiland", 5, 5, 5, ["Wald"], [], True)
# -> Stufe 1 -> +1
Roter_Gummikrieger = Lebewesen("Roter Gummikrieger", "Agressiver Krieger aus Gummi", 6, 7, 5, ["Wald", "Wüste"], ["Gummikrieger+Feuer"])
Blauer_Gummikrieger = Lebewesen("Blauer Gummikrieger", "Ausgeglichener Krieger mit balancierten Fähigkeiten", 6, 6, 6, ["Wald", "See"], ["Gummikrieger+Wasser"])
Weißer_Gummikrieger = Lebewesen("Weißer Gummikrieger", "Ausgeglichener Krieger mit balancierten Fähigkeiten", 6, 6, 6, ["Wald", "Berge"], ["Gummikrieger+Luft"])
Brauner_Gummikrieger = Lebewesen("Brauner Gummikrieger", "Krieger mit guten Abwehrfähigkeiten; stärker im Lebensraum Wald", 6, 5, 7, ["Wald"], ["Gummikrieger+Erde"])
Goldener_Gummikrieger = Lebewesen("Goldener Gummikrieger", "Krieger mit vergoldeter Oberfläche, überall überlebensfähig", 6, 6, 6, ["Alle"], ["Gummikrieger+Magie"])
# -> Stufe 2 -> +3
Wolkenkrieger = Lebewesen("Wolkenkrieger", "Flauschig wie eine Wolke", 8, 6, 10, ["Wald", "Berge"], ["Gummikrieger+Wölkchen"])
Gummibärchenkrieger = Lebewesen("Gummibärchenkrieger", "Verwirrt seine Gegner mit Duftstoffen", 8, 8, 8, ["Wald", "See"], ["Gummikrieger+Beere"])
Skelettkrieger = Lebewesen("Skelettkrieger", "Ist absolut furchtlos, da er bereits tot ist", 8, 10, 6, ["Wald", "Wüste"], ["Gummikrieger+Staub", "Gummikrieger+Asche"])
Weiser_Krieger = Lebewesen("Weiser Krieger", "Ist so alt wie die Zeit selbst", 8, 8, 8, ["Alle"], ["Gummikrieger+Zeit"])
# -> Stufe 3 -> +5
Bunter_Krieger = Lebewesen("Bunter Krieger", "Wäre lieber ein friedlicher Dorfbewohner; stärker im Lebensraum Wald", 10, 5, 15, ["Wald", "Berge"], ["Gummikrieger+Pusteblume", "Gummikrieger+Pfingstrose"])
Schimmernder_Krieger = Lebewesen("Schimmernder Krieger", "Umhüllt von einer mysteriösen glitzernden Schicht", 10, 10, 10, ["Wald", "See"], ["Gummikrieger+Perle"])
Marsianer = Lebewesen("Marsianer", "Ein Krieger vom Mars", 10, 10, 10, ["Wald", "Wüste"], ["Gummikrieger+Sternenstaub"])
Kristallkrieger = Lebewesen("Kristallkrieger", "So wunderschön wie ein Diamand", 10, 15, 5, ["Wald", "See"], ["Gummikrieger+Kristall"])
Böser_Krieger = Lebewesen("Böser Krieger", "Hat sein Herz in einem Kampf verloren", 10, 12, 8, ["Alle"], ["Gummikrieger+Dunkle Macht"])
# -> Stufe 4 -> +7
Ätzender_Krieger = Lebewesen("Ätzender Krieger", "Ist von einer giftigen Schleimschicht umgeben", 12, 12, 12, ["Wald", "See"], ["Gummikrieger+Schleim"])
Eiskrieger = Lebewesen("Eiskrieger", "Kämpft fast ohne Emotionen", 12, 12, 12, ["Wald", "Berge"], ["Gummikrieger+Eis"])
Mutiger_Krieger = Lebewesen("Mutiger Krieger", "Ehrenhaft und tapfer", 12, 14, 10, ["Wald", "Wüste"], ["Gummikrieger+Blut"])
Lichtkrieger = Lebewesen("Lichtkrieger", "Setzt die Energie von Blitzen gegen seine Gegner ein", 12, 12, 12, ["Wald", "Berge", "Wüste"], ["Gummikrieger+Blitz"])
Gütiger_Krieger = Lebewesen("Gütiger Krieger", "Ermöglicht dir 3 Extrazüge pro Runde, wenn er auf dem Feld platziert ist", 12, 4, 20, ["Alle"], ["Gummikrieger+Regenbogen", "Gummikrieger+Engelshaar", "Gummikrieger+Stein von Elyaris"])

#Starker Krieger -> Gummikrieger + Gummikrieger
Starker_Krieger = Lebewesen("Starker Krieger", "Ein guter und robuster Kämpfer", 10, 10, 10, ["Wald"], ["Gummikrieger+Gummikrieger"])
# -> Stufe 1 -> +1
Starker_Roter_Krieger = Lebewesen("Starker Roter Krieger", "Agressiver Krieger aus Gummi", 11, 13, 9, ["Wald", "Wüste"], ["Starker Krieger+Feuer"])
Starker_Blauer_Krieger = Lebewesen("Starker Blauer Krieger", "Ausgeglichener Krieger mit balancierten Fähigkeiten", 11, 11, 11, ["Wald", "See"], ["Starker Krieger+Wasser"])
Starker_Weißer_Krieger = Lebewesen("Starker Weißer Krieger", "Ausgeglichener Krieger mit balancierten Fähigkeiten", 11, 11, 11, ["Wald", "Berge"], ["Starker Krieger+Luft"])
Starker_Brauner_Krieger = Lebewesen("Starker Brauner Krieger", "Krieger mit guten Abwehrfähigkeiten; stärker im Lebensraum Wald", 11, 9, 13, ["Wald"], ["Starker Krieger+Erde"])
Starker_Goldener_Krieger = Lebewesen("Starker Goldener Gummikrieger", "Krieger mit vergoldeter Oberfläche, überall überlebensfähig", 11, 11, 11, ["Alle"], ["Starker Krieger+Magie"])
# -> Stufe 2 -> +3
Starker_Wolkenkrieger = Lebewesen("Starker Wolkenkrieger", "Flauschig wie eine Wolke", 13, 11, 15, ["Wald", "Berge"], ["Starker Krieger+Wölkchen"])
Starker_Gummibärchenkrieger = Lebewesen("Starker Gummibärchenkrieger", "Verwirrt seine Gegner mit Duftstoffen", 13, 13, 13, ["Wald", "See"], ["Starker Krieger+Beere"])
Starker_Skelettkrieger = Lebewesen("Starker Skelettkrieger", "Ist absolut furchtlos, da er bereits tot ist", 13, 15, 11, ["Wald", "Wüste"], ["Starker Krieger+Staub", "Starker Krieger+Asche"])
Starker_Weiser_Krieger = Lebewesen("Starker Weiser Krieger", "Ist so alt wie die Zeit selbst", 13, 13, 13, ["Alle"], ["Starker Krieger+Zeit"])
# -> Stufe 3 -> +5
Starker_Bunter_Krieger = Lebewesen("Starker Bunter Krieger", "Wäre lieber ein friedlicher Dorfbewohner; stärker im Lebensraum Wald", 15, 10, 20, ["Wald", "Berge"], ["Starker Krieger+Pusteblume", "Starker Krieger+Pfingstrose"])
Starker_Schimmernder_Krieger = Lebewesen("Starker Schimmernder Krieger", "Umhüllt von einer mysteriösen glitzernden Schicht", 15, 15, 15, ["Wald", "See"], ["Starker Krieger+Perle"])
Starker_Marsianer = Lebewesen("Starker Marsianer", "Ein Krieger vom Mars", 15, 15, 15, ["Wald", "Wüste"], ["Starker Krieger+Sternenstaub"])
Starker_Kristallkrieger = Lebewesen("Starker Kristallkrieger", "So wunderschön wie ein Diamand", 15, 20, 10, ["Wald", "See"], ["Starker Krieger+Kristall"])
Starker_Böser_Krieger = Lebewesen("Starker Böser Krieger", "Hat sein Herz in einem Kampf verloren", 15, 18, 12, ["Alle"], ["Starker Krieger+Dunkle Macht"])
# -> Stufe 4 -> +7
Starker_Ätzender_Krieger = Lebewesen("Starker Ätzender Krieger", "Ist von einer giftigen Schleimschicht umgeben", 17, 17, 17, ["Wald", "See"], ["Starker Krieger+Schleim"])
Starker_Eiskrieger = Lebewesen("Starker Eiskrieger", "Kämpft fast ohne Emotionen", 17, 17, 17, ["Wald", "Berge"], ["Starker Krieger+Eis"])
Starker_Mutiger_Krieger = Lebewesen("Starker Mutiger Krieger", "Ehrenhaft und tapfer", 17, 21, 13, ["Wald", "Wüste"], ["Starker Krieger+Blut"])
Starker_Lichtkrieger = Lebewesen("Starker Lichtkrieger", "Setzt die Energie von Blitzen gegen seine Gegner ein", 17, 17, 17, ["Wald", "Berge", "Wüste"], ["Starker Krieger+Blitz"])
Starker_Gütiger_Krieger = Lebewesen("Starker Gütiger Krieger", "Ermöglicht dir 5 Extrazüge pro Runde, wenn er auf dem Feld platziert ist", 17, 7, 27, ["Alle"], ["Starker Krieger+Regenbogen", "Starker Krieger+Engelshaar", "Starker Krieger+Stein von Elyaris"])

#Klumpi ###
Klumpi = Lebewesen("Klumpi", "Ein sehr anpassungsfähiges Lebewesen mit viel Potential zur Weiterentwicklung", 1, 1, 1, ["Alle"], [], True)
# -> Doppel ###
# -> Stufe 1 -> +1 #Feuer, Wasser, Luft#
Gräberling = Lebewesen("Gräberling", "Ein selten gesehenes Lebewesen, das unterirdisch weit verzweigte Tunnelsysteme gräbt; gibt dir eine weitere Elementkarte pro Runde, wenn er auf dem Feld platziert ist", 2, 2, 2, ["Wald"], ["Klumpi+Erde"])

Zauberer = Lebewesen("Zauberer", "Verwandelt Elemente in Zaubertränke (muss dazu auf dem Feld platziert sein)", 2, 2, 2, ["Alle"], ["Klumpi+Magie"])
# -> Stufe 2 -> +3
Koi = Lebewesen("Koi", "Eine chinesische Zuchtform des Karpfen, die sich der Legende nach in einen Drachen verwandeln kann; produziert jede Runde ein Element, das Lebensräume vergrößern oder Lebewesen verbessern kann", 4, 2, 6, ["See"], ["Klumpi+Wölkchen", "Klumpi+Beere"])
Parasit = Lebewesen("Parasit", "Kann einmal im Spiel die Werte eines beliebigen anderen Lebewesens aufnehmen. Dessen Werte werden dabei um 4 verringert (muss dazu auf dem Feld platziert sein)", 4, 4, 4, ["Alle"], ["Klumpi+Asche", "Klumpi+Staub"])
Sphinx = Lebewesen("Sphinx", "\"So, als wären sie jeden Augenblick im Begriff zu verschwinden, und würden gleichzeitig aus sich selbst heraus neu erschaffen\"; gibt dir pro Runde einen Extrazug, wenn sie auf dem Feld platziert ist", 4, 4, 4, ["Wüste"], ["Klumpi+Zeit"])
# -> Stufe 3 -> +5 #Pusteblume#
Sea_People = Lebewesen("Sea People", "Sind Teil der Wellen des Meeres und weisen Schiffen den Weg; können pro Runde die Werte eines Lebewesens um 3 erhöhen (müssen dazu auf dem Feld platziert sein)", 6, 5, 7, ["See"], ["Klumpi+Perle"])
Dunkler_Magier = Lebewesen("Dunkler Magier", "Stellt aus Elementen Gifte her, die du auf andere Spieler anwenden kannst (muss dazu auf dem Feld platziert sein)", 6, 6, 6, ["Alle"], ["Klumpi+Dunkle Macht"])
Marienkäfer = Lebewesen("Marienkäfer", "Bei der Zugreihenfolge des Auswahlstapels bist du vor den anderen Spielern an der Reihe, solange der Käfer auf dem Feld platziert ist", 6, 1, 11, ["Alle"], ["Klumpi+Pfingstrose"])
Joker = Lebewesen("Joker", "Kann dir einmal pro Runde eine Startkarte geben, bei der du entscheidest ob sie ein Element, Lebewesen oder Lebensraum sein soll, wenn er auf dem Feld platziert ist (dazu: Joker + gewünschte Kartenart)", 6, 6, 6, ["Alle"], ["Klumpi+Sternenstaub", "Klumpi+Kristall"])
# -> Stufe 4 -> +7 #Schleim, Eis, Blut, Blitz, Regenbogen, Engelshaar, Stein von Elyaris#

#Drachen
Drachenei = Lebewesen("Drachenei", "Benötigt einen Zug zum Schlüpfen, nachdem es im Lebensraum platziert wurde", 0, 0, 0, ["Berge"], [], True)
Drache = Lebewesen("Drache", "Ein starkes, geschupptes und flugfähiges Lebewesen", 8, 8, 8, ["Berge"], ["Koi+Koi"])
# -> Stufe 1 -> +1
Feuerdrache = Lebewesen("Feuerdrache", "Liebt Hitze über alles und bekämpft seine Feinde mit Feueratem", 9, 11, 7, ["Berge", "Wüste"], ["Drache+Feuer"])
Wasserdrache = Lebewesen("Wasserdrache", "Fühlt sich in feuchten Gebieten wohl, kann durch Kiemen sogar unter Wasser leben", 9, 9, 9, ["Berge", "See"], ["Drache+Wasser"])
Luftdrache = Lebewesen("Luftdrache", "Fühlt sich in luftigen Höhen wohl; stärker im Lebensraum Berge", 9, 9, 9, ["Berge"], ["Drache+Luft"])
Erddrache = Lebewesen("Erddrache", "Ein kleiner Drache, der lieber am Boden als in der Luft lebt", 9, 7, 11, ["Berge", "Wald"], ["Drache+Erde"])
Magiedrache = Lebewesen("Magiedrache", "Hat goldene Schuppen und magische Anpassungsfähigkeiten", 9, 9, 9, ["Alle"], ["Drache+Magie"])
# -> Stufe 2 -> +3
Wolkendrache = Lebewesen("Wolkendrache", "Dieser Drache lebt hoch über den Wolken; stärker im Lebensraum Berge", 11, 11, 11, ["Berge", "Wüste"], ["Drache+Wölkchen"])
Chamäleondrache = Lebewesen("Chamäleondrache", "Passt sich perfekt an seine Umgebung an", 11, 6, 16, ["Alle"], ["Drache+Beere", "Drache+Staub"])
Schattendrache = Lebewesen("Schattendrache", "Ist schwarz wie die Nacht und hat die Fähigkeit Energiebälle abzufeuern", 11, 16, 6, ["Berge", "See", "Wald"], ["Drache+Asche"])
Urdrache = Lebewesen("Urdrache", "Diese sehr ursprüngliche und alte Drachenart war wahrscheinlich die Erste, die sich in Klumpiland entwickelte", 11, 11, 11, ["Alle"], ["Drache+Zeit"])
# -> Stufe 3 -> +5
Wächterdrache = Lebewesen("Wächterdrache", "Wacht über einen riesigen Schatz in einer abgelegenen Höhle", 13, 16, 10, ["Berge"], ["Drache+Perle", "Drache+Kristall"])
Traumdrache = Lebewesen("Traumdrache", "Gibt dir pro Runde eine weitere zufällige Startkarte, wenn er auf dem Feld platziert ist", 13, 10, 16, ["Berge", "See"], ["Drache+Pusteblume", "Drache+Sternenstaub"])
Schreckensdrache = Lebewesen("Schreckensdrache", "Nachtschwarze Schuppen, blutverschmiertes Maul mit langen Zähnen und böse glühende Augen", 13, 20, 6, ["Berge", "Wüste", "See"], ["Drache+Dunkle Macht"])
Liebesdrache = Lebewesen("Liebesdrache", "Ein rotes, vor allem im Frühling gesehenes Tier, das im Gegensatz zu anderen Drachenarten meist in Rudeln lebt", 13, 8, 18, ["Berge", "See", "Wald"], ["Drache+Pfingstrose"])
# -> Stufe 4 -> +7
Temeraire = Lebewesen("Temeraire", "Ein äußerst seltener Himmelsdrache, der ursprünglich als Geschenk an Napoleon gedacht war, aber eine andere Bestimmung fand", 15, 18, 12, ["Berge"], ["Drache+Engelshaar", "Drache+Stein von Elyaris"])
Fuchur = Lebewesen("Fuchur", "\"Glücksdrachen dagegen sind Geschöpfe der Luft und der Wärme, Geschöpfe unbändiger Freude und trotz ihrer gewaltigen Körpergröße so leicht wie eine Sommerwolke\"", 15, 15, 15, ["Alle"], ["Drache+Regenbogen"])
Furchtdrache = Lebewesen("Furchtdrache", "Sein eisiges Feuer versteinert seine Gegener; kann pro Runde einmal einen Spieler einen Zug aussetzen lassen, wenn er auf dem Feld platziert ist (dazu: Furchtdrache + gewählter Spieler)", 15, 15, 15, ["Alle"], ["Drache+Blitz", "Drache+Eis"])
Glibberdrache = Lebewesen("Glibberdrache", "Verändert ständig seine Form und kann auch durch kleinste Öffnungen gelangen", 15, 12, 18, ["See", "Berge", "Wald"], ["Drache+Schleim", "Drache+Blut"])

#Starker Drache -> Drache + Drache
Starker_Drache = Lebewesen("Starker Drache", "Eines der stärksten Lebewesen in Klumpiland", 16, 16, 16, ["Berge"], ["Drache+Drache"])
# -> Stufe 1 -> +1
Starker_Feuerdrache = Lebewesen("Starker Feuerdrache", "Liebt Hitze über alles und bekämpft seine Feinde mit Feueratem", 17, 20, 14, ["Berge", "Wüste"], ["Starker Drache+Feuer"])
Starker_Wasserdrache = Lebewesen("Starker Wasserdrache", "Fühlt sich in feuchten Gebieten wohl, kann durch Kiemen sogar unter Wasser leben", 17, 17, 17, ["Berge", "See"], ["Starker Drache+Wasser"])
Starker_Luftdrache = Lebewesen("Starker Luftdrache", "Fühlt sich in luftigen Höhen wohl; stärker im Lebensraum Berge", 17, 17, 17, ["Berge"], ["Starker Drache+Luft"])
Starker_Erddrache = Lebewesen("Starker Erddrache", "Ein kleiner Drache, der lieber am Boden als in der Luft lebt", 17, 14, 20, ["Berge", "Wald"], ["Starker Drache+Erde"])
Starker_Magiedrache = Lebewesen("Starker Magiedrache", "Hat goldene Schuppen und magische Anpassungsfähigkeiten", 17, 17, 17, ["Alle"], ["Starker Drache+Magie"])
# -> Stufe 2 -> +3
Starker_Wolkendrache = Lebewesen("Starker Wolkendrache", "Dieser Drache lebt hoch über den Wolken; stärker im Lebensraum Berge", 19, 19, 19, ["Berge", "Wüste"], ["Starker Drache+Wölkchen"])
Starker_Chamäleondrache = Lebewesen("Starker Chamäleondrache", "Passt sich perfekt an seine Umgebung an", 19, 19, 19, ["Alle"], ["Starker Drache+Beere", "Starker Drache+Staub"])
Starker_Schattendrache = Lebewesen("Starker Schattendrache", "Ist schwarz wie die Nacht und hat die Fähigkeit Energiebälle abzufeuern", 19, 29, 9, ["Berge", "See", "Wald"], ["Starker Drache+Asche"])
Starker_Urdrache = Lebewesen("Starker Urdrache", "Diese sehr ursprüngliche und alte Drachenart war wahrscheinlich die Erste, die sich in Klumpiland entwickelte", 19, 19, 19, ["Alle"], ["Starker Drache+Zeit"])
# -> Stufe 3 -> +5
Starker_Wächterdrache = Lebewesen("Starker Wächterdrache", "Wacht über einen riesigen Schatz in einer abgelegenen Höhle", 21, 27, 15, ["Berge"], ["Starker Drache+Perle", "Starker Drache+Kristall"])
Starker_Traumdrache = Lebewesen("Starker Traumdrache", "Gibt dir pro Runde eine zufällige Karte, die keine Startkarte sein muss, wenn er auf dem Feld platziert ist", 21, 15, 27, ["Berge", "See"], ["Starker Drache+Pusteblume", "Starker Drache+Sternenstaub"])
Starker_Schreckensdrache = Lebewesen("Starker Schreckensdrache", "Nachtschwarze Schuppen, blutverschmiertes Maul mit langen Zähnen und böse glühende Augen", 21, 29, 13, ["Berge", "Wüste", "See"], ["Starker Drache+Dunkle Macht"])
Starker_Liebesdrache = Lebewesen("Starker Liebesdrache", "Ein rotes, vor allem im Frühling gesehenes Tier, das im Gegensatz zu anderen Drachenarten meist in Rudeln lebt", 21, 13, 29, ["Berge", "See", "Wald"], ["Starker Drache+Pfingstrose"])
# -> Stufe 4 -> +7
Starker_Himmelsdrache = Lebewesen("Starker Himmelsdrache", "Ein äußerst seltenes Tier, das in fernen Ländern gezüchtet wurde", 23, 31, 15, ["Berge"], ["Starker Drache+Engelshaar", "Starker Drache+Stein von Elyaris"])
Starker_Glücksdrache = Lebewesen("Starker Glücksdrache", "\"Glücksdrachen dagegen sind Geschöpfe der Luft und der Wärme, Geschöpfe unbändiger Freude und trotz ihrer gewaltigen Körpergröße so leicht wie eine Sommerwolke\"", 23, 23, 23, ["Alle"], ["Starker Drache+Regenbogen"])
Starker_Furchtdrache = Lebewesen("Starker Furchtdrache", "Sein eisiges Feuer versteinert seine Gegener; kann pro Runde einmal einen Spieler 3 Züge aussetzen lassen, wenn er auf dem Feld platziert ist (dazu: Starker Furchtdrache + gewählter Spieler)", 23, 23, 23, ["Alle"], ["Starker Drache+Blitz", "Starker Drache+Eis"])
Starker_Glibberdrache = Lebewesen("Starker Glibberdrache", "Verändert ständig seine Form und kann auch durch kleinste Öffnungen gelangen", 23, 15, 31, ["See", "Berge", "Wald"], ["Starker Drache+Schleim", "Starker Drache+Blut"])

#Zottel
Zottel = Lebewesen("Zottel", "Ein haariges Wesen mit großen Augen", 3, 3, 3, ["Berge", "Wald"], [], True)
# -> Stufe 1 -> +1
Feuriger_Zottel = Lebewesen("Feuriger Zottel", "Kann bei Gefahr sein Fell entzünden; stärker im Lebensraum Wüste", 4, 5, 3, ["Berge", "Wald", "Wüste"], ["Zottel+Feuer"])
Nasser_Zottel = Lebewesen("Nasser Zottel", "Schützt sich durch nasses Fell; stärker im Lebensraum See", 4, 3, 5, ["Berge", "Wald", "See"], ["Zottel+Wasser"])
Schwebender_Zottel = Lebewesen("Schwebender Zottel", "Kann durch Druckveränderung in seinem Inneren ohne Flügel fliegen; stärker im Lebensraum Berge", 4, 4, 4, ["Berge", "Wald", "See"], ["Zottel+Luft"])
Dreckiger_Zottel = Lebewesen("Dreckiger Zottel", "Lebt meistens in unterirdischen Gängen; stärker im Lebensraum Wald", 4, 4, 4, ["Berge", "Wald", "Wüste"], ["Zottel+Erde"])
Goldener_Zottel = Lebewesen("Goldener Zottel", "Offenbart nur wenigen Beobachtern seine wahre Fellfarbe", 4, 4, 4, ["Alle"], ["Zottel+Magie"])
# -> Stufe 2 -> +3
Flauschiger_Zottel = Lebewesen("Flauschiger Zottel", "Fell so weich wie die Wolken", 6, 2, 10, ["Alle"], ["Zottel+Wölkchen"])
Gefärbter_Zottel = Lebewesen("Gefärbter Zottel", "Schreckt seine Gegner durch die dunkle Fellfarbe ab", 6, 6, 6, ["Alle"], ["Zottel+Beere", "Zottel+Asche"])
Stachliger_Zottel = Lebewesen("Stachliger Zottel", "Sein Fell ist so trocken, dass es wie Stacheln wirkt; stärker im Lebensraum Wüste", 6, 10, 2, ["Alle"], ["Zottel+Staub", "Zottel+Zeit"])
# -> Stufe 3 -> +5
Funkelnder_Zottel = Lebewesen("Funkelnder Zottel", "Hat magische Diamanten in seinem Fell seit er den Prinzen von Klumpiland gerettet hat", 8, 8, 8, ["Alle"], ["Zottel+Kristall", "Zottel+Sternenstaub"])
Böser_Zottel = Lebewesen("Böser Zottel", "Der Begleiter des dunkeln Magiers", 8, 12, 4, ["Alle"], ["Zottel+Dunkle Macht"])
Heller_Zottel = Lebewesen("Heller Zottel", "Fell so sanft wie der Mond und Augen so glitzernd wie Sterne; stärker im Lebensraum See", 8, 4, 12, ["Alle"], ["Zottel+Perle", "Zottel+Pusteblume"])
Eigenwilliger_Zottel = Lebewesen("Eigenwilliger Zottel", "Im Gegensatz zu den meisten andere Zotteln sehr abweisend", 8, 8, 8, ["Alle"], ["Zottel+Pfingstrose"])
# -> Stufe 4 -> +7
Schleimiger_Zottel = Lebewesen("Schleimiger Zottel", "Sondert bei Gefahr ätzenden Schleim ab", 10, 11, 9, ["Alle"], ["Zottel+Schleim"])
Rubinzottel = Lebewesen("Rubinzottel", "Aus der Ferne gleicht er wegen seines leuchtend roten Fells einem Edelstein; stärker im Lebensraum Berge", 10, 8, 12, ["Alle"], ["Zottel+Blut"])
Mystischer_Zottel = Lebewesen("Mystischer Zottel", "Kommt so selten vor, dass man sich nicht sicher ist, ob er überhaupt exestiert; gibt dir eine weitere Startkarte pro Runde, wenn er auf dem Feld platziert ist", 10, 10, 10, ["Alle"], ["Zottel+Stein von Elyaris", "Zottel+Engelshaar"])
Himmelszottel = Lebewesen("Himmelszottel", "Kann pro Runde die Werte eines Lebewesens um 3 erhöhen (muss dazu auf dem Feld platziert sein)", 10, 10, 10, ["Alle"], ["Zottel+Eis", "Zottel+Regenbogen", "Zottel+Blitz"])

#Doppelzottel -> Zottel + Zottel
Doppelzottel = Lebewesen("Doppelzottel", "Ein untrennbares Paar aus zwei Zotteln", 6, 6, 6, ["Berge", "Wald"], ["Zottel+Zottel"])
# -> Stufe 1 -> +1
Feurige_Doppelzottel = Lebewesen("Feurige Doppelzottel", "Zwei Zottel, die bei Gefahr ihr Fell entzünden; stärker im Lebensraum Wüste", 7, 8, 6, ["Berge", "Wald", "Wüste"], ["Doppelzottel+Feuer"])
Nasse_Doppelzottel = Lebewesen("Nasse Doppelzottel", "Zwei Zottel, die sich durch nasses Fell schützen; stärker im Lebensraum See", 7, 6, 8, ["Berge", "Wald", "See"], ["Doppelzottel+Wasser"])
Schwebende_Doppelzottel = Lebewesen("Schwebende Doppelzottel", "Zwei Zottel, die durch Druckveränderung in ihrem Inneren ohne Flügel fliegen können; stärker im Lebensraum Berge", 7, 7, 7, ["Berge", "Wald", "See"], ["Doppelzottel+Luft"])
Dreckige_Doppelzottel = Lebewesen("Dreckige Doppelzottel", "Zwei Zottel, die meistens in unterirdischen Gängen leben; stärker im Lebensraum Wald", 7, 7, 7, ["Berge", "Wald", "Wüste"], ["Doppelzottel+Erde"])
Goldene_Doppelzottel = Lebewesen("Goldene Doppelzottel", "Zwei Zottel, die nur wenigen Beobachtern ihre wahre Fellfarbe offenbaren", 7, 7, 7, ["Alle"], ["Doppelzottel+Magie"])
# -> Stufe 2 -> +3
Flauschige_Doppelzottel = Lebewesen("Flauschige Doppelzottel", "Zwei Zottel mit Fell so weich wie die Wolken", 9, 3, 15, ["Alle"], ["Doppelzottel+Wölkchen"])
Gefärbte_Doppelzottel = Lebewesen("Gefärbte Doppelzottel", "Zwei Zottel, die ihre Gegner durch die dunkle Fellfarbe abschrecken", 9, 9, 9, ["Alle"], ["Doppelzottel+Beere", "Doppelzottel+Asche"])
Stachlige_Doppelzottel = Lebewesen("Stachlige Doppelzottel", "Zwei Zottel, deren Fell so trocken ist, dass es wie Stacheln wirkt; stärker im Lebensraum Wüste", 9, 15, 3, ["Alle"], ["Doppelzottel+Staub", "Doppelzottel+Zeit"])
# -> Stufe 3 -> +5
Funkelnde_Doppelzottel = Lebewesen("Funkelnde Doppelzottel", "Zwei Zottel, die magische Diamanten in ihrem Fell haben", 11, 11, 11, ["Alle"], ["Doppelzottel+Kristall", "Doppelzottel+Sternenstaub"])
Böse_Doppelzottel = Lebewesen("Böse Doppelzottel", "Zwei Zottel, die Begleiter des dunkeln Magiers sind", 11, 16, 6, ["Alle"], ["Doppelzottel+Dunkle Macht"])
Helle_Doppelzottel = Lebewesen("Helle Doppelzottel", "Zwei Zottel mit Fell so sanft wie der Mond und Augen so glitzernd wie Sterne; stärker im Lebensraum See", 11, 6, 16, ["Alle"], ["Doppelzottel+Perle", "Doppelzottel+Pusteblume"])
Eigenwillige_Doppelzottel = Lebewesen("Eigenwillige Doppelzottel", "Zwei Zottel, die im Gegensatz zu den meisten andere Zotteln sehr abweisend sind", 11, 11, 11, ["Alle"], ["Doppelzottel+Pfingstrose"])
# -> Stufe 4 -> +7
Schleimige_Doppelzottel = Lebewesen("Schleimige Doppelzottel", "Zwei Zottel, die bei Gefahr ätzenden Schleim absondern", 13, 15, 11, ["Alle"], ["Doppelzottel+Schleim"])
Rubin_Doppelzottel = Lebewesen("Rubin-Doppelzottel", "Zwei Zottel, die aus der Ferne Edelsteinen gleichen; stärker im Lebensraum Berge", 13, 10, 16, ["Alle"], ["Doppelzottel+Blut"])
Mystische_Doppelzottel = Lebewesen("Mystische Doppelzottel", "Zwei Zottel, die so selten vorkommen, dass man sich nicht sicher ist, ob sie überhaupt exestiert; geben dir eine weitere Karte, die keine Startkarte sein muss, pro Runde, wenn sie auf dem Feld platziert sind", 13, 13, 13, ["Alle"], ["Doppelzottel+Stein von Elyaris", "Doppelzottel+Engelshaar"])
Himmels_Doppelzottel = Lebewesen("Himmels-Doppelzottel", "Können pro Runde die Werte eines Lebewesens um 5 erhöhen (müssen dazu auf dem Feld platziert sein)", 13, 13, 13, ["Alle"], ["Doppelzottel+Eis", "Doppelzottel+Regenbogen", "Doppelzottel+Blitz"])

#Fee
Fee = Lebewesen("Fee", "Das Feenvolk ist gefürchtet und bewundert zugleich", 4, 4, 4, ["Alle"], [], True)
# -> Stufe 1 -> +1
Feuerfee = Lebewesen("Feuerfee", "Bändigt jede Flamme; stärker im Lebensraum Wüste", 5, 6, 4, ["Wüste", "Wald"], ["Fee+Feuer"])
Wasserfee = Lebewesen("Wasserfee", "Kontrolliert Regentropfen und Bäche; stärker im Lebensraum See", 5, 4, 6, ["See", "Berge"], ["Fee+Wasser"])
Luftfee = Lebewesen("Luftfee", "Kontrolliert Winde und Brisen; stärker im Lebensraum Berge", 5, 6, 4, ["Berge", "Wüste"], ["Fee+Luft"])
Naturfee = Lebewesen("Naturfee", "Kümmert sich um Tiere und Pflanzen; stärker im Lebensraum Wald", 5, 4, 6, ["Wald", "See"], ["Fee+Erde"])
Goldene_Fee = Lebewesen("Goldene Fee", "Versorgt das Feenvolk mit genügend Feenstaub", 5, 5, 5, ["Alle"], ["Fee+Magie"])
# -> Stufe 2 -> +3
Wetterfee = Lebewesen("Wetterfee", "Kann anderen Lebewesen ermöglichen in einem weiteren zufälligen Lebensraum zu überleben (muss dazu auf dem Feld platziert sein)", 7, 8, 6, ["Alle"], ["Fee+Wölkchen"])
Erntefee = Lebewesen("Erntefee", "Gibt dir eine weitere Elementkarte pro Runde, wenn sie auf dem Feld platziert ist", 7, 6, 8, ["Wald", "See", "Berge"], ["Fee+Beere"])
Zeitfee = Lebewesen("Zeitfee", "Gibt dir einen Extrazug pro Runde, wenn sie auf dem Feld platziert ist", 7, 7, 7, ["Alle"], ["Fee+Zeit"])
Todesfee = Lebewesen("Todesfee", "Kann zwischen dem Jenseits und dieser Welt wandern; stärker im Lebensraum See", 7, 9, 5, ["See", "Wüste", "Berge"], ["Fee+Staub", "Fee+Asche"])
# -> Stufe 3 -> +5
Schimmerfee = Lebewesen("Schimmerfee", "Kann anderen Lebewesen ermöglichen in allen Lebensräumen zu überleben (muss dazu auf dem Feld platziert sein)", 9, 8, 10, ["Alle"], ["Fee+Perle"])
Kristallfee = Lebewesen("Kristallfee", "Wunderschön und kaum von einem Kristall zu unterscheiden; stärker im Lebensraum Berge", 9, 12, 6, ["Alle"], ["Fee+Kristall"])
Glitzerfee = Lebewesen("Glitzerfee", "Versorgt die Sterne mit Feenstaub; stärker im Lebensraum Wüste", 9, 9, 9, ["Alle"], ["Fee+Sternenstaub"])
Dunkelfee = Lebewesen("Dunkelfee", "Wächterin der Nacht; kann pro Runde die Werte eines Lebewesens um 3 erhöhen (muss dazu auf dem Feld platziert sein)", 9, 9, 9, ["Alle"], ["Fee+Dunkle Macht"])
Babyfee = Lebewesen("Babyfee", "Gerade aus einer Blume geboren; ihr helles Lachen lässt jede Runde ein weiteres Lebewesen entstehen, wenn sie auf dem Feld platziert ist", 9, 2, 3, ["Alle"], ["Fee+Pusteblume", "Fee+Pfingstrose"])
# -> Stufe 4 -> +7
Unwetterfee = Lebewesen("Unwetterfee", "Extrafunktion", 11, 15, 7, ["Alle"], ["Fee+Blitz", "Fee+Eis", "Fee+Schleim"])
Lebensfee = Lebewesen("Lebensfee", "Gibt dir pro Runde eine zufällige Karte, die keine Startkarte sein muss, wenn sie auf dem Feld platziert ist", 11, 11, 11, ["Alle"], ["Fee+Blut", "Fee+Stein von Elyaris", "Fee+Regenbogen", "Fee+Engelshaar"])

#Feenkönigin -> Fee + Fee
Feenkönigin = Lebewesen("Feenkönigin", "Herrscht über das Feenvolk; kann pro Runde die Werte eines Lebewesens um 1 erhöhen (muss dazu auf dem Feld platziert sein)", 8, 8, 8, ["Alle"], ["Fee+Fee"])
# -> Stufe 1 -> +1
Feuer_Feenkönigin = Lebewesen("Feuer-Feenkönigin", "Bändigt jede Flamme; stärker im Lebensraum Wüste", 9, 10, 8, ["Wüste", "Wald"], ["Feenkönigin+Feuer"])
Wasser_Feenkönigin = Lebewesen("Wasser-Feenkönigin", "Kontrolliert Regentropfen und Bäche; stärker im Lebensraum See", 9, 8, 10, ["See", "Berge"], ["Feenkönigin+Wasser"])
Luft_Feenkönigin = Lebewesen("Luft-Feenkönigin", "Kontrolliert Winde und Brisen; stärker im Lebensraum Berge", 9, 10, 8, ["Berge", "Wüste"], ["Feenkönigin+Luft"])
Natur_Feenkönigin = Lebewesen("Natur-Feenkönigin", "Kümmert sich um Tiere und Pflanzen; stärker im Lebensraum Wald", 9, 8, 10, ["Wald", "See"], ["Feenkönigin+Erde"])
Goldene_Feenkönigin = Lebewesen("Goldene Feenkönigin", "Versorgt das Feenvolk mit genügend Feenstaub", 9, 9, 9, ["Alle"], ["Feenkönigin+Magie"])
# -> Stufe 2 -> +3
Wetter_Feenkönigin = Lebewesen("Wetter-Feenkönigin", "Kann anderen Lebewesen ermöglichen in allen Lebensräumen zu überleben (muss dazu auf dem Feld platziert sein)", 11, 15, 7, ["Alle"], ["Feenkönigin+Wölkchen"])
Ernte_Feenkönigin = Lebewesen("Ernte-Feenkönigin", "Gibt dir eine weitere Elementkarte, die keine Startkarte sein muss, pro Runde, wenn sie auf dem Feld platziert ist", 11, 9, 13, ["Wald", "See", "Berge"], ["Feenkönigin+Beere"])
Zeit_Feenkönigin = Lebewesen("Zeit-Feenkönigin", "Gibt dir 3 Extrazüge pro Runde, wenn sie auf dem Feld platziert ist", 11, 11, 11, ["Alle"], ["Feenkönigin+Zeit"])
Todes_Feenkönigin = Lebewesen("Todes-Feenkönigin", "Kann zwischen dem Jenseits und dieser Welt wandern; stärker im Lebensraum See", 11, 15, 7, ["See", "Wüste", "Berge"], ["Feenkönigin+Staub", "Feenkönigin+Asche"])
# -> Stufe 3 -> +5
Schimmer_Feenkönigin = Lebewesen("Schimmer-Feenkönigin", "Extrafunktion (muss dazu auf dem Feld platziert sein)", 13, 10, 16, ["Alle"], ["Feenkönigin+Perle"])
Kristall_Feenkönigin = Lebewesen("Kristall-Feenkönigin", "Wunderschön und kaum von einem Kristall zu unterscheiden; stärker im Lebensraum Berge", 13, 16, 10, ["Alle"], ["Feenkönigin+Kristall"])
Glitzer_Feenkönigin = Lebewesen("Glitzer-Feenkönigin", "Versorgt die Sterne mit Feenstaub; stärker im Lebensraum Wüste", 13, 13, 13, ["Alle"], ["Feenkönigin+Sternenstaub"])
Dunkel_Feenkönigin = Lebewesen("Dunkel-Feenkönigin", "Wächterin der Nacht; kann pro Runde die Werte eines Lebewesens um 5 erhöhen (muss dazu auf dem Feld platziert sein)", 13, 13, 13, ["Alle"], ["Feenkönigin+Dunkle Macht"])
Baby_Feenkönigin = Lebewesen("Baby_Feenkönigin", "Gerade aus einer Blume geboren und als Königin bestimmt; ihr helles Lachen lässt jede Runde ein weiteres Lebewesen, das keine Startkarte sein muss, entstehen, wenn sie auf dem Feld platziert ist", 13, 4, 5, ["Alle"], ["Feenkönigin+Pusteblume", "Feenkönigin+Pfingstrose"])
# -> Stufe 4 -> +7
Unwetter_Feenkönigin = Lebewesen("Unwetter-Feenkönigin", "Extrafunktion", 15, 20, 10, ["Alle"], ["Feenkönigin+Blitz", "Feenkönigin+Eis", "Feenkönigin+Schleim"])
Lebens_Feenkönigin = Lebewesen("Lebens-Feenkönigin", "Extrafunktion", 15, 15, 15, ["Alle"], ["Feenkönigin+Blut", "Feenkönigin+Stein von Elyaris", "Feenkönigin+Regenbogen", "Feenkönigin+Engelshaar"])

#Zeppelindrache -> Drache + Zottel ###
Zeppelindrache = Lebewesen("Zeppelindrache", "Riesiger Drache, der trotz fehlender Flügel schweben kann", 12, 4, 20, ["Berge"], ["Drache+Zottel"])
# -> Stufe 1 -> +1
Brennender_Zeppelindrache = Lebewesen("Brennender Zeppelindrache", "Das Feuer macht ihm nichts aus", 13, 6, 20, ["Berge", "Wüste"], ["Zeppelindrache+Feuer"])
Triefender_Zeppelindrache = Lebewesen("Triefender Zeppelindrache", "Kann aufgrund seines immer nassen Fells nicht fliegen, dafür aber unter Wasser atmen", 13, 5, 21, ["See"], ["Zeppelindrache+Wasser"])
Matschiger_Zeppelindrache = Lebewesen("Matschiger Zeppelindrache", "Wälzt sich im Matsch, um sein Fell zu schützen", 13, 5, 21, ["Wald", "Berge"], ["Zeppelindrache+Erde"])
Aufgeblähter_Zeppelindrache = Lebewesen("Aufgeblähter Zeppelindrache", "Fliegt höher als alle anderen Drachen", 13, 4, 22, ["Berge"], ["Zeppelindrache+Luft"])
Goldener_Zeppelindrache = Lebewesen("Goldener Zeppelindrache", "Hat vergoldetes Fell", 13, 5, 21, ["Berge"], ["Zeppelindrache+Magie"])
# -> Stufe 2 -> +3
Flauschiger_Zeppelindrache = Lebewesen("Flauschiger Zeppelindrache", "Kaum von einer echten Wolke zu unterscheiden", 15, 6, 24, ["Berge"], ["Zeppelindrache+Wölkchen"])
Alter_Zeppelindrache = Lebewesen("Alter Zeppelindrache", "Ein Kindheitsfreund der Prinzessin von Klumpiland", 15, 6, 24, ["Berge", "Wald"], ["Zeppelindrache+Zeit", "Zeppelindrache+Staub"])
Symbiotischer_Zeppelindrache = Lebewesen("Symbiotischer Zeppelindrache", "In seinem Fell nisten Vögel, die ihn im Gegenzug sauber halten und zu geeigneten Landeplätzen führen", 15, 8, 22, ["Berge", "Wald"], ["Zeppelindrache+Beere"])
Nacht_Zeppelindrache = Lebewesen("Nacht-Zeppelindrache", "Ist bestens an ein Leben in Dunkelheit angepasst und lebt am liebsten in tiefen Höhlen", 15, 6, 24, ["Berge"], ["Zeppelindrache+Asche"])
# -> Stufe 3 -> +5
Blühender_Zeppelindrache = Lebewesen("Blühender Zeppelindrache", "Verschiede Pflanzenarten leben in seinem Fell, sodass er vor allem im Frühling ein wunderschöner Anblick ist, wenn dieser Drache am Himmel schwebt", 17, 9, 25, ["Berge", "Wald"], ["Zeppelindrache+Pusteblume", "Zeppelindrache+Pfingstrose"])
Unsichtbarer_Zeppelindrache = Lebewesen("Unsichtbarer Zeppelindrache", "Jedes Haar seines Fells kann eine andere Farbe annehmen, wodurch er nicht von seiner Umgebung zu unterscheiden ist und kaum jemand von seiner Existenz weiß", 17, 9, 25, ["Alle"], ["Zeppelindrache+Perle"])
Toter_Zeppelindrache = Lebewesen("Toter Zeppelindrache", "Seine Augen sind leer, sein Inneres tot und er wird nur noch von der dunklen Macht bewegt", 17, 10, 24, ["Alle"], ["Zeppelindrache+Dunkle Macht"])
Kosmischer_Zeppelindrache = Lebewesen("Kosmischer Zeppelindrache", "Kann große Mengen an Sauerstoff in seinem Inneren speichern und so für eine Weile durch das Weltall schweben", 17, 8, 26, ["Alle"], ["Zeppelindrache+Sternenstaub"])
Durchsichtiger_Zeppelindrache = Lebewesen("Durchsichtiger Zeppelindrache", "Jede Zelle seines Körpers ist durchsichtig und bricht das Licht, wodurch er ein wunderschönes Farbenspiel am Himmel hinterlässt", 17, 8, 26, ["Alle"], ["Zeppelindrache+Kristall"])
# -> Stufe 4 -> +7 #Schleim, Eis, Blut, Blitz, Regenbogen, Engelshaar, Stein von Elyaris#

#Echsenmensch -> Drache + Klumpi ###
Echsenmensch = Lebewesen("Echsenmensch", "Die Gesellschaft der Echsenmenschen plant Klumpiland zu übernehmen", 10, 10, 10, ["Wüste"], ["Klumpi+Drache"])
# -> Stufe 1 -> +1 #Wasser, Feuer, Erde, Luft, Magie#
# -> Stufe 2 -> +3 #Wölkchen, Staub, Beere, Asche, Zeit#
#-> Stufe 3 -> +5 #Pusteblume, Pfingstrose, Perle, Sternenstaub, Kristall, Dunkle Macht#
# -> Stufe 4 -> +7 #Schleim, Eis, Blut, Blitz, Regenbogen, Engelshaar, Stein von Elyaris#

#Engel -> Klumpi + Fee ###
Engel = Lebewesen("Engel", "Ein reines und gutes Himmelswesen", 6, 6, 6, ["Alle"], ["Klumpi+Fee"])
# -> Stufe 1 -> +1 #Wasser, Feuer, Erde, Luft, Magie#
# -> Stufe 2 -> +3 #Wölkchen, Beere, Zeit#
Todesengel = Lebewesen("Todesengel", "Wacht über das Reich der Toten; stärker im Lebensraum See", 9, 10, 8, ["Alle"], ["Engel+Staub", "Engel+Asche"])
# -> Stufe 3 -> +5 #Pusteblume, Pfingstrose, Perle, Sternenstaub, Kristall#
Gefallener_Engel = Lebewesen("Gefallener Engel", "Wandte sich gegen die Himmelswesen und lebt nun unter den Menschen", 11, 11, 11, ["Alle"], ["Engel+Dunkle Macht"])
# -> Stufe 4 -> +7 #Blut, Stein von Elyaris#
Racheengel = Lebewesen("Racheengel", "Kämpft gegen die Himmelswesen um die Gerechtigkeit wieder herzustellen", 13, 13, 13, ["Alle"], ["Engel+Schleim", "Engel+Blitz", "Engel+Eis"])
Erzengel = Lebewesen("Erzengel", "Wacht über das gesamte Reich der Himmelswesen; gibt dir pro Runde eine zufällige Zusatzkarte, die keine Startkarte sein muss, wenn er auf dem Feld platziert ist", 13, 13, 13, ["Alle"], ["Engel+Engelshaar"])
Friedensengel = Lebewesen("Friedensengel", "Wacht über den Frieden im Himmelsreich und in Klumpiland; kann insgesamt 3 Lebensräume zu Wonderlands machen, in denen alle Lebewesen leben können", 13, 5, 21, ["Alle"], ["Engel+Regenbogen"])

#Rätselhafter Vogel -> Fee + Zottel ###
Rätselhafter_Vogel = Lebewesen("Rätselhafter Vogel", "In seine Augen scheinen alle Geheinmisse dieser Welt zu schimmern", 8, 6, 10, ["Alle"], ["Fee+Zottel"])
# -> Stufe 1 -> +1 #Wasser, Feuer, Erde, Magie#
Glühwürmchen = Lebewesen("Glühwürmchen", "Owl City - Fireflies", 9, 5, 13, ["Alle"], ["Rätselhafter Vogel+Feuer"])
Origami = Lebewesen("Origami", "Ein Vogel aus Papier, der seinen Erschaffer mit Informationen versorgt; gibt dir pro Runde einen Extrazug, wenn er auf dem Feld platziert ist", 9, 3, 15, ["Alle"], ["Rätselhafter Vogel+Luft"])
# -> Stufe 2 -> +3 #Staub, Beere#
Bernsteineule = Lebewesen("Bernsteineule", "Eine fast unbewegliche Eule mit klugen Augen; gibt dir pro Runde zwei Extrazüge, wenn sie auf dem Feld platziert ist", 11, 5, 17, ["Alle"], ["Rätselhafter Vogel+Zeit"])
Rabenschaar = Lebewesen("Rabenschaar", "Kündigen den Tod eines Mühlknappen an", 11, 15, 7, ["Alle"], ["Rätselhafter Vogel+Asche"])
Wolkenvogel = Lebewesen("Wolkenvogel", "Erschaffen von einem Mädchen, dessen Haare alle Farben des Lichts brachen", 11, 8, 14, ["Alle"], ["Rätselhafter Vogel+Wölkchen"])
# -> Stufe 3 -> +5 #Pusteblume, Perle, Sternenstaub, Kristall, Dunkle Macht#
Phönix = Lebewesen("Phönix", "Ein riesiger Vogel mit brennendem Gefieder", 13, 13, 13, ["Alle"], ["Rätselhafter Vogel+Pfingstrose"])
# -> Stufe 4 -> +7 #Eis, Blut, Regenbogen, Engelshaar, Stein von Elyaris#
Diebische_Elster = Lebewesen("Diebische Elster", "Kann 3 Mal das schlechteste Lebewesen eines gewählten Spielers für dich stehlen (dazu: Diebische Elster + gewählter Spieler)", 13, 15, 11, ["Alle"], ["Rätselhafter Vogel+Schleim", "Rätselhafter Vogel+Blitz"])

#Weltenwandler -> Gummikrieger + Fee ###
Weltenwandler = Lebewesen("Weltenwandler", "Eine gesichtslose Gestalt, die hin und wieder in dieser Welt auftaucht", 10, 10, 10, ["Alle"], ["Gummikrieger+Fee"])
# -> Stufe 1 -> +1 #Wasser, Feuer, Erde, Luft, Magie#
# -> Stufe 2 -> +3 #Wölkchen, Staub, Beere, Asche, Zeit#
#-> Stufe 3 -> +5 #Pusteblume, Pfingstrose, Perle, Sternenstaub, Kristall, Dunkle Macht#
# -> Stufe 4 -> +7 #Schleim, Eis, Blut, Blitz, Regenbogen, Engelshaar, Stein von Elyaris#

#Werwolf -> Zottel + Gummikrieger ###
Werwolf = Lebewesen("Werwolf", "Ein bei Tag unscheinbares Wesen, das sich erst bei Nacht in eine wolfsähnliche Kreatur verwandelt", 9, 10, 8, ["Wald"], ["Zottel+Gummikrieger"])
# -> Stufe 1 -> +1 #Wasser, Feuer, Erde, Luft, Magie#
# -> Stufe 2 -> +3 #Wölkchen, Beere, Zeit#
Urwolf = Lebewesen("Urwolf", "Ein alter grauer Werwolf, der einmal im Spiel eines deiner Lebewesen in einen Werwolf verwandeln kann (dazu: Urwolf + gewähltes Lebewesen)", 12, 14, 10, ["Wald"], ["Werwolf+Staub", "Werwolf+Asche"])
#-> Stufe 3 -> +5 #Pusteblume, Pfingstrose, Perle, Sternenstaub, Kristall, Dunkle Macht#
# -> Stufe 4 -> +7 #Schleim, Eis, Blut, Blitz, Regenbogen, Engelshaar, Stein von Elyaris#

#Troll -> Drache + Fee ###
Troll = ("Troll", "Trolle bitte nicht füttern", 13, 16, 12, ["Wald", "Berge"], ["Drache+Fee"])
# -> Stufe 1 -> +1 #Wasser, Feuer, Erde, Luft, Magie#
# -> Stufe 2 -> +3 #Wölkchen, Staub, Beere, Asche, Zeit#
#-> Stufe 3 -> +5 #Pusteblume, Pfingstrose, Perle, Sternenstaub, Kristall, Dunkle Macht#
# -> Stufe 4 -> +7 #Schleim, Eis, Blut, Blitz, Regenbogen, Engelshaar, Stein von Elyaris#

#Lebensraum
class Lebensraum(Karten):
    def __init__(self, Name, Beschreibung, Art, Punkte, Größe, Kombi = [], Start = False):
        Karten.__init__(self, Name, Beschreibung, Kombi, Start)
        self.Art = Art
        self.Punkte = Punkte
        self.Größe = Größe
        if self.Start == True:
            Start_Lebensraum.append(self)
        Alle_Lebensraum.append(self)

    #für Punkte
    def __repr__(self):
        CDS = Counter_Dict[Spieler]
        Mod_Größe = self.Größe
        if self in CDS:
            if CDS[self] == True:
                Verbesserung_Spieler = Verbesserung[Spieler]
                Verbesserung_Karte = Verbesserung_Spieler[self]
                Add_Größe = Verbesserung_Karte
                Mod_Größe = self.Größe + Add_Größe
                CDS[self] = False
        return "{} (Lebensraum):\n{} - Punkte: {} - Größe: {}".format(self.Name, self.Beschreibung, self.Punkte, Mod_Größe)

    #für Kampf
    def __str__(self):
        CDS = Counter_Dict[Spieler]
        Mod_Größe = self.Größe
        if self in CDS:
            if CDS[self] == True:
                Verbesserung_Spieler = Verbesserung[Spieler]
                Verbesserung_Karte = Verbesserung_Spieler[self]
                Add_Größe = Verbesserung_Karte
                Mod_Größe = self.Größe + Add_Größe
                CDS[self] = False
        return "{} (Lebensraum):\n{} - Größe: {}".format(self.Name, self.Beschreibung, Mod_Größe)

#Wald
Kleiner_Wald = Lebensraum("Kleiner Wald", "Kleiner schattiger Lebensraum", "Wald", 1, 1, [], True)
Wald = Lebensraum("Wald", "Mittelgroßer schattiger Lebensraum", "Wald", 2, 3, ["Kleiner Wald+Kleiner Wald"], True)
Großer_Wald = Lebensraum("Großer Wald", "Großer schattiger Lebensraum", "Wald", 4, 8, ["Wald+Wald"])
Magischer_Kleiner_Wald = Lebensraum("Magischer Kleiner Wald", "Verbessert alle Werte der hier lebenden Lebewesen um 1", "Wald", 2, 1, ["Kleiner Wald+Magie"])
Magischer_Wald = Lebensraum("Magischer Wald", "Verbessert alle Werte der hier lebenden Lebewesen um 1", "Wald", 3, 3, ["Wald+Magie", "Magischer Kleiner Wald+Magischer Kleiner Wald", "Magischer Kleiner Wald+Kleiner Wald"])
Magischer_Großer_Wald = Lebensraum("Magischer Großer Wald", "Verbessert alle Werte der hier lebenden Lebewesen um 1", "Wald", 5, 8, ["Großer Wald+Magie", "Magischer Wald+Magischer Wald", "Magischer Wald+Wald"])

#See
Kleiner_See = Lebensraum("Kleiner See", "Kleiner nasser Lebensraum", "See", 1, 1, [], True)
See = Lebensraum("See", "Mittelgroßer nasser Lebensraum", "See", 2, 3, ["Kleiner See+Kleiner See"], True)
Großer_See = Lebensraum("Großer See", "Großer nasser Lebensraum", "See", 4, 8, ["See+See"])
Magischer_Kleiner_See = Lebensraum("Magischer Kleiner See", "Verbessert alle Werte der hier lebenden Lebewesen um 1", "See", 2, 1, ["Kleiner See+Magie"])
Magischer_See = Lebensraum("Magischer See", "Verbessert alle Werte der hier lebenden Lebewesen um 1", "See", 3, 3, ["See+Magie", "Magischer Kleiner See+Magischer Kleiner See", "Magischer Kleiner See+Kleiner See"])
Magischer_Großer_See = Lebensraum("Magischer Großer See", "Verbessert alle Werte der hier lebenden Lebewesen um 1", "See", 5, 8, ["Großer See+Magie", "Magischer See+Magischer See", "Magischer See+See"])

#Wüste
Kleine_Wüste = Lebensraum("Kleine Wüste", "Kleiner heißer Lebensraum", "Wüste", 1, 1, [], True)
Wüste = Lebensraum("Wüste", "Mittelgroßer heißer Lebensraum", "Wüste", 2, 3, ["Kleine Wüste+Kleine Wüste"], True)
Große_Wüste = Lebensraum("Große Wüste", "Großer heißer Lebensraum", "Wüste", 4, 8, ["Wüste+Wüste"])
Magische_Kleine_Wüste = Lebensraum("Magische Kleine Wüste", "Verbessert alle Werte der hier lebenden Lebewesen um 1", "Wüste", 2, 1, ["Kleine Wüste+Magie"])
Magische_Wüste = Lebensraum("Magische Wüste", "Verbessert alle Werte der hier lebenden Lebewesen um 1", "Wüste", 3, 3, ["Wüste+Magie", "Magische Kleine Wüste+Magische Kleine Wüste", "Magische Kleine Wüste+Kleine Wüste"])
Magische_Große_Wüste = Lebensraum("Magische Große Wüste", "Verbessert alle Werte der hier lebenden Lebewesen um 1", "Wüste", 5, 8, ["Große Wüste+Magie", "Magische Wüste+Magische Wüste", "Magische Wüste+Wüste"])

#Berge
Kleine_Berge = Lebensraum("Kleine Berge", "Kleiner hügeliger Lebensraum", "Berge", 1, 1, [], True)
Berge = Lebensraum("Berge", "Mittelgroßer luftiger Lebensraum", "Berge", 2, 3, ["Kleine Berge+Kleine Berge"], True)
Große_Berge = Lebensraum("Große Berge", "Großer Lebensraum mit eisigen Bergspitzen", "Berge", 4, 8, ["Berge+Berge"])
Magische_Kleine_Berge = Lebensraum("Magische Kleine Berge", "Verbessert alle Werte der hier lebenden Lebewesen um 1", "Berge", 2, 1, ["Kleine Berge+Magie"])
Magische_Berge = Lebensraum("Magische Berge", "Verbessert alle Werte der hier lebenden Lebewesen um 1", "Berge", 3, 3, ["Berge+Magie", "Magische Kleine Berge+Magische Kleine Berge", "Magische Kleine Berge+Kleine Berge"])
Magische_Große_Berge = Lebensraum("Magische Große Berge", "Verbessert alle Werte der hier lebenden Lebewesen um 1", "Berge", 5, 8, ["Große Berge+Magie", "Magische Berge+Magische Berge", "Magische Berge+Berge"])

#Wonderland
Kleines_Wonderland = Lebensraum("Kleines Wonderland", "Hier können alle Lebewesen leben", "Wonderland", 6, 1)
Wonderland = Lebensraum("Wonderland", "Hier können alle Lebewesen leben", "Wonderland", 7, 3, ["Kleines Wonderland+Kleines Wonderland"])
Großes_Wonderland = Lebensraum("Großes Wonderland", "Hier können alle Lebewesen leben", "Wonderland", 9, 8, ["Wonderland+Wonderland"])
Magisches_Kleines_Wonderland = Lebensraum("Magisches Kleines Wonderland", "Hier können alle Lebewesen leben und ihre Werte werden um 1 verbessert", "Wonderland", 7, 1, ["Kleines Wonderland+Magie"])
Magisches_Wonderland = Lebensraum("Magisches Wonderland", "Hier können alle Lebewesen leben und ihre Werte werden um 1 verbessert", "Wonderland", 8, 3, ["Wonderland+Magie", "Magisches Kleines Wonderland+Magisches Kleines Wonderland", "Magisches Kleines Wonderland+Kleines Wonderland"])
Magisches_Großes_Wonderland = Lebensraum("Magisches Großes Wonderland", "Hier können alle Lebewesen leben und ihre Werte werden um 1 verbessert", "Wonderland", 10, 8, ["Großes Wonderland+Magie", "Magisches Wonderland+Magisches Wonderland", "Magisches Wonderland+Wonderland"])
for LW in Alle_Lebewesen:
    LW.Lebensraum.append("Wonderland")

#Elemente
class Elemente(Karten):
    def __init__(self, Name, Beschreibung, Kombi = [], Start = False):
        Karten.__init__(self, Name, Beschreibung, Kombi, Start)
        if self.Start == True:
            Start_Elemente.append(self)
        Alle_Elemente.append(self)

    #für Punkte und Kampf
    def __repr__(self):
        return "{} (Elemente):\n{}".format(self.Name, self.Beschreibung)

#Vordruck
# = Elemente("", "", [""])
#Start/Stufe 1 -> +1
Wasser = Elemente("Wasser", "Eines der vier klassischen Elemente", [], True)
Feuer = Elemente("Feuer", "Eines der vier klassischen Elemente", [], True)
Erde = Elemente("Erde", "Eines der vier klassischen Elemente", [], True)
Luft = Elemente("Luft", "Eines der vier klassischen Elemente", [], True)
Magie = Elemente("Magie", "Eine leuchtende Kugel aus unbestimmter Macht", [], True)
#Stufe 2 -> +3
Wölkchen = Elemente("Wölkchen", "Flauschige schwebende Masse", ["Feuer+Wasser", "Wasser+Luft", "Wasser+Wasser"])
Staub = Elemente("Staub", "Etwas aufgewirbelte Erde", ["Luft+Erde", "Erde+Erde", "Luft+Luft"])
Beere = Elemente("Beere", "Eine süße Frucht aus dem Nachtwald Perelín", ["Wasser+Erde", "Magie+Magie", "Magie+Wasser"])
Asche = Elemente("Asche", "Der erste Schritt auf die dunkle Seite", ["Feuer+Erde", "Feuer+Luft", "Feuer+Feuer"])
Zeit = Elemente("Zeit", "Tick-tack tick-tack", ["Magie+Luft", "Magie+Feuer", "Magie+Erde"])
#Stufe 3 -> +5
Pusteblume = Elemente("Pusteblume", "Wünsch' dir was", ["Luft+Beere", "Luft+Wölkchen", "Erde+Wölkchen", "Luft+Zeit"])
Pfingstrose = Elemente("Pfingstrose", "Eine wunderschöne Blume", ["Feuer+Beere", "Feuer+Wölkchen", "Erde+Beere", "Feuer+Zeit"])
Perle = Elemente("Perle", "Eine kleine glänzende Kugel", ["Wasser+Wölkchen", "Wasser+Staub", "Wasser+Beere", "Wasser+Asche", "Beere+Magie"])
Sternenstaub = Elemente("Sternenstaub", "Ein Beutel voller Glitzer", ["Staub+Magie", "Wölkchen+Magie", "Feuer+Staub", "Luft+Staub"])
Kristall = Elemente("Kristall", "Bricht das Licht in funkelnde Farben", ["Erde+Zeit", "Erde+Staub", "Wasser+Zeit"])
Dunkle_Macht = Elemente("Dunkle Macht", "Die dunkle Variante der Magie", ["Magie+Asche", "Magie+Zeit", "Feuer+Asche", "Erde+Asche", "Luft+Asche"])
#Stufe 4 -> +7
Schleim = Elemente("Schleim", "Eine glibbrige grüne Masse", ["Beere+Asche", "Beere+Staub", "Beere+Zeit", "Dunkle Macht+Erde", "Staub+Staub", "Asche+Asche"])
Eis = Elemente("Eis", "Zu kleinen Kristallen gefrorenes Wasser", ["Kristall+Wasser", "Dunkle Macht+Wasser", "Wasser+Pusteblume", "Wasser+Perle", "Luft+Perle"])
Blut = Elemente("Blut", "Ein dunkelroter Tropfen Leben", ["Feuer+Perle", "Feuer+Dunkle Macht", "Feuer+Kristall", "Magie+Pfingstrose", "Magie+Dunkle Macht", "Wasser+Pfingstrose", "Feuer+Pfingstrose"])
Blitz = Elemente("Blitz", "Ein glühender Strahl zwischen Regen und Donner", ["Wölkchen+Asche", "Luft+Dunkle Macht", "Feuer+Sternenstaub", "Wasser+Sternenstaub", "Luft+Pfingstrose"])
Regenbogen = Elemente("Regenbogen", "Mit einem Topf voller Gold am Ende (ja, es ist ein Kreis)", ["Beere+Wölkchen", "Wölkchen+Zeit", "Zeit+Staub", "Magie+Sternenstaub", "Erde+Sternenstaub", "Magie+Pusteblume", "Magie+Perle"])
Engelshaar = Elemente("Engelshaar", "Eine goldene Locke", ["Kristall+Luft", "Sternenstaub+Luft", "Staub+Wölkchen", "Feuer+Pusteblume", "Erde+Pusteblume", "Erde+Kristall", "Luft+Pusteblume", "Wölkchen+Wölkchen"])
Stein_von_Elyaris = Elemente("Stein von Elyaris", "Stammt von einer Insel und lässt einen alles vergessen", ["Staub+Asche", "Pfingstrose+Pusteblume", "Zeit+Asche", "Erde+Pfingstrose", "Erde+Perle", "Magie+Kristall", "Beere+Beere", "Zeit+Zeit"])

#Tränke -> Zauberer
#Tränke -> Stufe 1
Heißer_Trank = Elemente("Heißer Trank", "Ermöglicht einem Lebewesen in Wüsten zu leben")
Wässriger_Trank = Elemente("Wässriger Trank", "Ermöglicht einem Lebewesen in Seen zu leben")
Matschiger_Trank = Elemente("Matschiger Trank", "Ermöglicht einem Lebewesen in Wäldern zu leben")
Blubbernder_Trank = Elemente("Blubbernder Trank", "Ermöglicht einem Lebewesen in den Bergen zu leben")
Güldener_Trank = Elemente("Güldener Trank", "Erhöht die Werte eines Lebewesens um 3")
#Tränke -> Stufe 2
Level_Up_Trank = Elemente("Level-Up Trank", "Erhöht die Werte eines Lebewesens um 5")
Vergrößerungs_Trank = Elemente("Vergrößerungs-Trank", "Vergrößert einen Lebensraum um einen Platz")
Verkohlter_Trank = Elemente("Verkohlter Trank", "Härtet ein Lebewesen ab, sodass es in allen Lebensräumen leben kann")
#Tränke -> Stufe 3
Schwarzer_Trank = Elemente("Schwarzer Trank", "Verringert die Werte eines zufälligen gegnerischen Lebewesens um 5 (zum Anwenden den Tranknamen tippen)")
Glitzernder_Trank = Elemente("Glitzernder Trank", "Erhöht die Werte eines Lebewesens um 7", ["Zauberer+Perle", "Zauberer+Sternenstaub")
Duftender_Trank = Elemente("Duftender Trank", "Verwandelt einen Lebensraum in ein Wonderland, in dem alle Lebewesen leben können")
#Tränke -> Stufe 4
Himmlischer_Trank = Elemente("Himmlischer Trank", "Erhöht die Werte eines Lebewesens um 10")
Gefrorener_Trank = Elemente("Gefrorener Trank", "Friert alle Karten eines Spielers für 3 Züge ein (zum Anwenden Trankname + Spielername tippen)")
Dolly_Trank = Elemente("Dolly Trank", "Klont ein beliebiges Lebewesen")

Tränke_Kombi = {Heißer_Trank:[Feuer], Wässriger_Trank:[Wasser], Matschiger_Trank:[Erde], Blubbernder_Trank:[Luft], Güldener_Trank:[Magie],
                Level_Up_Trank:[Beere, Wölkchen], Vergrößerungs_Trank:[Staub], Verkohlter_Trank:[Asche, Zeit],
                Schwarzer_Trank:[Dunkle_Macht], Glitzernder_Trank:[Perle, Sternenstaub, Kristall], Duftender_Trank:[Pusteblume, Pfingstrose],
                Himmlischer_Trank:[Regenbogen, Engelshaar, Stein_von_Elyaris], Gefrorener_Trank:[Eis], Dolly_Trank:[Blut, Schleim, Blitz]}

#Gifte -> Dunkler Magier
#Gifte -> Stufe 1
Elementares_Gift = Elemente("Elementares Gift", "Verringert die Werte eines zufälligen Lebewesens des gewählten Spielers um 3")
Magisches_Gift = Elemente("Magisches Gift", "Der gewählte Spieler setzt einen Zug aus")
#Gifte -> Stufe 2
Pampiges_Gift = Elemente("Pampiges Gift", "Verringert die Werte eines zufälligen Lebewesens des gewählten Spielers um 5")
Reines_Gift = Elemente("Reines Gift", "Zerstört das schwächste Lebewesen des gewählten Spielers")
#Gifte -> Stufe 3
Trügerisches_Gift = Elemente("Trügerisches Gift", "Verringert die Werte eines zufälligen Lebewesens des gewählten Spielers um 7")
Lähmendes_Gift = Elemente("Lähmendes Gift", "Der gewählte Spieler setzt drei Züge aus")
#Gifte -> Stufe 4
Eisiges_Gift = Elemente("Eisiges Gift", "Der gewählte Spieler setzt fünf Züge aus")
Gift_des_Vergessens = Elemente("Gift des Vergessens", "Zerstört das beste Lebewesen des gewählten Spielers")
Blutiges_Gift = Elemente("Blutiges Gift", "Verringert die Werte eines zufälligen Lebewesens des gewählten Spielers um 10")
                                                                                         
Gifte_Kombi = {Elementares_Gift:[Feuer, Wasser, Erde, Luft],
               Magisches_Gift:[Magie],
               Pampiges_Gift:[Beere, Staub, Asche],
               Reines_Gift:[Wölkchen, Zeit],
               Trügerisches_Gift:[Sternenstaub, Perle, Kristall],
               Lähmendes_Gift:[Pusteblume, Pfingstrose, Dunkle_Macht],
               Eisiges_Gift:[Eis, Blitz],
               Gift_des_Vergessens:[Stein_von_Elyaris, Regenbogen, Engelshaar],
               Blutiges_Gift:[Blut, Schleim]}
                
#Doppelte Kombis Check
Alle_Kombis = []
for Karte in Alle_Karten:
    for Kombi_ in Karte.Kombi:
        Kombi_1 = Kombi_
        K = Kombi_.split("+")
        Kombi_2 = K[1] + "+" + K[0]
        if Kombi_1 in Alle_Kombis or Kombi_2 in Alle_Kombis:
            print("Fehler -> Doppelte Kombi")
            print(Kombi_)
        if not Kombi_1 in Alle_Kombis:
            Alle_Kombis.append(Kombi_1)
        if not Kombi_2 in Alle_Kombis:
            Alle_Kombis.append(Kombi_2)

#Vertippt Check
for Karte in Alle_Karten:
    for K in Karte.Kombi:
        Liste = K.split("+")
        if not len(Liste) == 2:
            print("Falsche Kombi: " + Karte.Name)
            break
        Karte_1 = False
        Karte_2 = False
        for Krt in Alle_Karten:
            if Liste[0] == Krt.Name:
                Karte_1 = True
            if Liste[1] == Krt.Name:
                Karte_2 = True
        if Karte_1 == False or Karte_2 == False:
            print("Vertippt: " + Karte.Name)

#Mehr Kombis, wenn selber Weg
def Mehr_Kombi(Grund_Karte):
    for LW in Alle_Lebewesen:
        Neue_Kombis = []
        for Kombi_ in LW.Kombi:
            if Grund_Karte in Kombi_:
                Kombi_Karten_Namen = Kombi_.split("+")
                Kombi_Karten = []
                for Nur_Karte in Alle_Karten:
                    if Nur_Karte.Name == Kombi_Karten_Namen[0]:
                        Kombi_Karten.append(Nur_Karte)
                    if Nur_Karte.Name == Kombi_Karten_Namen[1]:
                        Kombi_Karten.append(Nur_Karte)
                if not len(Kombi_Karten) == 2:
                    print("Mehr Kombi Fehler")
                for X in Kombi_Karten[0].Kombi:
                    Kombi_Kombi = X.split("+")
                    Kombi_1 = Kombi_Karten[1].Name + "+" + Kombi_Kombi[0]
                    Kombi_1_ = Kombi_Kombi[0] + "+" + Kombi_Karten[1].Name
                    Kombi_2 = Kombi_Karten[1].Name + "+" + Kombi_Kombi[1]
                    Kombi_2_ = Kombi_Kombi[1] + "+" + Kombi_Karten[1].Name
                    Karte_1 = None
                    Karte_2 = None
                    for A in Alle_Karten:
                        for K in A.Kombi:
                            if Kombi_1 == K or Kombi_1_ == K:
                                Karte_1 = A
                            if Kombi_2 == K or Kombi_2_ == K:
                                Karte_2 = A
                    if (not Karte_1 == None) and (not Karte_2 == None):
                        Neue_1 = Karte_1.Name + "+" + Kombi_Kombi[1]
                        Neue_1_ = Kombi_Kombi[1] + "+" + Karte_1.Name
                        Neue_2 = Karte_2.Name + "+" + Kombi_Kombi[0]
                        Neue_2_ = Kombi_Kombi[0] + "+" + Karte_2.Name
                        if (not Neue_1 in Neue_Kombis) and (not Neue_1_ in Neue_Kombis):
                            Neue_Kombis.append(Neue_1)
                        if (not Neue_2 in Neue_Kombis) and (not Neue_2_ in Neue_Kombis):
                            Neue_Kombis.append(Neue_2)
                for X in Kombi_Karten[1].Kombi:
                    Kombi_Kombi = X.split("+")
                    Kombi_1 = Kombi_Karten[0].Name + "+" + Kombi_Kombi[0]
                    Kombi_1_ = Kombi_Kombi[0] + "+" + Kombi_Karten[0].Name
                    Kombi_2 = Kombi_Karten[0].Name + "+" + Kombi_Kombi[1]
                    Kombi_2_ = Kombi_Kombi[1] + "+" + Kombi_Karten[0].Name
                    Karte_1 = None
                    Karte_2 = None
                    for A in Alle_Karten:
                        for K in A.Kombi:
                            if Kombi_1 == K or Kombi_1_ == K:
                                Karte_1 = A
                            if Kombi_2 == K or Kombi_2_ == K:
                                Karte_2 = A
                    if (not Karte_1 == None) and (not Karte_2 == None):
                        Neue_1 = Karte_1.Name + "+" + Kombi_Kombi[1]
                        Neue_1_ = Kombi_Kombi[1] + "+" + Karte_1.Name
                        Neue_2 = Karte_2.Name + "+" + Kombi_Kombi[0]
                        Neue_2_ = Kombi_Kombi[0] + "+" + Karte_2.Name
                        if (not Neue_1 in Neue_Kombis) and (not Neue_1_ in Neue_Kombis):
                            Neue_Kombis.append(Neue_1)
                        if (not Neue_2 in Neue_Kombis) and (not Neue_2_ in Neue_Kombis):
                            Neue_Kombis.append(Neue_2)
                for Kombi_1_ in Kombi_Karten[0].Kombi:
                    Kombi_1_L = Kombi_1_.split("+")
                    for Kombi_2_ in Kombi_Karten[1].Kombi:
                        Kombi_2_L = Kombi_2_.split("+")
                        Vier_Liste = []
                        for K in Kombi_1_L:
                            Vier_Liste.append(K)
                        for K in Kombi_2_L:
                            Vier_Liste.append(K)
                        Tief_K_1_1 = Vier_Liste[0] + "+" + Vier_Liste[2]
                        Tief_K_1_1_ = Vier_Liste[2] + "+" + Vier_Liste[0]
                        Tief_K_1_2 = Vier_Liste[1] + "+" + Vier_Liste[3]
                        Tief_K_1_2_ = Vier_Liste[3] + "+" + Vier_Liste[1]
                        Karte_1 = None
                        Karte_2 = None
                        for A in Alle_Karten:
                            for K in A.Kombi:
                                if Tief_K_1_1 == K or Tief_K_1_1_ == K:
                                    Karte_1 = A
                                if Tief_K_1_2 == K or Tief_K_1_2_ == K:
                                    Karte_2 = A
                        if (not Karte_1 == None) and (not Karte_2 == None):
                                Neue_1 = Karte_1.Name + "+" + Karte_2.Name
                                Neue_2 = Karte_2.Name + "+" + Karte_1.Name
                                if (not Neue_1 in Neue_Kombis) and (not Neue_2 in Neue_Kombis):
                                    Neue_Kombis.append(Neue_1)
                        Tief_K_2_1 = Vier_Liste[0] + "+" + Vier_Liste[3]
                        Tief_K_2_1_ = Vier_Liste[3] + "+" + Vier_Liste[0]
                        Tief_K_2_2 = Vier_Liste[1] + "+" + Vier_Liste[2]
                        Tief_K_2_2_ = Vier_Liste[2] + "+" + Vier_Liste[1]
                        Karte_1 = None
                        Karte_2 = None
                        for A in Alle_Karten:
                            for K in A.Kombi:
                                if Tief_K_2_1 == K or Tief_K_2_1_ == K:
                                    Karte_1 = A
                                if Tief_K_2_2 == K or Tief_K_2_2_ == K:
                                    Karte_2 = A
                        if (not Karte_1 == None) and (not Karte_2 == None):
                                Neue_1 = Karte_1.Name + "+" + Karte_2.Name
                                Neue_2 = Karte_2.Name + "+" + Karte_1.Name
                                if (not Neue_1 in Neue_Kombis) and (not Neue_2 in Neue_Kombis):
                                    Neue_Kombis.append(Neue_1)
        for Ding in Neue_Kombis:
            if not Ding in Alle_Kombis:
                Liste = LW.Kombi
                Liste.append(Ding)
                Alle_Kombis.append(Ding)

Mehr_Kombi_Liste = ["Gummikrieger", "Starker Krieger",
                    "Klumpi",
                    "Drache", "Starker Drache",
                    "Zottel", "Doppelzottel",
                    "Fee", "Feenkönigin",
                    "Zeppelindrache", "Echsenmensch", "Engel", "Rätselhafter Vogel", "Weltenwandler", "Werwolf"]        
for Grund_Karte in Mehr_Kombi_Liste:
    Mehr_Kombi(Grund_Karte)

#LW stärker in LR
Stärker_LR = {"Wald":[], "See":[], "Wüste":[], "Berge":[], "Wonderland":[]}
for Karte in Alle_Lebewesen:
    if "tärker im Lebensraum Wald" in Karte.Beschreibung:
        Stärker_LR["Wald"].append(Karte)
    elif "tärker im Lebensraum See" in Karte.Beschreibung:
        Stärker_LR["See"].append(Karte)
    elif "tärker im Lebensraum Wüste" in Karte.Beschreibung:
        Stärker_LR["Wüste"].append(Karte)
    elif "tärker im Lebensraum Berge" in Karte.Beschreibung:
        Stärker_LR["Berge"].append(Karte)

#Extra-LRs
LRs = ["Wald", "Wüste", "Berge", "See"]
ExtraLRs = {Wetterfee:"Zufall", Schimmerfee:"Alle", Wetter_Feenkönigin:"Alle"}

#Extrakarten - {Karte : Liste, aus der gewählt wird}
Extrakarten = {Traumdrache:random.choice(Alle_Start_Karten), #Startkarten
               Mystischer_Zottel:random.choice(Alle_Start_Karten),
               Lebensfee:random.choice(Alle_Verteilung), #Alle
               Erzengel:random.choice(Alle_Verteilung),
               Starker_Traumdrache:random.choice(Alle_Verteilung),
               Mystische_Doppelzottel:random.choice(Alle_Verteilung),
               Erntefee:Start_Elemente, #Sonstige
               Gräberling:Start_Elemente,
               Babyfee:Start_Lebewesen,
               Ernte_Feenkönigin:Alle_Elemente,
               Baby_Feenkönigin:Alle_Lebewesen}

#Extrazüge - {Karte : Anzahl}
Extrazüge = {Sphinx:1,
             Zeitfee:1,
             Origami:1,
             Bernsteineule:2,
             Gütiger_Krieger:3,
             Zeit_Feenkönigin:3,
             Starker_Gütiger_Krieger:5}

#Werteverbesserung - {Karte : wie viel}, einmal pro Runde möglich
Werteverbesserung_Übersicht = {Feenkönigin:1,
                               Dunkelfee:3,
                               Himmelszottel:3,
                               Sea_People:3,
                               Dunkel_Feenkönigin:5,
                               Himmels_Doppelzottel:5}
                    
#######################################################################################################################################################################################################################

##Spielprinzip##
#Funktionen
#Statistik
def Möglich(Karte_1, Karte_2): #Kombi möglich (zwei Karten)?, wenn ja: welche Karte wird daraus
    KM = []
    Kombi_1 = Karte_1 + "+" + Karte_2
    Kombi_2 = Karte_2 + "+" + Karte_1
    for Karte in Alle_Karten:
        if Kombi_1 in Karte.Kombi or Kombi_2 in Karte.Kombi:
            KM.append(Karte.Name)
    if len(KM) == 0:
        print("Keine Karte durch diese Kombi (" + Kombi_1 + ")")
    else:
        print("Karten durch diese Kombi (" + Kombi_1 + "):")
        for Karte in KM:
            print(Karte)
                    
def Stat_LR(): #Wie viele LW können in LR-Arten leben?
    LR_Arten = ["Wald", "See", "Wüste", "Berge"]
    Kombi_Counter = 0
    while Kombi_Counter <= (len(LR_Arten) - 1):
        print("Anzahl Lebewesen in dieser Lebensraum-Art: " + LR_Arten[Kombi_Counter])
        LWs_Counter = 0
        for Karte in Alle_Lebewesen:
            for LR in Karte.Lebensraum:
                if LR == LR_Arten[Kombi_Counter] or LR == "Alle":
                    LWs_Counter += 1
        print(LWs_Counter)
        Kombi_Counter += 1
        
#Regeln
def Regeln():
    print("Jeder Spieler erhält jede Runde einige Karten folgender Arten: Lebensräume, Lebewesen und Elemente. Die erhaltenen Karten befinden sich nun in deiner Ablage.")
    print("Lebensräume werden auf dem Feld platziert. Danach kannst du Lebewesen in ihnen leben lassen. Nur diese Lebewesen werden am Ende gewertet.")
    print("Um Lebewesen zu verbessern, kannst du sie mit Elementen oder mit anderen Lebewesen kombinieren. Lebensräume kannst du unter anderem durch das Element Magie verbessern.")
    print("Lebewesen kannst du nur innerhalb des Feldes oder innerhalb der Ablage kombinieren. Lebensräume kannst du auch zwischen Ablage und Feld kombinieren, darfst dafür aber nicht zwei genau gleiche Lebensräume auf dem Feld haben.")
    print("Einige Lebewesen haben Extrafunktionen. Platziere diese Lebewesen zuerst in Lebensräumen auf dem Feld, um diese zu nutzen.")
    print("Allerdings kannst du nur eine dieser Aktionen pro Zug ausführen. Davor kannst du beliebig viele Lebewesen auf dem Feld bewegen.")

#Ausgabe
def Ausgabe(Ort):
    global Modus
    #Ausgabe von Verbesserungen
    CDS = Counter_Dict[Spieler]
    Feld_Spieler = Feld[Spieler]
    if Ort == Ablage[Spieler]:
        for Karte in CDS:
            CDS[Karte] = False
            Test = True
            for LR in Feld[Spieler]:
                if Karte == LR or Karte in Feld_Spieler[LR]:
                    Test = False
            if Test == True and Karte in Ablage[Spieler]:
                CDS[Karte] = True
    elif Ort == Ende_LW[Spieler]:
        for Karte in CDS:
            CDS[Karte] = False
            if Karte in Ende_LW[Spieler]:
                CDS[Karte] = True            
    #Ausgabe        
    if len(Ort) == 0:
        print("/")
    elif Modus == "1":
        for Karte in Ort:
            if Karte in Alle_Lebensraum:
                print(repr(Karte) + "\n")
        for Karte in Ort:
            if Karte in Alle_Lebewesen:
                print(repr(Karte) + "\n")
        for Karte in Ort:
            if Karte in Alle_Elemente:
                print(repr(Karte) + "\n")
    elif Modus == "2":
        for Karte in Ort:
            if Karte in Alle_Lebensraum:
                print(Karte)
                print("\n")
        for Karte in Ort:
            if Karte in Alle_Lebewesen:
                print(Karte)
                print("\n")
        for Karte in Ort:
            if Karte in Alle_Elemente:
                print(Karte)
                print("\n")

def Ausgabe_Feld():
    global Modus
    #Ausgabe von Verbesserungen
    CDS = Counter_Dict[Spieler]
    Feld_Spieler = Feld[Spieler]
    MDS = Magisch_Dict[Spieler]
    SDS = Stärker_Dict[Spieler]
    for Karte in CDS:
        CDS[Karte] = False
        for LR in Feld[Spieler]:
            if Karte == LR or Karte in Feld_Spieler[LR]:
                CDS[Karte] = True
    for Karte in MDS:
        MDS[Karte] = 0
    for Karte in SDS:
        SDS[Karte] = 0
    for LR in Feld_Spieler:
        for LW in Feld_Spieler[LR]:
            if "Magisch" in LR.Name:
                if LW in MDS:
                    MDS[LW] += 1
                else:
                    MDS.update({LW:1})
            if LW in Stärker_LR[LR.Art]:
                if not LW in SDS:
                    SDS.update({LW:1})
                else:
                    SDS[LW] += 1
    #Ausgabe
    if len(Feld[Spieler]) == 0:
        print("/")
    elif Modus == "1":
        for Karte in Feld_Spieler:
            if "Klein" in Karte.Name:
                print(repr(Karte))
                if Feld_Spieler == []:
                    print("\n")
                Dings = 0
                for LW in Feld_Spieler[Karte]:
                    print("-> " + repr(LW))
                    Dings += 1
                    if Dings == len(Feld_Spieler[Karte]):
                        print("\n")
        for Karte in Feld_Spieler:
            if not "Klein" in Karte.Name and not "Groß" in Karte.Name:
                print(repr(Karte))
                if Feld_Spieler == []:
                    print("\n")
                Dings = 0
                for LW in Feld_Spieler[Karte]:
                    print("-> " + repr(LW))
                    Dings += 1
                    if Dings == len(Feld_Spieler[Karte]):
                        print("\n")
        for Karte in Feld_Spieler:
            if "Groß" in Karte.Name:
                print(repr(Karte))
                if Feld_Spieler == []:
                    print("\n")
                Dings = 0
                for LW in Feld_Spieler[Karte]:
                    print("-> " + repr(LW))
                    Dings += 1
                    if Dings == len(Feld_Spieler[Karte]):
                        print("\n")
    elif Modus == "2":
        for Karte in Feld_Spieler:
            if "Klein" in Karte.Name:
                print(Karte)
                if Feld_Spieler[Karte] == []:
                    print("\n")
                Dings = 0
                for LW in Feld_Spieler[Karte]:
                    print("->")
                    print(LW)
                    Dings += 1
                    if Dings == len(Feld_Spieler[Karte]):
                        print("\n")
        for Karte in Feld_Spieler:
            if not "Klein" in Karte.Name and not "Groß" in Karte.Name:
                print(Karte)
                if Feld_Spieler[Karte] == []:
                    print("\n")
                Dings = 0
                for LW in Feld_Spieler[Karte]:
                    print("->")
                    print(LW)
                    Dings += 1
                    if Dings == len(Feld_Spieler[Karte]):
                        print("\n")
        for Karte in Feld[Spieler]:
            if "Groß" in Karte.Name:
                print(Karte)
                if Feld_Spieler[Karte] == []:
                    print("\n")
                Dings = 0
                for LW in Feld_Spieler[Karte]:
                    print("->")
                    print(LW)
                    Dings += 1
                    if Dings == len(Feld_Spieler[Karte]):
                        print("\n")

#später für Züge
def Zug(Spieler):
    global Aus
    global Spieler_Zug
    Aus = True
    Spieler_Zug = False
    Ablage_Spieler = Ablage[Spieler]
    Feld_Spieler = Feld[Spieler]
    Ablage_Spieler = Ablage[Spieler]
    WAS = Werteverbesserung_Anzahl[Spieler]
    #Ablage und Feld ausgeben
    print("\n\n" + Spieler + "s Zug (" + Str_Übrig + ")")
    print("\nAblage:")
    Ausgabe(Ablage[Spieler])
    print("\nFeld:")
    Ausgabe_Feld()
    #Aussetzen?
    if Frost_Dict[Spieler] > 0:
        Frost_Dict[Spieler] -= 1
        print("Du musst diesen Zug aussetzen.")
        Aus = False
        Spieler_Zug = True
    #Input
    while Spieler_Zug == False:
        Input_ = input("\n")
        Input = Input_.strip()
        #Überspringen/Beenden
        if Input == "":
            Spieler_Zug = True
            Aus = False
        #Regeln
        elif Input == "Regeln":
            Regeln()
        #Kombi
        elif "+" in Input:
            Add(Input)
        #Schwarzer Trank
        elif Input == "Schwarzer Trank" or Input == "schwarzer Trank" or Input == "Schwarzer trank" or Input== "schwarzer Trank":
            if Schwarzer_Trank in Ablage[Spieler]:
                while True:
                    Gegner = random.choice(Alle_Spieler)
                    if not Spieler == Gegner:
                        break
                print("Ausgewählter Spieler: " + Gegner)
                VG = Verbesserung[Gegner]
                Gegner_LW = []
                for LW in Ablage[Gegner]:
                    if LW in Alle_Lebewesen:
                        Gegner_LW.append(LW)
                Feld_Gegner = Feld[Gegner]
                for LR in Feld_Gegner:
                    for LW in Feld_Gegner[LR]:
                        Gegner_LW.append(LW)
                LW = random.choice(Gegner_LW)
                print("Ausgewähltes Lebewesen:\n")
                if LW in Verbesserung[Gegner]:
                    VGK = VG[LW]
                    LW.Punkte += VGK["Punkte"]
                    LW.Angriff += VGK["Angriff"]
                    LW.Verteidigung += VGK["Verteidigung"]
                    for LR in VGK["Lebensräume"]:
                        LWLR = LW.Lebensraum
                        LWLR.append(LR)
                if Modus == "1":
                    repr(LW)
                elif Modus == "2":
                    str(LW)
                if LW in Verbesserung[Gegner]:
                    VGK = VG[LW]
                    LW.Punkte -= VGK["Punkte"]
                    LW.Angriff -= VGK["Angriff"]
                    LW.Verteidigung -= VGK["Verteidigung"]
                    for LR in VGK["Lebensräume"]:
                        LWLR = LW.Lebensraum
                        LWLR.remove(LR)
                print("\n------->\n")
                if not LW in Verbesserung_Spieler:
                    Counter_Dict[Gegner].update({LW:False})
                    Einmal_Dict[Gegner].update({LW:False})
                    Verbesserung[Gegner].update({LW:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                VGK = VG[LW]
                VGK["Punkte"] -= 5
                VGK["Angriff"] -= 5
                VGK["Verteidigung"] -= 5
                if (LW.Punkte + VGK["Punkte"]) < 0:
                    VGK["Punkte"] = 0 - LW.Punkte
                if (LW.Angriff + VGK["Angriff"]) < 0:
                    VGK["Angriff"] = 0 - LW.Angriff
                if (LW.Verteidigung + VGK["Verteidigung"]) < 0:
                    VGK["Verteidigung"] = 0 - LW.Verteidigung
                LW.Punkte += VGK["Punkte"]
                LW.Angriff += VGK["Angriff"]
                LW.Verteidigung += VGK["Verteidigung"]
                for LR in VGK["Lebensräume"]:
                    LWLR = LW.Lebensraum
                    LWLR.append(LR)
                if Modus == "1":
                    repr(LW)
                elif Modus == "2":
                    str(LW)
                LW.Punkte -= VGK["Punkte"]
                LW.Angriff -= VGK["Angriff"]
                LW.Verteidigung -= VGK["Verteidigung"]
                for LR in VGK["Lebensräume"]:
                    LWLR = LW.Lebensraum
                    LWLR.remove(LR)
                Spieler_Zug = True
                Ablage[Spieler].remove(Schwarzer_Trank)
            else:
                print("Du besitzt diese Karte nicht.")
        #Lebensraum auf Feld
        else:
            Counter_Input = 0
            for Karte in Ablage[Spieler]:
                Counter_Input += 1
                if Input == Karte.Name:
                    if Karte in Alle_Lebensraum:
                        if Karte not in Feld[Spieler]:
                            Ablage[Spieler].remove(Karte)
                            Feld[Spieler].update({Karte:[]})
                            Spieler_Zug = True
                            break
                        else:
                            print("Du kannst nur einmal denselben Lebensraum auf dem Feld haben.")
                            break
                    else:
                        print("Du kannst nur Lebensräume auf dem Feld platzieren.")
                        break
                elif Counter_Input == len(Ablage[Spieler]):
                    print("Du besitzt diese Karte nicht.")
        #Ablage und Feld ausgeben
        if not Aus == False:
            print("\nAblage:")
            Ausgabe(Ablage[Spieler])
            print("\nFeld:")
            Ausgabe_Feld()
    #Drachenei brüten
    #Werte minus 1 und Drachenei in Drachen nach einem Zug
    D = False
    for Wert in Drachenei_Dict[Spieler]:
        Drachenei_Dict[Spieler].remove(Wert)
        Wert -= 1
        Drachenei_Dict[Spieler].append(Wert)
        if Wert == 0:
            Drachenei_Dict[Spieler].remove(Wert)
            for LR in Feld_Spieler:
                for LW in Feld_Spieler[LR]:
                    if LW.Name == "Drachenei":
                        Feld_Spieler[LR].remove(LW)
                        for Karte in Alle_Karten:
                            if Karte.Name == "Drache":
                                Feld_Spieler[LR].append(Karte)
                                break
                        D = True
                        break
                if D == True:
                    break
    #Neue Counter für neue Dracheneier
    Counter = 0
    for LR in Feld_Spieler:
        for LW in Feld_Spieler[LR]:
            if LW.Name == "Drachenei":
                Counter += 1
    while Counter > len(Drachenei_Dict[Spieler]):
        Drachenei_Dict[Spieler].append(1)
    #Verbesserung nicht kleiner 0
    Verbesserung_Spieler = Verbesserung[Spieler]
    for Karte in Verbesserung_Spieler:
        VSK = Verbesserung_Spieler[Karte]
        if (Karte.Punkte + VSK["Punkte"]) < 0:
            VSK["Punkte"] = 0 - Karte.Punkte
        if (Karte.Angriff + VSK["Angriff"]) < 0:
            VSK["Angriff"] = 0 - Karte.Angriff
        if (Karte.Verteidigung + VSK["Verteidigung"]) < 0:
            VSK["Verteidigung"] = 0 - Karte.Verteidigung
    #Werteverbesserungskarten
    for WV_Karte in Werteverbesserung_Anzahl[Spieler]:
        Jetzt_Anzahl = 0
        for LR in Feld[Spieler]:
            for LW in Feld_Spieler[LR]:
                if LW == WV_Karte:
                    if (LW == Friedensengel) or (LW == Diebische_Elster):
                        Jetzt_Anzahl += 3
                    else:
                        Jetzt_Anzahl += 1   
        WASK = WAS[WV_Karte] #Werteverbesserung_Anzahl[Spieler[Karte]] -> [0] = Unverbrauchte/Mögliche, [1] = letzte Anzahl
        WASK[0] += (Jetzt_Anzahl - WASK[1])
        WASK[1] = Jetzt_Anzahl
        if WASK[0] < 0 or WASK[1] < 0:
            print("Fehler Werteverbesserungskarten, Dict Werte negativ")
            
#Kombi
def Add(Karten):
    global Spieler_Zug
    global Spieler
    Ablage_Spieler = Ablage[Spieler]
    Feld_Spieler = Feld[Spieler]
    Neue_Karte = False
    EDS = Einmal_Dict[Spieler]
    for Karte in EDS:
        EDS[Karte] = True
    WAS = Werteverbesserung_Anzahl[Spieler]
    Verbesserung_Spieler = Verbesserung[Spieler]
    Extra = False
    #Karten und Namen
    Karten_Liste = Karten.split("+")
    if len(Karten_Liste) == 3:
        if Karten_Liste[2] == "":
            Extra = True
            Karten_Liste.remove(Karten_Liste[2])
    Name_Karte_1 = Karten_Liste[0].strip()
    Name_Karte_2 = Karten_Liste[1].strip()
    Karte_1 = False
    Karte_2 = False
    for Karte in Alle_Karten:
        if Name_Karte_1 == Karte.Name:
            Karte_1 = Karte
        if Name_Karte_2 == Karte.Name:
            Karte_2 = Karte
    if (not Karte_1 == False) and (not Karte_2 == False):
        Gesuchte_Kombi_1 = Karte_1.Name + "+" + Karte_2.Name
        Gesuchte_Kombi_2 = Karte_2.Name + "+" + Karte_1.Name
        #Ort und Besitz?
        LR_1 = False
        LR_2 = False
        LR_Neu = False
        #Karte_1
        Ort_1 = False
        for Liste in Feld_Spieler:
            if Karte_1 in Feld_Spieler[Liste]:
                LR_1 = Liste
                Ort_1 = Feld_Spieler[Liste]
                break
        if Ort_1 == False:
            if Karte_1 in Feld[Spieler]:
                Ort_1 = Feld[Spieler]
        if Ort_1 == False:
            if Karte_1 in Ablage[Spieler]:
                Ort_1 = Ablage[Spieler]
        #Karte_2
        Ort_2 = False
        #Doppelte Karte/Karte 1 = Karte 2
        if Karte_1 == Karte_2:
            for Liste in Feld_Spieler:
                if Karte_2 in Feld_Spieler[Liste]:
                    if not Ort_1 == Feld_Spieler[Liste]:
                        LR_2 = Liste
                        Ort_2 = Feld_Spieler[Liste]
                        break
                    else:
                        Counter = 0
                        for Krt in Feld_Spieler[Liste]:
                            if Krt == Karte_2:
                                Counter += 1
                        if Counter >= 2:
                            LR_2 = Liste
                            Ort_2 = Feld_Spieler[Liste]
                            break
            if Ort_2 == False:
                if Karte_2 in Feld[Spieler]:
                    if not Ort_1 == Feld[Spieler]:
                        Ort_2 = Feld[Spieler]
                    else:
                        Counter = 0
                        for Krt in Feld[Spieler]:
                            if Krt == Karte_2:
                                Counter += 1
                        if Counter >= 2:
                            Ort_2 = Feld[Spieler]
            if Ort_2 == False:
                if Karte_2 in Ablage[Spieler]:
                    if not Ort_1 == Ablage[Spieler]:
                        Ort_2 = Ablage[Spieler]
                    else:
                        Counter = 0
                        for Krt in Ablage[Spieler]:
                            if Krt == Karte_2:
                                Counter += 1
                        if Counter >= 2:
                            Ort_2 = Ablage[Spieler]
        #Nicht doppelt
        else:
            for Liste in Feld_Spieler:
                if Karte_2 in Feld_Spieler[Liste]:
                    LR_2 = Liste
                    Ort_2 = Feld_Spieler[Liste]
                    break
            if Ort_2 == False:
                if Karte_2 in Feld[Spieler]:
                    Ort_2 = Feld[Spieler]
            if Ort_2 == False:
                if Karte_2 in Ablage[Spieler]:
                    Ort_2 = Ablage[Spieler]
        #Besitz?/andere Fehler
        if len(Karten_Liste) > 2 or len(Karten_Liste) < 2:
            print("Du kannst nur zwei Karten kombinieren.")
        elif Karte_1 == False or Karte_2 == False:
            print("Diese Karten existieren nicht.")
        elif Ort_1 == False or Ort_2 == False:
            print("Du besitzt eine oder beide Karten nicht.")
        #Extrafunktionen
        elif Extra == True:
            Counter = 0
            Reihe = [Karte_1, Karte_2]
            Test = False
            for E_Karte in Reihe:
                Counter += 1
                if E_Karte == Karte_1:
                    Andere_Karte = Karte_2
                    Ort = Ort_1
                    Anderer_Ort = Ort_2
                    Anderer_LR = LR_2
                else:
                    Andere_Karte = Karte_1
                    Ort = Ort_2
                    Anderer_Ort = Ort_1
                    Anderer_LR = LR_1
                if E_Karte in WAS:
                    WASK = WAS[E_Karte]
                #Parasit
                if E_Karte == Parasit:
                    if Andere_Karte in Alle_Lebewesen:
                        if WASK[0] > 0:
                            if not E_Karte in Verbesserung_Spieler:
                                Counter_Dict[Spieler].update({E_Karte:False})
                                Einmal_Dict[Spieler].update({E_Karte:False})
                                Verbesserung_Spieler.update({E_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                            VSK = Verbesserung_Spieler[E_Karte]
                            VSK["Punkte"] += Andere_Karte.Punkte
                            VSK["Angriff"] += Andere_Karte.Angriff
                            VSK["Verteidigung"] += Andere_Karte.Verteidigung
                            if not Andere_Karte in Verbesserung_Spieler:
                                Counter_Dict[Spieler].update({Andere_Karte:False})
                                Einmal_Dict[Spieler].update({Andere_Karte:False})
                                Verbesserung_Spieler.update({Andere_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                            VSK = Verbesserung_Spieler[Andere_Karte]
                            VSK["Punkte"] -= 4
                            VSK["Angriff"] -= 4
                            VSK["Verteidigung"] -= 4
                            WASK[0] -= 1
                            Spieler_Zug = True
                        else:
                            print("Fähigkeit kann nur einmal angewandt werden, Parasit muss auf dem Feld platziert sein.")
                    else:
                        print("Kann nur die Werte von Lebewesen aufnehmen.")
                #Werteverbesserungskarte
                elif E_Karte in Werteverbesserung_Übersicht:
                    if Andere_Karte in Alle_Lebewesen:
                        if WASK[0] > 0:
                            if not Andere_Karte in Verbesserung_Spieler:
                                Counter_Dict[Spieler].update({Andere_Karte:False})
                                Einmal_Dict[Spieler].update({Andere_Karte:False})
                                Verbesserung_Spieler.update({Andere_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                            VSK = Verbesserung_Spieler[Andere_Karte]
                            VSK["Punkte"] += Werteverbesserung_Übersicht[E_Karte]
                            VSK["Angriff"] += Werteverbesserung_Übersicht[E_Karte]
                            VSK["Verteidigung"] += Werteverbesserung_Übersicht[E_Karte]
                            WASK[0] -= 1
                            Spieler_Zug = True
                        else:
                            print("Fähigkeit kann nur einmal angewandt werden, Karte muss auf dem Feld platziert sein.")
                    else:
                        print("Kann nur die Werte von Lebewesen verbessern.")
                #Mehr Lebensräume
                elif E_Karte in ExtraLRs:
                    if Andere_Karte in Alle_Lebewesen:
                        if not Ort == Ablage[Spieler]:
                            #Alle?
                            Gesamt_LRs = []
                            for LR in Andere_Karte.Lebensraum:
                                Gesamt_LRs.append(LR)
                            if Andere_Karte in Verbesserung_Spieler:
                                VSK = Verbesserung_Spieler[Andere_Karte]
                                for LR in VSK["Lebensräume"]:
                                    Gesamt_LRs.append(LR)
                            if "Alle" in Gesamt_LRs:
                                print("Dieses Lebewesen kann bereits in allen Lebensräumen leben.")
                            else:
                                #Zufall
                                if ExtraLRs[E_Karte] == "Zufall":
                                    LRs_Kopie = LRs.copy()
                                    for LR in Gesamt_LRs:
                                        if not LR == "Wonderland":
                                            LRs_Kopie.remove(LR)
                                    Neu = random.choice(LRs_Kopie)
                                else:
                                    Neu = ExtraLRs[E_Karte]
                                if not Andere_Karte in Verbesserung_Spieler:
                                    Counter_Dict[Spieler].update({Andere_Karte:False})
                                    Einmal_Dict[Spieler].update({Andere_Karte:False})
                                    Verbesserung_Spieler.update({Andere_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                                VSK = Verbesserung_Spieler[Andere_Karte]
                                VSK["Lebensräume"].append(Neu)
                                Test_Liste = []
                                for LR in Andere_Karte.Lebensraum:
                                    if not LR == "Wonderland":
                                        Test_Liste.append(LR)
                                for LR in VSK["Lebensräume"]:
                                    Test_Liste.append(LR)
                                if len(Test_Liste) >= 4:
                                    VSK["Lebensräume"] = ["Alle"]
                        else:
                            print("Platziere Lebewesen auf dem Feld, um ihre Extrafunktion zu nutzen.")
                    else:
                        print("Kann nur auf Lebewesen angewandt werden.")
                #Friedensengel
                elif E_Karte == Friedensengel:
                    if Andere_Karte in Alle_Lebensraum:
                        if WASK[0] > 0:
                            if "Klein" in Andere_Karte.Name:
                                if "Magisch" in Andere_Karte.Name:
                                    Neue_Karte = Magisches_Kleines_Wonderland
                                else:
                                    Neue_Karte = Kleines_Wonderland
                            elif "Groß" in Andere_Karte.Name:
                                if "Magisch" in Andere_Karte.Name:
                                    Neue_Karte = Magisches_Großes_Wonderland
                                else:
                                    Neue_Karte = Großes_Wonderland
                            else:
                                if "Magisch" in Andere_Karte.Name:
                                    Neue_Karte = Magisches_Wonderland
                                else:
                                    Neue_Karte = Wonderland
                            if Andere_Karte in Feld[Spieler]:
                                Feld_Spieler.update({Neue_Karte:[]})
                                for LW in Feld_Spieler[Andere_Karte]:
                                    Feld_Spieler[Neue_Karte].append(LW)
                                del Feld_Spieler[Andere_Karte]
                            elif Andere_Karte in Ablage[Spieler]:
                                Ablage[Spieler].append(Neue_Karte)
                                Ablage[Spieler].remove(Andere_Karte)
                            Spieler_Zug = True
                            WASK[0] -= 1
                        else:
                            print("Muss auf dem Feld platziert sein und kann nur 3 Mal angewandt werden.")
                    else:
                        print("Extrafunktion kann nur auf Lebensräume angewandt werden.")
                #Zauberer
                elif E_Karte == Zauberer:
                    if Andere_Karte in Alle_Elemente:
                        if not Ort == Ablage[Spieler]:
                            for Trank in Tränke_Kombi:
                                if Andere_Karte in Tränke_Kombi[Trank]:
                                    Neue_Karte = Trank
                                    break
                            Ablage_Spieler.append(Neue_Karte)
                            Ablage_Spieler.remove(Andere_Karte)
                            Spieler_Zug = True
                        else:
                            print("Platziere den Zauberer im Feld um seine Funktion zu nutzen.")
                    else:
                        print("Zauberer kann nur Elemente in Tränke verwandeln.")
                #Dunkler Magier
                elif E_Karte == Dunkler_Magier:
                    if Andere_Karte in Alle_Elemente:
                        if not Ort == Ablage[Spieler]:
                            for Gift in Gifte_Kombi:
                                if Andere_Karte in Gifte_Kombi[Gift]:
                                    Neue_Karte = Gift
                                    break
                            Ablage_Spieler.append(Neue_Karte)
                            Ablage_Spieler.remove(Andere_Karte)
                            Spieler_Zug = True
                        else:
                            print("Platziere den Dunklen Magier im Feld um seine Funktion zu nutzen.")
                    else:
                        print("Dunkler Magier kann nur Elemente in Gifte verwandeln.")
                #Urwolf
                elif E_Karte == Urwolf:
                    if Andere_Karte in Alle_Lebewesen:
                        if WASK[0] > 0:
                            Weiter = True
                            if Andere_Karte.Punkte > Werwolf.Punkte:
                                print("Die Karte ist bereits besser als eine Werwolf-Karte.")
                                Input = input("Trotzdem tauschen?")
                                if Input == "Ja" or input == "ja":
                                    Weiter = True
                                else:
                                    Weiter = False
                            if not Anderer_Ort == Ablage[Spieler]:
                                if not Anderer_LR.Art == "Wald":
                                    print("Der Lebensraum ist für einen Werwolf nicht geeignet. Wähle ein Lebewesen in einem Wald oder in der Ablage.")
                                    Weiter = False
                            if Weiter == True:
                                Anderer_Ort.remove(Andere_Karte)
                                Anderer_Ort.append(Werwolf)
                                if Andere_Karte in Verbesserung_Spieler:
                                    if not Werwolf in Verbesserung_Spieler:
                                        Counter_Dict[Spieler].update({Werwolf:False})
                                        Einmal_Dict[Spieler].update({Werwolf:False})
                                        Verbesserung_Spieler.update({Werwolf:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                                    VSK = Verbesserung_Spieler[Werwolf]
                                    VSK["Punkte"] += Werteverbesserung_Übersicht[Andere_Karte]
                                    VSK["Angriff"] += Werteverbesserung_Übersicht[Andere_Karte]
                                    VSK["Verteidigung"] += Werteverbesserung_Übersicht[Andere_Karte]
                                    del Verbesserung_Spieler[Andere_Karte]
                                Spieler_Zug = True
                                WASK[0] -= 1
                        else:
                            print("Kann nur einmal im Spiel angewandt werden, Karte muss auf dem Feld platziert sein.")
                    else:
                        print("Kann nur auf Lebewesen angewandt werden.")
                else:
                    Test = True
                if Counter == 1 and Test == False:
                    break
                elif Counter == 2 and Test == True:
                    print("Keine der Karten hat eine Extrafunktion.")
        #LW bewegen
        elif (Karte_1 in Alle_Lebensraum and Karte_2 in Alle_Lebewesen) or (Karte_2 in Alle_Lebensraum and Karte_1 in Alle_Lebewesen):
            if Karte_1 in Alle_Lebensraum:
                LR_Karte = Karte_1
                LW_Karte = Karte_2
            else:
                LR_Karte = Karte_2
                LW_Karte = Karte_1
            #LR auf Feld
            Feld_Test = False
            if LR_Karte in Feld_Spieler:
                Feld_Test = True
            else:
                print("Platziere den Lebensraum erst auf dem Feld.")
            #Größe
            Voll_Test = False
            Art_Test = False
            if Feld_Test == True:
                Alte_LW = Feld_Spieler[LR_Karte]
                Größe = LR_Karte.Größe
                if LR_Karte in EDS:
                    if EDS[LR_Karte] == True:
                        Add_Größe = Verbesserung_Spieler[LR_Karte]
                        Größe = LR_Karte.Größe + Add_Größe                    
                if len(Alte_LW) < Größe:
                    Voll_Test = True
                else:
                    print("Dieser Lebensraum ist bereits voll.")
                #Art
                Art_Test = False
                Zusatz_LR = []
                if LW_Karte in EDS:
                    if EDS[LW_Karte] == True:
                        VSK = Verbesserung_Spieler[LW_Karte]
                        for LR in VSK["Lebensräume"]:
                            Zusatz_LR.append(LR)
                for LR in LW_Karte.Lebensraum:
                    if LR == LR_Karte.Art or LR == "Alle":
                        Art_Test = True
                        break
                for LR in Zusatz_LR:
                    if LR == LR_Karte.Art or LR == "Alle":
                        Art_Test = True
                        break
                if Art_Test == False:
                    print("Dieser Lebensraum ist für das Lebewesen nicht geeignet.")
            #Hinzufügen?
            if Voll_Test == True and Art_Test == True and Feld_Test == True:
                if LW_Karte in Ablage_Spieler:
                    Spieler_Zug = True
                if LW_Karte == Karte_1:
                    A = Karte_1
                    B = Karte_2
                    Ort = Ort_1                    
                elif LW_Karte == Karte_2:
                    A = Karte_2
                    B = Karte_1
                    Ort = Ort_2
                Feld_Spieler[B].append(A)
                if A in Ablage[Spieler]:
                    Ablage[Spieler].remove(A)
                else:
                    Ort.remove(A)
        #Tränke
        elif "Trank" in Karte_1.Name or "Trank" in Karte_2.Name:
            if "Trank" in Karte_1.Name:
                Trank_Karte = Karte_1
                Andere_Karte = Karte_2
            else:
                Trank_Karte = Karte_2
                Andere_Karte = Karte_1
            #Lebensraum-Tränke
            if "Lebensraum" in Trank_Karte.Beschreibung or "Duftender Trank" == Trank_Karte.Name:
                if Andere_Karte in Alle_Lebensraum:
                    #Vergrößerungs-Trank
                    if Trank_Karte.Name == "Vergrößerungs-Trank":
                        if not Andere_Karte in Verbesserung_Spieler:
                            Counter_Dict[Spieler].update({Andere_Karte:False})
                            Einmal_Dict[Spieler].update({Andere_Karte:False})
                            Verbesserung_Spieler.update({Andere_Karte:0})
                        Verbesserung_Spieler[Andere_Karte] += 1
                        Spieler_Zug = True
                        Ablage[Spieler].remove(Trank_Karte)
                    #Duftender Trank
                    elif Trank_Karte.Name == "Duftender Trank":
                        if "Klein" in Andere_Karte.Name:
                            if "Magisch" in Andere_Karte.Name:
                                Neue_Karte = Magisches_Kleines_Wonderland
                            else:
                                Neue_Karte = Kleines_Wonderland
                        elif "Groß" in Andere_Karte.Name:
                            if "Magisch" in Andere_Karte.Name:
                                Neue_Karte = Magisches_Großes_Wonderland
                            else:
                                Neue_Karte = Großes_Wonderland
                        else:
                            if "Magisch" in Andere_Karte.Name:
                                Neue_Karte = Magisches_Wonderland
                            else:
                                Neue_Karte = Wonderland
                        if Andere_Karte in Feld[Spieler]:
                            Feld_Spieler.update({Neue_Karte:[]})
                            for LW in Feld_Spieler[Andere_Karte]:
                                Feld_Spieler[Neue_Karte].append(LW)
                            del Feld_Spieler[Andere_Karte]
                        elif Andere_Karte in Ablage[Spieler]:
                            Ablage[Spieler].append(Neue_Karte)
                            Ablage[Spieler].remove(Andere_Karte)
                        Spieler_Zug = True
                        Ablage[Spieler].remove(Trank_Karte)
                else:
                    print("Du kannst diesen Trank nur auf Lebensräume anwenden.")
            #Lebewesen-Tränke     
            elif "Lebewesen" in Trank_Karte.Beschreibung:
                if Andere_Karte in Alle_Lebewesen:
                    Mehr_LRs_Tränke = ["Heißer Trank", "Wässriger Trank", "Matschiger Trank", "Blubbernder Trank", "Verkohlter Trank"]
                    Werte_Tränke = ["Güldener Trank", "Level-Up Trank", "Glitzernder Trank", "Himmlischer Trank"]
                    #Mehr LR Tränke
                    if Trank_Karte.Name in Mehr_LRs_Tränke:
                        if Trank_Karte.Name == "Heißer Trank":
                            LR = "Wüste"
                        elif Trank_Karte.Name == "Wässriger Trank":
                            LR = "See"
                        elif Trank_Karte.Name == "Matschiger Trank":
                            LR = "Wald"
                        elif Trank_Karte.Name == "Blubbernder Trank":
                            LR = "Berge"
                        elif Trank_Karte.Name == "Verkohlter Trank":
                            LR = "Alle"
                        if not Andere_Karte in Verbesserung_Spieler:
                            Counter_Dict[Spieler].update({Andere_Karte:False})
                            Einmal_Dict[Spieler].update({Andere_Karte:False})
                            Verbesserung_Spieler.update({Andere_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                        VSK = Verbesserung_Spieler[Andere_Karte]
                        if not LR in VSK["Lebensräume"]:
                            VSK["Lebensräume"].append(LR)
                        Spieler_Zug = True
                        Ablage[Spieler].remove(Trank_Karte)
                    #Werte Tränke
                    elif Trank_Karte.Name in Werte_Tränke:
                        if Trank_Karte.Name == "Güldener Trank":
                            Wert = 3
                        elif Trank_Karte.Name == "Level-Up Trank":
                            Wert = 5
                        elif Trank_Karte.Name == "Glitzernder Trank":
                            Wert = 7
                        elif Trank_Karte.Name == "Himmlischer Trank":
                            Wert = 10
                        if not Andere_Karte in Verbesserung_Spieler:
                            Counter_Dict[Spieler].update({Andere_Karte:False})
                            Einmal_Dict[Spieler].update({Andere_Karte:False})
                            Verbesserung_Spieler.update({Andere_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                        VSK = Verbesserung_Spieler[Andere_Karte]
                        VSK["Punkte"] += Wert
                        VSK["Angriff"] += Wert
                        VSK["Verteidigung"] += Wert
                        Spieler_Zug = True
                        Ablage[Spieler].remove(Trank_Karte)
                    #Dolly Trank
                    elif Trank_Karte.Name == "Dolly Trank":
                        Ablage[Spieler].append(Andere_Karte)
                        Spieler_Zug = True
                        Ablage[Spieler].remove(Trank_Karte)
                else:
                    print("Du kannst diesen Trank nur auf Lebenwesen anwenden.")
        #Schleifen-Start/Kombi oder nicht        
        else:
            Counter_Add = 0
            for Karte in Alle_Karten:
                Counter_Add += 1
                #Kombi
                if Gesuchte_Kombi_1 in Karte.Kombi or Gesuchte_Kombi_2 in Karte.Kombi:
                    Neue_Karte = Karte
                    #LR
                    if Karte_1 in Alle_Lebensraum or Karte_2 in Alle_Lebensraum:
                        if Karte_1 in Alle_Lebensraum:
                            LR_Karte = Karte_1
                            Andere_Karte = Karte_2
                        else:
                            LR_Karte = Karte_2
                            Andere_Karte = Karte_1
                        #LR + LR
                        if Andere_Karte in Alle_Lebensraum:
                            #min. eine Feld
                            if Ort_1 == Feld_Spieler or Ort_2 == Feld_Spieler:
                                Neue_LW = []
                                if Ort_1 == Feld_Spieler:
                                    LW_1 = Feld_Spieler[Karte_1]
                                    for LW in LW_1:
                                        Neue_LW.append(LW)
                                    del Feld_Spieler[Karte_1]
                                else:
                                    Ablage_Spieler.remove(Karte_1)
                                if Ort_2 == Feld_Spieler:
                                    LW_2 = Feld_Spieler[Karte_2]
                                    for LW in LW_2:
                                        Neue_LW.append(LW)
                                    del Feld_Spieler[Karte_2]
                                else:
                                    Ablage_Spieler.remove(Karte_2)
                                Feld_Spieler.update({Neue_Karte:[]})
                                if not Neue_LW == []:
                                    for LW in Neue_LW:
                                        Feld_Spieler[Neue_Karte].append(LW)
                                Spieler_Zug = True
                                break
                            #beide Ablage
                            elif Ort_1 == Ablage_Spieler and Ort_2 == Ablage_Spieler:
                                Ablage_Spieler.remove(Karte_1)
                                Ablage_Spieler.remove(Karte_2)
                                Ablage_Spieler.append(Neue_Karte)
                                Spieler_Zug = True
                                break
                        #LR + E
                        elif Andere_Karte in Alle_Elemente:
                            #LR in Feld
                            if LR_Karte in Feld_Spieler:
                                Feld_Spieler.update({Neue_Karte:[]})
                                for LW in Feld_Spieler[LR_Karte]:
                                    Feld_Spieler[Neue_Karte].append(LW)
                                del Feld_Spieler[LR_Karte]
                                Ablage_Spieler.remove(Andere_Karte)
                                Spieler_Zug = True
                                break
                            #LR in Ablage
                            elif LR_Karte in Ablage_Spieler:
                                Ablage_Spieler.remove(Karte_1)
                                Ablage_Spieler.remove(Karte_2)
                                Ablage_Spieler.append(Neue_Karte)
                                Spieler_Zug = True
                                break
                    #LW
                    elif Karte_1 in Alle_Lebewesen or Karte_2 in Alle_Lebewesen:
                        if Karte_1 in Alle_Lebewesen:
                            LW_Karte = Karte_1
                            Andere_Karte = Karte_2
                        else:
                            LW_Karte = Karte_2
                            Andere_Karte = Karte_1
                        #LW + LW
                        if Andere_Karte in Alle_Lebewesen:
                            #beide Ablage oder beide selber LR
                            if Ort_1 == Ort_2:
                                Ort_1.remove(Karte_1)
                                Ort_2.remove(Karte_2)
                                Ort_1.append(Neue_Karte)
                                Spieler_Zug = True
                                break
                            #unterschiedliche LRs
                            else:
                                #Falsch
                                if LR_1 == False or LR_2 == False:
                                    print("Du kannst nur innerhalb des Feldes oder der Ablage kombinieren.")
                                    break
                                #Ort/geeigneter LR
                                Fertig = False
                                Lebensräume = []
                                for LR in Neue_Karte.Lebensraum:
                                    Lebensräume.append(LR)
                                if Neue_Karte in EDS:
                                    if EDS[Neue_Karte] == True:
                                        VSK = Verbesserung_Spieler[Neue_Karte]
                                        for LR in VSK["Lebensräume"]:
                                            Lebensräume.append(LR)
                                for LR in Lebensräume:
                                    if LR == LR_1.Art or LR == "Alle":
                                        Ort_1.append(Neue_Karte)
                                        Ort_1.remove(Karte_1)
                                        Ort_2.remove(Karte_2)
                                        Fertig = True
                                        Spieler_Zug = True
                                        LR_Neu = LR_1
                                        break
                                    elif LR == LR_2.Art:
                                        Ort_2.append(Neue_Karte)
                                        Ort_1.remove(Karte_1)
                                        Ort_2.remove(Karte_2)
                                        Fertig = True
                                        Spieler_Zug = True
                                        LR_Neu = LR_2
                                        break
                                if Spieler_Zug == True:
                                    break
                                if Fertig == False:
                                    print("Keiner der beiden Lebensräume ist geeignet für das neue Lebewesen.")
                                    break
                        #LW + E
                        elif Andere_Karte in Alle_Elemente:
                            #in Ablage
                            if LW_Karte in Ablage_Spieler:
                                Ablage_Spieler.remove(LW_Karte)
                                Ablage_Spieler.remove(Andere_Karte)
                                Ablage_Spieler.append(Neue_Karte)
                                Spieler_Zug = True
                                break
                            #LW auf Feld/in LR
                            else:
                                Lebensräume = []
                                for LR in Neue_Karte.Lebensraum:
                                    Lebensräume.append(LR)
                                if Neue_Karte in EDS:
                                    if EDS[Neue_Karte] == True:
                                        VSK = Verbesserung_Spieler[Neue_Karte]
                                        for LR in VSK["Lebensräume"]:
                                            Lebensräume.append(LR)
                                if LW_Karte == Karte_1:
                                    for LR in Lebensräume:
                                        if LR == LR_1.Art or LR == "Alle":
                                            Ort_1.append(Neue_Karte)
                                            Ort_1.remove(Karte_1)
                                            Ablage_Spieler.remove(Karte_2)
                                            Spieler_Zug = True
                                            LR_Neu = LR_1
                                            break
                                    if Spieler_Zug == False:
                                        print("Der Lebensraum ist nicht geeignet für das neue Lebewesen.")
                                        break
                                    break
                                elif LW_Karte == Karte_2:
                                    for LR in Lebensräume:
                                        if LR == LR_2.Art or LR == "Alle":
                                            Ort_2.append(Neue_Karte)
                                            Ort_2.remove(Karte_2)
                                            Ablage_Spieler.remove(Karte_2)
                                            Spieler_Zug = True
                                            LR_Neu = LR_2
                                            break
                                    if Spieler_Zug == False:
                                        print("Der Lebensraum ist nicht geeignet für das neue Lebewesen.")
                                        break
                                    break
                    #E + E
                    elif Karte_1 in Alle_Elemente and Karte_2 in Alle_Elemente:
                        Ablage[Spieler].append(Neue_Karte)
                        Ablage[Spieler].remove(Karte_1)
                        Ablage[Spieler].remove(Karte_2)
                        Spieler_Zug = True
                        break
                #Keine Kombi möglich
                elif Counter_Add == len(Alle_Karten):
                    print("Diese Karten lassen sich nicht kombinieren.")
            #Verbesserungen
            if Spieler_Zug == True:
                #Weitergabe Verbesserungen
                if Neue_Karte in Alle_Lebensraum:
                    Counter = 0
                    if Karte_1 in Alle_Lebensraum and Karte_1 in Verbesserung_Spieler:
                        Counter += Verbesserung_Spieler[Karte_1]
                        del Verbesserung_Spieler[Karte_1]
                    if Karte_2 in Alle_Lebensraum and Karte_2 in Verbesserung_Spieler:
                        Counter += Verbesserung_Spieler[Karte_2]
                        del Verbesserung_Spieler[Karte_1]
                    if not Counter == 0:
                        if not Neue_Karte in Verbesserung_Spieler:
                            Counter_Dict[Spieler].update({Neue_Karte:False})
                            Einmal_Dict[Spieler].update({Neue_Karte:False})
                            Verbesserung_Spieler.update({Neue_Karte:0})
                        Verbesserung_Spieler[Neue_Karte] += Counter
                elif Neue_Karte in Alle_Lebewesen:
                    Counter_P = 0
                    Counter_A = 0
                    Counter_V = 0
                    if Karte_1 in Alle_Lebewesen and Karte_1 in Verbesserung_Spieler:
                        VSK = Verbesserung_Spieler[Karte_1]
                        Counter_P += VSK["Punkte"]
                        Counter_A += VSK["Angriff"]
                        Counter_V += VSK["Verteidigung"]
                        del Verbesserung_Spieler[Karte_1]
                    if Karte_2 in Alle_Lebewesen and Karte_2 in Verbesserung_Spieler:
                        VSK = Verbesserung_Spieler[Karte_2]
                        Counter_P += VSK["Punkte"]
                        Counter_A += VSK["Angriff"]
                        Counter_V += VSK["Verteidigung"]
                        del Verbesserung_Spieler[Karte_2]
                    if not (Counter_P == 0 and Counter_A == 0 and Counter_V == 0):
                        if not Neue_Karte in Verbesserung_Spieler:
                            Counter_Dict[Spieler].update({Neue_Karte:False})
                            Einmal_Dict[Spieler].update({Neue_Karte:False})
                            Verbesserung_Spieler.update({Neue_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                        VSK = Verbesserung_Spieler[Neue_Karte]
                        VSK["Punkte"] += Counter_P
                        VSK["Angriff"] += Counter_A
                        VSK["Verteidigung"] += Counter_V
    #Extra: Aktion mit anderem Spieler oder Joker
    elif (not Karte_1 == False) or (not Karte_2 == False):
        global Aus
        if not Karte_1 == False:
            E_Karte = Karte_1
            Andere_Name = Name_Karte_2
        else:
            E_Karte = Karte_2
            Andere_Name = Name_Karte_1
        Gegner = None
        for SP in Alle_Spieler:
            if SP == Andere_Name:
                Gegner = SP
        if Gegner == None:
            #Joker
            if E_Karte == Joker:
                WASK = WAS[Joker]
                if WASK[0] > 0:
                    Neue_Karte = None
                    if Andere_Name == "Lebewesen" or Andere_Name == "lebewesen":
                        Neue_Karte = random.choice(Start_Lebewesen)
                    elif Andere_Name == "Lebensraum" or Andere_Name == "lebensraum":
                        Neue_Karte = random.choice(Start_Lebensraum)
                    elif Andere_Name == "Element" or Andere_Name == "element":
                        Neue_Karte = random.choice(Start_Elemente)
                    if Neue_Karte == None:
                        print("Wähle zwischen Element, Lebewesen und Lebensraum.")
                    else:
                        Ablage[Spieler].append(Neue_Karte)
                        print("Neue Karte:\n")
                        if not Neue_Karte in Start_Elemente:
                            if Modus == "1":
                                print(repr(Neue_Karte))
                            elif Modus == "2":
                                print(str(Neue_Karte))
                        else:
                            print(Neue_Karte)
                        Spieler_Zug = True
                        Aus = False
                        WASK[0] -= 1
                else:
                    print("Kann nur einmal pro Runde angewandt werden, Karte muss auf dem Feld platziert sein.")
            else:
                print("Eine oder beide Karten existieren nicht.")
        else:
            #Aktion mit anderem Spieler
            VG = Verbesserung[Gegner]
            EDG = Einmal_Dict[Gegner]
            for Karte in EDG:
                EDG[Karte] = True
            #Gifte und Gefrorener Trank
            if "Gift" in E_Karte.Name or E_Karte.Name == "Gefrorener Trank":
                Werte_Gifte = [Elementares_Gift, Pampiges_Gift, Trügerisches_Gift, Blutiges_Gift]
                Aussetzen_Gifte = [Magisches_Gift, Lähmendes_Gift, Gefrorener_Trank, Eisiges_Gift]
                Zerstörungs_Gifte = [Reines_Gift, Gift_des_Vergessens]
                VG = Verbesserung[Gegner]
                #Werte Gifte
                if E_Karte in Werte_Gifte:
                    if E_Karte == Werte_Gifte[0]:
                        Wert = 3
                    elif E_Karte == Werte_Gifte[1]:
                        Wert = 5
                    elif E_Karte == Werte_Gifte[2]:
                        Wert = 7
                    elif E_Karte == Werte_Gifte[3]:
                        Wert = 10
                    Gegner_LW = []
                    for LW in Ablage[Gegner]:
                        if LW in Alle_Lebewesen:
                            Gegner_LW.append(LW)
                    Feld_Gegner = Feld[Gegner]
                    for LR in Feld_Gegner:
                        for LW in Feld_Gegner[LR]:
                            Gegner_LW.append(LW)
                    LW = random.choice(Gegner_LW)
                    print("Spieler: " + Gegner)
                    print("Ausgewähltes Lebewesen:\n")
                    if LW in Verbesserung[Gegner]:
                        VGK = VG[LW]
                        LW.Punkte += VGK["Punkte"]
                        LW.Angriff += VGK["Angriff"]
                        LW.Verteidigung += VGK["Verteidigung"]
                        for LR in VGK["Lebensräume"]:
                            LWLR = LW.Lebensraum
                            LWLR.append(LR)
                    if Modus == "1":
                        print(repr(Z_Karte))
                    elif Modus == "2":
                        print(str(Z_Karte))
                    if LW in Verbesserung[Gegner]:
                        VGK = VG[LW]
                        LW.Punkte -= VGK["Punkte"]
                        LW.Angriff -= VGK["Angriff"]
                        LW.Verteidigung -= VGK["Verteidigung"]
                        for LR in VGK["Lebensräume"]:
                            LWLR = LW.Lebensraum
                            LWLR.remove(LR)
                    print("\n------->\n")
                    if not LW in Verbesserung_Spieler:
                        Counter_Dict[Gegner].update({LW:False})
                        Einmal_Dict[Gegner].update({LW:False})
                        Verbesserung[Gegner].update({LW:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                    VGK = VG[LW]
                    VGK["Punkte"] -= Wert
                    VGK["Angriff"] -= Wert
                    VGK["Verteidigung"] -= Wert
                    if (LW.Punkte + VGK["Punkte"]) < 0:
                        VGK["Punkte"] = 0 - LW.Punkte
                    if (LW.Angriff + VGK["Angriff"]) < 0:
                        VGK["Angriff"] = 0 - LW.Angriff
                    if (LW.Verteidigung + VGK["Verteidigung"]) < 0:
                        VGK["Verteidigung"] = 0 - LW.Verteidigung
                    LW.Punkte += VGK["Punkte"]
                    LW.Angriff += VGK["Angriff"]
                    LW.Verteidigung += VGK["Verteidigung"]
                    for LR in VGK["Lebensräume"]:
                        LWLR = LW.Lebensraum
                        LWLR.append(LR)
                    if Modus == "1":
                        print(repr(Z_Karte))
                    elif Modus == "2":
                        print(str(Z_Karte))
                    LW.Punkte -= VGK["Punkte"]
                    LW.Angriff -= VGK["Angriff"]
                    LW.Verteidigung -= VGK["Verteidigung"]
                    for LR in VGK["Lebensräume"]:
                        LWLR = LW.Lebensraum
                        LWLR.remove(LR)
                    Spieler_Zug = True
                    Ablage[Spieler].remove(E_Karte)
                    Aus = False
                #Aussetzen Gifte
                elif E_Karte in Aussetzen_Gifte:
                    if E_Karte == Aussetzen_Gifte[0]:
                        Wert = 1
                    elif E_Karte == Aussetzen_Gifte[1] or E_Karte == Aussetzen_Gifte[2]:
                        Wert = 3
                    elif E_Karte == Aussetzen_Gifte[3]:
                        Wert = 5
                    Frost_Dict[Gegner] += Wert
                    if Wert == 1:
                        Druck = "einen Zug"
                    else:
                        Druck = str(Wert) + " Züge"
                    print("\n" + Gegner + " setzt " + Druck + " aus.\n")
                    Spieler_Zug = True
                    Ablage[Spieler].remove(E_Karte)
                    Aus = False
                #Zerstörungs Gifte
                elif E_Karte in Zerstörungs_Gifte:
                    Gegner_LW = []
                    for LW in Ablage[Gegner]:
                        if (LW in Alle_Lebewesen) and (LW not in Gegner_LW):
                            Gegner_LW.append(LW)
                    Feld_Gegner = Feld[Gegner]
                    for LR in Feld_Gegner:
                        for LW in Feld_Gegner[LR]:
                            if LW not in Gegner_LW:
                                Gegner_LW.append(LW)
                    if Gegner_LW == []:
                        print("Dieser Spieler besitzt keine Lebewesen.")
                    else:
                        LW_Dict = {}
                        for LW in Gegner_LW:
                            LW_Dict.update({LW:LW.Punkte})
                            if LW in Verbesserung[Gegner] and EDG[LW] == True:
                                VGK = VG[LW]
                                LW_Dict[LW] += VGK["Punkte"]
                                EDG[LW] = False
                        Werte_Liste = []
                        for LW in LW_Dict:
                            Werte_Liste.append(LW_Dict[LW])
                        Werte_Liste.sort()
                        if E_Karte == Zerstörungs_Gifte[0]:
                            for Karte in LW_Dict:
                                if Werte_Liste[0] == LW_Dict[Karte]:
                                    Z_Karte = Karte
                                    break
                        elif E_Karte == Zerstörungs_Gifte[1]:
                            for Karte in LW_Dict:
                                if Werte_Liste[-1] == LW_Dict[Karte]:
                                    Z_Karte = Karte
                                    break
                        Test = False
                        for Karte in Ablage[Gegner]:
                            if Karte == Z_Karte:
                                Ablage[Gegner].remove(Z_Karte)
                                Test = True
                                break
                        if Test == False:
                            for LR in Feld[Gegner]:
                                for LW in Feld_Gegner[LR]:
                                    if LW == Z_Karte:
                                        Feld_Gegner[LR].remove(Z_Karte)
                                        Test = True
                                        break
                                if Test == True:
                                    break
                        Counter = 0
                        for LW in Gegner_LW:
                            if LW == Z_Karte:
                                Counter += 1
                        print("Spieler: " + Gegner)
                        print("Ausgewähltes Lebewesen:\n")
                        if Z_Karte in Verbesserung[Gegner] and Counter == 1:
                            #Verbesserungen enfernen
                            CDG = Counter_Dict[Gegner]
                            del CDG[Z_Karte]
                            del EDG[Z_Karte]
                            del VG[Z_Karte]                            
                            #Verbesserungen für print
                            VGK = VG[Z_Karte]
                            Z_Karte.Punkte += VGK["Punkte"]
                            Z_Karte.Angriff += VGK["Angriff"]
                            Z_Karte.Verteidigung += VGK["Verteidigung"]
                            for LR in VGK["Lebensräume"]:
                                LWLR = Z_Karte.Lebensraum
                                LWLR.append(LR)
                        if Modus == "1":
                            print(repr(Z_Karte))
                        elif Modus == "2":
                            print(str(Z_Karte))
                        if Z_Karte in Verbesserung[Gegner] and Counter == 1:
                            VGK = VG[Z_Karte]
                            Z_Karte.Punkte -= VGK["Punkte"]
                            Z_Karte.Angriff -= VGK["Angriff"]
                            Z_Karte.Verteidigung -= VGK["Verteidigung"]
                            for LR in VGK["Lebensräume"]:
                                LWLR = Z_Karte.Lebensraum
                                LWLR.remove(LR)
                        print("\nWurde entfernt.")
                        Spieler_Zug = True
                        Ablage[Spieler].remove(E_Karte)
                        Aus = False
            #Diebische Elster
            elif E_Karte == Diebische_Elster:
                WASK = WAS[Diebische_Elster]
                if WASK[0] > 0:
                    Gegner_LW = []
                    for LW in Ablage[Gegner]:
                        if (LW in Alle_Lebewesen) and (LW not in Gegner_LW):
                            Gegner_LW.append(LW)
                    Feld_Gegner = Feld[Gegner]
                    for LR in Feld_Gegner:
                        for LW in Feld_Gegner[LR]:
                            if LW not in Gegner_LW:
                                Gegner_LW.append(LW)
                    if Gegner_LW == []:
                        print("Dieser Spieler besitzt keine Lebewesen.")
                    else:
                        LW_Dict = {}
                        for LW in Gegner_LW:
                            LW_Dict.update({LW:LW.Punkte})
                            if LW in Verbesserung[Gegner] and EDG[LW] == True:
                                VGK = VG[LW]
                                LW_Dict[LW] += VGK["Punkte"]
                                EDG[LW] = False
                        Werte_Liste = []
                        for LW in LW_Dict:
                            Werte_Liste.append(LW_Dict[LW])
                        Werte_Liste.sort()
                        for Karte in LW_Dict:
                            if Werte_Liste[0] == LW_Dict[Karte]:
                                Z_Karte = Karte
                                break
                        Test = False
                        for Karte in Ablage[Gegner]:
                            if Karte == Z_Karte:
                                Ablage[Gegner].remove(Z_Karte)
                                Test = True
                                break
                        if Test == False:
                            for LR in Feld[Gegner]:
                                for LW in Feld_Gegner[LR]:
                                    if LW == Z_Karte:
                                        Feld_Gegner[LR].remove(Z_Karte)
                                        Test = True
                                        break
                                if Test == True:
                                    break
                        Counter = 0
                        for LW in Gegner_LW:
                            if LW == Z_Karte:
                                Counter += 1
                        print("Spieler: " + Gegner)
                        print("Ausgewähltes Lebewesen:\n")
                        if Z_Karte in Verbesserung[Gegner] and Counter == 1:
                            VGK = VG[Z_Karte]
                            #Verbesserungen ins Dict bei Spieler
                            Verbesserung_Spieler = Verbesserung[Spieler]
                            if not Z_Karte in Verbesserung_Spieler:
                                Counter_Dict[Spieler].update({Z_Karte:False})
                                Einmal_Dict[Spieler].update({Z_Karte:False})
                                Verbesserung_Spieler.update({Z_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                            VSK = Verbesserung_Spieler[Z_Karte]
                            VSK["Punkte"] += VGK["Punkte"]
                            VSK["Angriff"] += VGK["Angriff"]
                            VSK["Verteidigung"] += VGK["Verteidigung"]
                            for LR in VGK["Lebensräume"]:
                                VSK["Lebensräume"].append(LR)
                            #Verbesserungen für print
                            Z_Karte.Punkte += VGK["Punkte"]
                            Z_Karte.Angriff += VGK["Angriff"]
                            Z_Karte.Verteidigung += VGK["Verteidigung"]
                            for LR in VGK["Lebensräume"]:
                                LWLR = Z_Karte.Lebensraum
                                LWLR.append(LR)
                        if Modus == "1":
                            print(repr(Z_Karte))
                        elif Modus == "2":
                            print(str(Z_Karte))
                        if Z_Karte in Verbesserung[Gegner] and Counter == 1:
                            VGK = VG[Z_Karte]
                            Z_Karte.Punkte -= VGK["Punkte"]
                            Z_Karte.Angriff -= VGK["Angriff"]
                            Z_Karte.Verteidigung -= VGK["Verteidigung"]
                            for LR in VGK["Lebensräume"]:
                                LWLR = Z_Karte.Lebensraum
                                LWLR.remove(LR)
                        print("\nWurde " + Gegner + " geklaut und " + Spieler + " gegeben.")
                        Ablage[Spieler].append(Z_Karte)
                        WASK[0] -= 1
                        Spieler_Zug = True
                        Aus = False
                else:
                    print("Fähigkeit kann nur 3 Mal angewandt werden, Diebische Elster muss auf dem Feld platziert sein.")
            #Furchtdrache
            elif E_Karte == Furchtdrache or E_Karte == Starker_Furchtdrache:
                WASK = WAS[E_Karte]
                if WASK[0] > 0:
                    if E_Karte == Furchtdrache:
                        Wert = 1
                    elif E_Karte == Starker_Furchtdrache:
                        Wert = 3
                    Frost_Dict[Gegner] += Wert
                    if Wert == 1:
                        Druck = "einen Zug"
                    else:
                        Druck = str(Wert) + " Züge"
                    print("\n" + Gegner + " setzt " + Druck + " aus.\n")
                    Spieler_Zug = True
                    Aus = False
                    WASK[0] -= 1
                else:
                    print("Extrafunktion kann nur einmal pro Runde angewandt werden, Karte muss auf dem Feld platziert sein.")
            else:
                ("Diese Karte hat keine Extrafunktion, die auf andere Spieler angewandt werden kann.")
        
    #Karten existieren nicht
    else:
        print("Eine oder beide Karten existieren nicht.")

#Modus
while True:
    Modus = input("Modus?\nPunkte (1)\nKampf (2)\n")
    if Modus == "1" or Modus == "2":
        break
    else:
        print("Ungültige Eingabe")

#Spieler
while True:
    Spieler_Input = input("Spieler? (2 bis 5 Spieler empfohlen, durch Kommas trennen)\n")
    Alle_Spieler_1 = Spieler_Input.split(",")
    Counter = 0
    Alle_Spieler = []
    while Counter <= (len(Alle_Spieler_1) - 1 ):
        Spieler = Alle_Spieler_1[Counter]
        Spieler_Neu = Spieler.strip()
        Alle_Spieler.append(Spieler_Neu)
        Counter += 1
    if len(Alle_Spieler) == 0:
            print("Ungültige Eingabe")
    else:
        Counter_Spieler = 0
        for Spieler in Alle_Spieler:
            for Anderer in Alle_Spieler:
                if Spieler == Anderer:
                    Counter_Spieler += 1
        if Counter_Spieler == len(Alle_Spieler):
            break
        else:
            print("Wähle unterschiedliche Spielernamen.")
            
#Runden und Züge
###Int Error excluden###
while True:
    Runden = int(input("Runden? (5 bis 20 Runden empfohlen, pro Runden werden neue Karten ausgegeben)\n"))
    if Runden <= 0:
        print("Ungültige Eingabe")
    else:
        break
while True:
    Züge = int(input("Züge? (5 bis 10 Züge empfohlen, pro Spieler pro Runde)\n"))
    if Züge <= 0:
        print("Ungültige Eingabe")
    else:
        break

#Anfangssatz
if Runden == 1:
    Runden_ = "eine Runde"
else:
    Runden_ = str(Runden) + " Runden"

if Züge == 1:
    Züge_ = "einem Zug"
else:
    Züge_ = str(Züge) + " Zügen"

Anfangssatz = "\nSpiel über {} mit je {} pro Spieler.".format(Runden_, Züge_)
print(Anfangssatz)

if Modus == "1":
    print("Ziel: Möglichst viele Punkte durch Kombination von Karten sammeln. Nur auf das Feld ausgespielte Karten werden gewertet.")
elif Modus == "2":
    print("Ziel: Durch Kombitation von Karten möglichst starke Lebewesen für folgende Kampfphase entwickeln. Nur auf das Feld ausgespielte Lebewesen-Karten können verwendet werden.")
print("\nViel Spaß! :D")

Ablage = {} #Ablage
Feld = {} #Feld für später
Ende_LW = {} #Kampf für Ende
Drachenei_Dict = {} #Drachenei brüten
#Werte Verbesserungs-Dict
Counter_Dict = {} #Einmal-Sicherung für Ausgabe
Einmal_Dict = {} #Einmal-Sicherung für Add
Verbesserung = {} #{Spieler:{LW_Karte:{"Punkte":xy, "Angriff":xy, "Verteidigung":xy, "Lebensräume":xy}, LR_Karte:{Größe}}
Magisch_Dict = {} #Verbesserung durch magischer LR
Stärker_Dict = {} #Verbesserung durch LR
Frost_Dict = {} #Aussetzen
Werteverbesserung_Anzahl = {} #Werteverbesserung - {Karte:[Mögliche, Letzte]}

for Spieler in Alle_Spieler:
    #1. Ausgabe
    Ablage.update({Spieler:[Urwolf]})
    Ablage[Spieler].append(random.choice(Start_Lebewesen))
    Ablage[Spieler].append(random.choice(Start_Lebensraum))
    Ablage[Spieler].append(random.choice(Start_Elemente))
    Ablage[Spieler].append(random.choice(random.choice(Nur)))
    Ablage[Spieler].append(random.choice(random.choice(Alle_Start_Karten)))
    #andere Dicts
    Feld.update({Spieler:{}})
    Ende_LW.update({Spieler:[]})
    Drachenei_Dict.update({Spieler:[]})
    Counter_Dict.update({Spieler:{}})
    Einmal_Dict.update({Spieler:{}})
    Verbesserung.update({Spieler:{}})
    Magisch_Dict.update({Spieler:{}})
    Stärker_Dict.update({Spieler:{}})
    Frost_Dict.update({Spieler:0})
    Werteverbesserung_Anzahl.update({Spieler:{Parasit:[0, 0], Friedensengel:[0, 0], Diebische_Elster:[0, 0], Furchtdrache:[0, 0], Starker_Furchtdrache:[0, 0], Joker:[0, 0], Urwolf:[0, 0]}})
    for Karte in Werteverbesserung_Übersicht:
        Werteverbesserung_Anzahl[Spieler].update({Karte:[0, 0]})
        
#Spielkern
#Runden
Runden_Counter = 0
while Runden_Counter < Runden:
    Runden_Counter += 1
    print("\nRunde " + str(Runden_Counter))
    if (Runden_Counter + 1) == Runden:
        print("Vorletzte Runde")
    elif Runden_Counter == Runden:
          print("Letzte Runde")
    Input_Enter = input("\n")
    #Karten für Runde
    if not Runden_Counter == 1:
        #Auswahlstapel
        if len(Alle_Spieler) <= 5:
            Anzahl_Auswahl_Karten = 2 * len(Alle_Spieler)
        elif len(Alle_Spieler) > 5:
            Anzahl_Auswahl_Karten = 4 * len(Alle_Spieler)
        Auswahl = []
        while Anzahl_Auswahl_Karten > 0:
            Auswahl.append(random.choice(random.choice(Alle_Start_Karten)))
            Anzahl_Auswahl_Karten -= 1
        #zufällige Reihenfolge
        Alle_Spieler_Kopie = Alle_Spieler.copy()
        Reihenfolge = []
        #Marienkäfer Extrafunktion
        Marienkäfer_Dict = {}
        for Spieler in Alle_Spieler:
            Counter = 0
            Feld_Spieler = Feld[Spieler]
            for LR in Feld[Spieler]:
                for LW in Feld_Spieler[LR]:
                    if LW.Name == "Marienkäfer":
                        Counter += 1
            if not Counter == 0:
                Marienkäfer_Dict.update({Spieler:Counter})
        Werte = []
        for Spieler in Marienkäfer_Dict:
            if not Marienkäfer_Dict[Spieler] in Werte:
                Werte.append(Marienkäfer_Dict[Spieler])
        Werte.sort(reverse = True)
        for Wert in Werte:
            Liste = []
            for Spieler in Marienkäfer_Dict:
                if Marienkäfer_Dict[Spieler] == Wert:
                    Liste.append(Spieler)
            S = random.choice(Liste)
            Reihenfolge.append(S)
            Alle_Spieler_Kopie.remove(S)
        while len(Alle_Spieler_Kopie) > 0:
            SP = random.choice(Alle_Spieler_Kopie)
            Reihenfolge.append(SP)
            Alle_Spieler_Kopie.remove(SP)
        #Erklärung
        print("\nAlle Spieler wählen in zufälliger Reihenfolge je eine Karte bis der Auswahlstapel leer ist.")
        print("\nAuswahlstapel:")
        Ausgabe(Auswahl)
        print("\nReihenfolge:")
        for S in Reihenfolge:
            print(S)
        #Auswahl
        while len(Auswahl) > 0:
            #Spieler
            for Spieler in Reihenfolge:
                print("\nAblage:")
                Ausgabe(Ablage[Spieler])
                print("\nFeld:")
                Ausgabe_Feld()
                #bis richtige Eingabe
                while True:
                    Wahl_Karte = input("\n" + Spieler + ": Wähle eine Karte. Tippe dazu ihren Namen.\n")
                    Durchgang_Counter = 0
                    for Karte in Auswahl:
                        Durchgang_Counter += 1
                        #Karte geben und aus Auswahl entfernen
                        if Karte.Name == Wahl_Karte:
                            Ablage[Spieler].append(Karte)
                            Auswahl.remove(Karte)
                            Done = True
                            break
                        #Nicht in Stapel
                        elif Durchgang_Counter == len(Auswahl):
                            print("Die Karte befindet sich nicht im Auswahlstapel.")
                            Done = False
                    #nächster Spieler oder nochmal weil falsch
                    if Done == True:
                        if not len(Auswahl) == 0:
                            print("\nAuswahlstapel:")
                            Ausgabe(Auswahl)
                        break
    #Extrakarten
    Extraprint = False
    for Spieler in Alle_Spieler:
        Feld_Spieler = Feld[Spieler]
        Dict = {}
        for LR in Feld[Spieler]:
            for LW in Feld_Spieler[LR]:
                if LW in Extrakarten:
                    Dict.update({LW:random.choice(Extrakarten[LW])})
        if not Dict == {}:
            if Extraprint == False:
                Extraprint = True
                print("\nExtrakarten\n")
            print(Spieler + ":\n")
            for Karte in Dict:
                Ablage[Spieler].append(Dict[Karte])
                print("durch " + Karte.Name + ":")
                print(Dict[Karte])                
    #Spieler Zug
    #Vor jeder Reihe von Zügen/pro Runde einmal
    Züge_Counter = 0
    print("\nTippe \"Karten Name 1 + Karten Name 2\" um zwei Karten zu kombinieren. Damit kannst du auch Lebewesen in Lebensräumen auf dem Feld platzieren.")
    print("Tippe den Namen eines Lebensraums in deiner Ablage, um diesen im Feld zu platzieren.")
    print("Vor diesen Aktionen kannst du beliebig viele Lebewesen innerhalb des Feldes bewegen (ebenfalls mit \"+\").")
    print("Für Extrafunktionen, die mit anderen Karten (nicht mit Spielern) interagieren: Um  die Extrafunktion zu nutzen, tippe ein \"+\" hinter deine Eingabe. Wenn beide Karten Extrafunktionen haben, tippe zuerst die, die du nutzen willst.")
    print("Um weitere Regeln zu sehen, tippe \"Regeln\". Um den Zug zu übersprigen, drücke Enter.")
    while Züge_Counter < Züge:
        Züge_Counter += 1
        Übrig = Züge - Züge_Counter + 1
        Str_Übrig = "noch " + str(Übrig)
        if Übrig == 1:
            Str_Übrig = "letzter"
        #Spieler Züge
        for Spieler in Alle_Spieler:
            Zug(Spieler)
    #Extrazüge
    Extraprint = False
    for Spieler in Alle_Spieler:
        Extracounter = 0
        Dict = {}
        Feld_Spieler = Feld[Spieler]
        for LR in Feld[Spieler]:
            for LW in Feld_Spieler[LR]:
                if LW in Extrazüge:
                    Extracounter += Extrazüge[LW]
                    Dict.update({LW:Extrazüge[LW]})
        if not Extracounter == 0:
            if Extraprint == False:
                Extraprint = True
                print("\nExtrazüge\n")
            print(Spieler + ":")
            for Karte in Dict:
                print(Karte.Name + ": + " + str(Extrazüge[Karte]))
        while Extracounter > 0:
            Übrig = Extracounter
            Str_Übrig = "noch " + str(Übrig)
            if Übrig == 1:
                Str_Übrig = "letzter"
            Extracounter -= 1
            Zug(Spieler)
        #Werteverbesserungskarten pro Runde
        WAS = Werteverbesserung_Anzahl[Spieler]
        for WV_Karte in WAS:
            if (not WV_Karte == Parasit) and (not WV_Karte == Friedensengel) and (not WV_Karte == Diebische_Elster) and (not WV_Karte == Urwolf):
                WASK = WAS[WV_Karte]
                WASK[0] = WASK[1]
            
#Auswertung
#Punkte
if Modus == "1":
    print("Ende\n")
    #Punkte addieren
    Auswertung = {}
    for Spieler in Alle_Spieler:
        MDS = Magisch_Dict[Spieler]
        SDS = Stärker_Dict[Spieler]
        Auswertung.update({Spieler:0})
        #Verbesserung durch LR
        for Karte in MDS:
            MDS[Karte] = 0
        for Karte in SDS:
            SDS[Karte] = 0
        for LR in Feld_Spieler:
            for LW in Feld_Spieler[LR]:
                if "Magisch" in LR.Name:
                    if LW in MDS:
                        MDS[LW] += 1
                    else:
                        MDS.update({LW:1})
                if LW in Stärker_LR[LR.Art]:
                    if not LW in SDS:
                        SDS.update({LW:1})
                    else:
                        SDS[LW] += 1                
        #Lebensraum
        for LR in Feld_Spieler:
            Auswertung[Spieler] += LR.Punkte
            #Lebewesen darin
            for LW in Feld_Spieler[LR]:
                Ende_Punkte = LW.Punkte
                if LW in Verbesserung_Spieler:
                    VSK = Verbesserung_Spieler[LW]
                    Add_Punkte = VSK["Punkte"]
                    if Add_Punkte < 0:
                        Add_Punkte = 0
                    Ende_Punkte += Add_Punkte
                    Verbesserung_Spieler.remove(LW)
                if LW in MDS:
                    if MDS > 0:
                        Ende_Punkte += 1
                        MSD -= 1
                if LW in SDS:
                    if SDS > 0:
                        Ende_Punkte += 2
                        SDS -= 1
                Auswertung[Spieler] += Ende_Punkte
    #Sortieren
    Werte = []
    for Spieler in Auswertung:
        if not Auswertung[Spieler] in Werte:
            Werte.append(Auswertung[Spieler])
    Werte.sort(reverse = True)
    Counter = 0
    #Ausgeben
    for Wert in Werte:
        Counter += 1
        print("\nPlatz " + str(Counter))
        for Spieler in Auswertung:
            if Auswertung[Spieler] == Wert:
                Druck = str(Auswertung[Spieler]) + " Punkte"
                if Wert == 1:
                    Druck = str(Auswertung[Spieler]) + " Punkt"
                print(Spieler + " - " + Druck)
#Kampf
elif Modus == "2":
    print("Ende der Aufbauphase\n")
    print("Kampfphase\n")
    input()
    #Lebewesen auf Feld in Liste
    for Spieler in Alle_Spieler:
        print("\n" + Spieler + "s Lebewesen:")
        for LR in Feld_Spieler:
            for LW in Feld_Spieler[LR]:
                Ende_LW[Spieler].append(LW)
        Ausgabe(Ende_LW[Spieler])
