import random
import pygame as pg
pg.init()
import Karten
import string
import textbox
import SchriftMaxgröße
SMaxG = SchriftMaxgröße.SchriftFunc

#Startbildschirm
screen = pg.display.set_mode((1600, 900), pg.FULLSCREEN)
pg.display.set_caption("Klumpen")
Info_Surf = pg.Surface((450, 900))
Feld_Übersicht_Surf = pg.Surface((950, 50))
Feld_Surf = pg.Surface((1050, 270))
Ablage_Surf = pg.Surface((1050, 270))

#Bilder laden
Bilder = {}
def get_image(path):
    global Bilder
    path = "Bilder/" + path
    Bild = Bilder.get(path)
    if Bild == None:
        Bild = pg.image.load(path).convert_alpha()
        Bilder.update({Bild:path})
    return Bild

#Text erstellen
def get_Text(Schrift, Größe, Farbe = (0, 0, 0)):
    return (pg.font.Font(None, Größe)).render(Schrift, True, Farbe)

#Buttons
Buttons = []
class Button:
    def __init__(self, Rect, Funktion, Bild = None, Text = None, Bild_2 = None, Füllung = None):
        self.Rect = Rect
        self.Funktion = Funktion
        self.Bild = Bild
        self.Text = Text
        self.Bild_2 = Bild_2
        self.Füllung = Füllung
        self.Maus_Pos = False
        if not Bild_2 == None:
            self.Switch = False

    def create_button(self):
        Oberfläche = pg.Surface((self.Rect[2], self.Rect[3]), pg.SRCALPHA)
        if not self.Füllung == None:
            Oberfläche.fill(self.Füllung)
        #Bild und Text in die Mitte des Buttons
        if not self.Bild == None:
            Oberfläche.blit(self.Bild, (Oberfläche.get_width() / 2 - self.Bild.get_width() / 2, Oberfläche.get_height() / 2 - self.Bild.get_height() / 2))
        if not self.Bild_2 == None:
            self.Switch = False
        if not self.Text == None:
            Oberfläche.blit(self.Text, (Oberfläche.get_width() / 2 - self.Text.get_width() / 2, Oberfläche.get_height() / 2 - self.Text.get_height() / 2))
        screen.blit(Oberfläche, (self.Rect[0], self.Rect[1]))
        Buttons.append(self)

    def Change(self):
        if self.Switch == False:
            Change_Bild = self.Bild_2
            self.Switch = True
        elif self.Switch == True:
            Change_Bild = self.Bild
            self.Switch = False
        Oberfläche = pg.Surface((self.Rect[2], self.Rect[3]), pg.SRCALPHA)
        if not self.Füllung == None:
            Oberfläche.fill(self.Füllung)
        #anderes Bild und Text in die Mitte des Buttons
        Oberfläche.blit(Change_Bild, (Oberfläche.get_width() / 2 - Change_Bild.get_width() / 2, Oberfläche.get_height() / 2 - Change_Bild.get_height() / 2))
        if not self.Text == None:
            Oberfläche.blit(self.Text, (Oberfläche.get_width() / 2 - self.Text.get_width() / 2, Oberfläche.get_height() / 2 - self.Text.get_height() / 2))
        screen.blit(Oberfläche, (self.Rect[0], self.Rect[1]))

#Startbildschirm
screen.blit(get_image("hintergrundblass.png"), (0, 0))
#Klumpen
Klecks_Blau = get_image("klecks.png")
screen.blit(Klecks_Blau, (screen.get_width() / 2 - Klecks_Blau.get_width() / 2, screen.get_height() / 2 - Klecks_Blau.get_height() / 2 - 200)) #mittig von Schrift
Text_K = get_Text("Klumpen", 90, (255, 255, 255))
screen.blit(Text_K, (screen.get_width() / 2 - Text_K.get_width() / 2, screen.get_height() / 2 - Text_K.get_height() / 2 - 200)) #mittig, etwas nach oben verschoben
#Regeln
Regeln_Button.create_button()
#Start
Start_Button.create_button()

#Buttons und Funktionen
Einstellungen = [None, [], 0, 0] #[Modus, Spieler, Runden, Züge]
#Modus
Kreis_Bild = get_image("kreisbild.png")
Kreis_Bild_2 = get_image("kreisbild2.png")
def Punkte_Funk():
    Einstellungen[0] = "Punkte"
    if Punkte_Button.Switch == False:
        Punkte_Button.Change()
    if Kampf_Button.Switch == True:
        Kampf_Button.Change()
Punkte_Rect = pg.Rect(220, 100, Kreis_Bild.get_width(), Kreis_Bild.get_height())
Punkte_Button = Button(Punkte_Rect, Punkte_Funk, Kreis_Bild, None, Kreis_Bild_2)
def Kampf_Funk():
    Einstellungen[0] = "Kampf"
    if Kampf_Button.Switch == False:
        Kampf_Button.Change()
    if Punkte_Button.Switch == True:
        Punkte_Button.Change()
Kampf_Rect = pg.Rect(screen.get_width() / 2 + 150, 100, Kreis_Bild.get_width(), Kreis_Bild.get_height())
Kampf_Button = Button(Kampf_Rect, Kampf_Funk, Kreis_Bild, None, Kreis_Bild_2)

#Spieler
Kleiner_Haken = get_image("hakenklein.png")
Kleiner_Haken_Blass = get_image("hakenkleinblass.png")
Kreuz = get_image("kreuz.png")
Kreuz_Blass = get_image("kreuzblass.png")
Input_Box = textbox.TextBox((900, 320, 420, 50))
def Print_Spieler():
    Spieler_Liste = Einstellungen[1]
    Counter = len(Spieler_Liste)
    Fertig = 0
    while Fertig < 5:
        Dings = Spieler_Hintergrund[Fertig+1]
        Fläche = Dings[1]
        pg.draw.rect(screen, (255, 255, 255), Fläche)
        pg.draw.rect(screen, (0, 0, 0), Fläche, 1)
        Weg_Button = Dings[0]
        if Weg_Button.Switch == True:
            Weg_Button.Change()
        Fertig += 1
    Fertig = 0
    while Counter > 0:
        Spieler_Name = Spieler_Liste[Fertig]
        Text = get_Text(Spieler_Name, 50)
        screen.blit(Text, (185, 305 + 20*(Fertig+1)+ 50*Fertig))
        Dings = Spieler_Hintergrund[Fertig+1]
        Weg_Button = Dings[0]
        if Weg_Button.Switch == False:
            Weg_Button.Change()
        Counter -= 1
        Fertig += 1
def Spieler_Entf(Index):
    Spieler_Liste = Einstellungen[1]
    if (Index + 1) <= len(Spieler_Liste):
        Spieler_Liste.remove(Spieler_Liste[Index])
        Print_Spieler()
Spieler_Hintergrund = {}
Weg_Button_1 = Button(pg.Rect(620, 325, Kreuz.get_width(), Kreuz.get_height()), lambda: Spieler_Entf(0), Kreuz_Blass, None, Kreuz)
Weg_Button_2 = Button(pg.Rect(620, 395, Kreuz.get_width(), Kreuz.get_height()), lambda: Spieler_Entf(1), Kreuz_Blass, None, Kreuz)
Weg_Button_3 = Button(pg.Rect(620, 465, Kreuz.get_width(), Kreuz.get_height()), lambda: Spieler_Entf(2), Kreuz_Blass, None, Kreuz)
Weg_Button_4 = Button(pg.Rect(620, 535, Kreuz.get_width(), Kreuz.get_height()), lambda: Spieler_Entf(3), Kreuz_Blass, None, Kreuz)
Weg_Button_5 = Button(pg.Rect(620, 605, Kreuz.get_width(), Kreuz.get_height()), lambda: Spieler_Entf(4), Kreuz_Blass, None, Kreuz)
Weg_Buttons = [Weg_Button_1, Weg_Button_2, Weg_Button_3, Weg_Button_4, Weg_Button_5]
Counter = 1
while Counter <= 5:
    for B in Weg_Buttons:
        Spieler_Hintergrund.update({Counter:[B]})
        Counter += 1
def Spieler_Hinzu(Name = None):
    if Spieler_Hinzu_Button.Switch == True:
        Input_Box.buffer = []
        if Name == None:
            Name = Input_Box.final
        if Name in Einstellungen[1]:
            Text = get_Text("Wähle unterschiedliche Spielernamen", 30, pg.Color("red"))
            screen.blit(Text, (900 + (210 - Text.get_width() / 2), 420))
        else:
            Einstellungen[1].append(Name)
            Print_Spieler()
Spieler_Hinzu_Button = Button(pg.Rect(1350, 320, Kleiner_Haken.get_width(), Kleiner_Haken.get_height()), Spieler_Hinzu, Kleiner_Haken_Blass, None, Kleiner_Haken)

#Runden und Züge
Runden_Box = textbox.TextBox((290, 800, 200, 50))
Züge_Box = textbox.TextBox((801.5, 800, 200, 50))
Boxen = [Input_Box, Runden_Box, Züge_Box]
#Fertig Button
Großer_Haken = get_image("hakengroß.png")
Großer_Haken_Blass = get_image("hakengroßblass.png")
def Fertig():
    if Fertig_Button.Switch == True:
        global Modus
        global Alle_Spieler
        global Runden
        global Züge
        Modus = Einstellungen[0]
        Alle_Spieler = Einstellungen[1]
        Runden = Einstellungen[2]
        Züge = Einstellungen[3]
        global Input
        Input = False
        global Buttons
        Buttons = []
        Spiel()
Fertig_Button = Button(pg.Rect(1250, 660, Großer_Haken.get_width(), Großer_Haken.get_height()), Fertig, Großer_Haken_Blass, None, Großer_Haken)

#Regeln
def Regeln():
    pass
Regeln_Bild = get_image("regeln.png")
Text_R = get_Text("Regeln", 70)
Regeln_Rect = pg.Rect(600 - Regeln_Bild.get_width(), 500, Regeln_Bild.get_width(), Regeln_Bild.get_height())
Regeln_Button = Button(Regeln_Rect, Regeln, Regeln_Bild, Text_R)

#Start
def Start():
    global Buttons
    Buttons = []
    screen.blit(get_image("hintergrundblass.png"), (0, 0))
    #Modus
    Text = get_Text("Modus?", 50)
    screen.blit(Text, (screen.get_width() / 2 - Text.get_width() / 2, 30))
    PT2 = get_Text("- Sammele möglichst viele Punkte", 30)
    PT3 = get_Text("   durch Kombination von Karten", 30)
    screen.blit(PT2, (320, 150))
    screen.blit(PT3, (320, 180))
    PT1 = get_Text("Punkte", 45)
    screen.blit(PT1, (320 + (PT2.get_width() / 2 - PT1.get_width() / 2), 100))
    KT2 = get_Text("- Entwickele durch Kombination starke", 30)
    KT3 = get_Text(" Lebewesen für die folgende Kampfphase", 30)
    screen.blit(KT2, (screen.get_width() / 2 + 300, 150))
    screen.blit(KT3, (screen.get_width() / 2 + 300, 180))
    KT1 = get_Text("Kampf", 45)
    screen.blit(KT1, ((screen.get_width() / 2 + 300) + (PT2.get_width() / 2 - PT1.get_width() / 2), 100))
    Punkte_Button.create_button()
    Kampf_Button.create_button()
    #Spieler
    Text = get_Text("Spieler?", 50)
    screen.blit(Text, (screen.get_width() / 2 - Text.get_width() / 2, 240))
    Text = get_Text("1 bis 5", 35)
    screen.blit(Text, (screen.get_width() / 2 - Text.get_width() / 2, 280))
    Text = get_Text("Spielernamen eingeben", 35)
    screen.blit(Text, (900 + (210 - Text.get_width() / 2), 380))
    Spieler_Hinzu_Button.create_button()
    Input_Box.process_kwargs({"command":Spieler_Hinzu, "clear_on_enter":True})
    Input_Box.update()
    Input_Box.draw(screen)
    for Num in Spieler_Hintergrund:
        Dings = Spieler_Hintergrund[Num]
        y = 300 + 20*Num + 50*(Num-1)
        Fläche = pg.Rect(180, y, 420, 50)
        pg.draw.rect(screen, (255, 255, 255), Fläche)
        pg.draw.rect(screen, (0, 0, 0), Fläche, 1)
        Dings[0].create_button()
        Spieler_Hintergrund[Num].append(Fläche)
    #Runden und Züge
    Text_1 = get_Text("Runden?", 50)
    screen.blit(Text_1, (180 + (210 - Text_1.get_width() / 2), 680))
    Text = get_Text("- 5 bis 20 Runden empfohlen", 30)
    screen.blit(Text, ((180 + (210 - Text_1.get_width() / 2)) - (Text.get_width() / 2 - Text_1.get_width() / 2), 730))
    Text = get_Text("- pro Runde werden neue Karten ausgegeben", 30)
    screen.blit(Text, ((180 + (210 - Text_1.get_width() / 2)) - (Text.get_width() / 2 - Text_1.get_width() / 2), 760))
    Text_2 = get_Text("Züge?", 50)
    screen.blit(Text_2, (850, 680))
    Text = get_Text("- 3 bis 10 Züge empfohlen", 30)
    screen.blit(Text, (850 - (Text.get_width() / 2 - Text_2.get_width() / 2), 730))
    Text = get_Text("- Aktionen pro Spieler pro Runde", 30)
    screen.blit(Text, (850 - (Text.get_width() / 2 - Text_2.get_width() / 2), 760))
    Runden_Box.process_kwargs({"ACCEPTED":string.digits})
    Runden_Box.update()
    Runden_Box.draw(screen)
    Züge_Box.process_kwargs({"ACCEPTED":string.digits})
    Züge_Box.update()
    Züge_Box.draw(screen)
    global Input
    Input = True
    #Fertig Button
    Fertig_Button.create_button()
Start_Bild = get_image("start.png")
Text_S = get_Text("Start", 70)
Start_Rect = pg.Rect(1000, 500, Start_Bild.get_width(), Start_Bild.get_height())
Start_Button = Button(Start_Rect, Start, Start_Bild, Text_S)

##############################################################################################################################################################################
###############################################################################################################################################################################
#Spiel
#Dicts; they work, don't touch
Feld = {}
Ablage = {}
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

###Buttons (self, Rect, Funktion, Bild = None, Text = None, Bild_2 = None, Füllung = None)###

##Schiebebuttons##
#Ablage schieben
#Hoch
Pfeil_Hoch_Blass = get_image("pfeilhochblass.png")
Pfeil_Hoch = get_image("pfeilhoch.png")
def Ablage_Hoch():
    pass
Hoch_Rect = pg.Rect(1590 - Pfeil_Hoch.get_width(), 480, Pfeil_Hoch.get_width(), Pfeil_Hoch.get_height())
Ablage_Hoch_Button = Button(Hoch_Rect, Ablage_Hoch, Pfeil_Hoch_Blass, None, Pfeil_Hoch)
def Ablage_Hoch():
    global Ablage_Alt_Range
    if Ablage_Hoch_Button.Switch == True:
        Ausgabe(Spieler, Ablage_Surf, range(Ablage_Alt_Range - 6, Ablage_Alt_Range - 1))
#Runter
Pfeil_Runter_Blass = get_image("pfeilrunterblass.png")
Pfeil_Runter = get_image("pfeilrunter.png")
def Ablage_Runter():
    pass
Runter_Rect = pg.Rect(1590 - Pfeil_Runter.get_width(), 750 - Pfeil_Runter.get_height(), Pfeil_Runter.get_width(), Pfeil_Runter.get_height())
Ablage_Runter_Button = Button(Runter_Rect, Ablage_Runter, Pfeil_Runter_Blass, None, Pfeil_Runter)
def Ablage_Runter():
    global Ablage_Alt_Range
    if Ablage_Runter_Button.Switch == True:
        Ausgabe(Spieler, Ablage_Surf, range(Ablage_Alt_Range + 6, Ablage_Alt_Range + 12))
#Feld Übersicht schieben
#Links
Pfeil_Links_Blass = get_image("pfeillinksblass.png")
Pfeil_Links = get_image("pfeillinks.png")
def Feld_Übersicht_Links():
    pass
Links_Rect = pg.Rect(455, 120, Pfeil_Links.get_width(), Pfeil_Links.get_height())
Feld_Übersicht_Links_Button = Button(Links_Rect, Feld_Übersicht_Links, Pfeil_Links_Blass, None, Pfeil_Links)
def Feld_Übersicht_Links():
    global Feld_Übersicht_Alt_Range
    if Feld_Übersicht_Links_Button.Switch == True:
        Ausgabe(Spieler, Feld_Übersicht_Surf, range(Feld_Übersicht_Alt_Range - 6, Feld_Übersicht_Alt_Range - 1))
#Rechts
Pfeil_Rechts_Blass = get_image("pfeilrechtsblass.png")
Pfeil_Rechts = get_image("pfeilrechts.png")
def Feld_Übersicht_Rechts():
    pass
Rechts_Rect = pg.Rect(1590 - Pfeil_Rechts.get_width(), 120, Pfeil_Rechts.get_width(), Pfeil_Rechts.get_height())
Feld_Übersicht_Rechts_Button = Button(Rechts_Rect, Feld_Übersicht_Rechts, Pfeil_Rechts_Blass, None, Pfeil_Rechts)
def Feld_Übersicht_Rechts():
    global Feld_Übersicht_Alt_Range
    if Feld_Übersicht_Rechts_Button.Switch == True:
        Ausgabe(Spieler, Feld_Übersicht_Surf, range(Feld_Übersicht_Alt_Range + 6, Feld_Übersicht_Alt_Range + 12))
#Feld schieben
#Hoch
def Feld_Hoch():
    pass
F_Hoch_Rect = pg.Rect(1590 - Pfeil_Hoch.get_width(), 180, Pfeil_Hoch.get_width(), Pfeil_Hoch.get_height())
Feld_Hoch_Button = Button(F_Hoch_Rect, Feld_Hoch, Pfeil_Hoch_Blass, None, Pfeil_Hoch)
def Feld_Hoch():
    global Feld_Alt_Range
    if Feld_Hoch_Button.Switch == True:
        Ausgabe(Spieler, Feld_Surf, range(Feld_Alt_Range - 6, Feld_Alt_Range - 1), Alt_LR_Pos)
#Runter
def Feld_Runter():
    pass
F_Runter_Rect = pg.Rect(1590 - Pfeil_Runter.get_width(), 450 - Pfeil_Runter.get_height(), Pfeil_Runter.get_width(), Pfeil_Runter.get_height())
Feld_Runter_Button = Button(F_Runter_Rect, Feld_Runter, Pfeil_Runter_Blass, None, Pfeil_Runter)
def Feld_Runter():
    global Feld_Alt_Range
    if Feld_Runter_Button.Switch == True:
        Ausgabe(Spieler, Feld_Surf, range(Feld_Alt_Range + 6, Feld_Alt_Range + 12), Alt_LR_Pos)

##Regeln und Nächster##
#Regeln
R_Bild = get_image("regelnklein.png")
R_Text = get_Text("Regeln", 40)
R_Rect = pg.Rect(455, 10, R_Bild.get_width(), R_Bild.get_height())
Regel_Spiel_Button = Button(R_Rect, Regeln, R_Bild, R_Text)
#Weiter
Runden_Counter = 0
Züge_Counter = 0
Extrazüge_Dict = {}
EZ = True
def Nächster():
    pass
Nächster_Bild = get_image("startklein.png")
Nächster_Text = get_Text("Fertig", 40)
Nächster_Rect = pg.Rect(1550 - Nächster_Bild.get_width(), 10, Nächster_Bild.get_width(), Nächster_Bild.get_height())
Nächster_Button = Button(Nächster_Rect, lambda: Nächster(Spieler), Start_Bild, Nächster_Text)
def Nächster(Alter_Spieler):
    pg.draw.rect(screen, (255, 255, 255), pg.Rect(610, 0, 800, 100))
    global Runden_Counter
    global Züge_Counter
    global Züge_String
    global Runden_String
    global Züge
    global Runden
    global Spieler
    global Extrazüge_Dict
    global EZ
    global Aktion
    Neuer_Spieler = None
    #Züge
    if Alter_Spieler == Alle_Spieler[-1]:
        Züge_Counter += 1
        #Überschrift
        Übrig = Züge - Züge_Counter
        Züge_String = "noch " + str(Übrig) + " Züge"
        if Übrig == 1:
            Züge_String = "letzter Zug"
        #Letzter Spieler mit letzem Zug -> Runde vorbei
        if Züge_Counter == Züge:
            #Extrazüge berechnen
            if EZ == True:
                EZ = False
                for Spieler in Alle_Spieler:
                    Extracounter = 0
                    Extrazüge_Dict.update({Spieler:[[], 0]})
                    Feld_Spieler = Feld[Spieler]
                    for LR in Feld[Spieler]:
                        for LW in Feld_Spieler[LR]:
                            if LW in Extrazüge:
                                Extracounter += Extrazüge[LW]
                                Extrazüge_Dict[Spieler][0].append(LW)
                    Extrazüge_Dict[Spieler][1] = Extracounter
            #Extrazüge ausführen#################Fehler########################
            for Spieler in Alle_Spieler:
                if Spieler in Extrazüge_Dict:
                    if Extrazüge_Dict[Spieler][1] == 0:
                        Extrazüge_Dict.pop(Spieler)
            if not Extrazüge_Dict == {}:
                Spieler = Extrazüge_Dict[0]
                String = "Extrazüge\n"
                for LW in Extrazüge_Dict[Spieler][0]:
                    String += Karte.Name + ": + " + str(Extrazüge[LW]) + "\n"
                String += "Insgesamt: + " + str(Extrazüge_Dict[Spieler][1])
                Info_Text(String)
                Extrazüge_Dict[Spieler][0].remove(Extrazüge_Dict[Spieler][0][0])
                Neuer_Spieler = Spieler
                Übrig = Extrazüge_Dict[Spieler][1]
                Züge_String = "noch " + str(Übrig) + " Züge"
                if Übrig == 1:
                    Züge_String = "letzter Zug"
            #Runde fertig wenn Extrazüge aufgebraucht
            if Extrazüge_Dict == {}:
                Runden_Counter += 1
                #Spiel zuende?
                if Runden_Counter == Runden:
                    Ende()
                    return
                Züge_Counter = 0
                Züge_String = "noch " + str(Züge) + " Züge"
                if Züge == 1:
                    Züge_String = "letzter Zug"
                Übrig = Runden - Runden_Counter
                Runden_String = "noch " + str(Übrig) + " Runden"
                if Übrig == 1:
                    Runden_String = "letzte Runde"
                EZ = True
                #Werteverbesserungskarten pro Runde
                WAS = Werteverbesserung_Anzahl[Spieler]
                for WV_Karte in WAS:
                    if (not WV_Karte == Karten.Parasit) and (not WV_Karte == Karten.Friedensengel) and (not WV_Karte == Karten.Diebische_Elster) and (not WV_Karte == Karten.Urwolf):
                        WASK = WAS[WV_Karte]
                        WASK[0] = WASK[1]
                #Auswahlstapel
                ##############
    #Neuer Spieler (der nach dem alten)
    if Neuer_Spieler == None:
        for N in range(0, len(Alle_Spieler)):
            if Alle_Spieler[N] == Alter_Spieler:
                Num = N + 1
                if Num > (len(Alle_Spieler) - 1):
                    Num = 0
                break
        Spieler = Alle_Spieler[Num]
        Info_Surf.fill((255, 255, 255))
        screen.blit(Info_Surf, (0, 0))
    else:
        Spieler = Neuer_Spieler
    global Spieler_Zug
    Spieler_Zug = False
    Aktion = None
    #Überschrift
    Text = SMaxG(Runden_String, None, 30)
    screen.blit(Text, (610 + (415 / 2 - Text.get_width() / 2), 10))
    Text = SMaxG(Züge_String, None, 30)
    screen.blit(Text, (610 + (415 / 2 - Text.get_width() / 2), 60))
    if Spieler[-1] == "s" or Spieler[-1] == "S" or Spieler[-1] == "X" or Spieler[-1] == "x":
        Text = SMaxG(Spieler + "\' Zug", 350, 50)
    else:
        Text = SMaxG(Spieler + "s Zug", 350, 50)
    screen.blit(Text, (1025 + (415 / 2 - Text.get_width() / 2), 50 - Text.get_height() / 2))
    Ausgabe(Spieler, Ablage_Surf)
    Ausgabe(Spieler, Feld_Übersicht_Surf)

##Karten Buttons##
#Ablage
Karten_Ablage_Rects = []
x = 475
y = 490
for Num in range(0, 6):
    KaAbRe = pg.Rect(x, y, 150, 250)
    Karten_Ablage_Rects.append(KaAbRe)
    x += 170

Ablage_Button_0 = Button(Karten_Ablage_Rects[0], lambda: Karten_Func("Ablage", 0))
Ablage_Button_1 = Button(Karten_Ablage_Rects[1], lambda: Karten_Func("Ablage", 1))
Ablage_Button_2 = Button(Karten_Ablage_Rects[2], lambda: Karten_Func("Ablage", 2))
Ablage_Button_3 = Button(Karten_Ablage_Rects[3], lambda: Karten_Func("Ablage", 3))
Ablage_Button_4 = Button(Karten_Ablage_Rects[4], lambda: Karten_Func("Ablage", 4))
Ablage_Button_5 = Button(Karten_Ablage_Rects[5], lambda: Karten_Func("Ablage", 5))

#Feld
Karten_Feld_Rects = []
x = 475
y = 190
for Num in range(0, 6):
    KaFeRe = pg.Rect(x, y, 150, 250)
    Karten_Feld_Rects.append(KaFeRe)
    x += 170

Feld_Button_0 = Button(Karten_Feld_Rects[0], lambda: Karten_Func("Feld", 0))
Feld_Button_1 = Button(Karten_Feld_Rects[1], lambda: Karten_Func("Feld", 1))
Feld_Button_2 = Button(Karten_Feld_Rects[2], lambda: Karten_Func("Feld", 2))
Feld_Button_3 = Button(Karten_Feld_Rects[3], lambda: Karten_Func("Feld", 3))
Feld_Button_4 = Button(Karten_Feld_Rects[4], lambda: Karten_Func("Feld", 4))
Feld_Button_5 = Button(Karten_Feld_Rects[5], lambda: Karten_Func("Feld", 5))

#Feld Übersicht
Karten_Feld_Übersicht_Rects = []
x = 585
y = 140
for Num in range(0, 9):
    KaÜbRe = pg.Rect(x, y, 80, 40)
    Karten_Feld_Übersicht_Rects.append(KaÜbRe)
    x += 100

Feld_Übersicht_Button_0 = Button(Karten_Feld_Übersicht_Rects[0], lambda: Karten_Func("Feld_Übersicht", 0))
Feld_Übersicht_Button_1 = Button(Karten_Feld_Übersicht_Rects[1], lambda: Karten_Func("Feld_Übersicht", 1))
Feld_Übersicht_Button_2 = Button(Karten_Feld_Übersicht_Rects[2], lambda: Karten_Func("Feld_Übersicht", 2))
Feld_Übersicht_Button_3 = Button(Karten_Feld_Übersicht_Rects[3], lambda: Karten_Func("Feld_Übersicht", 3))
Feld_Übersicht_Button_4 = Button(Karten_Feld_Übersicht_Rects[4], lambda: Karten_Func("Feld_Übersicht", 4))
Feld_Übersicht_Button_5 = Button(Karten_Feld_Übersicht_Rects[5], lambda: Karten_Func("Feld_Übersicht", 5))

#Karten Funktion
Alt_LR_Pos = 0
Kombi_List = []
def Karten_Func(Kategorie, Button_Num):
    global Spieler
    global Aktion
    global Kombi_List
    if Kategorie == "Ablage":
        List = Ablage[Spieler]
        global Ablage_Alt_Range
        Alt_Range = Ablage_Alt_Range
    elif Kategorie == "Feld":
        global Alt_LR_Pos
        List = Feld[Spieler][Alt_LR_Pos]
        global Feld_Alt_Range
        Alt_Range = Feld_Alt_Range
    elif Kategorie == "Feld_Übersicht":
        List = Feld[Spieler]
        global Feld_Übersicht_Alt_Range
        Alt_Range = Feld_Übersicht_Alt_Range
    Num = Alt_Range[Button_Num]
    if Num <= (len(List) - 1):
        Karte = List[Num]
        #Funktionen, Kombi, etc
        if Aktion == "Kombi":
            Kombi_List.append(Karte.Name)
            if len(Kombi_List) == 1:
                Info_Text("Kombi:\n" + Karte.Name + " + ?\nWähle eine weitere Karte")
            elif len(Kombi_List) == 2:
                Add(Kombi_List)
                Aktion = None
        #normal Text am Rand ausgeben
        else:
            if Kategorie == "Feld_Übersicht":
                Ausgabe(Spieler, Feld_Surf, range(0, 6), Num)
                if Modus == "Punkte":
                    Info_Text(Karte.Name + "\n" + Karte.Beschreibung + "\n" + "Punkte: " + Karte.Punkte)
                else:
                    Info_Text(Karte.Name + "\n" + Karte.Beschreibung)
            else:
                Info_Text(Karte.Name + "\n" + Karte.Beschreibung)

##Spielfunktionen Buttons##
Aktion = None
def Aktion_Func(Aktion_):
    global Aktion
    Aktion = Aktion_
    if Aktion == "Kombi":
        Info_Text("Wähle zwei Karten, die du kombinieren möchtest")
Kombi_Rect = pg.Rect()
Kombi_Button = Button(Kombi_Rect, Kombi_Func(), None, "Kombi")

##Ausgabefunktionen##
#Ausgabe von: Feld, Ablage, Übersicht
def Ausgabe(Spieler, Surf, Range = range(0, 6), LR_Pos = None):
    Feld_Spieler = Feld[Spieler]
    Surf.fill((255, 255, 255))
    global Feld_Übersicht_Alt_Range
    if Surf == Ablage_Surf or Surf == Feld_Surf:
        #Ablage
        if Surf == Ablage_Surf:
            y_Surf = 480
            x_Surf = 452
            List = Ablage[Spieler]
            #für Buttons
            global Ablage_Alt_Range
            Ablage_Alt_Range = Range
            #Ausgabe von Verbesserungen, alt
            CDS = Counter_Dict[Spieler]
            Feld_Spieler = Feld[Spieler]
            for Karte in CDS:
                CDS[Karte] = False
                Test = True
                for LR in Feld[Spieler]:
                    if Karte == LR or Karte in Feld_Spieler[LR]:
                        Test = False
                if Test == True and Karte in Ablage[Spieler]:
                    CDS[Karte] = True
            #Sortieren
            Liste = Ablage[Spieler].copy()
            Ablage[Spieler].clear()
            for Karte in Liste:
                if Karte in Karten.Alle_Lebewesen:
                    Ablage[Spieler].append(Karte)
            for Karte in Liste:
                if Karte in Karten.Alle_Lebensraum:
                    Ablage[Spieler].append(Karte)
            for Karte in Liste:
                if Karte in Karten.Alle_Elemente:
                    Ablage[Spieler].append(Karte)
            #Buttons wenn Ablage oben oder unten mehr Karten
            if Range[0] > 0 and Ablage_Hoch_Button.Switch == False:
                Ablage_Hoch_Button.Change()
            else:
                if Ablage_Hoch_Button.Switch == True:
                    Ablage_Hoch_Button.Change()
            if (len(Ablage[Spieler]) > (Range[-1])) and Ablage_Runter_Button.Switch == False:
                Ablage_Runter_Button.Change()
            else:
                if Ablage_Runter_Button.Switch == True:
                    Ablage_Runter_Button.Change()
        #Feld
        elif Surf == Feld_Surf:
            y_Surf = 180
            x_Surf = 452
            LR = Feld[Spieler][Feld[Spieler].keys()[Feld_Übersicht_Alt_Range[LR_Pos]]]
            List = Feld[Spieler][LR]
            #für Buttons
            global Feld_Alt_Range
            Feld_Alt_Range = Range
            global Alt_LR_Pos
            Alt_LR_Pos = LR_Pos
            #Ausgabe von Verbesserung, dont touch
            #Couter, Magisch, Stärker Dicts
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
            #Buttons
            if Range[0] > 0 and Feld_Hoch_Button.Switch == False:
                Feld_Hoch_Button.Change()
            else:
                if Feld_Hoch_Button.Switch == True:
                    Feld_Hoch_Button.Change()
            if (len(Feld_Spieler[LR]) > (Range[-1])) and Feld_Runter_Button.Switch == False:
                Feld_Runter_Button.Change()
            else:
                if Feld_Runter_Button.Switch == True:
                    Feld_Runter_Button.Change()
        #Teile drucken
        Width = 25
        Height = 10
        for Num in Range:
            if len(List) >= (Num + 1):
                Surf.blit(Druck(List[Num], Spieler), (Width, Height))
                Width += 170
    #Feld Übersicht
    elif Surf == Feld_Übersicht_Surf:
        y_Surf = 130
        x_Surf = 520
        Feld_Übersicht_Alt_Range = Range
        Range_1 = range(Range[0], Range[0] + 9)
        #Surface zusammensetzen
        Dings = pg.Surface((80, 40))
        y = 10
        x = 35
        for Num in Range_1:
            if len(Feld_Spieler) >= (Num + 1):
                LR = Feld_Spieler[Feld_Spieler.keys()[Num]]
                Mod_Größe = LR.Größe
                if LR in CDS:
                    Verbesserung_Spieler = Verbesserung[Spieler]
                    Verbesserung_Karte = Verbesserung_Spieler[LR]
                    Add_Größe = Verbesserung_Karte
                    Mod_Größe = LR.Größe + Add_Größe
                if LR.Art == "Wald":
                    Hintergrund = (190, 240, 50)
                elif LR.Art == "Wüste":
                    Hintergrund = (255, 190, 0)
                elif LR.Art == "Berge":
                    Hintergrund = (220, 170, 130)
                elif LR.Art == "See":
                    Hintergrund = (170, 240, 255)
                elif LR.Art == "Wonderland":
                    Hintergrund = (240, 170, 255)
                Dings.fill(Hintergrund)
                Cap = SMaxG(LR.Name, 80, 18)
                Inside = SMaxG(str(len(Feld[Spieler][LR])) + " / " + str(LR.Mod_Größe), 80, 18)
                Dings.blit(Cap, (40 - Cap.get_width() / 2, 5))
                Dings.blit(Inside, (40 - Inside.get_width() / 2, 22))
                Feld_Übersicht_Surf.blit(Dings, (x, y))
                x += 100
        #Buttons wenn Übersicht links oder rechts
        if Range[0] > 0 and Feld_Übersicht_Links_Button.Switch == False:
            Feld_Übersicht_Links_Button.Change()
        else:
            if Feld_Übersicht_Links_Button.Switch == True:
                Feld_Übersicht_Links_Button.Change()
        if (len(Feld[Spieler]) > (Range[-1])) and Feld_Übersicht_Rechts_Button.Switch == False:
            Feld_Übersicht_Rechts_Button.Change()
        else:
            if Feld_Übersicht_Rechts_Button.Switch == True:
                Feld_Übersicht_Rechts_Button.Change()
    #Surface auf Bildschirm
    screen.blit(Surf, (x_Surf, y_Surf))        

#einzelne Karte ausgeben
def Druck(Karte, Spieler):
    global Modus
    CDS = Counter_Dict[Spieler]
    MDS = Magisch_Dict[Spieler]
    SDS = Stärker_Dict[Spieler]
    Surf = pg.Surface((150, 250))
    #Hintergrund und Art
    if Karte in Karten.Alle_Lebewesen:
        Hintergrund = get_image("lw_hintergrund.png")
        Cap = SMaxG("Lebewesen", 150, 20)
    elif Karte in Karten.Alle_Lebensraum:
        Hintergrund = get_image("lr_hintergrund.png")
        Cap = SMaxG("Lebensraum", 150, 20)
    elif Karte in Karten.Alle_Elemente:
        Hintergrund = get_image("e_hintergrund.png")
        Cap = SMaxG("Element", 150, 20)
    Surf.blit(Hintergrund, (0, 0))
    Surf.blit(Cap, (150 / 2 - Cap.get_width() / 2, 5))
    #Name
    if " " in Karte.Name:
        Namen_Liste = Karte.Name.split()
        Name_1 = get_Text(Namen_Liste[0], 58)
        if Name_1.get_width() > 150:
            Name_1 = SMaxG(Namen_Liste[0], 150)
        Name_2 = get_Text(Namen_Liste[1], 58)
        if Name_2.get_width() > 150:
            Name_2 = SMaxG(Namen_Liste[1], 150)
        Surf.blit(Name_1, (150 / 2 - Name_1.get_width() / 2, 35))
        Surf.blit(Name_2, (150 / 2 - Name_2.get_width() / 2, 80))
    else:
        Name = get_Text(Karte.Name, 58)
        if Name.get_width() > 150:
            Name = SMaxG(Karte.Name, 150)
        Surf.blit(Name, (150 / 2 - Name.get_width() / 2, 35))
    #Lebewesen: LRs, Punkte/Kampf, Verteidigung 
    if Karte in Karten.Alle_Lebewesen:
        #altes repr, dont touch
        Mod_Punkte = Karte.Punkte
        Mod_Angriff = Karte.Angriff
        Mod_Verteidigung = Karte.Verteidigung
        Mod_Lebensraum_ = []
        for LR in Karte.Lebensraum:
            if not LR == "Wonderland":
                Mod_Lebensraum_.append(LR)
        Mod_Lebensraum = ""
        for LR in Mod_Lebensraum_:
            Mod_Lebensraum = Mod_Lebensraum + LR + ", "
        Mod_Lebensraum = Mod_Lebensraum.strip(", ")
        if Karte in CDS:
            if CDS[Karte] == True:
                Verbesserung_Spieler = Verbesserung[Spieler]
                Verbesserung_Karte = Verbesserung_Spieler[Karte]
                Add_Angriff = Verbesserung_Karte["Angriff"]
                Mod_Angriff = Karte.Angriff + Add_Angriff
                if Mod_Angriff < 0:
                    Mod_Angriff = 0
                Add_Verteidigung = Verbesserung_Karte["Verteidigung"]
                Mod_Verteidigung = Karte.Verteidigung + Add_Verteidigung
                if Mod_Verteidigung < 0:
                    Mod_Verteidigung = 0
                Add_Punkte = Verbesserung_Karte["Punkte"]
                Mod_Punkte = Karte.Punkte + Add_Punkte
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
                CDS[Karte] = False
        if Karte in Magisch_Dict[Spieler]:
            if MDS[Karte] > 0:
                Mod_Angriff += 1
                Mod_Verteidigung += 1
                Mod_Punkte += 1
                MDS[Karte] -= 1
        if Karte in Stärker_Dict[Spieler]:
            if SDS[Karte] > 0:
                Mod_Angriff += 2
                Mod_Verteidigung += 2
                Mod_Punkte += 2
                SDS[Karte] -= 1
        #Lebensräume
        LRs = get_Text("LRs:", 30)
        Surf.blit(LRs, (5, 135))
        LR_Text = SMaxG(Mod_Lebensraum, 140 - LRs.get_width(), LRs.get_height())
        Surf.blit(LR_Text, (LRs.get_width() + ((150 - LRs.get_width()) / 2 - LR_Text.get_width() / 2), 135))
        #Punkte
        if Modus == "Punkte":
            P_Text = get_Text("Punkte:", 30)
            Surf.blit(P_Text, (5, 175))
            P_Num = get_Text(str(Mod_Punkte), 30)
            Surf.blit(P_Num, (P_Text.get_width() + (250 / 2 - P_Text.get_width() - P_Num.get_width() / 2), 175))
        #Angriff und Verteidungung
        elif Modus == "Kampf":
            A_Text = get_Text("Angriff:", 30)
            Surf.blit(A_Text, (5, 175))
            A_Num = get_Text(str(Mod_Angriff), 30)
            Surf.blit(A_Num, (A_Text.get_width() + (250 / 2 - A_Text.get_width() - A_Num.get_width() / 2), 175))
            V_Text = get_Text("Vtdg:", 30)
            Surf.blit(V_Text, (5, 215))
            V_Num = get_Text(str(Mod_Verteidigung), 30)
            Surf.blit(V_Num, (V_Text.get_width() + (250 / 2 - V_Text.get_width() - V_Num.get_width() / 2), 215))
    elif Karte in Karten.Alle_Lebensraum:
        #altes repr, dont touch
        Mod_Größe = Karte.Größe
        if Karte in CDS:
            if CDS[Karte] == True:
                Verbesserung_Spieler = Verbesserung[Spieler]
                Verbesserung_Karte = Verbesserung_Spieler[Karte]
                Add_Größe = Verbesserung_Karte
                Mod_Größe = Karte.Größe + Add_Größe
                CDS[Karte] = False
        #Größe
        G_Text = get_Text("Größe:", 30)
        Surf.blit(G_Text, (5, 135))
        G_Num = get_Text(str(Mod_Größe), 30)
        Surf.blit(G_Num, (G_Text.get_width() + (250 / 2 - G_Text.get_width() - G_Num.get_width() / 2), 135))
        #Punkte
        if Modus == "Punkte":
            P_Text = get_Text("Punkte:", 30)
            Surf.blit(P_Text, (5, 175))
            P_Num = get_Text(str(Karte.Punkte), 30)
            Surf.blit(P_Num, (P_Text.get_width() + (250 / 2 - P_Text.get_width() - P_Num.get_width() / 2), 175))
    return Surf

#Text auf Infosurf ausgeben
def Info_Text(Text_Raw):
    Info_Surf.fill((255, 255, 255))
    y = 10
    if "\n" in Text_Raw:
        Text = Text_Raw.split("\n")
    else:
        Text = [Text_Raw]
    for Schriftteil in Text:
        Test = False
        for Karte in Karten.Alle_Karten:
            if Schriftteil == Karte.Name:
                Test = True
        if Test == True:
            Dings = SMaxG("Karte: " + Schriftteil, 400, 45)
            Info_Surf.blit(Dings, (450 / 2 - Dings.get_width() / 2, 20))
        else:
            Textline = Schriftteil.split(" ")
            Größe = 35
            Lines = []
            Line = ""
            for Wort in Textline:
                Line = Line + Wort + " "
                Realtext = get_Text(Line, Größe)
                if Realtext.get_width() >= 440:
                    Line = Line[:-(len(Wort) + 1)]
                    Lines.append(Line)
                    Line = Wort + " "
            if not Line in Lines:
                Lines.append(Line)
            y = 80
            for Line in Lines:
                Teil = get_Text(Line, Größe)
                Info_Surf.blit(Teil, (450 / 2 - Teil.get_width() / 2, y))
                y += 40
    screen.blit(Info_Surf, (0, 0))

##Spielkern##
#Spielmodus Screen
Züge_String = None
Runden_String = None
def Spiel_Screen():
    global Spieler
    global Züge_String
    global Runden_String
    global Züge
    global Runden
    screen.fill((255, 255, 255))
    #Buttons
    global Buttons
    Buttons = []
    Ablage_Runter_Button.create_button()
    Ablage_Hoch_Button.create_button()
    Feld_Übersicht_Links_Button.create_button()
    Feld_Übersicht_Rechts_Button.create_button()
    Feld_Runter_Button.create_button()
    Feld_Hoch_Button.create_button()
    Regel_Spiel_Button.create_button()
    Nächster_Button.create_button()
    Ablage_Button_0.create_button()
    Ablage_Button_1.create_button()
    Ablage_Button_2.create_button()
    Ablage_Button_3.create_button()
    Ablage_Button_4.create_button()
    Ablage_Button_5.create_button()
    Feld_Button_0.create_button()
    Feld_Button_1.create_button()
    Feld_Button_2.create_button()
    Feld_Button_3.create_button()
    Feld_Button_4.create_button()
    Feld_Button_5.create_button()
    Feld_Übersicht_Button_0.create_button()
    Feld_Übersicht_Button_1.create_button()
    Feld_Übersicht_Button_2.create_button()
    Feld_Übersicht_Button_3.create_button()
    Feld_Übersicht_Button_4.create_button()
    Feld_Übersicht_Button_5.create_button()
    #Linien
    Start_Ende = [[(450, 0), (450, 900)], [(450, 100), (1600, 100)], [(450, 450), (1600, 450)], [(450, 750), (1600, 750)]]
    for Linie in Start_Ende:
        pg.draw.line(screen, (0, 0, 0), Linie[0], Linie[1], 1)
    #Überschrift
    if Runden_String == None:
        if str(Runden) == "1":
            Runden_String = "letzte Runde"
        else:
            Runden_String = "noch " + str(Runden) + " Runden"
    if Züge_String == None:
        if str(Züge) == "1":
            Züge_String = "letzter Zug"
        else:
            Züge_String = "noch " + str(Züge) + " Züge"
    Text = SMaxG(Runden_String, None, 30)
    screen.blit(Text, (610 + (415 / 2 - Text.get_width() / 2), 10))
    Text = SMaxG(Züge_String, None, 30)
    screen.blit(Text, (610 + (415 / 2 - Text.get_width() / 2), 60))
    if Spieler[-1] == "s" or Spieler[-1] == "S" or Spieler[-1] == "X" or Spieler[-1] == "x":
        Text = SMaxG(Spieler + "\' Zug", 350, 50)
    else:
        Text = SMaxG(Spieler + "s Zug", 350, 50)
    screen.blit(Text, (1025 + (415 / 2 - Text.get_width() / 2), 50 - Text.get_height() / 2))

#Anfang vom Spiel
Start = False
def Spiel():
    global Spieler
    for Spieler in Alle_Spieler:
        #1. Ausgabe
        Ablage.update({Spieler:[]})
        Ablage[Spieler].append(random.choice(Karten.Start_Lebewesen))
        Ablage[Spieler].append(random.choice(Karten.Start_Lebensraum))
        Ablage[Spieler].append(random.choice(Karten.Start_Elemente))
        Ablage[Spieler].append(random.choice(random.choice(Karten.Nur)))
        Ablage[Spieler].append(random.choice(random.choice(Karten.Alle_Start_Karten)))
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
        Werteverbesserung_Anzahl.update({Spieler:{Karten.Parasit:[0, 0],
                                                  Karten.Friedensengel:[0, 0],
                                                  Karten.Diebische_Elster:[0, 0],
                                                  Karten.Furchtdrache:[0, 0],
                                                  Karten.Starker_Furchtdrache:[0, 0],
                                                  Karten.Joker:[0, 0],
                                                  Karten.Urwolf:[0, 0]}})
        for Karte in Karten.Werteverbesserung_Übersicht:
            Werteverbesserung_Anzahl[Spieler].update({Karte:[0, 0]})
    Spieler = Alle_Spieler[0]
    Spiel_Screen()
    Ausgabe(Spieler, Ablage_Surf)
    Ausgabe(Spieler, Feld_Übersicht_Surf)

#Kombi
#def Add(Karten_Liste, Extra = False):
    #Überprüfung und Zuweisung von Variablen
    #if beide Listenelemente Karten:
        #if Ort nicht definiert:
            #Meldung
            #break
        #elif Extra == True:
            #Extrafunktionen
        #elif Lw und LR:
            #LW bewegen
        #elif Trank in Name:
            #Tränke
        #else:
            #for Karte in Alle_Karten:
                #if Gesuchte_Kombi in Karte.Kombi:
                    #if eine Karte == LR:
                        #LR + LR
                        #LR + E
                    #elif eine Karte == LW:
                        #LW + LW
                        #LW + E
                    #else:
                        #E + E
                #elif Counter == len:
                    #Keine Kombi möglich
            #if Spieler_Zug == True: (erfolgreicher Zug)
                #übertragene Verbesserungen
    #elif ein Listenelement Karte: ###ab hier überarbeiten###
        #if Gegener == None:
            #Extraaktion ohne Gegner mit anderer Extrainfo
        #else:
            #Extraaktion mit Gegner
    #else:
        #Eine oder beide Karten existieren nicht
def Add(Karten_Liste, Extra = False):
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
    #Karten und Namen
    Name_Karte_1 = Karten_Liste[0]
    Name_Karte_2 = Karten_Liste[1]
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
        if Ort_1 == False or Ort_2 == False:
            print("Fehler Add(); Ort_1 oder Ort_2 nicht definiert")
        #Extrafunktionen
        elif Extra == True:
            E_Karte = Karte_1
            Andere_Karte = Karte_2
            Ort = Ort_1
            Anderer_Ort = Ort_2
            Anderer_LR = LR_2
            if E_Karte in WAS:
                WASK = WAS[E_Karte]
            #Parasit
            if E_Karte == Karten.Parasit:
                if Andere_Karte in Karten.Alle_Lebewesen:
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
                        Info_Text("Fähigkeit kann nur einmal angewandt werden, Parasit muss auf dem Feld platziert sein.")
                else:
                    Info_Text("Kann nur die Werte von Lebewesen aufnehmen.")
            #Werteverbesserungskarte
            elif E_Karte in Karten.Werteverbesserung_Übersicht:
                if Andere_Karte in Karten.Alle_Lebewesen:
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
                            Info_Text("Fähigkeit kann nur einmal angewandt werden, Karte muss auf dem Feld platziert sein.")
                    else:
                        Info_Text("Kann nur die Werte von Lebewesen verbessern.")
            #Mehr Lebensräume
            elif E_Karte in Karten.ExtraLRs:
                if Andere_Karte in Karten.Alle_Lebewesen:
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
                            Info_Text("Dieses Lebewesen kann bereits in allen Lebensräumen leben.")
                        else:
                            #Zufall
                            Spieler_Zug = True
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
                        Info_Text("Platziere Lebewesen auf dem Feld, um ihre Extrafunktion zu nutzen.")
                else:
                    Info_Text("Kann nur auf Lebewesen angewandt werden.")
            #Friedensengel
            elif E_Karte == Karten.Friedensengel:
                if Andere_Karte in Karten.Alle_Lebensraum:
                    if WASK[0] > 0:
                        if "Klein" in Andere_Karte.Name:
                            if "Magisch" in Andere_Karte.Name:
                                Neue_Karte = Karten.Magisches_Kleines_Wonderland
                            else:
                                Neue_Karte = Karten.Kleines_Wonderland
                        elif "Groß" in Andere_Karte.Name:
                            if "Magisch" in Andere_Karte.Name:
                                Neue_Karte = Karten.Magisches_Großes_Wonderland
                            else:
                                Neue_Karte = Karten.Großes_Wonderland
                        else:
                            if "Magisch" in Andere_Karte.Name:
                                Neue_Karte = Karten.Magisches_Wonderland
                            else:
                                Neue_Karte = Karten.Wonderland
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
                        Info_Text("Muss auf dem Feld platziert sein und kann nur 3 Mal angewandt werden.")
                else:
                    Info_Text("Extrafunktion kann nur auf Lebensräume angewandt werden.")
            #Zauberer
            elif E_Karte == Karten.Zauberer:
                if Andere_Karte in Karten.Alle_Elemente:
                    if not Ort == Ablage[Spieler]:
                        for Trank in Karten.Tränke_Kombi:
                            if Andere_Karte in Karten.Tränke_Kombi[Trank]:
                                Neue_Karte = Trank
                                break
                        Ablage_Spieler.append(Neue_Karte)
                        Ablage_Spieler.remove(Andere_Karte)
                        Spieler_Zug = True
                    else:
                        Info_Text("Platziere den Zauberer im Feld um seine Funktion zu nutzen.")
                else:
                    Info_Text("Zauberer kann nur Elemente in Tränke verwandeln.")
            #Dunkler Magier
            elif E_Karte == Karten.Dunkler_Magier:
                if Andere_Karte in Karten.Alle_Elemente:
                    if not Ort == Ablage[Spieler]:
                        for Gift in Karten.Gifte_Kombi:
                            if Andere_Karte in Karten.Gifte_Kombi[Gift]:
                                Neue_Karte = Gift
                                break
                        Ablage_Spieler.append(Neue_Karte)
                        Ablage_Spieler.remove(Andere_Karte)
                        Spieler_Zug = True
                    else:
                        Info_Text("Platziere den Dunklen Magier im Feld um seine Funktion zu nutzen.")
                else:
                    Info_Text("Dunkler Magier kann nur Elemente in Gifte verwandeln.")
            #Urwolf
            elif E_Karte == Karten.Urwolf:
                if Andere_Karte in Karten.Alle_Lebewesen:
                    if WASK[0] > 0:
                        Weiter = True
                        if Andere_Karte.Punkte > Karten.Werwolf.Punkte:
                            Info_Text("Die Karte ist bereits besser als eine Werwolf-Karte.")
                            Weiter = False
                        if not Anderer_Ort == Ablage[Spieler]:
                            if not Anderer_LR.Art == "Wald":
                                Info_Text("Der Lebensraum ist für einen Werwolf nicht geeignet. Wähle ein Lebewesen in einem Wald oder in der Ablage.")
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
                        Info_Text("Kann nur einmal im Spiel angewandt werden, Karte muss auf dem Feld platziert sein.")
                else:
                    Info_Text("Kann nur auf Lebewesen angewandt werden.")
            else:
                Info_Text("Keine der Karten hat eine Extrafunktion.")
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
                Info_Text("Platziere den Lebensraum erst auf dem Feld.")
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
                    Info_Text("Dieser Lebensraum ist bereits voll.")
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
                    Info_Text("Dieser Lebensraum ist für das Lebewesen nicht geeignet.")
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
                if Andere_Karte in Karten.Alle_Lebensraum:
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
                                Neue_Karte = Karten.Magisches_Kleines_Wonderland
                            else:
                                Neue_Karte = Karten.Kleines_Wonderland
                        elif "Groß" in Andere_Karte.Name:
                            if "Magisch" in Andere_Karte.Name:
                                Neue_Karte = Karten.Magisches_Großes_Wonderland
                            else:
                                Neue_Karte = Karten.Großes_Wonderland
                        else:
                            if "Magisch" in Andere_Karte.Name:
                                Neue_Karte = Karten.Magisches_Wonderland
                            else:
                                Neue_Karte = Karten.Wonderland
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
                    Info_Text("Du kannst diesen Trank nur auf Lebensräume anwenden.")
            #Lebewesen-Tränke     
            elif "Lebewesen" in Trank_Karte.Beschreibung:
                if Andere_Karte in Karten.Alle_Lebewesen:
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
                    Info_Text("Du kannst diesen Trank nur auf Lebenwesen anwenden.")
        #Schleifen-Start/Kombi oder nicht        
        else:
            Counter_Add = 0
            for Karte in Alle_Karten:
                Counter_Add += 1
                #Kombi
                if Gesuchte_Kombi_1 in Karte.Kombi or Gesuchte_Kombi_2 in Karte.Kombi:
                    Neue_Karte = Karte
                    #LR
                    if Karte_1 in Karten.Alle_Lebensraum or Karte_2 in Karten.Alle_Lebensraum:
                        if Karte_1 in Karten.Alle_Lebensraum:
                            LR_Karte = Karte_1
                            Andere_Karte = Karte_2
                        else:
                            LR_Karte = Karte_2
                            Andere_Karte = Karte_1
                        #LR + LR
                        if Andere_Karte in Karten.Alle_Lebensraum:
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
                        elif Andere_Karte in Karten.Alle_Elemente:
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
                    elif Karte_1 in Karten.Alle_Lebewesen or Karte_2 in Karten.Alle_Lebewesen:
                        if Karte_1 in Karten.Alle_Lebewesen:
                            LW_Karte = Karte_1
                            Andere_Karte = Karte_2
                        else:
                            LW_Karte = Karte_2
                            Andere_Karte = Karte_1
                        #LW + LW
                        if Andere_Karte in Karten.Alle_Lebewesen:
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
                                    Info_Text("Du kannst nur innerhalb des Feldes oder der Ablage kombinieren.")
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
                                    Info_Text("Keiner der beiden Lebensräume ist geeignet für das neue Lebewesen.")
                                    break
                        #LW + E
                        elif Andere_Karte in Karten.Alle_Elemente:
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
                                        Info_Text("Der Lebensraum ist nicht geeignet für das neue Lebewesen.")
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
                                        Info_Text("Der Lebensraum ist nicht geeignet für das neue Lebewesen.")
                                        break
                                    break
                    #E + E
                    elif Karte_1 in Karten.Alle_Elemente and Karte_2 in Karten.Alle_Elemente:
                        Ablage[Spieler].append(Neue_Karte)
                        Ablage[Spieler].remove(Karte_1)
                        Ablage[Spieler].remove(Karte_2)
                        Spieler_Zug = True
                        break
                #Keine Kombi möglich
                elif Counter_Add == len(Alle_Karten):
                    Info_Text("Diese Karten lassen sich nicht kombinieren.")
            #Verbesserungen
            if Spieler_Zug == True:
                #Weitergabe Verbesserungen
                if Neue_Karte in Karten.Alle_Lebensraum:
                    Counter = 0
                    if Karte_1 in Karten.Alle_Lebensraum and Karte_1 in Verbesserung_Spieler:
                        Counter += Verbesserung_Spieler[Karte_1]
                        del Verbesserung_Spieler[Karte_1]
                    if Karte_2 in Karten.Alle_Lebensraum and Karte_2 in Verbesserung_Spieler:
                        Counter += Verbesserung_Spieler[Karte_2]
                        del Verbesserung_Spieler[Karte_1]
                    if not Counter == 0:
                        if not Neue_Karte in Verbesserung_Spieler:
                            Counter_Dict[Spieler].update({Neue_Karte:False})
                            Einmal_Dict[Spieler].update({Neue_Karte:False})
                            Verbesserung_Spieler.update({Neue_Karte:0})
                        Verbesserung_Spieler[Neue_Karte] += Counter
                elif Neue_Karte in Karten.Alle_Lebewesen:
                    Counter_P = 0
                    Counter_A = 0
                    Counter_V = 0
                    if Karte_1 in Karten.Alle_Lebewesen and Karte_1 in Verbesserung_Spieler:
                        VSK = Verbesserung_Spieler[Karte_1]
                        Counter_P += VSK["Punkte"]
                        Counter_A += VSK["Angriff"]
                        Counter_V += VSK["Verteidigung"]
                        del Verbesserung_Spieler[Karte_1]
                    if Karte_2 in Karten.Alle_Lebewesen and Karte_2 in Verbesserung_Spieler:
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
            #############Joker######################
            if E_Karte == Karten.Joker:
                WASK = WAS[Joker]
                if WASK[0] > 0:
                    Neue_Karte = None
                    #######Auswahl als Buttons
                    if Andere_Name == "Lebewesen" or Andere_Name == "lebewesen":
                        Neue_Karte = random.choice(Start_Lebewesen)
                    elif Andere_Name == "Lebensraum" or Andere_Name == "lebensraum":
                        Neue_Karte = random.choice(Start_Lebensraum)
                    elif Andere_Name == "Element" or Andere_Name == "element":
                        Neue_Karte = random.choice(Start_Elemente)
                    if Neue_Karte == None:
                        Info_Text("Wähle zwischen Element, Lebewesen und Lebensraum.")
                    else:
                        Ablage[Spieler].append(Neue_Karte)
                        Info_Text("Neue Karte:")
                        #####################
                        if not Neue_Karte in Karten.Start_Elemente:
                            if Modus == "1":
                                print(repr(Neue_Karte))
                            elif Modus == "2":
                                print(str(Neue_Karte))
                        else:
                            print(Neue_Karte)
                        Spieler_Zug = True
                        WASK[0] -= 1
                else:
                    Info_Text("Kann nur einmal pro Runde angewandt werden, Karte muss auf dem Feld platziert sein.")
            else:
                Info_Text("Eine oder beide Karten existieren nicht.")
        else:
            ########################Aktion mit anderem Spieler##############################
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
        Info_Text("Eine oder beide Karten existieren nicht.")

#Events
Spieler_Zug = False #Zug Ende
Aus = True #Ausgabe nach Zugende ja oder nein
Input = False #Input Box Einstellungen
done = False
while done == False:
    for event in pg.event.get():
        if event.type == pg.QUIT:
                done = True
                break
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                done = True
                break
        elif event.type == pg.MOUSEMOTION:
            for Button in Buttons:
                if Button.Rect.collidepoint(pg.mouse.get_pos()):
                    Button.Maus_Pos = True
                else:
                    Button.Maus_Pos = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            for Button in Buttons:
                if Button.Maus_Pos == True:
                    Button.Funktion()
        #Einstellungen Anfang
        if Input == True:
            #Inputboxen
            for Box in Boxen:
                Box.get_event(event)
                Box.update()
                Box.draw(screen)
            #Spieler
            if (not Input_Box.final == "") and (len(Einstellungen[1]) < 5):
                if Spieler_Hinzu_Button.Switch == False:
                    Spieler_Hinzu_Button.Change()
            else:
                if Spieler_Hinzu_Button.Switch == True:
                    Spieler_Hinzu_Button.Change()
            #Runden und Züge
            if (not Runden_Box.final == ""):
                Einstellungen[2] = int(Runden_Box.final)
            else:
                Einstellungen[2] = 0
            if (not Züge_Box.final == ""):
                Einstellungen[3] = int(Züge_Box.final)
            else:
                Einstellungen[3] = 0
            #Fertig Button
            if None in Einstellungen or [] in Einstellungen or 0 in Einstellungen:
                if Fertig_Button.Switch == True:
                    Fertig_Button.Change()
            else:
                if Fertig_Button.Switch == False:
                    Fertig_Button.Change()
        
    pg.display.flip()