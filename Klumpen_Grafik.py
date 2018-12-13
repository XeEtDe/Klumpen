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

#Buttons (self, Rect, Funktion, Bild = None, Text = None, Bild_2 = None, Füllung = None)
#Ablage schieben
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
def Feld_Hoch():
    pass
F_Hoch_Rect = pg.Rect(1590 - Pfeil_Hoch.get_width(), 180, Pfeil_Hoch.get_width(), Pfeil_Hoch.get_height())
Feld_Hoch_Button = Button(F_Hoch_Rect, Feld_Hoch, Pfeil_Hoch_Blass, None, Pfeil_Hoch)
def Feld_Hoch():
    global Feld_Alt_Range
    if Feld_Hoch_Button.Switch == True:
        Ausgabe(Spieler, Feld_Surf, range(Feld_Alt_Range - 6, Feld_Alt_Range - 1), Alt_LR_Pos)

def Feld_Runter():
    pass
F_Runter_Rect = pg.Rect(1590 - Pfeil_Runter.get_width(), 450 - Pfeil_Runter.get_height(), Pfeil_Runter.get_width(), Pfeil_Runter.get_height())
Feld_Runter_Button = Button(F_Runter_Rect, Feld_Runter, Pfeil_Runter_Blass, None, Pfeil_Runter)
def Feld_Runter():
    global Feld_Alt_Range
    if Feld_Runter_Button.Switch == True:
        Ausgabe(Spieler, Feld_Surf, range(Feld_Alt_Range + 6, Feld_Alt_Range + 12), Alt_LR_Pos)

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

#Karten Buttons
def Karten_Func(Kategorie, Button_Num):
    global Spieler
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
    Karte = List[Num]
    #Funktionen, Kombi, etc
    if False:
        pass
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

#Ausgabe
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
            V_Text = get_Text("Verteidungung:", 30)
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
                Test = "Name"
            elif Schriftteil == Karte.Beschreibung:
                Test = "Beschreibung"
        if Test == "Name":
            Dings = SMaxG("Karte: " + Schriftteil, 400, 45)
            Info_Surf.blit(Dings, (450 / 2 - Dings.get_width() / 2, 20))
        elif Test == "Beschreibung":
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
        else:
            Teil = get_Text(Teil, 35)
            Info_Surf.blit(Teil, (450 / 2 - Teil.get_width() / 2, y + 5))
    screen.blit(Info_Surf, (0, 0))

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