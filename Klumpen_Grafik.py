import random
import pygame as pg
pg.init()
import Karten
import string
import textbox
import SchriftMaxgröße as SMaxG

#Startbildschirm
screen = pg.display.set_mode((1600, 900), pg.FULLSCREEN)
pg.display.set_caption("Klumpen")
Info_Surf = pg.Surface((450, 900))
Feld_Surf = pg.Surface((1150, 350))
Ablage_Surf = pg.Surface((1150, 300))

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
Hoch_Rect = pg.Rect(1560 - Pfeil_Hoch.get_width(), 600, Pfeil_Hoch.get_width(), Pfeil_Hoch.get_height())
Ablage_Hoch_Button = Button(Hoch_Rect, Ablage_Hoch, Pfeil_Hoch_Blass, None, Pfeil_Hoch)
def Ablage_Hoch():
    global Ablage_Alt_Range
    if Ablage_Hoch_Button.Switch == True:
        Print_Ablage(Spieler, range(Ablage_Alt_Range - 6, Ablage_Alt_Range - 1))

Pfeil_Runter_Blass = get_image("pfeilrunterblass.png")
Pfeil_Runter = get_image("pfeilrunter.png")
def Ablage_Runter():
    pass
Runter_Rect = pg.Rect(1560 - Pfeil_Runter.get_width(), 850 - Pfeil_Runter.get_height(), Pfeil_Runter.get_width(), Pfeil_Runter.get_height())
Ablage_Runter_Button = Button(Runter_Rect, Ablage_Runter, Pfeil_Runter_Blass, None, Pfeil_Runter)
def Ablage_Runter():
    global Ablage_Alt_Range
    if Ablage_Runter_Button.Switch == True:
        Print_Ablage(Spieler, range(Ablage_Alt_Range + 6, Ablage_Alt_Range + 12))

#Feld Übersicht schieben
Pfeil_Links_Blass = get_image("pfeillinksblass.png")
Pfeil_Links = get_image("pfeillinks.png")
def Feld_Übersicht_Links():
    pass
Links_Rect = pg.Rect(510, 135, Pfeil_Links.get_width(), Pfeil_Links.get_height())
Feld_Übersicht_Links_Button = Button(Links_Rect, Feld_Übersicht_Links, Pfeil_Links_Blass, None, Pfeil_Links)
def Feld_Übersicht_Links():
    global Feld_Übersicht_Alt_Range
    if Feld_Übersicht_Links_Button.Switch == True:
        Print_Feld_Übersicht(Spieler, range(Feld_Übersicht_Alt_Range - 6, Feld_Übersicht_Alt_Range - 1))

Pfeil_Rechts_Blass = get_image("pfeilrechtsblass.png")
Pfeil_Rechts = get_image("pfeilrechts.png")
def Feld_Übersicht_Rechts():
    pass
Rechts_Rect = pg.Rect(1590 - Pfeil_Rechts.get_width(), 135, Pfeil_Rechts.get_width(), Pfeil_Rechts.get_height())
Feld_Übersicht_Rechts_Button = Button(Rechts_Rect, Feld_Übersicht_Rechts, Pfeil_Rechts_Blass, None, Pfeil_Rechts)
def Feld_Übersicht_Rechts():
    global Feld_Übersicht_Alt_Range
    if Feld_Übersicht_Rechts_Button.Switch == True:
        Print_Feld_Übersicht(Spieler, range(Feld_Übersicht_Alt_Range + 6, Feld_Übersicht_Alt_Range + 12))

#Regeln
R_Rect = pg.Rect(510, 10, 270, 50)
Regel_Spiel_Button = Button(R_Rect, Regeln, None, get_Text("Regeln", 40))

#Weiter
def Nächster():
    pass
Nächster_Image = get_image("fertig.png")
Nächster_Rect = pg.Rect(1170, 5, 150, 90)
Nächster_Button = Button(Nächster_Rect, Nächster)

#Anfang vom Spiel
Start = False
def Spiel():
    global Start
    screen.fill((255, 255, 255))
    global Buttons
    Buttons = []
    Ablage_Runter_Button.create_button()
    Ablage_Hoch_Button.create_button()
    Feld_Übersicht_Links_Button.create_button()
    Feld_Übersicht_Rechts_Button.create_button()
    pg.draw.rect(screen, (0, 0, 0), pg.Rect(510, 10, 270, 50), 3)
    Regel_Spiel_Button.create_button()
    Nächster_Button.create_button()
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
    Start = True

#Ablage Ausgeben
def Print_Ablage(Spieler, Range = range(0, 6)):
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
    #für Buttons
    global Ablage_Alt_Range
    Ablage_Alt_Range = Range
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
    #Teile drucken
    Height = 35
    Width = 25
    for Num in Range:
        if len(Ablage[Spieler]) >= (Num + 1):
            Width += 170
            Ablage_Surf.blit(Druck(Ablage[Spieler][Num], Spieler), (Width, Height))
    #Buttons wenn Ablage oben oder unten mehr Karten
    if Range[0] > 0 and Ablage_Hoch_Button.Switch == False:
        Ablage_Hoch_Button.Change()
    else:
        if Ablage_Hoch_Button.Switch == True:
            Ablage_Hoch_Button.Change()
    if (len(Ablage[Spieler]) > (Range[-1] + 1)) and Ablage_Runter_Button.Switch == False:
        Ablage_Runter_Button.Change()
    else:
        if Ablage_Runter_Button.Switch == True:
            Ablage_Runter_Button.Change()

#Feld ausgeben
def Print_Feld_Übersicht(Spieler, Range = range(0, 6)):
    global Feld_Übersicht_Alt_Range
    Feld_Übersicht_Alt_Range = Range
    Surf = pg.Surface(50, 40)
    y = 35
    x = 70
    for Num in Range:
        LR = Feld_Spieler[Num]
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
        Surf.fill(Hintergrund)
        Cap = SMaxG(LR.Name, 50, 18)
        Inside = SMaxG(str(len(Feld[Spieler][LR])) + " / " + str(LR.Mod_Größe), 50, 18)
        Surf.blit(Cap, (25 - Cap.get_width() / 2, 5))
        Surf.blit(Inside, (25 - Inside.get_width() / 2, 22))
        Feld_Surf.blit(Surf, (x, y))
        x += 60
    #Buttons wenn Übersicht links oder rechts
    if Range[0] > 0 and Feld_Übersicht_Links_Button.Switch == False:
        Feld_Übersicht_Links_Button.Change()
    else:
        if Feld_Übersicht_Links_Button.Switch == True:
            Feld_Übersicht_Links_Button.Change()
    if (len(Feld[Spieler]) > (Range[-1] + 1)) and Feld_Übersicht_Rechts_Button.Switch == False:
        Feld_Übersicht_Rechts_Button.Change()
    else:
        if Feld_Übersicht_Rechts_Button.Switch == True:
            Feld_Übersicht_Rechts_Button.Change()

def Print_Feld(Spieler, LR_Pos, Range = range(0, 6)):
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
    #Ausgabe
    global Feld_Übersicht_Alt_Range
    Num = Feld_Übersicht_Alt_Range[LR_Pos + 1]
    LR = Feld_Spieler[Num]
    global Alt_Pos
    Alt_Pos = LR_Pos
    global Feld_Alt_Range
    Feld_Alt_Range = Range




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
        Name_1 = SMaxG(Namen_Liste[0], 150, 40)
        Name_2 = SMaxG(Namen_Liste[1], 150, 40)
        Surf.blit(Name_1, (150 / 2 - Name_1.get_width() / 2, 35))
        Surf.blit(Name_2, (150 / 2 - Name_2.get_width() / 2, 80))
    else:
        Name = SMaxG(Karte.Name, 150, 90)
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
        LRs = get_Text("Lebensräume:", 10)
        Surf.blit(LRs, (5, 135))
        LR_Text = get_Text(Mod_Lebensraum, 10)
        Surf.blit(LR_Text, (50 + (50 - LR_Text.get_width() / 2), 135))
        #Punkte
        if Modus == "Punkte":
            P_Text = get_Text("Punkte:", 10)
            Surf.blit(P_Text, (5, 175))
            P_Num = get_Text(str(Mod_Punkte), 10)
            Surf.blit(P_Num, (50 + (50 - P_Num.get_width() / 2), 175))
        #Angriff und Verteidungung
        elif Modus == "Kampf":
            A_Text = get_Text("Angriff:", 10)
            Surf.blit(A_Text, (5, 175))
            A_Num = get_Text(str(Mod_Angriff), 10)
            Surf.blit(A_Num, (50 + (50 - A_Num.get_width() / 2), 175))
            V_Text = get_Text("Verteidungung:", 10)
            Surf.blit(V_Text, (5, 215))
            V_Num = get_Text(str(Mod_Verteidigung), 10)
            Surf.blit(V_Num, (50 + (50 - V_Num.get_width() / 2), 215))
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
        G_Text = get_Text("Größe:", 10)
        Surf.blit(G_Text, (5, 135))
        G_Num = get_Text(str(Mod_Größe), 10)
        Surf.blit(G_Num, (50 + (50 - G_Num.get_width() / 2), 135))
        #Punkte
        if Modus == "Punkte":
            P_Text = get_Text("Punkte:", 10)
            Surf.blit(P_Text, (5, 175))
            P_Num = get_Text(str(Karte.Punkte), 10)
            Surf.blit(P_Num, (50 + (50 - P_Num.get_width() / 2), 175))
    return Surf

def Split_Beschreibung(Karte):
    Beschreibung = Karte.Beschreibung.split(" ")
    Lines = []
    Line = ""
    for Wort in Beschreibung:
        Line = Line + Wort
        Text = get_Text(Line, 40)
        if Text.get_width() >= 400:
            Line = Line[:-len(Wort)]
            Lines.append(Line)
            Line = Wort
    y = 100
    for Line in Lines:
        Text = get_Text(Line, 40)
        Info_Surf.blit(Text, (250 - Text.get_width() / 2, y))
        y += 15

#Bildschirm ausgeben/wechseln
def Render_Bildschirm(Spieler):
    Print_Ablage(Spieler)

#Zug pro Spieler
def Zug(Spieler):
    #Zeug
    global Aus
    global Spieler_Zug
    Aus = True
    Spieler_Zug = False
    Ablage_Spieler = Ablage[Spieler]
    Feld_Spieler = Feld[Spieler]
    Ablage_Spieler = Ablage[Spieler]
    WAS = Werteverbesserung_Anzahl[Spieler]
    #Bildschirmausgabe
    Render_Bildschirm(Spieler)



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
Spieler_Zug = False
Input = False
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
    #Spielkern
    if Start == True:
        pass

    pg.display.flip()