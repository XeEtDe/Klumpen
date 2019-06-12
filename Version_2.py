import random
import pygame as pg
pg.init()
import Karten
import string
import textbox
from SchriftMaxgröße import SchriftFunc as SMaxG
from operator import itemgetter

#Startbildschirm
screen = pg.display.set_mode((1600, 900), pg.FULLSCREEN)
pg.display.set_caption("Klumpen")
Info_Surf = pg.Surface((450, 900))
Feld_Übersicht_Surf = pg.Surface((950, 49))
Feld_Surf = pg.Surface((1050, 268))
Ablage_Surf = pg.Surface((1050, 268))

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
        else:
            self.Switch = None

    def create_button(self):
        if not self in Buttons:
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

    def delete_button(self):
        if self in Buttons:
            self.Maus_Pos = False
            if not self.Bild_2 == None:
                self.Switch = False
            Buttons.remove(self)

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
        pg.draw.rect(screen, (255, 255, 255), self.Rect)
        screen.blit(Oberfläche, (self.Rect[0], self.Rect[1]))

# #Buttons und Funktionen
# Einstellungen = [None, [], 0, 0] #[Modus, Spieler, Runden, Züge]
# #Modus
# Kreis_Bild = get_image("kreisbild.png")
# Kreis_Bild_2 = get_image("kreisbild2.png")
# def Punkte_Funk():
#     Einstellungen[0] = "Punkte"
#     if Punkte_Button.Switch == False:
#         Punkte_Button.Change()
#     if Kampf_Button.Switch == True:
#         Kampf_Button.Change()
# Punkte_Rect = pg.Rect(220, 100, Kreis_Bild.get_width(), Kreis_Bild.get_height())
# Punkte_Button = Button(Punkte_Rect, Punkte_Funk, Kreis_Bild, None, Kreis_Bild_2)
# def Kampf_Funk():
#     Einstellungen[0] = "Kampf"
#     if Kampf_Button.Switch == False:
#         Kampf_Button.Change()
#     if Punkte_Button.Switch == True:
#         Punkte_Button.Change()
# Kampf_Rect = pg.Rect(screen.get_width() / 2 + 150, 100, Kreis_Bild.get_width(), Kreis_Bild.get_height())
# Kampf_Button = Button(Kampf_Rect, Kampf_Funk, Kreis_Bild, None, Kreis_Bild_2)

# #Spieler
# Kleiner_Haken = get_image("hakenklein.png")
# Kleiner_Haken_Blass = get_image("hakenkleinblass.png")
# Kreuz = get_image("kreuz.png")
# Kreuz_Blass = get_image("kreuzblass.png")
# Input_Box = textbox.TextBox((900, 320, 420, 50))
# def Print_Spieler():
#     Spieler_Liste = Einstellungen[1]
#     Counter = len(Spieler_Liste)
#     Fertig = 0
#     while Fertig < 5:
#         Dings = Spieler_Hintergrund[Fertig+1]
#         Fläche = Dings[1]
#         pg.draw.rect(screen, (255, 255, 255), Fläche)
#         pg.draw.rect(screen, (0, 0, 0), Fläche, 1)
#         Weg_Button = Dings[0]
#         if Weg_Button.Switch == True:
#             Weg_Button.Change()
#         Fertig += 1
#     Fertig = 0
#     while Counter > 0:
#         Spieler_Name = Spieler_Liste[Fertig]
#         Text = get_Text(Spieler_Name, 50)
#         screen.blit(Text, (185, 305 + 20*(Fertig+1)+ 50*Fertig))
#         Dings = Spieler_Hintergrund[Fertig+1]
#         Weg_Button = Dings[0]
#         if Weg_Button.Switch == False:
#             Weg_Button.Change()
#         Counter -= 1
#         Fertig += 1
# def Spieler_Entf(Index):
#     Spieler_Liste = Einstellungen[1]
#     if (Index + 1) <= len(Spieler_Liste):
#         Spieler_Liste.remove(Spieler_Liste[Index])
#         Print_Spieler()
# Spieler_Hintergrund = {}
# Weg_Button_1 = Button(pg.Rect(620, 325, Kreuz.get_width(), Kreuz.get_height()), lambda: Spieler_Entf(0), Kreuz_Blass, None, Kreuz)
# Weg_Button_2 = Button(pg.Rect(620, 395, Kreuz.get_width(), Kreuz.get_height()), lambda: Spieler_Entf(1), Kreuz_Blass, None, Kreuz)
# Weg_Button_3 = Button(pg.Rect(620, 465, Kreuz.get_width(), Kreuz.get_height()), lambda: Spieler_Entf(2), Kreuz_Blass, None, Kreuz)
# Weg_Button_4 = Button(pg.Rect(620, 535, Kreuz.get_width(), Kreuz.get_height()), lambda: Spieler_Entf(3), Kreuz_Blass, None, Kreuz)
# Weg_Button_5 = Button(pg.Rect(620, 605, Kreuz.get_width(), Kreuz.get_height()), lambda: Spieler_Entf(4), Kreuz_Blass, None, Kreuz)
# Weg_Buttons = [Weg_Button_1, Weg_Button_2, Weg_Button_3, Weg_Button_4, Weg_Button_5]
# Counter = 1
# while Counter <= 5:
#     for Bttn in Weg_Buttons:
#         Spieler_Hintergrund.update({Counter:[Bttn]})
#         Counter += 1
# def Spieler_Hinzu(Name = None):
#     if Spieler_Hinzu_Button.Switch == True:
#         Input_Box.buffer = []
#         if Name == None:
#             Name = Input_Box.final
#         if Name in Einstellungen[1]:
#             Text = get_Text("Wähle unterschiedliche Spielernamen", 30, pg.Color("red"))
#             screen.blit(Text, (900 + (210 - Text.get_width() / 2), 420))
#         else:
#             Einstellungen[1].append(Name)
#             Print_Spieler()
# Spieler_Hinzu_Button = Button(pg.Rect(1350, 320, Kleiner_Haken.get_width(), Kleiner_Haken.get_height()), Spieler_Hinzu, Kleiner_Haken_Blass, None, Kleiner_Haken)

# #Runden und Züge
# Runden_Box = textbox.TextBox((290, 800, 200, 50))
# Züge_Box = textbox.TextBox((801.5, 800, 200, 50))
# Boxen = [Input_Box, Runden_Box, Züge_Box]
# #Fertig Button
# Großer_Haken = get_image("hakengroß.png")
# Großer_Haken_Blass = get_image("hakengroßblass.png")
# Einstellungen_Fertig = False
# def Fertig():
#     if Fertig_Button.Switch == True:
#         global Einstellungen_Fertig
#         Einstellungen_Fertig = True
#         global Modus
#         global Alle_Spieler
#         global Runden
#         global Züge
#         Modus = Einstellungen[0]
#         Alle_Spieler = Einstellungen[1]
#         Runden = Einstellungen[2]
#         Züge = Einstellungen[3]
#         global Input
#         Input = False
#         global Buttons
#         Buttons = []
#         Spiel()
# Fertig_Button = Button(pg.Rect(1250, 660, Großer_Haken.get_width(), Großer_Haken.get_height()), Fertig, Großer_Haken_Blass, None, Großer_Haken)

# #Regeln
# def Regeln():
#     pass
# Regeln_Bild = get_image("regeln.png")
# Text_R = get_Text("Regeln", 70)
# Regeln_Rect = pg.Rect(600 - Regeln_Bild.get_width(), 500, Regeln_Bild.get_width(), Regeln_Bild.get_height())
# Regeln_Button = Button(Regeln_Rect, Regeln, Regeln_Bild, Text_R)

#Start
# def Start():
#     global Buttons
#     Buttons = []
#     screen.blit(get_image("hintergrundblass.png"), (0, 0))
#     #Modus
#     Text = get_Text("Modus?", 50)
#     screen.blit(Text, (screen.get_width() / 2 - Text.get_width() / 2, 30))
#     PT2 = get_Text("- Sammele möglichst viele Punkte", 30)
#     PT3 = get_Text("   durch Kombination von Karten", 30)
#     screen.blit(PT2, (320, 150))
#     screen.blit(PT3, (320, 180))
#     PT1 = get_Text("Punkte", 45)
#     screen.blit(PT1, (320 + (PT2.get_width() / 2 - PT1.get_width() / 2), 100))
#     KT2 = get_Text("- Entwickele durch Kombination starke", 30)
#     KT3 = get_Text(" Lebewesen für die folgende Kampfphase", 30)
#     screen.blit(KT2, (screen.get_width() / 2 + 300, 150))
#     screen.blit(KT3, (screen.get_width() / 2 + 300, 180))
#     KT1 = get_Text("Kampf", 45)
#     screen.blit(KT1, ((screen.get_width() / 2 + 300) + (PT2.get_width() / 2 - PT1.get_width() / 2), 100))
#     Punkte_Button.create_button()
#     Kampf_Button.create_button()
#     #Spieler
#     Text = get_Text("Spieler?", 50)
#     screen.blit(Text, (screen.get_width() / 2 - Text.get_width() / 2, 240))
#     Text = get_Text("1 bis 5", 35)
#     screen.blit(Text, (screen.get_width() / 2 - Text.get_width() / 2, 280))
#     Text = get_Text("Spielernamen eingeben", 35)
#     screen.blit(Text, (900 + (210 - Text.get_width() / 2), 380))
#     Spieler_Hinzu_Button.create_button()
#     Input_Box.process_kwargs({"command":Spieler_Hinzu, "clear_on_enter":True})
#     Input_Box.update()
#     Input_Box.draw(screen)
#     for Num in Spieler_Hintergrund:
#         Dings = Spieler_Hintergrund[Num]
#         y = 300 + 20*Num + 50*(Num-1)
#         Fläche = pg.Rect(180, y, 420, 50)
#         pg.draw.rect(screen, (255, 255, 255), Fläche)
#         pg.draw.rect(screen, (0, 0, 0), Fläche, 1)
#         Dings[0].create_button()
#         Spieler_Hintergrund[Num].append(Fläche)
#     #Runden und Züge
#     Text_1 = get_Text("Runden?", 50)
#     screen.blit(Text_1, (180 + (210 - Text_1.get_width() / 2), 680))
#     Text = get_Text("- 5 bis 20 Runden empfohlen", 30)
#     screen.blit(Text, ((180 + (210 - Text_1.get_width() / 2)) - (Text.get_width() / 2 - Text_1.get_width() / 2), 730))
#     Text = get_Text("- pro Runde werden neue Karten ausgegeben", 30)
#     screen.blit(Text, ((180 + (210 - Text_1.get_width() / 2)) - (Text.get_width() / 2 - Text_1.get_width() / 2), 760))
#     Text_2 = get_Text("Züge?", 50)
#     screen.blit(Text_2, (850, 680))
#     Text = get_Text("- 3 bis 10 Züge empfohlen", 30)
#     screen.blit(Text, (850 - (Text.get_width() / 2 - Text_2.get_width() / 2), 730))
#     Text = get_Text("- Aktionen pro Spieler pro Runde", 30)
#     screen.blit(Text, (850 - (Text.get_width() / 2 - Text_2.get_width() / 2), 760))
#     Runden_Box.process_kwargs({"ACCEPTED":string.digits})
#     Runden_Box.update()
#     Runden_Box.draw(screen)
#     Züge_Box.process_kwargs({"ACCEPTED":string.digits})
#     Züge_Box.update()
#     Züge_Box.draw(screen)
#     global Input
#     Input = True
#     #Fertig Button
#     Fertig_Button.create_button()
# Start_Bild = get_image("start.png")
# Text_S = get_Text("Start", 70)
# Start_Rect = pg.Rect(1000, 500, Start_Bild.get_width(), Start_Bild.get_height())
# Start_Button = Button(Start_Rect, Start, Start_Bild, Text_S)

# #Startbildschirm
# screen.blit(get_image("hintergrundblass.png"), (0, 0))
# #Klumpen
# Klecks_Blau = get_image("klecks.png")
# screen.blit(Klecks_Blau, (screen.get_width() / 2 - Klecks_Blau.get_width() / 2, screen.get_height() / 2 - Klecks_Blau.get_height() / 2 - 200)) #mittig von Schrift
# Text_K = get_Text("Klumpen", 90, (255, 255, 255))
# screen.blit(Text_K, (screen.get_width() / 2 - Text_K.get_width() / 2, screen.get_height() / 2 - Text_K.get_height() / 2 - 200)) #mittig, etwas nach oben verschoben
# #Regeln
# Regeln_Button.create_button()
# #Start
# Start_Button.create_button()

#Löschen wenn fertig:
Einstellungen = ["Punkte", ["Spieler 1", "Spieler 2"], 3, 5]
Modus = Einstellungen[0]
Alle_Spieler = Einstellungen[1]
Züge = Einstellungen[2]
Runden = Einstellungen[3]
def Regeln():
    pass
Start_Bild = get_image("start.png")
Einstellungen_Fertig = True
Input = False
Buttons = []
##############################################################################################################################################################################
###############################################################################################################################################################################
#Spiel
Alle_Spieler = []
class Spieler_Klasse:
    def __init__(self, SP_Name):
        self.SP_Name = SP_Name
        self.Aussetzen = 0
        Alle_Spieler.append(self)

    #Listen sortieren: Lebewesen, Lebensraum, Element + gleiche nebeneinander
    def Sortieren():
        #Ablage
        #Sortieren
        Ablage = []
        for K_Liste in [Karten.Alle_Lebewesen, Karten.Alle_Lebensraum, Karten.Alle_Elemente]:
            S_Liste = []
            for Pos in self.__dict__:
                if "A" in Pos and self.__dict__[Pos] in K_Liste:
                    S_Liste.append(self.__dict__[Pos])
            S_Liste.sort(key = itemgetter[0].Name)
            Ablage.append(S_Liste)
        #neue Position
        Start = 0
        for Liste in Ablage:
            for Num, Karte in enumerate(Liste, Start):
                setattr(self, "A_" + str(Num), Karte)
            Start += len(Liste)
        #zu hohe löschen
        for Pos in self.__dict__:
            Num_ = int(Pos[2])
            if "A" in Pos and Num_ >= Start:
                delattr(self, Pos)
        #Feld
        


#Attr_Lw = [Karten.Karte, Punkte, Lebensraum, falls Drachenei: Counter/falls Extrafunktion: Counter]
#Attr_Lr = [Karten.Karte, Punkte, Größe]
#Attr_E = [Karten.Karte]

First = Spieler_Klasse(self, Alle_Spieler_[0])
if len(Alle_Spieler_) >= 2:
    Second = Spieler_Klasse(self, Alle_Spieler_[1])
    if len(Alle_Spieler_) >= 3:
        Third = Spieler_Klasse(self, Alle_Spieler_[2])
        if len(Alle_Spieler_) >= 4:
            Fourth = Spieler_Klasse(self, Alle_Spieler_[3])
            if len(Alle_Spieler_) == 5:
                Fifth = Spieler_Klasse(self, Alle_Spieler_[4])

#Wie oft kann Extrafunktion benutzt werden/Dauer brüten bei Drachenei
def Extra_Neue_Karte(Spieler, Pos):
    if getattr(Spieler, Pos)[0] in Karten.Extrafunktion_Anzahl:
        while len(getattr(Spieler, Pos)) >= 4:
            getattr(Spieler, Pos).pop()
        getattr(Spieler, Pos).append(Extrafunktion_Anzahl[getattr(Spieler, Pos)[0]])
    elif getattr(Spieler, Pos)[0] == Karten.Drachenei:
        while len(getattr(Spieler, Pos)) >= 4:
            getattr(Spieler, Pos).pop()
        getattr(Spieler, Pos).append(2)

###Buttons (self, Rect, Funktion, Bild = None, Text = None, Bild_2 = None, Füllung = None)###

##Schiebebuttons##
#Ablage schieben
#Hoch
Pfeil_Hoch_Blass = get_image("pfeilhochblass.png")
Pfeil_Hoch = get_image("pfeilhoch.png")
Hoch_Rect = pg.Rect(1590 - Pfeil_Hoch.get_width(), 490, Pfeil_Hoch.get_width(), Pfeil_Hoch.get_height())
Ablage_Hoch_Button = Button(Hoch_Rect, lambda: Ausgabe(Spieler, Ablage_Surf, range(Ablage_Alt_Range[0] - 6, Ablage_Alt_Range[0])), Pfeil_Hoch_Blass, None, Pfeil_Hoch)
#Runter
Pfeil_Runter_Blass = get_image("pfeilrunterblass.png")
Pfeil_Runter = get_image("pfeilrunter.png")
Runter_Rect = pg.Rect(1590 - Pfeil_Runter.get_width(), 740 - Pfeil_Runter.get_height(), Pfeil_Runter.get_width(), Pfeil_Runter.get_height())
Ablage_Runter_Button = Button(Runter_Rect, lambda: Ausgabe(Spieler, Ablage_Surf, range(Ablage_Alt_Range[0] + 6, Ablage_Alt_Range[0] + 12)), Pfeil_Runter_Blass, None, Pfeil_Runter)

#Feld Übersicht schieben
#Links
Pfeil_Links_Blass = get_image("pfeillinksblass.png")
Pfeil_Links = get_image("pfeillinks.png")
Links_Rect = pg.Rect(455, 131, Pfeil_Links.get_width(), Pfeil_Links.get_height())
Feld_Übersicht_Links_Button = Button(Links_Rect, lambda: Ausgabe(Spieler, Feld_Übersicht_Surf, range(Feld_Übersicht_Alt_Range[0] - 8, Feld_Übersicht_Alt_Range[0])), Pfeil_Links_Blass, None, Pfeil_Links)
#Rechts
Pfeil_Rechts_Blass = get_image("pfeilrechtsblass.png")
Pfeil_Rechts = get_image("pfeilrechts.png")
Rechts_Rect = pg.Rect(1580 - Pfeil_Rechts.get_width(), 131, Pfeil_Rechts.get_width(), Pfeil_Rechts.get_height())
Feld_Übersicht_Rechts_Button = Button(Rechts_Rect, lambda: Ausgabe(Spieler, Feld_Übersicht_Surf, range(Feld_Übersicht_Alt_Range[0] + 8, Feld_Übersicht_Alt_Range[0] + 16)), Pfeil_Rechts_Blass, None, Pfeil_Rechts)

#Feld schieben
#Hoch
F_Hoch_Rect = pg.Rect(1590 - Pfeil_Hoch.get_width(), 190, Pfeil_Hoch.get_width(), Pfeil_Hoch.get_height())
Feld_Hoch_Button = Button(F_Hoch_Rect, lambda: Ausgabe(Spieler, Feld_Surf, range(Feld_Alt_Range[0] - 6, Feld_Alt_Range[0]), Alt_LR_Pos), Pfeil_Hoch_Blass, None, Pfeil_Hoch)
#Runter
F_Runter_Rect = pg.Rect(1590 - Pfeil_Runter.get_width(), 440 - Pfeil_Runter.get_height(), Pfeil_Runter.get_width(), Pfeil_Runter.get_height())
Feld_Runter_Button = Button(F_Runter_Rect, lambda: Ausgabe(Spieler, Feld_Surf, range(Feld_Alt_Range[0] + 6, Feld_Alt_Range[0] + 12), Alt_LR_Pos), Pfeil_Runter_Blass, None, Pfeil_Runter)


##Regeln und Nächster##
#Regeln
R_Bild = get_image("regelnklein.png")
R_Text = get_Text("Regeln", 40)
R_Rect = pg.Rect(460, 10, R_Bild.get_width(), R_Bild.get_height())
Regel_Spiel_Button = Button(R_Rect, Regeln, R_Bild, R_Text)
#Weiter
Runden_Counter = 0
Züge_Counter = 0
Ex_Zü = False
def Nach_Zug(Spieler, Aussetzen = False):
    global Züge_Counter
    if Aussetzen == False:
        #Drachenei brüten
        #Werte minus 1 und Drachenei in Drachen nach einem Zug
        for Attr in Spieler.__dict__:
            if Karten.Drachenei == getattr(Spieler, Attr)[0]:
                getattr(Spieler, Attr)[-1] -= 1
                if getattr(Spieler, Attr)[-1] == 0:
                    getattr(Spieler, Attr) = [Karten.Drache, Karten.Drache.Punkte, Karten.Drache.Lebensraum]
        #Verbesserung nicht kleiner 0
        for Karte in Spieler.__dict__.values():
            if Karte[1] < 0:
                Karte[1] = 0
    #letzter Spieler -> ##Züge aufgebraucht -> Auswahl oder Ende## oder ##nächster Spieler##
    #Extrazüge
    if Ex_Zü == True:
        Extrazüge()
        return
    #letzter für Runde
    if Spieler == Alle_Spieler[-1]:
        Züge_Counter += 1
        #Runde vorbei?
        if Züge_Counter == Züge:
            Extrazüge_Dict.clear()
            for Spieler_ in Alle_Spieler:
                Liste = []
                for Karte in Spieler_.__dict__.values():
                    if Karte[0] in Karten.Extrazüge:
                        Liste.append(Karte)
                if not Liste == []:
                    Extrazüge_Dict.update({Spieler_:Liste})
            Extrazüge()
            return
        #nächster Spieler selbe Runde
        else:
            Neuer_Spieler = Alle_Spieler[0]
            Vor_Zug(Neuer_Spieler)
    #nächster
    else:
        Neuer_Spieler = Alle_Spieler[Alle_Spieler.index(Spieler) + 1]
        Vor_Zug(Neuer_Spieler)

def Vor_Zug(Spieler_):
    global Spieler
    Spieler = Spieler_
    Clear()
    #Aussetzen
    if Spieler.Aussetzen > 0:
        Spieler.Aussetzen -= 1
        #Buttons
        while len(Buttons) > 0:
            Buttons[0].delete_button()
        #Grafik
        screen.blit(get_image("transparenter_hintergrund.png"), (0, 0))
        pg.draw.rect(screen, (255, 255, 255), pg.Rect(500, 350, 600, 200))
        pg.draw.rect(screen, (0, 0, 0), pg.Rect(500, 350, 600, 200), 3)
        Text = get_Text("Du musst diesen Zug aussetzen", 40)
        screen.blit(Text, (800 - Text.get_width() / 2, 370))
        if Spieler.Aussetzen > 0:
            Text = get_Text("Du setzt noch einen weiteren Zug aus" if Spieler.Aussetzen == 1 else "Du setzt noch " + str(Spieler.Aussetzen) + " Züge aus", 30)
            screen.blit(Text, (800 - Text.get_width() / 2, 410))    
        Aussetzen_Button.create_button()
        return  
    #Überschrift
    pg.draw.rect(screen, (255, 255, 255), pg.Rect(622, 0, 800, 89))
    if Ex_Zü == True:
        Text = SMaxG("Extrazüge", 300, 40)
        screen.blit(Text, (620 + (415 / 2 - Text.get_width() / 2), 50 - Text.get_height() / 2))
    else:
        #Runden
        Übrig = Runden - Runden_Counter
        Runden_String = "letzte Runde" if Übrig == 1 else "noch " + str(Übrig) + " Runden"
        Text = SMaxG(Runden_String, None, 30)
        screen.blit(Text, (620 + (415 / 2 - Text.get_width() / 2), 10))
        #Züge
        Übrig = Züge - Züge_Counter
        Züge_String = "letzter Zug" if Übrig == 1 else "noch " + str(Übrig) + " Züge"
        Text = SMaxG(Züge_String, None, 30)
        screen.blit(Text, (620 + (415 / 2 - Text.get_width() / 2), 60))
    #Spieler
    if Spieler.SP_Name[-1] == "s" or Spieler.SP_Name[-1] == "S" or Spieler.SP_Name[-1] == "X" or Spieler.SP_Name[-1] == "x":
        Text = SMaxG(Spieler.SP_Name + "\' Zug", 300, 50)
    else:
        Text = SMaxG(Spieler.SP_Name + "s Zug", 300, 50)
    screen.blit(Text, (1025 + (415 / 2 - Text.get_width() / 2), 50 - Text.get_height() / 2))
    #weiter
    global Spieler_Zug
    Spieler_Zug = False
    for Bttn in Aktions_Buttons:
        if Bttn.Switch == False:
            Bttn.Change()
Nächster_Bild = get_image("startklein.png")
Nächster_Text = get_Text("Fertig", 40)
Nächster_Button = Button(pg.Rect(1590 - Nächster_Bild.get_width(), 10, Nächster_Bild.get_width(), Nächster_Bild.get_height()), lambda: Nach_Zug(Spieler), Nächster_Bild, Nächster_Text)

Aussetzen_Button = Button(pg.Rect(800 - Nächster_Bild.get_width() / 2, 450, Nächster_Bild.get_width(), Nächster_Bild.get_height()), lambda: Nach_Zug(Spieler, True), Nächster_Bild, get_Text("Okay", 40))

Extrazüge_Dict = {}
Gemachte_Extrazüge = 0
def Extrazüge():
    global Ex_Zü
    if not Extrazüge_Dict == {}:
        global Gemachte_Extrazüge
        global Spieler
        for Spieler_ in Alle_Spieler:
            if Spieler_ in Extrazüge_Dict:
                Spieler = Spieler_
                break
        Ex_Zü = True
        String = "Extrazüge\n"
        Counter = 0
        for Karte in Extrazüge_Dict[Spieler]:
            String += Karte[0].Name + ": + " + str(Karten.Extrazüge[Karte[0]]) + "\n"
            Counter += Karten.Extrazüge[Karte[0]]
        Str_Counter = "ein Extrazug" if Counter == 1 else str(Counter) + " Extrazüge"
        String += "Insgesamt: + " + Str_Counter
        String += "\n" + "Davon noch: " + str(Counter - Gemachte_Extrazüge)
        if Gemachte_Extrazüge < Counter:
            Gemachte_Extrazüge += 1
            Vor_Zug(Spieler)
            Info_Text(String)
        else:
            Gemachte_Extrazüge = 0
            del Extrazüge_Dict[Spieler]
            Extrazüge()
    else:
        Ex_Zü = False
        Nach_Extrazügen()

def Nach_Extrazügen():
    global Runden_Counter
    global Züge_Counter
    Runden_Counter += 1
    Züge_Counter = 0
    #Spiel Ende?
    if Runden_Counter == Runden:
        Ende() ##################
    else:
        #Werteverbesserungskarten pro Runde
        for Spieler_ in Alle_Spieler:
            for Pos in Spieler_.__dict__:
                Karte = Spieler.__dict__[Pos]
                if "F" in Pos:
                    if Karte[0] in Karten.Extrafunktion_Anzahl and not Karte[0] in Karten.Einmal_pro_Spiel:
                        getattr(Spieler, Pos)[-1] = Karten.Extrafunktion_Anzahl[Karte[0]]
        #Auswahl
        Auswahlstapel()

##Karten Buttons##
#Ablage
Karten_Ablage_Rects = []
x = 475
y = 490
for Num in range(0, 6):
    KaAbRe = pg.Rect(x, y, 153, 253)
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
    KaFeRe = pg.Rect(x, y, 153, 253)
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
x = 555
y = 135
for Num in range(0, 8):
    KaÜbRe = pg.Rect(x, y, 90, 43)
    Karten_Feld_Übersicht_Rects.append(KaÜbRe)
    x += 119

Feld_Übersicht_Button_0 = Button(Karten_Feld_Übersicht_Rects[0], lambda: Karten_Func("Feld_Übersicht", 0))
Feld_Übersicht_Button_1 = Button(Karten_Feld_Übersicht_Rects[1], lambda: Karten_Func("Feld_Übersicht", 1))
Feld_Übersicht_Button_2 = Button(Karten_Feld_Übersicht_Rects[2], lambda: Karten_Func("Feld_Übersicht", 2))
Feld_Übersicht_Button_3 = Button(Karten_Feld_Übersicht_Rects[3], lambda: Karten_Func("Feld_Übersicht", 3))
Feld_Übersicht_Button_4 = Button(Karten_Feld_Übersicht_Rects[4], lambda: Karten_Func("Feld_Übersicht", 4))
Feld_Übersicht_Button_5 = Button(Karten_Feld_Übersicht_Rects[5], lambda: Karten_Func("Feld_Übersicht", 5))
Feld_Übersicht_Button_6 = Button(Karten_Feld_Übersicht_Rects[6], lambda: Karten_Func("Feld_Übersicht", 6))
Feld_Übersicht_Button_7 = Button(Karten_Feld_Übersicht_Rects[7], lambda: Karten_Func("Feld_Übersicht", 7))

#Leuchtrand von Karten für später
Leuchtrand_Farbe = (255, 200, 0)

#Karten Funktion
Alt_LR_Pos = 0
Extra_List = []
def Karten_Func(Kategorie, Button_Num):
    global Spieler_Zug
    if Kategorie == "Ablage":
        Alt_Range = Ablage_Alt_Range
        Str = "A_" + str(Alt_Range[Button_Num])
        Rects = Karten_Ablage_Rects
    elif Kategorie == "Feld":
        Alt_Range = Feld_Alt_Range
        Str = "F_" + str(Alt_LR_Pos) + "_" + str(Alt_Range[Button_Num])
        Rects = Karten_Feld_Rects
    elif Kategorie == "Feld_Übersicht":
        Alt_Range = Feld_Übersicht_Alt_Range
        Str = "F_" + str(Alt_Range[Button_Num])
        Rects = Karten_Feld_Übersicht_Rects
    try:
        Karte = getattr(Spieler, Str)
    except AtrributeError:
        pass
    else:
        #Leuchtrand
        Warumeinfachwennsauchkompliziertgeht = {"Ablage":Ablage_Surf, "Feld":Feld_Surf, "Feld_Übersicht":Feld_Übersicht_Surf}
        if Kategorie == "Feld":
            Ausgabe(Spieler, Warumeinfachwennsauchkompliziertgeht[Kategorie], Alt_Range, Alt_LR_Pos)
        else:
            Ausgabe(Spieler, Warumeinfachwennsauchkompliziertgeht[Kategorie], Alt_Range)
        pg.draw.rect(screen, Leuchtrand_Farbe, Rects[Button_Num], 3)
        #Funktionen, Kombi, etc
        if Aktion == "Kombi":
            Extra_List.append(Str)
            if len(Extra_List) == 1:
                Info_Text("Kombi:\n" + Karte[0].Name + " + ?\nWähle eine weitere Karte")
            elif len(Extra_List) == 2:
                Kombi_Func(Extra_List)
        elif Aktion == "Extrafunktion":
            Extra_List.append(Str)
            if len(Extra_List) == 1:
                if Extra_List[0][0] == Karten.Joker:
                    Info_Text("Wähle eine Kartenart, aus der zufällig eine Startkarte gewählt wird")
                    for Bttn in Joker_Buttons:
                        Bttn.create_button()
                elif "Gift" in Extra_List[0][0].Name or Extra_List[0][0] in Karten.Gegner_Nötig:
                    Info_Text("Wähle einen deiner Gegner")
                    global Gift_Karte
                    Gift_Karte = Extra_List[0]
                    for Bttn in Gegner_Buttons:
                        Bttn.create_button()
                else:
                    Info_Text("Extrafunktion der Karte: " + Karte[0].Name + "\nWähle eine Karte, auf die du die Extrafunktion anwenden möchstest")
            elif len(Extra_List) == 2:
                Extra_Func(Extra_List)
        elif Aktion == "Lebensraum platzieren":
            if Karte[0] in Karten.Alle_Lebensraum:
                if "A" in Str:
                    Spieler.F = Karte
                    delattr(Spieler, Str)
                    Spieler.Sortieren()
                    Spieler_Zug = True
                    Clear()
                else:
                    Info_Text("Der Lebensraum muss aus der Ablage gewählt werden")
            else:
                Info_Text("Du kannst nur Lebensräume auf dem Feld platzieren")
        elif Aktion == "Lebewesen bewegen":
            if len(Extra_List) == 0:
                if Karte[0] in Karten.Alle_Lebewesen:
                    if Kategorie == "Ablage":
                        if Spieler_Zug == True:
                            Info_Text("Du hast deinen Zug bereits gemacht und kannst nur noch Lebewesen innerhalb des Feldes bewegen")
                            Clear()
                        else:
                            Extra_List.append(Str)
                            Info_Text("Wähle einen Lebensraum, in dem du das Lebewesen platzieren möchtest: " + Karte[0].Name)
                    else:
                        Extra_List.append(Str)
                        Info_Text("Wähle einen Lebensraum, in dem du das Lebewesen platzieren möchtest: " + Karte[0].Name)
                else:
                    Info_Text("Du kannst nur Lebewesen bewegen")
            elif len(Extra_List) == 1:
                if Karte[0] in Karten.Alle_Lebensraum:
                    Extra_List.append(Str)
                    if "F" in Str:
                        LW_Karte = Extra_List[0]
                        LR_Karte = Extra_List[1]
                        #Größe
                        Voll_Test = False
                        Alte_LW = []
                        for Pos in Spieler.__dict__:
                            if Pos[2] == LR_Karte[2]:
                                Alte_LW.append(Pos)
                        Größe = Spieler.LR_Karte[2]                
                        if len(Alte_LW) < Größe:
                            Voll_Test = True
                        else:
                            Info_Text("Dieser Lebensraum ist bereits voll")
                        #Art
                        Art_Test = False
                        for Lr in Spieler.LW_Karte[2]:
                            if Lr == Spieler.LR_Karte[3] or Lr == "Alle":
                                Art_Test = True
                                break
                        if Art_Test == False:
                            Info_Text("Dieser Lebensraum ist für das Lebewesen nicht geeignet")
                        #Hinzufügen?
                        if Voll_Test == True and Art_Test == True:
                            if "A" in LW_Karte:
                                Spieler_Zug = True
                            Karte = Spieler.LW_Karte
                            Attr = "F_" + LR_Karte[2] + "_"
                            setattr(Spieler, Attr, Karte)
                            delattr(Spieler, LW_Karte)
                    else:
                        Info_Text("Der Lebensraum muss sich auf dem Feld befinden")
                    Clear(False)
                else:
                    Info_Text("Wähle einen Lebensraum")
        #normal Text am Rand ausgeben
        else:
            if Kategorie == "Feld_Übersicht":
                Ausgabe(Spieler, Feld_Surf, range(0, 6), Num)
            Info_Text(Karte[0].Name + "\n" + Karte[0].Beschreibung + "\n" + "Punkte: " + str(Karte[1]))

##Spielfunktionen Buttons##
Aktion = None
def Aktion_Func(Aktion_, B):
    global Aktion
    Extra_List.clear()
    if B.Switch == True:
        Aktion = Aktion_
        Aktion_An(Aktion)
        if Aktion == "Kombi":
            Info_Text("Wähle zwei Karten, die du kombinieren möchtest")
        elif Aktion == "Extrafunktion":
            Info_Text("Wähle die Karte, deren Extrafunktion du anwenden möchtest")
        elif Aktion == "Lebensraum platzieren":
            Info_Text("Wähle einen Lebensraum aus deiner Ablage, den du auf dem Feld platzieren möchtest")
        elif Aktion == "Lebewesen bewegen":
            Info_Text("Wähle ein Lebewesen auf dem Feld, das du bewegen möchtest")
    else:
        Info_Text("Du hast deinen Zug bereits gemacht")
Weißer_Hgrund = get_image("weißer_hgrund.png")
Blauer_Hgrund = get_image("blauer_hgrund.png")
Kombi_Rect = pg.Rect(451, 801, 285.5, 98)
Kombi_Button = Button(Kombi_Rect, lambda: Aktion_Func("Kombi", Kombi_Button), Weißer_Hgrund, get_Text("Kombi", 30), Blauer_Hgrund)
Lila_Hgrund = get_image("lila_hgrund.png")
Extra_Rect = pg.Rect(738.5, 801, 285.5, 98)
Extra_Button = Button(Extra_Rect, lambda: Aktion_Func("Extrafunktion", Extra_Button), Weißer_Hgrund, get_Text("Extrafunktion", 30), Lila_Hgrund)
Gelber_Hgrund = get_image("gelber_hgrund.png")
LR_Rect = pg.Rect(1026, 801, 285.5, 98)
LR_Button = Button(LR_Rect, lambda: Aktion_Func("Lebensraum platzieren", LR_Button), Weißer_Hgrund, get_Text("Lebensraum platzieren", 30), Gelber_Hgrund)
Roter_Hgrund = get_image("roter_hgrund.png")
LW_Rect = pg.Rect(1313.5, 801, 285.5, 98)
LW_Button = Button(LW_Rect, lambda: Aktion_Func("Lebewesen bewegen", LW_Button), Weißer_Hgrund, get_Text("Lebewesen bewegen", 30), Roter_Hgrund)

def Kombi_Func(Karten_Liste):
    #Karten_Liste = [Position Karte 1, Position Karte 2]
    global Spieler_Zug
    Neue_Karte = False
    #Verbesserung für später, Differenz zu Original-Werten
    Add_Größe = 0
    Add_Punkte = 0
    Add_Lebensräume = []
    for Posi in range(0, 2):
        if getattr(Spieler, Karten_Liste[Posi])[0] in Karten.Alle_Lebensraum:
            Add_Größe += getattr(Spieler, Karten_Liste[Posi])[2] - getattr(Spieler, Karten_Liste[Posi])[0].Größe
            Add_Punkte += getattr(Spieler, Karten_Liste[Posi])[1] - getattr(Spieler, Karten_Liste[Posi])[0].Punkte
        elif getattr(Spieler, Karten_Liste[Posi])[0] in Karten.Alle_Lebewesen:
            Add_Punkte += getattr(Spieler, Karten_Liste[Posi])[1] - getattr(Spieler, Karten_Liste[Posi])[0].Punkte
            for Lr in getattr(Spieler, Karten_Liste[Posi])[2]:
                if (not Lr in getattr(Spieler, Karten_Liste[Posi])[0].Lebensraum) and (not Lr in Add_Lebensräume):
                    Add_Lebensräume.append(Lr)
    Gesuchte_Kombi_1 = getattr(Spieler, Karten_Liste[0])[0].Name + "+" + getattr(Spieler, Karten_Liste[1])[0].Name
    Gesuchte_Kombi_2 = getattr(Spieler, Karten_Liste[1])[0].Name + "+" + getattr(Spieler, Karten_Liste[0])[0].Name
    for Counter_Add, Karte in enumerate(Karten.Alle_Karten):
        #Kombi
        if Gesuchte_Kombi_1 in Karte.Kombi or Gesuchte_Kombi_2 in Karte.Kombi:
            Neue_Karte = Karte
            #Lr
            if getattr(Spieler, Karten_Liste[0])[0] in Karten.Alle_Lebensraum or getattr(Spieler, Karten_Liste[1])[0] in Karten.Alle_Lebensraum:
                if getattr(Spieler, Karten_Liste[0])[0] in Karten.Alle_Lebensraum:
                    LR_Karte = getattr(Spieler, Karten_Liste[0])
                    LR_Pos = Karten_Liste[0]
                    Andere_Karte = getattr(Spieler, Karten_Liste[1])[0]
                    Andere_Pos = Karten_Liste[1]
                else:
                    Andere_Karte = getattr(Spieler, Karten_Liste[0])
                    Andere_Pos = Karten_Liste[0]
                    LR_Karte = getattr(Spieler, Karten_Liste[1])[0]
                    LR_Pos = Karten_Liste[1]
                #Lr + Lr
                if Andere_Karte[0] in Karten.Alle_Lebensraum:
                    #beide Feld oder beide Ablage
                    if ("F" in LR_Pos and "F" in Andere_Pos) or ("A" in LR_Pos and "A" in Andere_Pos):
                        for Num, Pos in enumerate(Spieler.__dict__):
                            if Pos[2] == LR_Pos[2] or Pos[2] == Andere_Pos[2]:
                                setattr(Spieler, LR_Pos + "_" + str(Num), Spieler.__dict__[Pos])
                                delattr(Spieler, Pos)
                        delattr(Spieler, Andere_Pos)
                        setattr(Spieler, LR_Pos, [Neue_Karte, Neue_Karte.Punkte, Neue_Karte.Größe])
                        Neue_Pos = LR_Pos
                        Spieler_Zug = True
                        break
                    else:
                        Info_Text("Du kannst Lebensräume nur innerhalb des Feldes oder innerhalb der Ablage kombinieren")
                        break
                #Lr + E
                elif Andere_Karte[0] in Karten.Alle_Elemente:
                    for Num, Pos in enumerate(Spieler.__dict__):
                        if Pos[2] == LR_Pos[2]:
                            setattr(Spieler, LR_Pos + "_" + str(Num), Spieler.__dict__[Pos])
                            delattr(Spieler, Pos)
                        delattr(Spieler, Andere_Pos)
                        setattr(Spieler, LR_Pos, [Neue_Karte, Neue_Karte.Punkte, Neue_Karte.Größe])
                        Neue_Pos = LR_Pos
                        Spieler_Zug = True
                        break
            #Lw
            if getattr(Spieler, Karten_Liste[0])[0] in Karten.Alle_Lebewesen or getattr(Spieler, Karten_Liste[1])[0] in Karten.Alle_Lebewesen:
                if getattr(Spieler, Karten_Liste[0])[0] in Karten.Alle_Lebewesen:
                    LW_Karte = getattr(Spieler, Karten_Liste[0])
                    LW_Pos = Karten_Liste[0]
                    Andere_Karte = getattr(Spieler, Karten_Liste[1])[0]
                    Andere_Pos = Karten_Liste[1]
                else:
                    Andere_Karte = getattr(Spieler, Karten_Liste[0])
                    Andere_Pos = Karten_Liste[0]
                    LW_Karte = getattr(Spieler, Karten_Liste[1])[0]
                    LW_Pos = Karten_Liste[1]
                #Lw + Lw
                if Andere_Karte[0] in Karten.Alle_Lebewesen:
                    #beide Ablage oder beide selber Lr
                    if "F" in LW_Pos and "F" in Andere_Pos:
                        #geeigneter Lebensraum?
                        for Lr in Neue_Karte.Lebensraum:
                            if Lr == getattr(Spieler, LW_Pos[0:2])[3]:
                                delattr(Spieler, Andere_Pos)
                                setattr(Spieler, LW_Pos, [Neue_Karte, Neue_Karte.Punkte, Neue_Karte.Lebensraum])
                                Neue_Pos = LW_Pos
                                Spieler_Zug = True
                                break
                            elif Lr == getattr(Spieler, Andere_Pos[0:2])[3]:
                                delattr(Spieler, LW_Pos)
                                setattr(Spieler, Andere_Pos, [Neue_Karte, Neue_Karte.Punkte, Neue_Karte.Lebensraum])
                                Neue_Pos = Andere_Pos
                                Spieler_Zug = True
                                break
                            else:
                                Info_Text("Keiner der beiden Lebensräume ist geeignet für das neue Lebewesen")
                                break
                    elif "A" in LW_Pos and "A" in Andere_Pos:
                        delattr(Spieler, Andere_Pos)
                        setattr(Spieler, LW_Pos, [Neue_Karte, Neue_Karte.Punkte, Neue_Karte.Lebensraum])
                        Neue_Pos = LW_Pos
                        Spieler_Zug = True
                        break
                    else:
                        Info_Text("Du kannst nur innerhalb des Feldes oder der Ablage kombinieren")
                        break
                #Lw + E
                elif Andere_Karte[0] in Karten.Alle_Elemente:
                    if "F" in LW_Pos:
                        #geeigneter Lebensraum?
                        for Lr in Neue_Karte.Lebensraum:
                            if Lr == getattr(Spieler, LW_Pos[0:2])[3]:
                                delattr(Spieler, Andere_Pos)
                                setattr(Spieler, LW_Pos, [Neue_Karte, Neue_Karte.Punkte, Neue_Karte.Lebensraum])
                                Neue_Pos = LW_Pos
                                Spieler_Zug = True
                                break
                            else:
                                Info_Text("Der Lebensraum ist nicht geeignet für das neue Lebewesen")
                                break
                    elif "A" in LW_Pos:
                        delattr(Spieler, Andere_Pos)
                        setattr(Spieler, LW_Pos, [Neue_Karte, Neue_Karte.Punkte, Neue_Karte.Lebensraum])
                        Neue_Pos = LW_Pos
                        Spieler_Zug = True
                        break
            #E + E
            elif getattr(Spieler, Karten_Liste[0])[0] in Karten.Alle_Elemente and getattr(Spieler, Karten_Liste[1])[0] in Karten.Alle_Elemente:
                delattr(Spieler, Karten_Liste[1])
                setattr(Spieler, Karten_Liste[0], [Neue_Karte])
                Neue_Pos = Karten_Liste[0]
                Spieler_Zug = True
                break
        #Keine Kombi möglich
        elif Counter_Add == len(Karten.Alle_Karten):
            Info_Text("Diese Karten lassen sich nicht kombinieren")
    #Verbesserungen
    if Spieler_Zug == True:
        Info_Text("Neue Karte: " + Neue_Karte.Name)
        #Weitergabe Verbesserungen
        if getattr(Spieler, Neue_Pos)[0] in Karten.Alle_Lebensraum:
            getattr(Spieler, Neue_Pos)[1] += Add_Punkte
            getattr(Spieler, Neue_Pos)[2] += Add_Größe
        elif getattr(Spieler, Neue_Pos)[0] in Karten.Alle_Lebewesen:
            getattr(Spieler, Neue_Pos)[1] += Add_Punkte
            for Lr in Add_Lebensräume:
                if not Lr in getattr(Spieler, Neue_Pos)[2] and not "Alle" in getattr(Spieler, Neue_Pos)[2]:
                    getattr(Spieler, Neue_Pos)[2].append(Lr)
            if "Wald" in getattr(Spieler, Neue_Pos)[2] and "Berge" in getattr(Spieler, Neue_Pos)[2] and "See" in getattr(Spieler, Neue_Pos)[2] and "Wüste" in getattr(Spieler, Neue_Pos)[2]:
                getattr(Spieler, Neue_Pos)[2] = ["Alle"]
        #Extrafunktion Counter
        Extra_Neue_Karte(Spieler, Neue_Pos)
        Spieler.Sortieren()
    Clear(False)

def Extra_Func(Karten_Liste):
    global Spieler_Zug
    Neue_Karte = False
    E_Karte = getattr(Spieler, Karten_Liste[0])
    Andere_Karte = getattr(Spieler, Karten_Liste[1])
    E_Pos = Karten_Liste[0]
    Andere_Pos = Karten_Liste[1]
    #Tränke
    if "Trank" in E_Karte[0].Name:
        #Lebensraum-Tränke
        if "Lebensraum" in E_Karte[0].Beschreibung or E_Karte[0] == Karten.Duftender_Trank:
            if Andere_Karte[0] in Karten.Alle_Lebensraum:
                #Vergrößerungs-Trank
                if E_Karte[0] == Karten.Vergrößerungs_Trank:
                    getattr(Spieler, Andere_Pos)[2] += 1
                    delattr(Spieler, E_Pos)
                    Spieler_Zug = True
                    Info_Text("Größe des Lebensraums " + Andere_Karte[0].Name + " um 1 verbessert")
                #Duftender Trank
                elif E_Karte[0] == Karten.Duftender_Trank:
                    Add_Größe = getattr(Spieler, Andere_Pos)[2] - getattr(Spieler, Andere_Pos)[0].Größe
                    Add_Punkte = getattr(Spieler, Andere_Pos)[1] - getattr(Spieler, Andere_Pos)[0].Punkte
                    if "Klein" in Andere_Karte[0].Name:
                        if "Magisch" in Andere_Karte[0].Name:
                            Neue_Karte = Karten.Magisches_Kleines_Wonderland
                        else:
                            Neue_Karte = Karten.Kleines_Wonderland
                    elif "Groß" in Andere_Karte[0].Name:
                        if "Magisch" in Andere_Karte[0].Name:
                            Neue_Karte = Karten.Magisches_Großes_Wonderland
                        else:
                            Neue_Karte = Karten.Großes_Wonderland
                    else:
                        if "Magisch" in Andere_Karte[0].Name:
                            Neue_Karte = Karten.Magisches_Wonderland
                        else:
                            Neue_Karte = Karten.Wonderland
                    for Num, Pos in enumerate(Spieler.__dict__):
                        if Pos[2] == Karten_Liste[1][2]:
                                setattr(Spieler, Karten_Liste[1] + "_" + str(Num), Spieler.__dict__[Pos])
                                if "Magisch" in Neue_Karte.Name:
                                    getattr(Spieler, Karten_Liste[1] + "_" + str(Num))[1] += 1
                                delattr(Spieler, Pos)
                        delattr(Spieler, Karten_Liste[0])
                        setattr(Spieler, Karten_Liste[1], [Neue_Karte, Neue_Karte.Punkte + Add_Punkte, Neue_Karte.Größe + Add_Größe])
                    Spieler_Zug = True
                    Info_Text(Andere_Karte[0].Name + " durch " + Neue_Karte.Name + " ersetzt")
            else:
                Info_Text("Du kannst diesen Trank nur auf Lebensräume anwenden")
        #Lebewesen-Tränke     
        elif "Lebewesen" in E_Karte[0].Beschreibung:
            if Andere_Karte[0] in Karten.Alle_Lebewesen:
                Mehr_LRs_Tränke = {Karten.Heißer_Trank:"Wüste", Karten.Wässriger_Trank:"See", Karten.Matschiger_Trank:"Wald", Karten.Blubbernder_Trank:"Berge", Karten.Verkohlter_Trank:"Alle"}
                Werte_Tränke = {Karten.Güldener_Trank:3, Karten.Level_Up_Trank:5, Karten.Glitzernder_Trank:7, Karten.Himmlischer_Trank:10}
                #Mehr Lr Tränke
                if E_Karte[0] in Mehr_LRs_Tränke:
                    Lr = Mehr_LRs_Tränke[E_Karte[0]]
                    if not Lr in Andere_Karte[2]:
                        if Lr == "Alle":
                            getattr(Spieler, Andere_Pos)[2] = ["Alle"]
                        else:
                            getattr(Spieler, Andere_Pos)[2].append[Lr]
                            if "Wald" in getattr(Spieler, Andere_Pos)[2] and "Berge" in getattr(Spieler, Andere_Pos)[2] and "See" in getattr(Spieler, Andere_Pos)[2] and "Wüste" in getattr(Spieler, Andere_Pos)[2]:
                                getattr(Spieler, Andere_Pos)[2] = ["Alle"]
                        delattr(Spieler, E_Pos)
                        Spieler_Zug = True
                        if Lr == "Alle":
                            Lr = "Alle Lebensräume"
                        Info_Text(Andere_Karte[0].Name + " kann jetzt hier leben: " + Lr)
                    else:
                        Info_Text("Das Lebewesen " + Andere_Karte[0].Name + " kann in dem Lebensraum bereits leben")
                #Werte Tränke
                elif E_Karte[0] in Werte_Tränke:
                    getattr(Spieler, Andere_Pos)[1] += Werte_Tränke[E_Kate[0]]
                    delattr(Spieler, E_Pos)
                    Spieler_Zug = True
                    Info_Text("Punkte der Karte " + Andere_Karte.Name + " um " + str(Wert) + " verbessert")
                #Dolly Trank
                elif E_Karte[0] == Karten.Dolly_Trank:
                    setattr(Spieler, "A_", Andere_Karte)
                    delattr(Spieler, E_Pos)
                    Spieler_Zug = True
                    Extra_Neue_Karte(Spieler, "A_")
                    Info_Text("Neue Karte: " + Andere_Karte[0].Name)
            else:
                Info_Text("Du kannst diesen Trank nur auf Lebenwesen anwenden")
    #Parasit
    elif E_Karte[0] == Karten.Parasit:
        if Andere_Karte[0] in Karten.Alle_Lebewesen:
            if E_Karte[-1] > 0:
                getattr(Spieler, E_Pos)[1] += Andere_Karte[1]
                getattr(Spieler, Andere_Pos)[1] -= 4
                getattr(Spieler, E_Pos)[-1] -= 1
                Spieler_Zug = True
                Info_Text("Parasit um die Punkte der Karte " + Andere_Karte[0].Name + " verbessert, " + Andere_Karte[0].Name + " um 4 verschlechtert")
            else:
                Info_Text("Fähigkeit kann nur einmal angewandt werden, Parasit muss auf dem Feld platziert sein")
        else:
            Info_Text("Kann nur die Werte von Lebewesen aufnehmen")
    #Werteverbesserungskarte
    elif E_Karte[0] in Karten.Werteverbesserung_Übersicht:
        if Andere_Karte[0] in Karten.Alle_Lebewesen:
            if E_Karte[-1] > 0:
                getattr(Spieler, Andere_Pos)[1] += Karten.Werteverbesserung_Übersicht[E_Karte[0]]
                getattr(Spieler, E_Pos)[-1] -= 1
                Spieler_Zug = True
                Info_Text("Alle Werte der Karte " + Andere_Karte[0].Name + " um " + str(Wert) + "verbessert")
            else:
                Info_Text("Fähigkeit kann nur einmal angewandt werden, Karte muss auf dem Feld platziert sein")
        else:
            Info_Text("Kann nur die Werte von Lebewesen verbessern")
    #Mehr Lebensräume
    elif E_Karte[0] in Karten.ExtraLRs:
        if Andere_Karte[0] in Karten.Alle_Lebewesen:
            if not "A" in E_Pos:
                #Alle?
                if "Alle" in Andere_Karte[2]:
                    Info_Text("Dieses Lebewesen kann bereits in allen Lebensräumen leben")
                else:
                    #Zufall
                    Spieler_Zug = True
                    Tets = True
                    if Karten.ExtraLRs[E_Karte[0]] == "Zufall":
                        LRs_Kopie = Karten.LRs.copy()
                        for Lr in Andere_Karte[2]:
                            if not Lr == "Wonderland" and Lr in LRs_Kopie:
                                LRs_Kopie.remove(Lr)
                        Neu = random.choice(LRs_Kopie)
                    else:
                        Neu = ExtraLRs[E_Karte[0]]
                        if Neu in Andere_Karte[2]:
                            Info_Text("Dieses Lebewesen kann in dem Lebensraum " + Neu + " bereits leben")
                            Test = False
                    if Test == True:
                        getattr(Spieler, Andere_Pos)[2].append(Neu)
                        if "Wald" in getattr(Spieler, Andere_Pos)[2] and "Berge" in getattr(Spieler, Andere_Pos)[2] and "See" in getattr(Spieler, Andere_Pos)[2] and "Wüste" in getattr(Spieler, Andere_Pos)[2]:
                            getattr(Spieler, Andere_Pos)[2] = ["Alle"]
                            Neu = "Alle Lebensräume"
                        if Neu == "Alle":
                            Neu = "Alle Lebensräume"                                 
                    Info_Text("Die Karte " + Andere_Karte[0].Name + " kann jetzt hier leben: " + Neu)
            else:
                Info_Text("Platziere Lebewesen auf dem Feld, um ihre Extrafunktion zu nutzen")
        else:
            Info_Text("Kann nur auf Lebewesen angewandt werden")
    #Friedensengel
    elif E_Karte[0] == Karten.Friedensengel:
        if Andere_Karte[0] in Karten.Alle_Lebensraum:
            if E_Karte[-1] > 0:
                Add_Größe = getattr(Spieler, Andere_Pos)[2] - getattr(Spieler, Andere_Pos)[0].Größe
                Add_Punkte = getattr(Spieler, Andere_Pos)[1] - getattr(Spieler, Andere_Pos)[0].Punkte
                if "Klein" in Andere_Karte[0].Name:
                    if "Magisch" in Andere_Karte[0].Name:
                        Neue_Karte = Karten.Magisches_Kleines_Wonderland
                    else:
                        Neue_Karte = Karten.Kleines_Wonderland
                elif "Groß" in Andere_Karte[0].Name:
                    if "Magisch" in Andere_Karte[0].Name:
                        Neue_Karte = Karten.Magisches_Großes_Wonderland
                    else:
                        Neue_Karte = Karten.Großes_Wonderland
                else:
                    if "Magisch" in Andere_Karte[0].Name:
                        Neue_Karte = Karten.Magisches_Wonderland
                    else:
                        Neue_Karte = Karten.Wonderland
                for Num, Pos in enumerate(Spieler.__dict__):
                    if Pos[2] == Andere_Pos[2]:
                        setattr(Spieler, Andere_Pos + "_" + str(Num), Spieler.__dict__[Pos])
                        if "Magisch" in Neue_Karte.Name:
                            getattr(Spieler, Andere_Pos + "_" + str(Num))[1] += 1
                        delattr(Spieler, Pos)
                getattr(Spieler, E_Pos)[-1] -= 1
                setattr(Spieler, Andere_Pos, [Neue_Karte, Neue_Karte.Punkte + Add_Punkte, Neue_Karte.Größe + Add_Größe])
                Spieler_Zug = True
                Info_Text(Andere_Karte[0].Name + " durch " + Neue_Karte.Name + " ersetzt")
            else:
                Info_Text("Muss auf dem Feld platziert sein und kann nur 3 Mal angewandt werden")
        else:
            Info_Text("Extrafunktion kann nur auf Lebensräume angewandt werden")
    #Zauberer
    elif E_Karte[0] == Karten.Zauberer:
        if Andere_Karte[0] in Karten.Alle_Elemente:
            if not "A" in E_Pos:
                for Trank in Karten.Tränke_Kombi:
                    if Andere_Karte[0] in Karten.Tränke_Kombi[Trank]:
                        Neue_Karte = Trank
                        break
                setattr(Spieler, Andere_Pos, [Neue_Karte])
                Spieler_Zug = True
                Info_Text("Neue Karte: " + Neue_Karte.Name)
            else:
                Info_Text("Platziere den Zauberer im Feld um seine Funktion zu nutzen")
        else:
            Info_Text("Zauberer kann nur Elemente in Tränke verwandeln")
    #Dunkler Magier
    elif E_Karte[0] == Karten.Dunkler_Magier:
        if Andere_Karte[0] in Karten.Alle_Elemente:
            if not "A" in E_Pos:
                for Gift in Karten.Gifte_Kombi:
                    if Andere_Karte[0] in Karten.Gifte_Kombi[Gift]:
                        Neue_Karte = Gift
                        break
                setattr(Spieler, Andere_Pos, [Neue_Karte])
                Spieler_Zug = True
                Info_Text("Neue Karte: " + Neue_Karte.Name)
            else:
                Info_Text("Platziere den Dunklen Magier im Feld um seine Funktion zu nutzen")
        else:
            Info_Text("Dunkler Magier kann nur Elemente in Gifte verwandeln")
    #Urwolf
    elif E_Karte[0] == Karten.Urwolf:
        if Andere_Karte[0] in Karten.Alle_Lebewesen:
            if E_Karte[-1] > 0:
                Weiter = True
                if Andere_Karte[1] > Karten.Werwolf.Punkte:
                    Info_Text("Die Karte ist bereits besser als eine Werwolf-Karte")
                    Weiter = False
                if not "A" in Andere_Pos:
                    if not getattr(Spieler, Andere_Pos[0:3])[0].Art == "Wald":
                        Info_Text("Der Lebensraum ist für einen Werwolf nicht geeignet - Wähle ein Lebewesen in einem Wald oder in der Ablage")
                        Weiter = False
                if Weiter == True:
                    Add_Punkte = getattr(Spieler, Andere_Pos)[1] - getattr(Spieler, Andere_Pos)[0].Punkte
                    Add_Lebensräume = []
                    for Lr in getattr(Spieler, Andere_Pos)[2]:
                        if (not Lr in getattr(Spieler, Andere_Pos)[0].Lebensraum) and (not Lr in Add_Lebensräume):
                            Add_Lebensräume.append(Lr)
                    setattr(Spieler, Andere_Pos, [Karten.Werwolf, Werwolf.Punkte + Add_Punkte, Werwolf.Lebensraum])
                    for Lr in Add_Lebensräume:
                        if not Lr in getattr(Spieler, Andere_Pos)[2] and not "Alle" in getattr(Spieler, Andere_Pos)[2]:
                            getattr(Spieler, Neue_Pos)[2].append(Lr)
                    if "Wald" in getattr(Spieler, Neue_Pos)[2] and "Berge" in getattr(Spieler, Neue_Pos)[2] and "See" in getattr(Spieler, Neue_Pos)[2] and "Wüste" in getattr(Spieler, Neue_Pos)[2]:
                        getattr(Spieler, Neue_Pos)[2] = ["Alle"]
                    Spieler_Zug = True
                    getattr(Spieler, E_Pos)[-1] -= 1
                    Info_Text(Andere_Karte[0].Name + " in Werwolf verwandelt")
            else:
                Info_Text("Kann nur einmal im Spiel angewandt werden, Karte muss auf dem Feld platziert sein")
        else:
            Info_Text("Kann nur auf Lebewesen angewandt werden")
    #Joker
    elif E_Karte[0] == Karten.Joker:
        if E_Karte[-1] > 0:
            Neue_Karte = None
            if Andere_Karte == "Lw":
                Neue_Karte = random.choice(Karten.Start_Lebewesen)
                Karte = [Karten.Neue_Karte, Neue_Karte.Punkte, Neue_Karte.Lebensraum]
            elif Andere_Karte == "Lr":
                Neue_Karte = random.choice(Karten.Start_Lebensraum)
                Karte = [Karten.Neue_Karte, Neue_Karte.Punkte, Neue_Karte.Größe]
            elif Andere_Karte == "E":
                Neue_Karte = random.choice(Karten.Start_Elemente)
                Karte = [Karten.Neue_Karte]
            setattr(Spieler, "A_", Karte)
            Spieler_Zug = True
            Extra_Neue_Karte(Spieler, "A_")
            getattr(Spieler, E_Pos)[-1] -= 1
            Info_Text("Neue Karte: " + Neue_Karte.Name)
        else:
            Info_Text("Kann nur einmal pro Runde angewandt werden, Karte muss auf dem Feld platziert sein")
    #Gifte bzw Gefrorener Trank oder Diebische Elster
    elif "Gift" in E_Karte[0].Name or E_Karte[0] == Karten.Gefrorener_Trank or E_Karte[0] == Karten.Schwarzer_Trank or E_Karte[0] == Karten.Diebische_Elster:
        Werte_Gifte = {Karten.Elementares_Gift:3, Karten.Pampiges_Gift:5, Karten.Schwarzer_Trank:5, Karten.Trügerisches_Gift:7, Karten.Blutiges_Gift:10}
        Aussetzen_Gifte = {Karten.Magisches_Gift:1, Karten.Lähmendes_Gift:3, Karten.Gefrorener_Trank:3, Karten.Eisiges_Gift:5}
        Zerstörungs_Gifte = [Karten.Reines_Gift, Karten.Gift_des_Vergessens]
        Gegner = Andere_Karte
        #Werte Gifte
        if E_Karte[0] in Werte_Gifte:
            #Lw zufällig wählen
            Gegner_LW = []
            for Pos in Gegner.__dict__:
                if Gegner.__dict__[Pos][0] in Karten.Alle_Lebewesen:
                    Gegner_LW.appen(Pos)
            Gewähltes_Lw = random.choice(Gegner_LW)
            #Werte verschlechtern
            getattr(Gegner, Gewähltes_Lw)[1] -= Werte_Gifte[E_Karte[0]]
            delattr(Spieler, E_Pos)
            Spieler_Zug = True
            Info_Text("Die Karte " + getattr(Gegner, Gewähltes_Lw)[0].Name + " des Spielers " + Gegner.SP_Name + " um " + str(Werte_Gifte[E_Karte[0]]) + " verschlechtert")
        #Aussetzen Gifte
        elif E_Karte[0] in Aussetzen_Gifte:
            Gegner.Aussetzen += Aussetzen_Gifte[E_Karte[0]]
            delattr(Spieler, E_Pos)
            Spieler_Zug = True
            Info_Text(Gegner.SP_Name + " setzt " + ("einen Zug" if Aussetzen_Gifte[E_Karte[0]] == 1 else (str(Aussetzen_Gifte[E_Karte[0]]) + " Züge")) + " aus")
        #Zerstörungs Gifte
        elif E_Karte[0] in Zerstörungs_Gifte or E_Karte[0] == Karten.Diebische_Elster:
            #Lebewesen nach Werten (Punkten) ordnen
            Gegner_LW = {}
            Werte_Liste = []
            for Pos in Gegner.__dict__:
                if getattr(Gegner, Pos)[0] in Karten.Alle_Lebewesen:
                    Werte_Liste.append(getattr(Gegner, Pos)[1])
                    if not getattr(Gegner, Pos)[1] in Gegner_LW:
                        Gegner_LW.update({getattr(Gegner, Pos)[1]:[Pos]})
                    else:
                        Gegner_LW[getattr(Gegner, Pos)[1]].append(Pos)
            if Gegner_LW == {}:
                Info_Text("Dieser Gegner besitzt keine Lebewesen")
                Clear(False)
                return
            #Lebewesen für Trank auswählen
            Werte_Liste.sort()
            if E_Karte[0] == Karten.Reines_Gift or E_Karte[0] == Karten.Diebische_Elster:
                Löschen_Karte = random.choice(Gegner_LW[Werte_Liste[0]])
            elif E_Karte[0] == Karten.Gift_des_Vergessens:
                Löschen_Karte = random.choice(Gegner_LW[Werte_Liste[-1]])
            #Ausführen
            Name = getattr(Gegner, Löschen_Karte)[0].Name
            if E_Karte[0] in Zerstörungs_Gifte:
                delattr(Gegner, Löschen_Karte)
                delattr(Spieler, E_Pos)
                Spieler_Zug = True
                Info_Text("Lebewesen " + Name + " des Spielers " + Gegner.SP_Name + " wurde zerstört")
            elif E_Karte[0] == Karten.Diebische_Elster:
                if E_Karte[-1] > 0:
                    setattr(Spieler, "A_", getattr(Gegner, Löschen_Karte))
                    delattr(Gegner, Löschen_Karte)
                    Spieler_Zug = True
                    Extra_Neue_Karte(Spieler, "A_")
                    getattr(Spieler, E_Pos)[-1] -= 1
                    Info_Text("Lebewesen " + Name + " vom Spieler " + Gegner.SP_Name + " gestohlen")
                else:
                    Info_Text("Fähigkeit kann nur 3 Mal angewandt werden, Diebische Elster muss auf dem Feld platziert sein")
    #Aussetzen
    elif E_Karte[0] in Karten.Aussetzen_Karten:
        if E_Karte[-1] > 0:
            Gegner = Andere_Karte
            Gegner.Aussetzen += Karten.Aussetzen_Karten[E_Karte[0]]       
            Spieler_Zug = True
            getattr(Spieler, E_Pos)[-1] -= 1
            Info_Text(Gegner + " setzt " + ("einen Zug" if Wert == 1 else str(Wert) + " Züge") + " aus")
        else:
            Info_Text("Extrafunktion kann nur einmal pro Runde angewandt werden, Karte muss auf dem Feld platziert sein")
    #Lebensraum vergrößern
    elif E_Karte[0] in Karten.Lr_Vergrößern:
        if E_Karte[-1] > 0:
            if Andere_Karte[0] in Karten.Alle_Lebensraum:
                getattr(Spieler, Andere_Pos)[2] += Karten.Lr_Vergrößern[E_Karte[0]]
                Spieler_Zug = True
                getattr(Spieler, E_Pos)[-1] -= 1
                Info_Text("Größe des Lebensraums " + Andere_Karte[0].Name + " um " + str(Karten.Lr_Vergrößern[E_Karte[0]]) + " verbessert")
            else:
                Info_Text("Kann nur auf Lebensräume angewandt werden")
        else:
            Info_Text("Extrafunktion kann nur einmal pro Runde angewandt werden, Karte muss auf dem Feld platziert sein")
    #Goldstück oder Goldkessel von Verrückter Gnom bzw. Kobold
    elif E_Karte[0] == Karten.Goldstück or E_Karte[0] == Karten.Kessel_voller_Gold:
        if Andere_Karte[0] in Karten.Alle_Lebewesen:
            if E_Karte[0] == Karten.Goldstück:
                Wert = 3
            else:
                Wert = 5
            getattr(Spieler, Andere_Pos)[1] += Wert
            Spieler_Zug = True
            delattr(Spieler, E_Pos)
            Info_Text("Lebewesen " + Andere_Karte[0].Name + " um " + str(Wert) + " verbessert")
        elif Andere_Karte[0] in Karten.Alle_Lebensraum:
            if E_Karte[0] == Karten.Goldstück:
                Wert = 1
            else:
                Wert = 3
            getattr(Spieler, Andere_Pos)[2] += Wert
            Spieler_Zug = True
            delattr(Spieler, E_Pos)
            Info_Text("Lebensraum " + Andere_Karte[0].Name + " um " + str(Wert) + " verbessert")
        else:
            Info_Text("Wähle ein Lebewesen oder einen Lebensraum")
    else:
        Info_Text("Diese Karte hat keine Extrafunktion")
    Clear(False)

#Extrabuttons für Extrafunktionen
Extra_Buttons = []
#Joker
Joker_LW_Button = Button(pg.Rect(175, 100, 120, 50), lambda: Extra_Func([Karten.Joker, "Lw"]), get_image("joker_lw.png"), get_Text("Lebewesen", 26))
Joker_LR_Button = Button(pg.Rect(175, 170, 120, 50), lambda: Extra_Func([Karten.Joker, "Lr"]), get_image("joker_lr.png"), get_Text("Lebensraum", 26))
Joker_E_Button = Button(pg.Rect(175, 240, 120, 50), lambda: Extra_Func([Karten.Joker, "E"]), get_image("joker_e.png"), get_Text("Element", 26))
Joker_Buttons = [Joker_LW_Button, Joker_LR_Button, Joker_E_Button]
#werden später gelöscht
for Bttn in Joker_Buttons:
    Extra_Buttons.append(Bttn)
#Gegner für Gifte
def Gegner_Bild(Num):
    if len(Alle_Spieler) >= (Num + 1):
        return get_image("gegner_bild.png")
    else:
        return None
def Gegner_Text(Num):
    if len(Alle_Spieler) >= (Num + 1):
        return SMaxG(Alle_Spieler[Num].SP_Name, 110, 45)
    else:
        return None
def Gegner_wählen(Num):
    if len(Alle_Spieler) >= (Num + 1):
        Extra_Func([Gift_Karte, Alle_Spieler[Num]])
    else:
        pass
Gegner_1_Button = Button(pg.Rect(175, 100, 120, 50), lambda: Gegner_wählen(0), Gegner_Bild(0), Gegner_Text(0))
Gegner_2_Button = Button(pg.Rect(175, 170, 120, 50), lambda: Gegner_wählen(1), Gegner_Bild(1), Gegner_Text(1))
Gegner_3_Button = Button(pg.Rect(175, 240, 120, 50), lambda: Gegner_wählen(2), Gegner_Bild(2), Gegner_Text(2))
Gegner_4_Button = Button(pg.Rect(175, 310, 120, 50), lambda: Gegner_wählen(3), Gegner_Bild(3), Gegner_Text(3))
Gegner_5_Button = Button(pg.Rect(175, 380, 120, 50), lambda: Gegner_wählen(4), Gegner_Bild(4), Gegner_Text(4))
Gegner_Buttons = [Gegner_1_Button, Gegner_2_Button, Gegner_3_Button, Gegner_4_Button, Gegner_5_Button]
for Bttn in Gegner_Buttons:
    Extra_Buttons.append(Bttn)

#Aktion beenden
Aktions_Buttons = [Kombi_Button, Extra_Button, LR_Button, LW_Button]
def Clear(Info = True):
    global Aktion
    for Bttn in Extra_Buttons:
        Bttn.delete_button()
    Extra_List.clear()
    Aktion = None
    Aktion_Aus()
    if Spieler_Zug == True:
        for Bttn in Aktions_Buttons:
            if Bttn.Switch == True and not Bttn == LW_Button:
                Bttn.Change()
    if Info == True:
        Info_Surf.fill((255, 255, 255))
        screen.blit(Info_Surf, (0, 0))
    Feld_Surf.fill((255, 255, 255))
    screen.blit(Feld_Surf, (474, 182))
    Ausgabe(Spieler, Ablage_Surf)
    Ausgabe(Spieler, Feld_Übersicht_Surf)

##Ausgabefunktionen##
#Ausgabe von: Feld, Ablage, Übersicht
Feld_Alt_Range = range(0, 6)
def Ausgabe(Spieler, Surf, Range = range(0, 6), LR_Pos = None):
    Surf.fill((255, 255, 255))
    global Feld_Übersicht_Alt_Range
    List = []
    if Surf == Ablage_Surf or Surf == Feld_Surf:
        #Ablage
        if Surf == Ablage_Surf:
            y_Surf = 482
            x_Surf = 452
            #Liste aus Objekten
            for Num, Pos in enumerate(Spieler.__dict__):
                if Pos == "A_" + str(Num):
                    List.append(Pos)
            #für Buttons
            global Ablage_Alt_Range
            Ablage_Alt_Range = Range
            #Buttons wenn Ablage oben oder unten mehr Karten
            if Range[0] > 0:
                if Ablage_Hoch_Button.Switch == False:
                    Ablage_Hoch_Button.Change()
            else:
                if Ablage_Hoch_Button.Switch == True:
                    Ablage_Hoch_Button.Change()
            if len(Ablage[Spieler]) > ((Range[-1]) + 1):
                if Ablage_Runter_Button.Switch == False:
                    Ablage_Runter_Button.Change()
            else:
                if Ablage_Runter_Button.Switch == True:
                    Ablage_Runter_Button.Change()
        #Feld
        elif Surf == Feld_Surf:
            y_Surf = 182
            x_Surf = 452
            #Liste aus Objekten
            Lr_Num = Feld_Übersicht_Alt_Range[LR_Pos]
            for Num, Pos in Spieler.__dict__:
                if Pos == "F_" + str(Lr_Num) + str(Num):
                    List.append(Pos)
            #für Buttons
            global Feld_Alt_Range
            Feld_Alt_Range = Range
            global Alt_LR_Pos
            Alt_LR_Pos = LR_Pos
            #Buttons
            if Range[0] > 0:
                if Feld_Hoch_Button.Switch == False:
                    Feld_Hoch_Button.Change()
            else:
                if Feld_Hoch_Button.Switch == True:
                    Feld_Hoch_Button.Change()
            if (len(Feld[Spieler][Lr]) > (Range[-1]) + 1):
                if Feld_Runter_Button.Switch == False:
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
        y_Surf = 131
        x_Surf = 520
        global Feld_Übersicht_Alt_Range
        Feld_Übersicht_Alt_Range = Range
        Range_1 = range(Range[0], Range[0] + 8)
        #Liste aus Objekten
        for Num, Pos in Spieler.__dict__:
            if Pos == "F_" + str(Num):
                List.append(Pos)
        #Surface zusammensetzen
        Dings_a = 90
        Dings = pg.Surface((Dings_a, 42))
        y = 4
        x = 35
        for Num in Range_1:
            if len(List) >= (Num + 1):
                Lr = getattr(Spieler, List[Num])[0]
                Verbrauchte_Lr = 0
                for Pos in Spieler.__dict__:
                    if "F_" + Str(Num) + "_" in Pos:
                        Verbrauchte_Lr += 1
                Mod_Größe = getattr(Spieler, Lr)[2]
                if Lr.Art == "Wald":
                    Hintergrund = (190, 240, 50)
                elif Lr.Art == "Wüste":
                    Hintergrund = (255, 190, 0)
                elif Lr.Art == "Berge":
                    Hintergrund = (220, 170, 130)
                elif Lr.Art == "See":
                    Hintergrund = (170, 240, 255)
                elif Lr.Art == "Wonderland":
                    Hintergrund = (240, 170, 255)
                Dings.fill(Hintergrund)
                Cap = SMaxG(Lr.Name, Dings_a, 19)
                Inside = SMaxG(str(Verbrauchte_Lr) + " / " + str(Mod_Größe), Dings_a, 19)
                Dings.blit(Cap, (Dings_a / 2 - Cap.get_width() / 2, 5))
                Dings.blit(Inside, (Dings_a / 2 - Inside.get_width() / 2, 22))
                Feld_Übersicht_Surf.blit(Dings, (x, y))
                x += 119
        #Buttons wenn Übersicht links oder rechts
        if Range_1[0] > 0:
            if Feld_Übersicht_Links_Button.Switch == False:
                Feld_Übersicht_Links_Button.Change()
        else:
            if Feld_Übersicht_Links_Button.Switch == True:
                Feld_Übersicht_Links_Button.Change()
        if (len(Feld[Spieler]) > (Range_1[-1]) + 1):
            if Feld_Übersicht_Rechts_Button.Switch == False:
                Feld_Übersicht_Rechts_Button.Change()
        else:
            if Feld_Übersicht_Rechts_Button.Switch == True:
                Feld_Übersicht_Rechts_Button.Change()
    #Surface auf Bildschirm
    screen.blit(Surf, (x_Surf, y_Surf))

#einzelne Karte ausgeben
def Druck(Karte_, Spieler, Auswahl = False):
    Surf = pg.Surface((150, 250))
    Karte = getattr(Spieler, Karte_)
    #Hintergrund und Art
    if Karte[0] in Karten.Alle_Lebewesen:
        Hintergrund = get_image("lw_hintergrund.png")
        Cap = SMaxG("Lebewesen", 150, 20)
    elif Karte[0] in Karten.Alle_Lebensraum:
        Hintergrund = get_image("lr_hintergrund.png")
        Cap = SMaxG("Lebensraum", 150, 20)
    elif Karte[0] in Karten.Alle_Elemente:
        Hintergrund = get_image("e_hintergrund.png")
        Cap = SMaxG("Element", 150, 20)
    Surf.blit(Hintergrund, (0, 0))
    Surf.blit(Cap, (150 / 2 - Cap.get_width() / 2, 5))
    #Name
    if " " in Karte[0].Name:
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
    if Karte[0] in Karten.Alle_Lebewesen:
        Punkte = Karte[1]
        if Punkte < 0:
            Punkte = 0
        Lebensraum = ""
        for Lr in Karte[2]:
            if not Lr == "Wonderland":
                Lebensraum = Lebensraum + Lr + ", "
        Lebensraum = Lebensraum.strip(", ")
        #Lebensräume
        LRs = get_Text("LRs:", 30)
        Surf.blit(LRs, (5, 135))
        LR_Text = SMaxG(Lebensraum, 140 - LRs.get_width(), LRs.get_height())
        Surf.blit(LR_Text, (LRs.get_width() + ((150 - LRs.get_width()) / 2 - LR_Text.get_width() / 2), 135))
        #Punkte
        P_Text = get_Text("Punkte:", 30)
        Surf.blit(P_Text, (5, 175))
        P_Num = get_Text(str(Punkte), 30)
        Surf.blit(P_Num, (P_Text.get_width() + (250 / 2 - P_Text.get_width() - P_Num.get_width() / 2), 175))
    elif Karte[0] in Karten.Alle_Lebensraum:
        Größe = Karte[2]
        #Größe
        G_Text = get_Text("Größe:", 30)
        Surf.blit(G_Text, (5, 135))
        G_Num = get_Text(str(Größe), 30)
        Surf.blit(G_Num, (G_Text.get_width() + (250 / 2 - G_Text.get_width() - G_Num.get_width() / 2), 135))
        #Punkte
        Punkte = Karte[1]
        if Punkte < 0:
            Punkte = 0
        P_Text = get_Text("Punkte:", 30)
        Surf.blit(P_Text, (5, 175))
        P_Num = get_Text(str(Punkte), 30)
        Surf.blit(P_Num, (P_Text.get_width() + (250 / 2 - P_Text.get_width() - P_Num.get_width() / 2), 175))
    return Surf

#Text auf Infosurf ausgeben
def Info_Text(Text_Raw):
    Info_Surf.fill((255, 255, 255))
    y = 20
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
            Info_Surf.blit(Dings, (450 / 2 - Dings.get_width() / 2, y))
            y += 60
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
            for Line in Lines:
                Teil = get_Text(Line, Größe)
                Info_Surf.blit(Teil, (450 / 2 - Teil.get_width() / 2, y))
                y += 40
    screen.blit(Info_Surf, (0, 0))

##Spielkern##
#Spielmodus Screen
def Spiel_Screen():
    screen.fill((255, 255, 255))
    #Buttons
    while len(Buttons) > 0:
        Buttons[0].delete_button()
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
    Feld_Übersicht_Button_6.create_button()
    Feld_Übersicht_Button_7.create_button()
    Kombi_Button.create_button()
    Extra_Button.create_button()
    LR_Button.create_button()
    LW_Button.create_button()
    for Bttn in Aktions_Buttons:
        Bttn.Change()
    #Linien
    Start_Ende = [[(450, 0), (450, 900)], [(450, 100), (1600, 100)], [(450, 450), (1600, 450)], [(450, 750), (1600, 750)], 
                  [(737.5, 750), (737.5, 900)], [(1025, 750), (1025, 900)], [(1312.5, 750), (1312.5, 900)], [(450, 800), (1600, 800)],
                  [(450, 130), (1600, 130)], [(450, 480), (1600, 480)], [(450, 180), (1600, 180)]]
    for Linie in Start_Ende:
        pg.draw.line(screen, (0, 0, 0), Linie[0], Linie[1], 1)
    if Ex_Zü == True:
        global Gemachte_Extrazüge
        Gemachte_Extrazüge -= 1
        Extrazüge()
        return
    #Überschrift
    if (Runden - Runden_Counter) == 1:
        Runden_String = "letzte Runde"
    else:
        Runden_String = "noch " + str(Runden - Runden_Counter) + " Runden"
    if (Züge - Züge_Counter) == 1:
        Züge_String = "letzter Zug"
    else:
        Züge_String = "noch " + str(Züge - Züge_Counter) + " Züge"
    #Surf Beschriftungen
    Text = SMaxG("Feld", None, 30)
    screen.blit(Text, (450 + (1150 / 2 - Text.get_width() / 2), 100 + (15 - Text.get_height() / 2)))
    Text = SMaxG("Ablage", None, 30)
    screen.blit(Text, (450 + (1150 / 2 - Text.get_width() / 2), 450 + (15 - Text.get_height() / 2)))
    #Züge, Runden, Spieler
    Text = SMaxG(Runden_String, None, 30)
    screen.blit(Text, (620 + (415 / 2 - Text.get_width() / 2), 10))
    Text = SMaxG(Züge_String, None, 30)
    screen.blit(Text, (620 + (415 / 2 - Text.get_width() / 2), 60))
    if Spieler.SP_Name[-1] == "s" or Spieler.SP_Name[-1] == "S" or Spieler.SP_Name[-1] == "X" or Spieler.SP_Name[-1] == "x":
        Text = SMaxG(Spieler + "\' Zug", 300, 50)
    else:
        Text = SMaxG(Spieler + "s Zug", 300, 50)
    screen.blit(Text, (1025 + (415 / 2 - Text.get_width() / 2), 50 - Text.get_height() / 2))
    Clear()

#Anfang vom Spiel
Start = False
def Spiel():
    global Spieler
    for Spieler in Alle_Spieler:
        #1. Ausgabe
        Erste_Ausgabe = [random.choice(Karten.Start_Lebewesen),
                         random.choice(Karten.Start_Lebensraum),
                         random.choice(Karten.Start_Elemente),
                         random.choice(random.choice(Karten.Nur)),
                         random.choice(random.choice(Karten.Alle_Start_Karten))]
        for Num, Karte in Erste_Ausgabe:
            if Karte in Karten.Alle_Lebewesen:
                Neu = [Karte, Karte.Punkte, Karte.Lebensraum]
            elif Karte in Karten.Alle_Lebensraum:
                Neu = [Karte, Karte.Punkte, Karte.Größe]
            else:
                Neu = [Karte]
            setattr(Spieler, "A_" + str(Num), Neu)
    Spieler = Alle_Spieler[0]
    Spiel_Screen()

#Zeugsfunktionen
#Aktion Abbrechen und Anzeige
Aktion_Anzeige = pg.Surface((900, 48))
def Aktion_An(Aktion):
    Text = get_Text("Aktuelle Aktion: " + Aktion, 40)
    Aktion_Anzeige.fill((255, 255, 255))
    Aktion_Anzeige.blit(Text, (450 - Text.get_width() / 2, 24 - Text.get_height() / 2))
    screen.blit(Aktion_Anzeige, (500, 751))
    Abbrechen_Button.create_button()
def Aktion_Aus():
    Text = get_Text("Wähle eine Aktion:", 40)
    Aktion_Anzeige.fill((255, 255, 255))
    Aktion_Anzeige.blit(Text, (450 - Text.get_width() / 2 + 75, 24 - Text.get_height() / 2))
    screen.blit(Aktion_Anzeige, (500, 751))
    Abbrechen_Button.delete_button()
    pg.draw.rect(screen, (255, 255, 255), pg.Rect(1450, 751, 150, 48))
Abbrechen_Rect = pg.Rect(1475, 755, 100, 40)
Abbrechen_Button = Button(Abbrechen_Rect, Clear, None, SMaxG("Abbrechen", 90, 35), None, (128, 0, 0))

#"Wirklich Verlassen?" Fenster
def Verlassen():
    global done
    done = True
def Nicht_Verlassen():
    Verlassen_Button.delete_button()
    Nicht_Verlassen_Button.delete_button()
    if Auswahl_Bool == True:
        Auswahlstapel()
    elif Extrakarten_Bool == True:
        Extrakarten_Func()
    else:
        Spiel_Screen()
Verlassen_Button = Button(pg.Rect(645, 460, 60, 30), Verlassen, None, SMaxG("Ja", 50, 20), None, (76, 117, 28))
Nicht_Verlassen_Button = Button(pg.Rect(895, 460, 60, 30), Nicht_Verlassen, None, SMaxG("Nein", 50, 20), None, (128, 0, 0))
def Wirklich_Verlassen():
    global done
    if Einstellungen_Fertig == True:
        while len(Buttons) > 0:
            Buttons[0].delete_button()
        screen.blit(get_image("transparenter_hintergrund.png"), (0, 0))
        Surf = pg.Surface((500, 100))
        Surf.fill((255, 255, 255))
        pg.draw.rect(screen, (0, 0, 0), pg.Rect(550, 400, 500, 100), 5)
        Schrift = SMaxG("Spiel wirklich verlassen?", 480, 30)
        Surf.blit(Schrift, (250 - Schrift.get_width() / 2, 10))
        screen.blit(Surf, (550, 400))
        Verlassen_Button.create_button()
        Nicht_Verlassen_Button.create_button()
    else:
        done = True

#Auswahlstapel nach fertigen Runden
#Buttons - Karten anklicken
Karten_Auswahl_Rects = []
x = 482.5
y = 170
for Num in range(0, 12):
    KaAuRe = pg.Rect(x, y, 151, 251)
    Karten_Auswahl_Rects.append(KaAuRe)
    if Num == 5:
        x = 482.5
        y = 480
    else:
        x += 165

Auswahl_Button_0 = Button(Karten_Auswahl_Rects[0], lambda: Auswahl_Karten_Func(0))
Auswahl_Button_1 = Button(Karten_Auswahl_Rects[1], lambda: Auswahl_Karten_Func(1))
Auswahl_Button_2 = Button(Karten_Auswahl_Rects[2], lambda: Auswahl_Karten_Func(2))
Auswahl_Button_3 = Button(Karten_Auswahl_Rects[3], lambda: Auswahl_Karten_Func(3))
Auswahl_Button_4 = Button(Karten_Auswahl_Rects[4], lambda: Auswahl_Karten_Func(4))
Auswahl_Button_5 = Button(Karten_Auswahl_Rects[5], lambda: Auswahl_Karten_Func(5))
Auswahl_Button_6 = Button(Karten_Auswahl_Rects[6], lambda: Auswahl_Karten_Func(6))
Auswahl_Button_7 = Button(Karten_Auswahl_Rects[7], lambda: Auswahl_Karten_Func(7))
Auswahl_Button_8 = Button(Karten_Auswahl_Rects[7], lambda: Auswahl_Karten_Func(8))
Auswahl_Button_9 = Button(Karten_Auswahl_Rects[9], lambda: Auswahl_Karten_Func(9))
Auswahl_Button_10 = Button(Karten_Auswahl_Rects[10], lambda: Auswahl_Karten_Func(10))
Auswahl_Button_11 = Button(Karten_Auswahl_Rects[11], lambda: Auswahl_Karten_Func(11))

def Auswahl_Karten_Func(Button_Num):
    Num = Auswahl_Alt_Range[Button_Num]
    if Num <= (len(Auswahl_List) - 1):
        Counter = 0
        for Dings in Auswahl_List:
            if Counter == Num:
                Karte = Dings
                break
            Counter += 1
        #Beschreibung als Info
        Info_Text(Karte.Name + "\n" + Karte.Beschreibung)
        #Leuchtrand
        Ausgabe_Auswahl(Auswahl_Alt_Range)
        pg.draw.rect(screen, Leuchtrand_Farbe, Karten_Auswahl_Rects[Num], 3)
        #Karte merken
        global Letzte_Auswahl_Karte
        Letzte_Auswahl_Karte = Karte
        if Auswahl_Auswählen_Button.Switch == False:
            Auswahl_Auswählen_Button.Change()

def Ausgabe_Auswahl(Range = range(0, 12)):
    pg.draw.rect(screen, (255, 255, 255), pg.Rect(471, 121, 988, 658))
    Info_Text(" ")
    global Auswahl_Alt_Range
    Auswahl_Alt_Range = Range
    Width = 482.5
    Height = 170
    for Num in Range:
        if len(Auswahl_List) >= (Num + 1):
            screen.blit(Druck(Auswahl_List[Num], None, True), (Width, Height))
            if Num == 5:
                Width = 482.5
                Height = 480
            else:
                Width += 165
    #Buttons wenn Auswahl oben oder unten mehr Karten
    if Range[0] > 0:
        if Auswahl_Hoch_Button.Switch == False:
            Auswahl_Hoch_Button.Change()
    else:
        if Auswahl_Hoch_Button.Switch == True:
            Auswahl_Hoch_Button.Change()
    if len(Auswahl_List) > ((Range[-1]) + 1):
        if Auswahl_Runter_Button.Switch == False:
            Auswahl_Runter_Button.Change()
    else:
        if Auswahl_Runter_Button.Switch == True:
            Auswahl_Runter_Button.Change()

#Buttons - Schieben
#Hoch um eine Reihe
Auswahl_Hoch_Rect = pg.Rect(1480, 150, Pfeil_Hoch.get_width(), Pfeil_Hoch.get_height())
Auswahl_Hoch_Button = Button(Auswahl_Hoch_Rect, lambda: Ausgabe_Auswahl(range(Auswahl_Alt_Range[0] - 6, Auswahl_Alt_Range[0] + 6)), Pfeil_Hoch_Blass, None, Pfeil_Hoch)
#Runter um eine Reihe
Auswahl_Runter_Rect = pg.Rect(1480, 750 - Pfeil_Runter.get_height(), Pfeil_Runter.get_width(), Pfeil_Runter.get_height())
Auswahl_Runter_Button = Button(Auswahl_Runter_Rect, lambda: Ausgabe_Auswahl(range(Auswahl_Alt_Range[0] + 6, Auswahl_Alt_Range[0] + 18)), Pfeil_Runter_Blass, None, Pfeil_Runter)

#Buttons - Auswählen der Karte
Auswählen_Blass_Hgrund = get_image("auswählen_blass.png")
Auswählen_Hgrund = get_image("auswählen.png")
Auswählen_Rect = pg.Rect(850, 820, Auswählen_Hgrund.get_width(), Auswählen_Hgrund.get_height())
def Auswahl_Auswählen():
    global Auswahl_Bool
    if Auswahl_Auswählen_Button.Switch == True:
        global Spieler
        Alter_Spieler = Spieler
        global Letzte_Auswahl_Karte
        #Karte hinzufügen
        Ablage[Spieler].append(Letzte_Auswahl_Karte)
        Auswahl_List.remove(Letzte_Auswahl_Karte)
        #Nächster Spieler
        for N in range(0, len(Reihenfolge)):
            if Reihenfolge[N] == Alter_Spieler:
                Num = N + 1
                if Num > (len(Reihenfolge) - 1):
                    Num = 0
                break
        Spieler = Reihenfolge[Num]
        Ausgabe_Auswahl()
        #Überschrift anpassen
        pg.draw.rect(screen, (255, 255, 255), pg.Rect(452, 52, 1146, 48))
        Text = SMaxG(Spieler + ": Wähle eine Karte", None, 30)
        screen.blit(Text, (450 + (1150 / 2 - Text.get_width() / 2), 60))
        #Button ausschalten
        Letzte_Auswahl_Karte = None
        Auswahl_Auswählen_Button.Change()
        #Beenden wenn Auswahl leer -> weiter mit nächster Runde
        if len(Auswahl_List) == 0:
            while len(Buttons) > 0:
                Buttons[0].delete_button()
            screen.fill((255, 255, 255))
            Auswahl_Bool = False
            Extrakarten_Func()
Auswahl_Auswählen_Button = Button(Auswählen_Rect, Auswahl_Auswählen, Auswählen_Blass_Hgrund, SMaxG("Auswählen", 300, 40, (255, 255, 255)), Auswählen_Hgrund)

#Buttons - Erklärung/Fragezeichen Button
#Auswahl_Erklärung_Button = 

Auswahl_Bool = False
#Funktion/Screen
def Auswahlstapel():
    global Auswahl_Bool
    screen.fill((255, 255, 255))
    #Erstes Mal in Runde
    if Auswahl_Bool == False:
        while len(Buttons) > 0:
                Buttons[0].delete_button()
        #Auswahlstapel zufällig wählen
        Anzahl_Auswahl_Karten = 3 * len(Alle_Spieler)
        if Züge > 10:
            Anzahl_Auswahl_Karten = 5 * len(Alle_Spieler)
        elif Züge > 20:
            Anzahl_Auswahl_Karten = 10 * len(Alle_Spieler)
        global Auswahl_List
        Auswahl_List = []
        Jedes = Anzahl_Auswahl_Karten // 3
        while Jedes > 0:
            Auswahl_List.append(random.choice(Karten.Start_Lebewesen))
            Auswahl_List.append(random.choice(Karten.Start_Lebensraum))
            Auswahl_List.append(random.choice(Karten.Start_Elemente))
            Jedes -= 1
            Anzahl_Auswahl_Karten -= 3
        while Anzahl_Auswahl_Karten > 0:
            Auswahl_List.append(random.choice(random.choice(Karten.Alle_Start_Karten)))
            Anzahl_Auswahl_Karten -= 1
        Sortieren(Auswahl_List)
        #zufällige Reihenfolge
        Alle_Spieler_Kopie = Alle_Spieler.copy()
        global Reihenfolge
        Reihenfolge = []
        #Marienkäfer Extrafunktion
        Marienkäfer_Dict = {}
        for Spieler_ in Alle_Spieler:
            Counter = 0
            Feld_Spieler = Feld[Spieler_]
            for Lr in Feld[Spieler_]:
                for Lw in Feld_Spieler[Lr]:
                    if Lw.Name == "Marienkäfer":
                        Counter += 1
            if not Counter == 0:
                Marienkäfer_Dict.update({Spieler_:Counter})
        Werte = []
        for Spieler_ in Marienkäfer_Dict:
            if not Marienkäfer_Dict[Spieler_] in Werte:
                Werte.append(Marienkäfer_Dict[Spieler_])
        Werte.sort(reverse = True)
        for Wert in Werte:
            Liste = []
            for Spieler_ in Marienkäfer_Dict:
                if Marienkäfer_Dict[Spieler_] == Wert:
                    Liste.append(Spieler_)
            S = random.choice(Liste)
            Reihenfolge.append(S)
            Alle_Spieler_Kopie.remove(S)
        while len(Alle_Spieler_Kopie) > 0:
            Sp = random.choice(Alle_Spieler_Kopie)
            Reihenfolge.append(Sp)
            Alle_Spieler_Kopie.remove(Sp)
        global Spieler
        Spieler = Reihenfolge[0]
    #Screen
    #Linien
    Start_Ende_Auswahl = [[(450, 0), (450, 900)], [(470, 120), (1560, 120)], [(470, 780), (1560, 780)], [(1464, 120), (1464, 780)], [(470, 120), (470, 780)], [(1560, 120), (1560, 780)]]
    for Linie in Start_Ende_Auswahl:
        pg.draw.line(screen, (0, 0, 0), Linie[0], Linie[1], 1)
    #Buttons
    Auswahl_Button_0.create_button()
    Auswahl_Button_1.create_button()
    Auswahl_Button_2.create_button()
    Auswahl_Button_3.create_button()
    Auswahl_Button_4.create_button()
    Auswahl_Button_5.create_button()
    Auswahl_Button_6.create_button()
    Auswahl_Button_7.create_button()
    Auswahl_Button_8.create_button()
    Auswahl_Button_9.create_button()
    Auswahl_Button_10.create_button()
    Auswahl_Button_11.create_button()
    Auswahl_Hoch_Button.create_button()
    Auswahl_Runter_Button.create_button()
    Auswahl_Auswählen_Button.create_button()
    #Auswahl_Erklärung_Button.create_button()
    #Überschrift
    Text = SMaxG("Auswahlstapel", None, 40)
    screen.blit(Text, (450 + (1150 / 2 - Text.get_width() / 2), 10))
    Text = SMaxG(Spieler + ": Wähle eine Karte", None, 30)
    screen.blit(Text, (450 + (1150 / 2 - Text.get_width() / 2), 60))
    Auswahl_Bool = True
    Ausgabe_Auswahl()

Extrakarten_Bool = False
#Extrakarten nach jeder Runde, wenn bestimmte Karten auf Feld
def Extrakarten_Func():
    global Extrakarten_Bool
    Extrakarten = {}
    for Spieler in Alle_Spieler:
        Liste = []
        for Lr in Feld[Spieler]:
            for Lw in Feld[Spieler][Lr]:
                if Lw in Karten.Extrakarten:
                    Liste.append(Lw)
        if not Liste == []:
            Extrakarten.update({Spieler:Liste})
    if Extrakarten == {}:
        Spiel_Screen()
        Vor_Zug(Alle_Spieler[0])
        return
    #Screen front
    Extrakarten_Func_Button.create_button()
    Überschrift = SMaxG("Extrakarten", None, 40)
    screen.blit(Überschrift, (800 - Überschrift.get_width() / 2, 10))
    Surf_Width = 1600 // len(Extrakarten)
    x = 0
    for Spieler in Extrakarten:
        Surf = pg.Surface((Surf_Width, 650))
        Surf.fill((255, 255, 255))
        Spieler_Überschrift = get_Text(Spieler, 50)
        Surf.blit(Spieler_Überschrift, (Surf_Width / 2 - Spieler_Überschrift.get_width() / 2, 10))
        Height = 550 / (len(Extrakarten[Spieler]) + 15)
        for Lw in Extrakarten[Spieler]:
            Neues = random.choice(Karten.Extrakarten[Lw])
            Text = SMaxG(Lw.Name + ": " + Neues.Name, Surf_Width - 20, Height if Height <= 25 else 25)
            if Extrakarten_Bool == False:
                Ablage[Spieler].append(Neues)
            a = 80
            Surf.blit(Text, (Surf_Width / 2 - Text.get_width() / 2, a))
            a += Text.get_height() + 15
        screen.blit(Surf, (x, 100))
        x += Surf_Width
    Extrakarten_Bool = False

def Extrakarten_Ende():
    Extrakarten_Func_Button.delete_button()
    Spiel_Screen()
    Vor_Zug(Alle_Spieler[0])
Extrakarten_Func_Button = Button(pg.Rect(750, 810, 100, 70), Extrakarten_Ende, None, SMaxG("Okay", 90, 60, (255, 255, 255)), None, (76, 117, 28))

def Punktezählen(Spieler):
    return Score
    # Auswertung = {}
    # for Spieler in Alle_Spieler:
    #     Auswertung.update({Spieler:0})
    #     #Verbesserung durch Lr
    #     for Karte in Magisch_Dict[Spieler]:
    #         Magisch_Dict[Spieler][Karte] = 0
    #     for Karte in Stärker_Dict[Spieler]:
    #         Stärker_Dict[Spieler][Karte] = 0
    #     for Lr in Feld_Spieler:
    #         for Lw in Feld_Spieler[Lr]:
    #             if "Magisch" in Lr.Name:
    #                 if Lw in Magisch_Dict[Spieler]:
    #                     Magisch_Dict[Spieler][Lw] += 1
    #                 else:
    #                     Magisch_Dict[Spieler].update({Lw:1})
    #             if Lw in Stärker_LR[Lr.Art]:
    #                 if not Lw in Stärker_Dict[Spieler]:
    #                     Stärker_Dict[Spieler].update({Lw:1})
    #                 else:
    #                     Stärker_Dict[Spieler][Lw] += 1                
    #     #Lebensraum
    #     for Lr in Feld_Spieler:
    #         Auswertung[Spieler] += Lr.Punkte
    #         #Lebewesen darin
    #         for Lw in Feld_Spieler[Lr]:
    #             Ende_Punkte = Lw.Punkte
    #             if Lw in Verbesserung_Spieler:
    #                 Add_Punkte = Verbesserung_Spieler[Lw]["Punkte"]
    #                 if Add_Punkte < 0:
    #                     Add_Punkte = 0
    #                 Ende_Punkte += Add_Punkte
    #                 Verbesserung[Spieler].remove(Lw)
    #             if Lw in Magisch_Dict[Spieler]:
    #                 if Magisch_Dict[Spieler] > 0:
    #                     Ende_Punkte += 1
    #                     Magisch_Dict[Spieler] -= 1
    #             if Lw in Stärker_Dict[Spieler]:
    #                 if Stärker_Dict[Spieler] > 0:
    #                     Ende_Punkte += 2
    #                     Stärker_Dict[Spieler] -= 1
    #             Auswertung[Spieler] += Ende_Punkte
    # #Sortieren
    # Werte = []
    # for Spieler in Auswertung:
    #     if not Auswertung[Spieler] in Werte:
    #         Werte.append(Auswertung[Spieler])
    # Werte.sort(reverse = True)
    # Counter = 0
    # #Ausgeben
    # for Wert in Werte:

#Nach letzter Runde
def Ende():
    Auswertung = {}
    Vor = {}
    Liste = []
    for Spieler in Alle_Spieler:
        Punkte = Punktezählen(Spieler)
        Liste.append(Punkte)
        if not Punkte in Vor:
            Vor.update({Punkte:[Spieler]})
        else:
            Vor[Punkte].append(Spieler)
    Liste.sort(reverse = True)
    for Num in Liste:
        Auswertung.update({Num:Vor[Num]})

        
    #Screen
    screen.fill((255, 255, 255))
    Überschrift = get_Text("Auswertung", 70)
    screen.blit(Überschrift, (800 - Überschrift.get_width() / 2, 50))
    for Num, Wert in enumerate(Auswertung):
        if Num == 0:
            Str = "erster.png"
            Zahl = "1."
        elif Num == 1:
            Str = "zweiter.png"
            Zahl = "2."
        elif Num == 2:
            Str = "dritter.png"
            Zahl = "3."
        else:
            Str = "vierterfünfter.png"
            if Num == 3:
                Zahl = "4."
            else:
                Zahl = "5."
        for Num_, Spieler in enumerate(Auswertung[Wert]):
            Surf = pg.Surface((1300, 100))
            Surf.fill((255, 255, 255))
            Bild = get_image(Str)
            Surf.blit(Bild, (0, 0))
            Text = get_Text(Zahl, 70)
            Surf.blit(Text, (50 - Text.get_width() / 2, 50 - Text.get_height() / 2))
            Dings = str(Wert) + " Punkte" if not Wert == 1 else "1 Punkt"
            Name = get_Text(Spieler + " - " + Dings, 60)
            Surf.blit(Name, (200, 50 - Name.get_height() / 2))
            screen.blit(Surf, (300, 150 + (Num + Num_) * 150))
        
#Events
Spieler_Zug = False #Zug Ende
Aus = True #Ausgabe nach Zugende ja oder nein
Input = False #Input Box Einstellungen
done = False
########Löschen wenn fertig###############
#Spiel()
Ende()
##########################################
while done == False:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Wirklich_Verlassen()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                if not Aktion == None:
                    Clear()
                else:
                    Wirklich_Verlassen()
        elif event.type == pg.MOUSEMOTION:
            for Bttn in Buttons:
                if Bttn.Rect.collidepoint(pg.mouse.get_pos()):
                    Bttn.Maus_Pos = True
                else:
                    Bttn.Maus_Pos = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            for Bttn in Buttons:
                if Bttn.Maus_Pos == True:
                    if Bttn.Switch == True or Bttn.Switch == None:
                        Bttn.Funktion()
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