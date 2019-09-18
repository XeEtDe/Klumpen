import random
##Klassen und Karten##
Start_Lebewesen = []
Start_Lebensraum = []
Start_Elemente = []
Nur = [Start_Lebewesen, Start_Elemente]
Alle_Start_Karten = [Start_Lebewesen, Start_Lebensraum, Start_Elemente]

Alle_Lebewesen = []
Alle_Lebensraum = []
Alle_Elemente = []
Alle_Verteilung = [Alle_Lebewesen, Alle_Lebensraum, Alle_Elemente]

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
    def __init__(self, Name, Beschreibung, Punkte, Lebensraum, Kombi = [], Start = False):
        Karten.__init__(self, Name, Beschreibung, Kombi, Start)
        self.Punkte = Punkte
        self.Lebensraum = Lebensraum
        if self.Start == True:
            Start_Lebewesen.append(self)
        Alle_Lebewesen.append(self)
        self.Neue_Kombis = []

#Vordruck
# = Lebewesen("", "", P, A, V, ["L"], ["K"])
# -> Stufe 1 -> +2 #Wasser, Feuer, Erde, Luft, Magie#
# -> Stufe 2 -> +4 #Wölkchen, Staub, Beere, Asche, Zeit#
# -> Stufe 3 -> +6 #Pusteblume, Pfingstrose, Perle, Sternenstaub, Kristall, Dunkle Macht#
# -> Stufe 4 -> +8 #Schleim, Eis, Blut, Blitz, Regenbogen, Engelshaar, Stein von Elyaris#

#Kombi-Prinzip: Lebewesengrundkarte+Element für neue Stufe (automatisch mehr Kombis berechnet) oder Lebewesengrundkarte+Lebewesengrundkarte für neue Grundkarte

#Gummikrieger
Gummikrieger = Lebewesen("Gummikrieger", "Einst zum Schutz der königlichen Familie erschaffen, lebt nun aber frei in den Wäldern von Klumpiland", 5, ["Wald"], [], True)
# -> Stufe 1 -> +2
Roter_Gummikrieger = Lebewesen("Roter Gummikrieger", "In seinem Inneren brennen tausend Flammen", 7, ["Wald", "Wüste"], ["Gummikrieger+Feuer"])
Blauer_Gummikrieger = Lebewesen("Blauer Gummikrieger", "Aus ihm strahlt die Ruhe des Meeres", 7, ["Wald", "See"], ["Gummikrieger+Wasser"])
Weißer_Gummikrieger = Lebewesen("Weißer Gummikrieger", "Wie ein Windhauch sich zum Sturm entwickelt", 7, ["Wald", "Berge"], ["Gummikrieger+Luft"])
Brauner_Gummikrieger = Lebewesen("Brauner Gummikrieger", "Käpmft mit der unendlichen Kraft der Erde; stärker im Lebensraum Wald", 7, ["Wald"], ["Gummikrieger+Erde"])
Goldener_Gummikrieger = Lebewesen("Goldener Gummikrieger", "Krieger mit vergoldeter Oberfläche, überall überlebensfähig", 7, ["Alle"], ["Gummikrieger+Magie"])
# -> Stufe 2 -> +4
Wolkenkrieger = Lebewesen("Wolkenkrieger", "Flauschig wie eine Wolke", 9, ["Wald", "Berge"], ["Gummikrieger+Wölkchen"])
Gummibärchenkrieger = Lebewesen("Gummibärchenkrieger", "Verwirrt seine Gegner mit Duftstoffen", 9, ["Wald", "See"], ["Gummikrieger+Beere"])
Skelettkrieger = Lebewesen("Skelettkrieger", "Ist absolut furchtlos, da er bereits tot ist", 9, ["Wald", "Wüste"], ["Gummikrieger+Staub", "Gummikrieger+Asche"])
Weiser_Krieger = Lebewesen("Weiser Krieger", "Ist so alt wie die Zeit selbst", 9, ["Alle"], ["Gummikrieger+Zeit"])
# -> Stufe 3 -> +6
Bunter_Krieger = Lebewesen("Bunter Krieger", "Wäre lieber ein friedlicher Dorfbewohner; stärker im Lebensraum Wald", 11, ["Wald", "Berge"], ["Gummikrieger+Pusteblume", "Gummikrieger+Pfingstrose"])
Schimmernder_Krieger = Lebewesen("Schimmernder Krieger", "Umhüllt von einer mysteriösen glitzernden Schicht", 11, ["Wald", "See"], ["Gummikrieger+Perle"])
Marsianer = Lebewesen("Marsianer", "Ein Krieger vom Mars", 11, ["Wald", "Wüste"], ["Gummikrieger+Sternenstaub"])
Kristallkrieger = Lebewesen("Kristallkrieger", "So wunderschön wie ein Diamand", 11, ["Wald", "See"], ["Gummikrieger+Kristall"])
Böser_Krieger = Lebewesen("Böser Krieger", "Hat sein Herz in einem Kampf verloren", 11, ["Alle"], ["Gummikrieger+Dunkle Macht"])
# -> Stufe 4 -> +8
Ätzender_Krieger = Lebewesen("Ätzender Krieger", "Ist von einer giftigen Schleimschicht umgeben", 13, ["Wald", "See"], ["Gummikrieger+Schleim"])
Eiskrieger = Lebewesen("Eiskrieger", "Kämpft fast ohne Emotionen", 13, ["Wald", "Berge"], ["Gummikrieger+Eis"])
Mutiger_Krieger = Lebewesen("Mutiger Krieger", "Ehrenhaft und tapfer", 13, ["Wald", "Wüste"], ["Gummikrieger+Blut"])
Lichtkrieger = Lebewesen("Lichtkrieger", "Setzt die Energie von Blitzen gegen seine Gegner ein", 13, ["Wald", "Berge", "Wüste"], ["Gummikrieger+Blitz"])
Gütiger_Krieger = Lebewesen("Gütiger Krieger", "Ermöglicht dir 3 Extrazüge pro Runde, wenn er auf dem Feld platziert ist", 13, ["Alle"], ["Gummikrieger+Regenbogen", "Gummikrieger+Engelshaar", "Gummikrieger+Stein von Elyaris"])

#Starker Krieger -> Gummikrieger + Gummikrieger
Starker_Krieger = Lebewesen("Starker Krieger", "Ein guter und robuster Kämpfer", 11, ["Wald"], ["Gummikrieger+Gummikrieger"])
# -> Stufe 1 -> +2
Starker_Roter_Krieger = Lebewesen("Starker Roter Krieger", "In seinem Inneren brennen tausend Flammen", 13, ["Wald", "Wüste"], ["Starker Krieger+Feuer"])
Starker_Blauer_Krieger = Lebewesen("Starker Blauer Krieger", "Aus ihm strahlt die Ruhe des Meeres", 13, ["Wald", "See"], ["Starker Krieger+Wasser"])
Starker_Weißer_Krieger = Lebewesen("Starker Weißer Krieger", "Wie ein Windhauch sich zum Sturm entwickelt", 13, ["Wald", "Berge"], ["Starker Krieger+Luft"])
Starker_Brauner_Krieger = Lebewesen("Starker Brauner Krieger", "Käpmft mit der unendlichen Kraft der Erde; stärker im Lebensraum Wald", 13, ["Wald"], ["Starker Krieger+Erde"])
Starker_Goldener_Krieger = Lebewesen("Starker Goldener Gummikrieger", "Krieger mit vergoldeter Oberfläche", 13, ["Alle"], ["Starker Krieger+Magie"])
# -> Stufe 2 -> +4
Starker_Wolkenkrieger = Lebewesen("Starker Wolkenkrieger", "Flauschig wie eine Wolke", 15, ["Wald", "Berge"], ["Starker Krieger+Wölkchen"])
Starker_Gummibärchenkrieger = Lebewesen("Starker Gummibärchenkrieger", "Verwirrt seine Gegner mit Duftstoffen", 15, ["Wald", "See"], ["Starker Krieger+Beere"])
Starker_Skelettkrieger = Lebewesen("Starker Skelettkrieger", "Ist absolut furchtlos, da er bereits tot ist", 15, ["Wald", "Wüste"], ["Starker Krieger+Staub", "Starker Krieger+Asche"])
Starker_Weiser_Krieger = Lebewesen("Starker Weiser Krieger", "Ist so alt wie die Zeit selbst", 15, ["Alle"], ["Starker Krieger+Zeit"])
# -> Stufe 3 -> +6
Starker_Bunter_Krieger = Lebewesen("Starker Bunter Krieger", "Wäre lieber ein friedlicher Dorfbewohner; stärker im Lebensraum Wald", 17, ["Wald", "Berge"], ["Starker Krieger+Pusteblume", "Starker Krieger+Pfingstrose"])
Starker_Schimmernder_Krieger = Lebewesen("Starker Schimmernder Krieger", "Umhüllt von einer mysteriösen glitzernden Schicht", 17, ["Wald", "See"], ["Starker Krieger+Perle"])
Starker_Marsianer = Lebewesen("Starker Marsianer", "Ein Krieger vom Mars", 17, ["Wald", "Wüste"], ["Starker Krieger+Sternenstaub"])
Starker_Kristallkrieger = Lebewesen("Starker Kristallkrieger", "So wunderschön wie ein Diamand", 17, ["Wald", "See"], ["Starker Krieger+Kristall"])
Starker_Böser_Krieger = Lebewesen("Starker Böser Krieger", "Hat sein Herz in einem Kampf verloren", 17, ["Alle"], ["Starker Krieger+Dunkle Macht"])
# -> Stufe 4 -> +8
Starker_Ätzender_Krieger = Lebewesen("Starker Ätzender Krieger", "Ist von einer giftigen Schleimschicht umgeben", 19, ["Wald", "See"], ["Starker Krieger+Schleim"])
Starker_Eiskrieger = Lebewesen("Starker Eiskrieger", "Kämpft fast ohne Emotionen", 19, ["Wald", "Berge"], ["Starker Krieger+Eis"])
Starker_Mutiger_Krieger = Lebewesen("Starker Mutiger Krieger", "Ehrenhaft und tapfer", 19, ["Wald", "Wüste"], ["Starker Krieger+Blut"])
Starker_Lichtkrieger = Lebewesen("Starker Lichtkrieger", "Setzt die Energie von Blitzen gegen seine Gegner ein", 19, ["Wald", "Berge", "Wüste"], ["Starker Krieger+Blitz"])
Starker_Gütiger_Krieger = Lebewesen("Starker Gütiger Krieger", "Ermöglicht dir 5 Extrazüge pro Runde, wenn er auf dem Feld platziert ist", 19, ["Alle"], ["Starker Krieger+Regenbogen", "Starker Krieger+Engelshaar", "Starker Krieger+Stein von Elyaris"])

#Klumpi ###
Klumpi = Lebewesen("Klumpi", "Ein sehr anpassungsfähiges Lebewesen mit viel Potential zur Weiterentwicklung", 1, ["Alle"], [], True)
# -> Doppel ###
# -> Stufe 1 -> +2 #Feuer, Wasser#
Gräberling = Lebewesen("Gräberling", "Gräbt unterirdisch weit verzweigte Tunnelsysteme; gibt dir auf dem Feld platiert eine weitere Elementkarte pro Runde", 3, ["Wald"], ["Klumpi+Erde"])
Kleiner_Wirbelwind = Lebewesen("Kleiner Wirbelwind", "Kann ein Lebewesen pro Runde in einem weiteren zufälligen Lebensraum leben lassen", 3, ["Alle"], ["Klumpi+Luft"])
Zauberer = Lebewesen("Zauberer", "Verwandelt Elemente in Zaubertränke", 3, ["Alle"], ["Klumpi+Magie"])
# -> Stufe 2 -> +4
Koi = Lebewesen("Koi", "Eine chinesische Zuchtform des Karpfen, die sich der Legende nach in einen Drachen verwandeln kann; kann Lebensräume um einen Platz vergrößern", 5, ["See"], ["Klumpi+Wölkchen", "Klumpi+Beere"])
Parasit = Lebewesen("Parasit", "Kann einmal im Spiel die Werte eines beliebigen anderen Lebewesens aufnehmen. Dessen Werte werden dabei um 4 verringert", 5, ["Alle"], ["Klumpi+Asche", "Klumpi+Staub"])
Sphinx = Lebewesen("Sphinx", "\"So, als wären sie jeden Augenblick im Begriff zu verschwinden, und würden gleichzeitig aus sich selbst heraus neu erschaffen\"; gibt dir auf dem Feld platziert pro Runde einen Extrazug", 5, ["Wüste"], ["Klumpi+Zeit"])
# -> Stufe 3 -> +6
Verrückter_Gnom = Lebewesen("Verrückter Gnom", "An manchen Tagen hallt das Lachen diesen kleinen Männchens durch den Wald; gibt dir pro Runde ein Goldstück, wenn er auf dem Feld platziert ist", 7, ["Wald"], ["Klumpi+Pusteblume"])
Sea_People = Lebewesen("Sea People", "Sind Teil der Wellen des Meeres und weisen Schiffen den Weg; können pro Runde die Werte eines Lebewesens um 2 erhöhen", 7, ["See"], ["Klumpi+Perle"])
Dunkler_Magier = Lebewesen("Dunkler Magier", "Stellt aus Elementen Gifte her, die du auf andere Spieler anwenden kannst", 7, ["Alle"], ["Klumpi+Dunkle Macht"])
Marienkäfer = Lebewesen("Marienkäfer", "Bei der Zugreihenfolge des Auswahlstapels bist du vor den anderen Spielern an der Reihe, solange der Käfer auf dem Feld platziert ist", 7, ["Alle"], ["Klumpi+Pfingstrose"])
Joker = Lebewesen("Joker", "Kann dir einmal pro Runde eine Startkarte geben, bei der du entscheidest ob sie ein Element, Lebewesen oder Lebensraum sein soll", 7, ["Alle"], ["Klumpi+Sternenstaub", "Klumpi+Kristall"])
# -> Stufe 4 -> +8 #Schleim, Engelshaar, Stein von Elyaris#
Kobold = Lebewesen("Kobold", "Gibt dir pro Runde einen Kessel voller Gold, wenn er auf dem Feld platziert ist", 9, ["Alle"], ["Klumpi+Regenbogen"])
Schreier = Lebewesen("Schreier", "Sein greller Schrei hallt noch Tage in den Ohren derer, die ihn hörten; kann drei Mal im Spiel einen Spieler drei Züge aussetzen lassen", 9, ["Alle"], ["Klumpi+Eis", "Klumpi+Blitz"])
Vampir = Lebewesen("Vampir", "Kann pro Runde einmal die Punkte eines zufälligen gegnerischen Lebewesens aufsaugen", 9, ["Alle"], ["Klumpi+Blut"])


#Drachen
Drachenei = Lebewesen("Drachenei", "Benötigt einen Zug zum Schlüpfen, nachdem es im Lebensraum platziert wurde", 0, ["Berge"], [], True)
Drache = Lebewesen("Drache", "Ein starkes, geschupptes und flugfähiges Lebewesen", 8, ["Berge"], [])
# -> Stufe 1 -> +2
Feuerdrache = Lebewesen("Feuerdrache", "Liebt Hitze über alles und bekämpft seine Feinde mit Feueratem", 10, ["Berge", "Wüste"], ["Drache+Feuer"])
Wasserdrache = Lebewesen("Wasserdrache", "Fühlt sich in feuchten Gebieten wohl, kann durch Kiemen sogar unter Wasser leben", 10, ["Berge", "See"], ["Drache+Wasser"])
Luftdrache = Lebewesen("Luftdrache", "Fühlt sich in luftigen Höhen wohl; stärker im Lebensraum Berge", 10, ["Berge"], ["Drache+Luft"])
Erddrache = Lebewesen("Erddrache", "Ein kleiner Drache, der lieber am Boden als in der Luft lebt", 10, ["Berge", "Wald"], ["Drache+Erde"])
Magiedrache = Lebewesen("Magiedrache", "Hat goldene Schuppen und magische Anpassungsfähigkeiten", 10, ["Alle"], ["Drache+Magie"])
# -> Stufe 2 -> +4
Wolkendrache = Lebewesen("Wolkendrache", "Dieser Drache lebt hoch über den Wolken; stärker im Lebensraum Berge", 12, ["Berge", "Wüste"], ["Drache+Wölkchen"])
Chamäleondrache = Lebewesen("Chamäleondrache", "Passt sich perfekt an seine Umgebung an", 12, ["Alle"], ["Drache+Beere", "Drache+Staub"])
Schattendrache = Lebewesen("Schattendrache", "Ist schwarz wie die Nacht und hat die Fähigkeit Energiebälle abzufeuern", 12, ["Berge", "See", "Wald"], ["Drache+Asche"])
Urdrache = Lebewesen("Urdrache", "Diese sehr ursprüngliche und alte Drachenart war wahrscheinlich die Erste, die sich in Klumpiland entwickelte", 12, ["Alle"], ["Drache+Zeit"])
# -> Stufe 3 -> +6
Wächterdrache = Lebewesen("Wächterdrache", "Wacht über einen riesigen Schatz in einer abgelegenen Höhle", 14, ["Berge"], ["Drache+Perle", "Drache+Kristall"])
Traumdrache = Lebewesen("Traumdrache", "Gibt dir pro Runde eine weitere zufällige Startkarte, wenn er auf dem Feld platziert ist", 14, ["Berge", "See"], ["Drache+Pusteblume", "Drache+Sternenstaub"])
Schreckensdrache = Lebewesen("Schreckensdrache", "Nachtschwarze Schuppen, blutverschmiertes Maul mit langen Zähnen und böse glühende Augen", 14, ["Berge", "Wüste", "See"], ["Drache+Dunkle Macht"])
Liebesdrache = Lebewesen("Liebesdrache", "Ein rotes, vor allem im Frühling gesehenes Tier, das im Gegensatz zu anderen Drachenarten meist in Rudeln lebt", 14, ["Berge", "See", "Wald"], ["Drache+Pfingstrose"])
# -> Stufe 4 -> +8
Temeraire = Lebewesen("Temeraire", "Ein äußerst seltener Himmelsdrache, der ursprünglich als Geschenk gedacht war, aber eine andere Bestimmung fand", 16, ["Berge"], ["Drache+Engelshaar", "Drache+Stein von Elyaris"])
Fuchur = Lebewesen("Fuchur", "\"Glücksdrachen dagegen sind Geschöpfe der Luft und der Wärme, Geschöpfe unbändiger Freude und trotz ihrer gewaltigen Körpergröße so leicht wie eine Sommerwolke\"", 16, ["Alle"], ["Drache+Regenbogen"])
Furchtdrache = Lebewesen("Furchtdrache", "Sein eisiges Feuer versteinert seine Gegener; kann pro Runde einmal einen Spieler einen Zug aussetzen lassen", 16, ["Alle"], ["Drache+Blitz", "Drache+Eis"])
Glibberdrache = Lebewesen("Glibberdrache", "Verändert ständig seine Form und kann auch durch kleinste Öffnungen gelangen", 16, ["See", "Berge", "Wald"], ["Drache+Schleim", "Drache+Blut"])

#Starker Drache -> Drache + Drache
Starker_Drache = Lebewesen("Starker Drache", "Eines der stärksten Lebewesen in Klumpiland", 17, ["Berge"], ["Drache+Drache"])
# -> Stufe 1 -> +2
Starker_Feuerdrache = Lebewesen("Starker Feuerdrache", "Liebt Hitze über alles und bekämpft seine Feinde mit Feueratem", 19, ["Berge", "Wüste"], ["Starker Drache+Feuer"])
Starker_Wasserdrache = Lebewesen("Starker Wasserdrache", "Fühlt sich in feuchten Gebieten wohl, kann durch Kiemen sogar unter Wasser leben", 19, ["Berge", "See"], ["Starker Drache+Wasser"])
Starker_Luftdrache = Lebewesen("Starker Luftdrache", "Fühlt sich in luftigen Höhen wohl; stärker im Lebensraum Berge", 19, ["Berge"], ["Starker Drache+Luft"])
Starker_Erddrache = Lebewesen("Starker Erddrache", "Ein kleiner Drache, der lieber am Boden als in der Luft lebt", 19, ["Berge", "Wald"], ["Starker Drache+Erde"])
Starker_Magiedrache = Lebewesen("Starker Magiedrache", "Hat goldene Schuppen und magische Anpassungsfähigkeiten", 19, ["Alle"], ["Starker Drache+Magie"])
# -> Stufe 2 -> +4
Starker_Wolkendrache = Lebewesen("Starker Wolkendrache", "Dieser Drache lebt hoch über den Wolken; stärker im Lebensraum Berge", 21, ["Berge", "Wüste"], ["Starker Drache+Wölkchen"])
Starker_Chamäleondrache = Lebewesen("Starker Chamäleondrache", "Passt sich perfekt an seine Umgebung an", 21, ["Alle"], ["Starker Drache+Beere", "Starker Drache+Staub"])
Starker_Schattendrache = Lebewesen("Starker Schattendrache", "Ist schwarz wie die Nacht und hat die Fähigkeit Energiebälle abzufeuern", 21, ["Berge", "See", "Wald"], ["Starker Drache+Asche"])
Starker_Urdrache = Lebewesen("Starker Urdrache", "Diese sehr ursprüngliche und alte Drachenart war wahrscheinlich die Erste, die sich in Klumpiland entwickelte", 21, ["Alle"], ["Starker Drache+Zeit"])
# -> Stufe 3 -> +6
Starker_Wächterdrache = Lebewesen("Starker Wächterdrache", "Wacht über einen riesigen Schatz in einer abgelegenen Höhle", 23, ["Berge"], ["Starker Drache+Perle", "Starker Drache+Kristall"])
Starker_Traumdrache = Lebewesen("Starker Traumdrache", "Gibt dir pro Runde eine zufällige Karte, die keine Startkarte sein muss, wenn er auf dem Feld platziert ist", 23, ["Berge", "See"], ["Starker Drache+Pusteblume", "Starker Drache+Sternenstaub"])
Starker_Schreckensdrache = Lebewesen("Starker Schreckensdrache", "Nachtschwarze Schuppen, blutverschmiertes Maul mit langen Zähnen und böse glühende Augen", 23, ["Berge", "Wüste", "See"], ["Starker Drache+Dunkle Macht"])
Starker_Liebesdrache = Lebewesen("Starker Liebesdrache", "Ein rotes, vor allem im Frühling gesehenes Tier, das im Gegensatz zu anderen Drachenarten meist in Rudeln lebt", 23, ["Berge", "See", "Wald"], ["Starker Drache+Pfingstrose"])
# -> Stufe 4 -> +8
Starker_Himmelsdrache = Lebewesen("Starker Himmelsdrache", "Ein äußerst seltenes Tier, das in fernen Ländern gezüchtet wurde", 25, ["Berge"], ["Starker Drache+Engelshaar", "Starker Drache+Stein von Elyaris"])
Starker_Glücksdrache = Lebewesen("Starker Glücksdrache", "\"Glücksdrachen dagegen sind Geschöpfe der Luft und der Wärme, Geschöpfe unbändiger Freude und trotz ihrer gewaltigen Körpergröße so leicht wie eine Sommerwolke\"", 25, ["Alle"], ["Starker Drache+Regenbogen"])
Starker_Furchtdrache = Lebewesen("Starker Furchtdrache", "Sein eisiges Feuer versteinert seine Gegener; kann pro Runde einmal einen Spieler 3 Züge aussetzen lassen, wenn er auf dem Feld platziert ist", 25, ["Alle"], ["Starker Drache+Blitz", "Starker Drache+Eis"])
Starker_Glibberdrache = Lebewesen("Starker Glibberdrache", "Verändert ständig seine Form und kann auch durch kleinste Öffnungen gelangen", 25, ["See", "Berge", "Wald"], ["Starker Drache+Schleim", "Starker Drache+Blut"])

#Zottel
Zottel = Lebewesen("Zottel", "Ein haariges Wesen mit großen Augen", 3, ["Berge", "Wald"], [], True)
# -> Stufe 1 -> +2
Feuriger_Zottel = Lebewesen("Feuriger Zottel", "Kann bei Gefahr sein Fell entzünden; stärker im Lebensraum Wüste", 5, ["Berge", "Wald", "Wüste"], ["Zottel+Feuer"])
Nasser_Zottel = Lebewesen("Nasser Zottel", "Schützt sich durch nasses Fell; stärker im Lebensraum See", 5, ["Berge", "Wald", "See"], ["Zottel+Wasser"])
Schwebender_Zottel = Lebewesen("Schwebender Zottel", "Kann durch Druckveränderung in seinem Inneren ohne Flügel fliegen; stärker im Lebensraum Berge", 5, ["Berge", "Wald", "See"], ["Zottel+Luft"])
Dreckiger_Zottel = Lebewesen("Dreckiger Zottel", "Lebt meistens in unterirdischen Gängen; stärker im Lebensraum Wald", 5, ["Berge", "Wald", "Wüste"], ["Zottel+Erde"])
Goldener_Zottel = Lebewesen("Goldener Zottel", "Offenbart nur wenigen Beobachtern seine wahre Fellfarbe", 5, ["Alle"], ["Zottel+Magie"])
# -> Stufe 2 -> +4
Flauschiger_Zottel = Lebewesen("Flauschiger Zottel", "Fell so weich wie die Wolken", 7, ["Alle"], ["Zottel+Wölkchen"])
Gefärbter_Zottel = Lebewesen("Gefärbter Zottel", "Schreckt seine Gegner durch die dunkle Fellfarbe ab", 7, ["Alle"], ["Zottel+Beere", "Zottel+Asche"])
Stachliger_Zottel = Lebewesen("Stachliger Zottel", "Sein Fell ist so trocken, dass es wie Stacheln wirkt; stärker im Lebensraum Wüste", 7, ["Alle"], ["Zottel+Staub", "Zottel+Zeit"])
# -> Stufe 3 -> +6
Funkelnder_Zottel = Lebewesen("Funkelnder Zottel", "Hat magische Diamanten in seinem Fell seit er den Prinzen von Klumpiland gerettet hat", 9, ["Alle"], ["Zottel+Kristall", "Zottel+Sternenstaub"])
Böser_Zottel = Lebewesen("Böser Zottel", "Der Begleiter des dunkeln Magiers", 9, ["Alle"], ["Zottel+Dunkle Macht"])
Heller_Zottel = Lebewesen("Heller Zottel", "Fell so sanft wie der Mond und Augen so glitzernd wie Sterne; stärker im Lebensraum See", 9, ["Alle"], ["Zottel+Perle", "Zottel+Pusteblume"])
Eigenwilliger_Zottel = Lebewesen("Eigenwilliger Zottel", "Im Gegensatz zu den meisten andere Zotteln sehr abweisend", 9, ["Alle"], ["Zottel+Pfingstrose"])
# -> Stufe 4 -> +8
Schleimiger_Zottel = Lebewesen("Schleimiger Zottel", "Sondert bei Gefahr ätzenden Schleim ab", 11, ["Alle"], ["Zottel+Schleim"])
Rubinzottel = Lebewesen("Rubinzottel", "Aus der Ferne gleicht er wegen seines leuchtend roten Fells einem Edelstein; stärker im Lebensraum Berge", 11, ["Alle"], ["Zottel+Blut"])
Mystischer_Zottel = Lebewesen("Mystischer Zottel", "Kommt so selten vor, dass man sich nicht sicher ist, ob er überhaupt exestiert; gibt dir eine weitere Startkarte pro Runde, wenn er auf dem Feld platziert ist", 11, ["Alle"], ["Zottel+Stein von Elyaris", "Zottel+Engelshaar"])
Himmelszottel = Lebewesen("Himmelszottel", "Kann pro Runde die Werte eines Lebewesens um 3 erhöhen", 11, ["Alle"], ["Zottel+Eis", "Zottel+Regenbogen", "Zottel+Blitz"])

#Doppelzottel -> Zottel + Zottel
Doppelzottel = Lebewesen("Doppelzottel", "Ein untrennbares Paar aus zwei Zotteln", 6, ["Berge", "Wald"], ["Zottel+Zottel"])
# -> Stufe 1 -> +2
Feurige_Doppelzottel = Lebewesen("Feurige Doppelzottel", "Zwei Zottel, die bei Gefahr ihr Fell entzünden; stärker im Lebensraum Wüste", 8, ["Berge", "Wald", "Wüste"], ["Doppelzottel+Feuer"])
Nasse_Doppelzottel = Lebewesen("Nasse Doppelzottel", "Zwei Zottel, die sich durch nasses Fell schützen; stärker im Lebensraum See", 8, ["Berge", "Wald", "See"], ["Doppelzottel+Wasser"])
Schwebende_Doppelzottel = Lebewesen("Schwebende Doppelzottel", "Zwei Zottel, die durch Druckveränderung in ihrem Inneren ohne Flügel fliegen können; stärker im Lebensraum Berge", 8, ["Berge", "Wald", "See"], ["Doppelzottel+Luft"])
Dreckige_Doppelzottel = Lebewesen("Dreckige Doppelzottel", "Zwei Zottel, die meistens in unterirdischen Gängen leben; stärker im Lebensraum Wald", 8, ["Berge", "Wald", "Wüste"], ["Doppelzottel+Erde"])
Goldene_Doppelzottel = Lebewesen("Goldene Doppelzottel", "Zwei Zottel, die nur wenigen Beobachtern ihre wahre Fellfarbe offenbaren", 8, ["Alle"], ["Doppelzottel+Magie"])
# -> Stufe 2 -> +4
Flauschige_Doppelzottel = Lebewesen("Flauschige Doppelzottel", "Zwei Zottel mit Fell so weich wie die Wolken", 10, ["Alle"], ["Doppelzottel+Wölkchen"])
Gefärbte_Doppelzottel = Lebewesen("Gefärbte Doppelzottel", "Zwei Zottel, die ihre Gegner durch die dunkle Fellfarbe abschrecken", 10, ["Alle"], ["Doppelzottel+Beere", "Doppelzottel+Asche"])
Stachlige_Doppelzottel = Lebewesen("Stachlige Doppelzottel", "Zwei Zottel, deren Fell so trocken ist, dass es wie Stacheln wirkt; stärker im Lebensraum Wüste", 10, ["Alle"], ["Doppelzottel+Staub", "Doppelzottel+Zeit"])
# -> Stufe 3 -> +6
Funkelnde_Doppelzottel = Lebewesen("Funkelnde Doppelzottel", "Zwei Zottel, die magische Diamanten in ihrem Fell haben", 12, ["Alle"], ["Doppelzottel+Kristall", "Doppelzottel+Sternenstaub"])
Böse_Doppelzottel = Lebewesen("Böse Doppelzottel", "Zwei Zottel, die Begleiter des dunkeln Magiers sind", 12, ["Alle"], ["Doppelzottel+Dunkle Macht"])
Helle_Doppelzottel = Lebewesen("Helle Doppelzottel", "Zwei Zottel mit Fell so sanft wie der Mond und Augen so glitzernd wie Sterne; stärker im Lebensraum See", 12, ["Alle"], ["Doppelzottel+Perle", "Doppelzottel+Pusteblume"])
Eigenwillige_Doppelzottel = Lebewesen("Eigenwillige Doppelzottel", "Zwei Zottel, die im Gegensatz zu den meisten andere Zotteln sehr abweisend sind", 12, ["Alle"], ["Doppelzottel+Pfingstrose"])
# -> Stufe 4 -> +8
Schleimige_Doppelzottel = Lebewesen("Schleimige Doppelzottel", "Zwei Zottel, die bei Gefahr ätzenden Schleim absondern", 14, ["Alle"], ["Doppelzottel+Schleim"])
Rubin_Doppelzottel = Lebewesen("Rubin-Doppelzottel", "Zwei Zottel, die aus der Ferne Edelsteinen gleichen; stärker im Lebensraum Berge", 14, ["Alle"], ["Doppelzottel+Blut"])
Mystische_Doppelzottel = Lebewesen("Mystische Doppelzottel", "Geben dir pro Runde eine weitere Karte, die keine Startkarte sein muss, wenn sie auf dem Feld platziert sind", 14, ["Alle"], ["Doppelzottel+Stein von Elyaris", "Doppelzottel+Engelshaar"])
Himmels_Doppelzottel = Lebewesen("Himmels-Doppelzottel", "Können pro Runde die Werte eines Lebewesens um 5 erhöhen", 14, ["Alle"], ["Doppelzottel+Eis", "Doppelzottel+Regenbogen", "Doppelzottel+Blitz"])

#Fee
Fee = Lebewesen("Fee", "Das Feenvolk ist gefürchtet und bewundert zugleich", 4, ["Alle"], [], True)
# -> Stufe 1 -> +2
Feuerfee = Lebewesen("Feuerfee", "Bändigt jede Flamme; stärker im Lebensraum Wüste", 6, ["Wüste", "Wald"], ["Fee+Feuer"])
Wasserfee = Lebewesen("Wasserfee", "Kontrolliert Regentropfen und Bäche; stärker im Lebensraum See", 6, ["See", "Berge"], ["Fee+Wasser"])
Luftfee = Lebewesen("Luftfee", "Kontrolliert Winde und Brisen; stärker im Lebensraum Berge", 6, ["Berge", "Wüste"], ["Fee+Luft"])
Naturfee = Lebewesen("Naturfee", "Kümmert sich um Tiere und Pflanzen; stärker im Lebensraum Wald", 6, ["Wald", "See"], ["Fee+Erde"])
Goldene_Fee = Lebewesen("Goldene Fee", "Versorgt das Feenvolk mit genügend Feenstaub", 6, ["Alle"], ["Fee+Magie"])
# -> Stufe 2 -> +4
Wetterfee = Lebewesen("Wetterfee", "Kann anderen Lebewesen ermöglichen in einem weiteren zufälligen Lebensraum zu überleben", 8, ["Alle"], ["Fee+Wölkchen"])
Erntefee = Lebewesen("Erntefee", "Gibt dir eine weitere Elementkarte pro Runde, wenn sie auf dem Feld platziert ist", 8, ["Wald", "See", "Berge"], ["Fee+Beere"])
Zeitfee = Lebewesen("Zeitfee", "Gibt dir einen Extrazug pro Runde, wenn sie auf dem Feld platziert ist", 8, ["Alle"], ["Fee+Zeit"])
Todesfee = Lebewesen("Todesfee", "Kann zwischen dem Jenseits und dieser Welt wandern; stärker im Lebensraum See", 8, ["See", "Wüste", "Berge"], ["Fee+Staub", "Fee+Asche"])
# -> Stufe 3 -> +6
Schimmerfee = Lebewesen("Schimmerfee", "Kann anderen Lebewesen ermöglichen in allen Lebensräumen zu überleben", 10, ["Alle"], ["Fee+Perle"])
Kristallfee = Lebewesen("Kristallfee", "Wunderschön und kaum von einem Kristall zu unterscheiden; stärker im Lebensraum Berge", 10, ["Alle"], ["Fee+Kristall"])
Glitzerfee = Lebewesen("Glitzerfee", "Versorgt die Sterne mit Feenstaub; stärker im Lebensraum Wüste", 10, ["Alle"], ["Fee+Sternenstaub"])
Dunkelfee = Lebewesen("Dunkelfee", "Wächterin der Nacht; kann pro Runde die Werte eines Lebewesens um 3 erhöhen", 10, ["Alle"], ["Fee+Dunkle Macht"])
Babyfee = Lebewesen("Babyfee", "Gerade aus einer Blume geboren; ihr helles Lachen lässt jede Runde ein weiteres Lebewesen entstehen, wenn sie auf dem Feld platziert ist", 10, ["Alle"], ["Fee+Pusteblume", "Fee+Pfingstrose"])
# -> Stufe 4 -> +8
Unwetterfee = Lebewesen("Unwetterfee", "Kann einmal pro Runde einen Spieler 3 Züge aussetzen lassen", 12, ["Alle"], ["Fee+Blitz", "Fee+Eis", "Fee+Schleim"])
Lebensfee = Lebewesen("Lebensfee", "Gibt dir pro Runde eine zufällige Startkarte, wenn sie auf dem Feld platziert ist", 12, ["Alle"], ["Fee+Blut", "Fee+Stein von Elyaris", "Fee+Regenbogen", "Fee+Engelshaar"])

#Feenkönigin -> Fee + Fee
Feenkönigin = Lebewesen("Feenkönigin", "Herrscht über das Feenvolk; kann pro Runde die Werte eines Lebewesens um 1 erhöhen", 9, ["Alle"], ["Fee+Fee"])
# -> Stufe 1 -> +2
Feuer_Feenkönigin = Lebewesen("Feuer-Feenkönigin", "Bändigt jede Flamme; stärker im Lebensraum Wüste", 11, ["Wüste", "Wald"], ["Feenkönigin+Feuer"])
Wasser_Feenkönigin = Lebewesen("Wasser-Feenkönigin", "Kontrolliert Regentropfen und Bäche; stärker im Lebensraum See", 11, ["See", "Berge"], ["Feenkönigin+Wasser"])
Luft_Feenkönigin = Lebewesen("Luft-Feenkönigin", "Kontrolliert Winde und Brisen; stärker im Lebensraum Berge", 11, ["Berge", "Wüste"], ["Feenkönigin+Luft"])
Natur_Feenkönigin = Lebewesen("Natur-Feenkönigin", "Kümmert sich um Tiere und Pflanzen; stärker im Lebensraum Wald", 11, ["Wald", "See"], ["Feenkönigin+Erde"])
Goldene_Feenkönigin = Lebewesen("Goldene Feenkönigin", "Versorgt das Feenvolk mit genügend Feenstaub", 11, ["Alle"], ["Feenkönigin+Magie"])
# -> Stufe 2 -> +4
Wetter_Feenkönigin = Lebewesen("Wetter-Feenkönigin", "Kann anderen Lebewesen ermöglichen in allen Lebensräumen zu überleben", 13, ["Alle"], ["Feenkönigin+Wölkchen"])
Ernte_Feenkönigin = Lebewesen("Ernte-Feenkönigin", "Gibt dir eine weitere Elementkarte, die keine Startkarte sein muss, pro Runde, wenn sie auf dem Feld platziert ist", 13, ["Wald", "See", "Berge"], ["Feenkönigin+Beere"])
Zeit_Feenkönigin = Lebewesen("Zeit-Feenkönigin", "Gibt dir 3 Extrazüge pro Runde, wenn sie auf dem Feld platziert ist", 13, ["Alle"], ["Feenkönigin+Zeit"])
Todes_Feenkönigin = Lebewesen("Todes-Feenkönigin", "Kann zwischen dem Jenseits und dieser Welt wandern; stärker im Lebensraum See", 13, ["See", "Wüste", "Berge"], ["Feenkönigin+Staub", "Feenkönigin+Asche"])
# -> Stufe 3 -> +6
Schimmer_Feenkönigin = Lebewesen("Schimmer-Feenkönigin", "Kann pro Runde einen Lebensraum um 3 vergrößern", 15, ["Alle"], ["Feenkönigin+Perle"])
Kristall_Feenkönigin = Lebewesen("Kristall-Feenkönigin", "Wunderschön und kaum von einem Kristall zu unterscheiden; stärker im Lebensraum Berge", 15, ["Alle"], ["Feenkönigin+Kristall"])
Glitzer_Feenkönigin = Lebewesen("Glitzer-Feenkönigin", "Versorgt die Sterne mit Feenstaub; stärker im Lebensraum Wüste", 15, ["Alle"], ["Feenkönigin+Sternenstaub"])
Dunkel_Feenkönigin = Lebewesen("Dunkel-Feenkönigin", "Wächterin der Nacht; kann pro Runde die Werte eines Lebewesens um 5 erhöhen", 15, ["Alle"], ["Feenkönigin+Dunkle Macht"])
Baby_Feenkönigin = Lebewesen("Baby_Feenkönigin", "Ihr helles Lachen lässt jede Runde ein weiteres Lebewesen, das keine Startkarte sein muss, entstehen, wenn sie auf dem Feld platziert ist", 15, ["Alle"], ["Feenkönigin+Pusteblume", "Feenkönigin+Pfingstrose"])
# -> Stufe 4 -> +8
Unwetter_Feenkönigin = Lebewesen("Unwetter-Feenkönigin", "Kann einmal pro Runde einen Spieler 5 Züge aussetzen lassen", 17, ["Alle"], ["Feenkönigin+Blitz", "Feenkönigin+Eis", "Feenkönigin+Schleim"])
Lebens_Feenkönigin = Lebewesen("Lebens-Feenkönigin", "Gibt dir pro Runde eine zufällige Karte, die keine Startkarte sein muss, wenn sie auf dem Feld platziert ist", 17, ["Alle"], ["Feenkönigin+Blut", "Feenkönigin+Stein von Elyaris", "Feenkönigin+Regenbogen", "Feenkönigin+Engelshaar"])

#Zeppelindrache -> Drache + Zottel
Zeppelindrache = Lebewesen("Zeppelindrache", "Riesiger Drache, der trotz fehlender Flügel schweben kann", 12, ["Berge"], ["Drache+Zottel"])
# -> Stufe 1 -> +2
Brennender_Zeppelindrache = Lebewesen("Brennender Zeppelindrache", "Das Feuer macht ihm nichts aus", 14, ["Berge", "Wüste"], ["Zeppelindrache+Feuer"])
Triefender_Zeppelindrache = Lebewesen("Triefender Zeppelindrache", "Kann aufgrund seines immer nassen Fells nicht fliegen, dafür aber unter Wasser atmen", 14, ["See"], ["Zeppelindrache+Wasser"])
Matschiger_Zeppelindrache = Lebewesen("Matschiger Zeppelindrache", "Wälzt sich im Matsch, um sein Fell zu schützen", 14, ["Wald", "Berge"], ["Zeppelindrache+Erde"])
Aufgeblähter_Zeppelindrache = Lebewesen("Aufgeblähter Zeppelindrache", "Fliegt höher als alle anderen Drachen", 14, ["Berge"], ["Zeppelindrache+Luft"])
Goldener_Zeppelindrache = Lebewesen("Goldener Zeppelindrache", "Hat vergoldetes Fell", 14, ["Berge"], ["Zeppelindrache+Magie"])
# -> Stufe 2 -> +4
Flauschiger_Zeppelindrache = Lebewesen("Flauschiger Zeppelindrache", "Kaum von einer echten Wolke zu unterscheiden", 16, ["Berge"], ["Zeppelindrache+Wölkchen"])
Alter_Zeppelindrache = Lebewesen("Alter Zeppelindrache", "Ein Kindheitsfreund der Prinzessin von Klumpiland", 16, ["Berge", "Wald"], ["Zeppelindrache+Zeit", "Zeppelindrache+Staub"])
Symbiotischer_Zeppelindrache = Lebewesen("Symbiotischer Zeppelindrache", "In seinem Fell nisten Vögel, die ihn im Gegenzug sauber halten und zu geeigneten Landeplätzen führen", 16, ["Berge", "Wald"], ["Zeppelindrache+Beere"])
Nacht_Zeppelindrache = Lebewesen("Nacht-Zeppelindrache", "Ist bestens an ein Leben in Dunkelheit angepasst und lebt am liebsten in tiefen Höhlen", 16, ["Berge"], ["Zeppelindrache+Asche"])
# -> Stufe 3 -> +6
Blühender_Zeppelindrache = Lebewesen("Blühender Zeppelindrache", "Verschiede Pflanzenarten leben in seinem Fell, sodass er vor allem im Frühling ein wunderschöner Anblick ist, wenn dieser Drache am Himmel schwebt", 18, ["Berge", "Wald"], ["Zeppelindrache+Pusteblume", "Zeppelindrache+Pfingstrose"])
Unsichtbarer_Zeppelindrache = Lebewesen("Unsichtbarer Zeppelindrache", "Jedes Haar seines Fells kann eine andere Farbe annehmen, wodurch er nicht von seiner Umgebung zu unterscheiden ist und kaum jemand von seiner Existenz weiß", 18, ["Alle"], ["Zeppelindrache+Perle"])
Toter_Zeppelindrache = Lebewesen("Toter Zeppelindrache", "Seine Augen sind leer, sein Inneres tot und er wird nur noch von der dunklen Macht bewegt", 18, ["Alle"], ["Zeppelindrache+Dunkle Macht"])
Kosmischer_Zeppelindrache = Lebewesen("Kosmischer Zeppelindrache", "Kann große Mengen an Sauerstoff in seinem Inneren speichern und so für eine Weile durch das Weltall schweben", 18, ["Alle"], ["Zeppelindrache+Sternenstaub"])
Durchsichtiger_Zeppelindrache = Lebewesen("Durchsichtiger Zeppelindrache", "Jede Zelle seines Körpers ist durchsichtig und bricht das Licht, wodurch er ein wunderschönes Farbenspiel am Himmel hinterlässt", 18, ["Alle"], ["Zeppelindrache+Kristall"])
# -> Stufe 4 -> +8
Frost_Zeppelindrache = Lebewesen("Frost-Zeppelindrache", "Lebt im ewigen Eis des hohen Nordens", 20, ["Berge"], ["Zeppelindrache+Eis"])
Rubin_Zeppelindrache = Lebewesen("Rubin-Zeppelindrache", "Sein Fell glänzt blutrot während er am Himmel vorbei schwebt; stärker im Lebensraum Wüste", 20, ["Alle"], ["Zeppelindrache+Blut"])
Gewitter_Zeppelindrache = Lebewesen("Gewitter-Zeppelindrache", "Sein Fell speichert Elektrizität und kann bei Gefahr ein Gewitter aus grellen Blitzen entfachen", 20, ["Alle"], ["Zeppelindrache+Blitz"])
Sumpfiger_Zeppelindrache = Lebewesen("Sumpfiger Zeppelindrache", "Eine Jahre alte Schicht aus Schlamm, Blättern und Bakterien umhüllt ihn zu seinem Schutz; stärker im Lebensraum See", 20, ["Alle"], ["Zeppelindrache+Schleim"])
Himmlischer_Zeppelindrache = Lebewesen("Himmlischer Zeppelindrache", "Wurde von den Himmelswesen erschaffen und dient diesen", 20, ["Berge"], ["Zeppelindrache+Engelshaar", "Zeppelindrache+Regenbogen", "Zeppelindrache+Stein von Elyaris"])

#Echsenmensch -> Drache + Klumpi ###
Echsenmensch = Lebewesen("Echsenmensch", "Die Gesellschaft der Echsenmenschen plant Klumpiland zu übernehmen", 10, ["Wüste"], ["Klumpi+Drache"])
# -> Stufe 1 -> +2 #Wasser, Feuer, Erde, Luft, Magie#
# -> Stufe 2 -> +4 #Wölkchen, Staub, Beere, Asche, Zeit#
# -> Stufe 3 -> +6 #Pusteblume, Pfingstrose, Perle, Sternenstaub, Kristall, Dunkle Macht#
# -> Stufe 4 -> +8 #Schleim, Eis, Blut, Blitz, Regenbogen, Engelshaar, Stein von Elyaris#

#Engel -> Klumpi + Fee ### -> Extrafunktionen
Engel = Lebewesen("Engel", "Ein geflügeltes Himmelswesen", 6, ["Alle"], ["Klumpi+Fee"])
# -> Stufe 1 -> +2 #Wasser, Erde, Luft, Magie#
Brennender_Engel = Lebewesen("Brennender Engel", "In seinem Ehrgeiz kam er der Sonne etwas zu nahe", 8, ["Alle"], ["Engel+Feuer"])
# -> Stufe 2 -> +4 #Wölkchen, Beere, Zeit#
Todesengel = Lebewesen("Todesengel", "Wacht über das Reich der Toten; stärker im Lebensraum See", 10, ["Alle"], ["Engel+Staub", "Engel+Asche"])
# -> Stufe 3 -> +6 #Pusteblume, Pfingstrose, Perle, Sternenstaub, Kristall#
Gefallener_Engel = Lebewesen("Gefallener Engel", "Wandte sich gegen die Himmelswesen und lebt nun unter den Menschen", 12, ["Alle"], ["Engel+Dunkle Macht"])
# -> Stufe 4 -> +8 #Blut#
Reiner_Engel = Lebewesen("Reiner Engel", "Bleibt für ewig jung und weiß nichts vom Leid der Welt", 14, ["Alle"], ["Engel+Stein von Elyaris"])
Racheengel = Lebewesen("Racheengel", "Kämpft gegen die Himmelswesen um die Gerechtigkeit wieder herzustellen", 14, ["Alle"], ["Engel+Schleim", "Engel+Blitz", "Engel+Eis"])
Erzengel = Lebewesen("Erzengel", "Wacht über das gesamte Reich der Himmelswesen; gibt dir pro Runde eine zufällige Zusatzkarte, die keine Startkarte sein muss, wenn er auf dem Feld platziert ist", 14, ["Alle"], ["Engel+Engelshaar"])
Friedensengel = Lebewesen("Friedensengel", "Wacht über den Frieden im Himmelsreich und in Klumpiland; kann insgesamt 3 Lebensräume zu Wonderlands machen, in denen alle Lebewesen leben können", 14, ["Alle"], ["Engel+Regenbogen"])

#Rätselhafter Vogel -> Fee + Zottel ###
Rätselhafter_Vogel = Lebewesen("Rätselhafter Vogel", "In seine Augen scheinen alle Geheinmisse dieser Welt zu schimmern, doch ist er wirklich real?", 8, ["Alle"], ["Fee+Zottel"])
# -> Stufe 1 -> +2 #Wasser, Erde, Magie#
Glühwürmchen = Lebewesen("Glühwürmchen", "Owl City - Fireflies", 10, ["Alle"], ["Rätselhafter Vogel+Feuer"])
Origami = Lebewesen("Origami", "Ein Vogel aus Papier, der seinen Erschaffer mit Informationen versorgt; gibt dir pro Runde einen Extrazug, wenn er auf dem Feld platziert ist", 10, ["Alle"], ["Rätselhafter Vogel+Luft"])
# -> Stufe 2 -> +4 #Staub, Beere#
Bernsteineule = Lebewesen("Bernsteineule", "Eine fast unbewegliche Eule mit klugen Augen; gibt dir pro Runde zwei Extrazüge, wenn sie auf dem Feld platziert ist", 12, ["Alle"], ["Rätselhafter Vogel+Zeit"])
Rabenschaar = Lebewesen("Rabenschaar", "Kündigt den Tod eines Mühlknappen an", 12, ["Alle"], ["Rätselhafter Vogel+Asche"])
Wolkenvogel = Lebewesen("Wolkenvogel", "Erschaffen von einem Mädchen, dessen Haare alle Farben des Lichts brachen", 12, ["Alle"], ["Rätselhafter Vogel+Wölkchen"])
# -> Stufe 3 -> +6 #Pusteblume, Perle, Sternenstaub, Kristall, Dunkle Macht#
Phönix = Lebewesen("Phönix", "Am Ende seines Lebenszyklus verbrennt er, um aus der Asche neu geboren zu werden", 14, ["Alle"], ["Rätselhafter Vogel+Pfingstrose"])
# -> Stufe 4 -> +8 #Eis, Blut, Regenbogen, Engelshaar, Stein von Elyaris#
Diebische_Elster = Lebewesen("Diebische Elster", "Kann 3 Mal im Spiel das schlechteste Lebewesen eines gewählten Spielers für dich stehlen", 16, ["Alle"], ["Rätselhafter Vogel+Schleim", "Rätselhafter Vogel+Blitz"])

#Weltenwanderer -> Gummikrieger + Fee ###
Weltenwanderer = Lebewesen("Weltenwanderer", "Eine gesichtslose Gestalt, die hin und wieder in dieser Welt auftaucht", 10, ["Alle"], ["Gummikrieger+Fee"])
# -> Stufe 1 -> +2 #Magie#
Wüstenwanderer = Lebewesen("Wüstenwanderer", "Taucht bevorzugt in endlosen heißen Wüsten oder Vulkanen auf; stärker im Lebensraum Wüste", 12, ["Alle"], ["Weltenwanderer+Feuer"])
Wasserwanderer = Lebewesen("Wasserwanderer", "Ein kleiner Junge der in einer fernen Welt in einem winzigen Bergsee ertrank und seitdem zwischen den Welten festhängt; stärker im Lebensraum See", 12, ["Alle"], ["Weltenwanderer+Wasser"])
Höhenwanderer = Lebewesen("Höhenwanderer", "Manchmal wirkt es so, als würde er ein Stückchen neben dem Berg in der Luft hängen; stärker im Lebensraum Berge", 12, ["Alle"], ["Weltenwanderer+Luft"])
Erdwanderer = Lebewesen("Erdwanderer", "Fühlt eine tiefe Verbundenheit zur Natur; stärker im Lebensraum Wald", 12, ["Alle"], ["Weltenwanderer+Erde"])
# -> Stufe 2 -> +4 #Wölkchen, Staub, Beere, Asche, Zeit#
# -> Stufe 3 -> +6 #Pusteblume, Pfingstrose, Perle, Sternenstaub, Kristall, Dunkle Macht#
# -> Stufe 4 -> +8 #Schleim, Eis, Blut, Blitz, Regenbogen, Engelshaar, Stein von Elyaris#

#Werwolf -> Zottel + Gummikrieger ###
Werwolf = Lebewesen("Werwolf", "Ein bei Tag unscheinbares Wesen, das sich erst bei Nacht in eine wolfsähnliche Kreatur verwandelt", 9, ["Wald"], ["Zottel+Gummikrieger"])
# -> Stufe 1 -> +2 #Wasser, Feuer, Erde, Luft, Magie#
# -> Stufe 2 -> +4 #Wölkchen, Beere, Zeit#
Urwolf = Lebewesen("Urwolf", "Ein alter grauer Werwolf, der einmal im Spiel eines deiner Lebewesen in einen Werwolf verwandeln kann", 13, ["Wald"], ["Werwolf+Staub", "Werwolf+Asche"])
# -> Stufe 3 -> +6 #Pusteblume, Pfingstrose, Perle, Sternenstaub, Kristall, Dunkle Macht#
# -> Stufe 4 -> +8 #Schleim, Eis, Blitz, Regenbogen, Engelshaar, Stein von Elyaris#
Blutwolf = Lebewesen("Blutwolf", "Rotes Fell in Erinnerung an eine Schlacht die den Mond blutig färbte", 17, ["Wald"], ["Werwolf+Blut"])


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
for Lw in Alle_Lebewesen:
    Lw.Lebensraum.append("Wonderland")

#Elemente
class Elemente(Karten):
    def __init__(self, Name, Beschreibung, Kombi = [], Start = False):
        Karten.__init__(self, Name, Beschreibung, Kombi, Start)
        if self.Start == True:
            Start_Elemente.append(self)
        Alle_Elemente.append(self)

#Vordruck
# = Elemente("", "", [""])
#Start/Stufe 1 -> +1
Wasser = Elemente("Wasser", "Eines der vier klassischen Elemente", [], True)
Feuer = Elemente("Feuer", "Eines der vier klassischen Elemente", [], True)
Erde = Elemente("Erde", "Eines der vier klassischen Elemente", [], True)
Luft = Elemente("Luft", "Eines der vier klassischen Elemente", [], True)
Magie = Elemente("Magie", "Eine leuchtende Kugel aus unbestimmter Macht", [], True)
#Stufe 2 -> +3
#Chaos = Elemente("Chaos", "Völliges Durcheinander", ["Magie+Magie"])
Wölkchen = Elemente("Wölkchen", "Flauschige schwebende Masse", ["Feuer+Wasser", "Wasser+Luft", "Wasser+Wasser"])
Staub = Elemente("Staub", "Etwas aufgewirbelte Erde", ["Luft+Erde", "Erde+Erde", "Luft+Luft"])
Beere = Elemente("Beere", "Eine süße Frucht aus dem Nachtwald Perelín", ["Wasser+Erde", "Magie+Erde", "Magie+Wasser"])
Asche = Elemente("Asche", "Der erste Schritt auf die dunkle Seite", ["Feuer+Erde", "Feuer+Luft", "Feuer+Feuer"])
Zeit = Elemente("Zeit", "Tick-tack tick-tack", ["Magie+Luft", "Magie+Feuer", "Magie+Magie"])
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
Stein_von_Elyaris = Elemente("Stein von Elyaris", "Stammt von einer Insel der 1. Überdimension und lässt einen alles vergessen", ["Staub+Asche", "Pfingstrose+Pusteblume", "Zeit+Asche", "Erde+Pfingstrose", "Erde+Perle", "Magie+Kristall", "Beere+Beere", "Zeit+Zeit"])
#für Verrückten Gnom/Kobold
Goldstück = Elemente("Goldstück", "Kann die Werte eines Lebewesens um 3 erhöhen oder einen Lebensraum um eins vergrößern")
Kessel_voller_Gold = Elemente("Kessel voller Gold", "Kann die Werte eines Lebewesens um 5 erhöhen oder einen Lebensraum um 3 vergrößern")

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
Schwarzer_Trank = Elemente("Schwarzer Trank", "Verringert die Werte eines zufälligen gegnerischen Lebewesens um 5")
Glitzernder_Trank = Elemente("Glitzernder Trank", "Erhöht die Werte eines Lebewesens um 7")
Duftender_Trank = Elemente("Duftender Trank", "Verwandelt einen Lebensraum in ein Wonderland, in dem alle Lebewesen leben können")
#Tränke -> Stufe 4
Himmlischer_Trank = Elemente("Himmlischer Trank", "Erhöht die Werte eines Lebewesens um 10")
Gefrorener_Trank = Elemente("Gefrorener Trank", "Friert alle Karten eines Spielers für 3 Züge ein")
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
#für alle Lebewesen alle möglichen Kombis mit allen Lebwesen und Elementen durchgehen
for Num_1, Lewe in enumerate(Alle_Lebewesen):
    #Lebewesen in Lebewesen und Element aus Kombi trennen wenn möglich, sonst keine weiteren Kombis
    Lewe_Lw = None
    Lewe_E = None
    #zufällige vorgegebene Kombi (nicht eindeutig wenn mit allen)
    if not Lewe.Kombi == []:
        Kom = random.choice(Lewe.Kombi)
        for Karte in Alle_Lebewesen:
            if Karte.Name == Kom.split("+")[0]:
                Lewe_Lw = Karte
                break
        for Karte in Alle_Elemente:
            if Karte.Name == Kom.split("+")[1]:
                Lewe_E = Karte
        if Lewe_E == None:
            Lewe_Lw = Lewe
    else:
        Lewe_Lw = Lewe
    #für alle Lebewesen, Kombis möglich mit Lewe?
    for Lw in Alle_Lebewesen[Num_1:]:
        #Lw in Lebewesen und Element aus Kombi trennen, wenn möglich, sonst weiter mit Lw
        Test = False
        if not Lw.Kombi == []:
            #zufällige Kombi
            K_ = random.choice(Lw.Kombi)
            Lw_Lw = None
            Lw_E = None
            for Karte in Alle_Lebewesen:
                if Karte.Name == K_.split("+")[0]:
                    Lw_Lw = Karte
                    break
            for Karte in Alle_Elemente:
                if Karte.Name == K_.split("+")[1]:
                    Lw_E = Karte
                    break
            if Lw_E == None:
                #weiter mit Lw
                Test = True
            else:
                #Lewe_lw und LW_Lw kombinieren und Lewe_e und Lw_e kombinieren, Kombi aus beidem -> Karte deren neue Kombi: Lewe+Lw
                Zwischen_Lw = None
                Zwischen_E = None
                for Karte in Alle_Lebewesen:
                    if Lewe_Lw.Name + "+" + Lw_Lw.Name in Karte.Kombi or Lw_Lw.Name + "+" + Lewe_Lw.Name in Karte.Kombi:
                        Zwischen_Lw = Karte
                        break
                for Karte in Alle_Elemente:
                    if Lewe_E == None:
                        Zwischen_E = Lw_E
                    else:
                        if Lewe_E.Name + "+" + Lw_E.Name in Karte.Kombi or Lw_E.Name + "+" + Lewe_E.Name in Karte.Kombi:
                            Zwischen_E = Karte
                            break
                if not Zwischen_Lw == None and not Zwischen_E == None:
                    for Karte in Alle_Lebewesen:
                        if Zwischen_Lw.Name + "+" + Zwischen_E.Name in Karte.Kombi:
                            if (not Lewe.Name + "+" + Lw.Name in Karte.Neue_Kombis) and (not Lw.Name + "+" + Lewe.Name in Karte.Neue_Kombis):
                                Karte.Neue_Kombis.append(Lewe.Name + "+" + Lw.Name)
                            break
        elif (Lw.Kombi == [] or Test == True) and not Lewe_E == None:
            #beide Lebewesen kombinieren + Element, Karte deren neue Kombi: Lewe+Lw
            Zwischen_Lw = None
            for Karte in Alle_Lebewesen:
                if Lewe_Lw.Name + "+" + Lw.Name in Karte.Kombi or Lw.Name + "+" + Lewe_Lw.Name in Karte.Kombi:
                    Zwischen_Lw = Karte
                    break
            if not Zwischen_Lw == None:
                for Karte in Alle_Lebewesen:
                    if Zwischen_Lw.Name + "+" + Lewe_E.Name in Karte.Kombi:
                        if not Lewe.Name + "+" + Lw.Name in Karte.Neue_Kombis and not Lw.Name + "+" + Lewe.Name in Karte.Neue_Kombis:
                            Karte.Neue_Kombis.append(Lewe.Name + "+" + Lw.Name)
                        break
    #für alle Elemente, Kombis möglich mit Lewe?
    for E in Alle_Elemente:
        Zwischen_E = None
        if Lewe_E == None:
            Zwischen_E = E
        else:
            for Karte in Alle_Elemente:
                if Lewe_E.Name + "+" + E.Name in Karte.Kombi or E.Name + "+" + Lewe_E.Name in Karte.Kombi:
                    Zwischen_E = Karte
                    break
        if not Zwischen_E == None:
            for Karte in Alle_Lebewesen:
                if Lewe_Lw.Name + "+" + Zwischen_E.Name in Karte.Kombi:
                    if not Lewe.Name + "+" + E.Name in Karte.Neue_Kombis:
                        Karte.Neue_Kombis.append(Lewe.Name + "+" + E.Name)
                    break
for Lw in Alle_Lebewesen:
    for Kom in Lw.Neue_Kombis:
        if not Kom in Lw.Kombi:
            Lw.Kombi.append(Kom)
Drache.Kombi.append("Koi+Koi")

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
ExtraLRs = {Wetterfee:"Zufall", Kleiner_Wirbelwind:"Zufall", Schimmerfee:"Alle", Wetter_Feenkönigin:"Alle"}

#Extrakarten - {Karte : Liste, aus der gewählt wird}
Extrakarten = {Traumdrache:random.choice(Alle_Start_Karten), #Startkarten
               Mystischer_Zottel:random.choice(Alle_Start_Karten),
               Lebensfee:random.choice(Alle_Start_Karten),
               Lebens_Feenkönigin:random.choice(Alle_Verteilung), #Alle
               Erzengel:random.choice(Alle_Verteilung),
               Starker_Traumdrache:random.choice(Alle_Verteilung),
               Mystische_Doppelzottel:random.choice(Alle_Verteilung),
               Erntefee:Start_Elemente, #Sonstige
               Gräberling:Start_Elemente,
               Babyfee:Start_Lebewesen,
               Ernte_Feenkönigin:Alle_Elemente,
               Baby_Feenkönigin:Alle_Lebewesen,
               Verrückter_Gnom:[Goldstück],
               Kobold:[Kessel_voller_Gold]}

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
                               Sea_People:2,
                               Dunkelfee:3,
                               Himmelszottel:3,
                               Dunkel_Feenkönigin:5,
                               Himmels_Doppelzottel:5}

#Aussetzen - {Karte:Anzahl Züge}, einmal pro Runde
Aussetzen_Karten = {Furchtdrache:1,
                    Starker_Furchtdrache:3,
                    Schreier:3,
                    Unwetterfee:3,
                    Unwetter_Feenkönigin:5}

#Lebensraum vergrößern - {Karte:Anzahl weiterer Plätze}, einmal pro Runde
Lr_Vergrößern = {Koi:1,
                 Schimmer_Feenkönigin:3}

#Gegner nötig für Extrafunktion
Gegner_Nötig = [Gefrorener_Trank, Diebische_Elster]
for Karte in Aussetzen_Karten:
    Gegner_Nötig.append(Karte)

#Counter für Extrafunktion nicht nach jeder Runde zurücksetzen z.B. für Karten mit Funktion einmal pro Spiel
Einmal_pro_Spiel = [Parasit, Friedensengel, Diebische_Elster, Urwolf, Schreier]

#Karten mit beschränkter Extrafunktion
Extrafunktion_Anzahl = {Parasit:1, Friedensengel:3, Diebische_Elster:3, Joker:1, Urwolf:1, Kleiner_Wirbelwind:1}
for Karte in Werteverbesserung_Übersicht:
    Extrafunktion_Anzahl.update({Karte:1})
for Karte in Aussetzen_Karten:
    if Karte == Schreier:
        Extrafunktion_Anzahl.update({Karte:3})
    else:
        Extrafunktion_Anzahl.update({Karte:1})
for Karte in Lr_Vergrößern:
    Extrafunktion_Anzahl.update({Karte:1})

#Lebewesen als Ziel von Extrafunktion: wenn Lr auf Feld gewählt, wird der aufgeklappt
Lw_Ziel = [Heißer_Trank, Wässriger_Trank, Matschiger_Trank, Blubbernder_Trank, Verkohlter_Trank, Güldener_Trank, Level_Up_Trank, Glitzernder_Trank, Himmlischer_Trank, #Tränke
           Parasit, Urwolf]
for Liste in [ExtraLRs, Werteverbesserung_Übersicht]:
    for Karte in Liste.keys():
        Lw_Ziel.append(Karte)

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