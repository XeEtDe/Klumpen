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
#Dicts; they work, don't touch
Feld = {}
Ablage = {}
Ende_LW = {} #Kampf für Ende
Drachenei_Dict = {} #Drachenei brüten
#Werte Verbesserungs-Dict
Counter_Dict = {} #Einmal-Sicherung für Ausgabe
Einmal_Dict = {} #Einmal-Sicherung für Add
Verbesserung = {} #{Spieler:{LW_Karte:{"Punkte":xy, "Angriff":xy, "Verteidigung":xy, "Lebensräume":xy}, LR_Karte:{Größe}}
Magisch_Dict = {} #Verbesserung durch magischer Lr
Stärker_Dict = {} #Verbesserung durch Lr
Aussetzen_Dict = {} #Aussetzen
Werteverbesserung_Anzahl = {} #Werteverbesserung - {Karte:[Mögliche, Letzte]}

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
        D = False
        for Wert in Drachenei_Dict[Spieler]:
            Drachenei_Dict[Spieler].remove(Wert)
            Wert -= 1
            Drachenei_Dict[Spieler].append(Wert)
            if Wert == 0:
                Drachenei_Dict[Spieler].remove(Wert)
                for Lr in Feld[Spieler]:
                    for Lw in Feld[Spieler][Lr]:
                        if Lw.Name == "Drachenei":
                            Feld[Spieler][Lr].remove(Lw)
                            Feld[Spieler][Lr].append(Karten.Drache)
                            D = True
                            break
                    if D == True:
                        break
        #Neue Counter für neue Dracheneier
        Counter = 0
        for Lr in Feld[Spieler]:
            for Lw in Feld[Spieler][Lr]:
                if Lw.Name == "Drachenei":
                    Counter += 1
        while Counter > len(Drachenei_Dict[Spieler]):
            Drachenei_Dict[Spieler].append(1)
        #Verbesserung nicht kleiner 0
        Verbesserung[Spieler] = Verbesserung[Spieler]
        for Karte in Verbesserung[Spieler]:
            VB_SP_Ka = Verbesserung[Spieler][Karte]
            if (Karte.Punkte + VB_SP_Ka["Punkte"]) < 0:
                VB_SP_Ka["Punkte"] = 0 - Karte.Punkte
            if (Karte.Angriff + VB_SP_Ka["Angriff"]) < 0:
                VB_SP_Ka["Angriff"] = 0 - Karte.Angriff
            if (Karte.Verteidigung + VB_SP_Ka["Verteidigung"]) < 0:
                VB_SP_Ka["Verteidigung"] = 0 - Karte.Verteidigung
        #Werteverbesserungskarten
        for WV_Karte in Werteverbesserung_Anzahl[Spieler]:
            Jetzt_Anzahl = 0
            for Lr in Feld[Spieler]:
                for Lw in Feld[Spieler][Lr]:
                    if Lw == WV_Karte:
                        if (Lw == Karten.Friedensengel) or (Lw == Karten.Diebische_Elster) or (Lw == Karten.Schreier):
                            Jetzt_Anzahl += 3
                        else:
                            Jetzt_Anzahl += 1
            WV_An_SP_Ka = Werteverbesserung_Anzahl[Spieler][WV_Karte] #Werteverbesserung_Anzahl[Spieler[Karte]] -> [0] = Unverbrauchte/Mögliche, [1] = letzte Anzahl
            WV_An_SP_Ka[0] += (Jetzt_Anzahl - WV_An_SP_Ka[1])
            WV_An_SP_Ka[1] = Jetzt_Anzahl
            if WV_An_SP_Ka[0] < 0:
                WV_An_SP_Ka[0] = 0
            if WV_An_SP_Ka[1] < 0:
                WV_An_SP_Ka[1] = 0
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
                for Lr in Feld[Spieler_]:
                    for Lw in Feld[Spieler_][Lr]:
                        if Lw in Karten.Extrazüge:
                            Liste.append(Lw)
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
    if Aussetzen_Dict[Spieler] > 0:
        Aussetzen_Dict[Spieler] -= 1
        #Buttons
        while len(Buttons) > 0:
            Buttons[0].delete_button()
        #Grafik
        screen.blit(get_image("transparenter_hintergrund.png"), (0, 0))
        pg.draw.rect(screen, (255, 255, 255), pg.Rect(500, 350, 600, 200))
        pg.draw.rect(screen, (0, 0, 0), pg.Rect(500, 350, 600, 200), 3)
        Text = get_Text("Du musst diesen Zug aussetzen", 40)
        screen.blit(Text, (800 - Text.get_width() / 2, 370))
        if Aussetzen_Dict[Spieler] > 0:
            Text = get_Text("Du setzt noch einen weiteren Zug aus" if Aussetzen_Dict[Spieler] == 1 else "Du setzt noch " + str(Aussetzen_Dict[Spieler]) + " Züge aus", 30)
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
    if Spieler[-1] == "s" or Spieler[-1] == "S" or Spieler[-1] == "X" or Spieler[-1] == "x":
        Text = SMaxG(Spieler + "\' Zug", 300, 50)
    else:
        Text = SMaxG(Spieler + "s Zug", 300, 50)
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
            String += Karte.Name + ": + " + str(Karten.Extrazüge[Karte]) + "\n"
            Counter += Karten.Extrazüge[Karte]
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
            for WV_Karte in Werteverbesserung_Anzahl[Spieler_]:
                if not WV_Karte in Karten.Einmal_pro_Spiel:
                    Werteverbesserung_Anzahl[Spieler_][WV_Karte][0] = Werteverbesserung_Anzahl[Spieler_][WV_Karte][1]
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
    Ein_Di_SP = Einmal_Dict[Spieler]
    for Karte in Ein_Di_SP:
        Ein_Di_SP[Karte] = True
    List = None
    if Kategorie == "Ablage":
        List = Ablage[Spieler]
        Alt_Range = Ablage_Alt_Range
        Rects = Karten_Ablage_Rects
    elif Kategorie == "Feld":
        Counter = 0
        for Lr in Feld[Spieler]:
            if Counter == Alt_LR_Pos:
                List = Feld[Spieler][Lr]
                break
            Counter += 1
        Alt_Range = Feld_Alt_Range
        Rects = Karten_Feld_Rects
    elif Kategorie == "Feld_Übersicht":
        List = Feld[Spieler]
        Alt_Range = Feld_Übersicht_Alt_Range
        Rects = Karten_Feld_Übersicht_Rects
    if not List == None:
        Num = Alt_Range[Button_Num]
        if Num <= (len(List) - 1):
            Counter = 0
            for Dings in List:
                if Counter == Num:
                    Karte = Dings
                    break
                Counter += 1
            #Leuchtrand
            Warumeinfachwennsauchkompliziertgeht = {"Ablage":Ablage_Surf, "Feld":Feld_Surf, "Feld_Übersicht":Feld_Übersicht_Surf}
            if Kategorie == "Feld":
                Ausgabe(Spieler, Warumeinfachwennsauchkompliziertgeht[Kategorie], Alt_Range, Alt_LR_Pos)
            else:
                Ausgabe(Spieler, Warumeinfachwennsauchkompliziertgeht[Kategorie], Alt_Range)
            pg.draw.rect(screen, Leuchtrand_Farbe, Rects[Button_Num], 3)
            #Funktionen, Kombi, etc
            if Aktion == "Kombi":
                Extra_List.append(Karte)
                if len(Extra_List) == 1:
                    Info_Text("Kombi:\n" + Karte.Name + " + ?\nWähle eine weitere Karte")
                elif len(Extra_List) == 2:
                    Kombi_Func(Extra_List)
            elif Aktion == "Extrafunktion":
                Extra_List.append(Karte)
                if len(Extra_List) == 1:
                    if Extra_List[0] == Karten.Joker:
                        Info_Text("Wähle eine Kartenart, aus der zufällig eine Startkarte gewählt wird")
                        for Bttn in Joker_Buttons:
                            Bttn.create_button()
                    elif "Gift" in Extra_List[0].Name or Extra_List[0] in Karten.Gegner_Nötig:
                        Info_Text("Wähle einen deiner Gegner")
                        global Gift_Karte
                        Gift_Karte = Extra_List[0]
                        for Bttn in Gegner_Buttons:
                            Bttn.create_button()
                    else:
                        Info_Text("Extrafunktion der Karte: " + Karte.Name + "\nWähle eine Karte, auf die du die Extrafunktion anwenden möchstest")
                elif len(Extra_List) == 2:
                    Extra_Func(Extra_List)
            elif Aktion == "Lebensraum platzieren":
                if Karte in Karten.Alle_Lebensraum:
                    if (not Karte in Feld[Spieler]) and (Karte in Ablage[Spieler]):
                        Ablage[Spieler].remove(Karte)
                        Feld[Spieler].update({Karte:[]})
                        Spieler_Zug = True
                        Clear()
                    else:
                        Info_Text("Du kannst nur einmal denselben Lebensraum auf dem Feld haben und der Lebensraum muss aus der Ablage gewählt werden")
                else:
                    Info_Text("Du kannst nur Lebensräume auf dem Feld platzieren")
            elif Aktion == "Lebewesen bewegen":
                if len(Extra_List) == 0:
                    if Karte in Karten.Alle_Lebewesen:
                        if Kategorie == "Ablage":
                            if Spieler_Zug == True:
                                Info_Text("Du hast deinen Zug bereits gemacht und kannst nur noch Lebewesen innerhalb des Feldes bewegen")
                                Clear()
                            else:
                                Extra_List.append([Karte, "Ablage"])
                                Info_Text("Wähle einen Lebensraum, in dem du das Lebewesen platzieren möchtest: " + Karte.Name)
                        else:
                            Extra_List.append([Karte, "Feld"])
                            Info_Text("Wähle einen Lebensraum, in dem du das Lebewesen platzieren möchtest: " + Karte.Name)
                    else:
                        Info_Text("Du kannst nur Lebewesen bewegen")
                elif len(Extra_List) == 1:
                    if Karte in Karten.Alle_Lebensraum:
                        Extra_List.append(Karte)
                        if Karte in Feld[Spieler]:
                            LR_Karte = Extra_List[1]
                            LW_Karte = Extra_List[0][0]
                            #Größe
                            Voll_Test = False
                            Art_Test = False
                            Alte_LW = Feld[Spieler][LR_Karte]
                            Größe = LR_Karte.Größe
                            if LR_Karte in Ein_Di_SP:
                                if Ein_Di_SP[LR_Karte] == True:
                                    Add_Größe = Verbesserung[Spieler][LR_Karte]
                                    Größe = LR_Karte.Größe + Add_Größe                    
                            if len(Alte_LW) < Größe:
                                Voll_Test = True
                            else:
                                Info_Text("Dieser Lebensraum ist bereits voll")
                            #Art
                            Art_Test = False
                            Zusatz_LR = []
                            if LW_Karte in Ein_Di_SP:
                                if Ein_Di_SP[LW_Karte] == True:
                                    VB_SP_Ka = Verbesserung[Spieler][LW_Karte]
                                    for Lr in VB_SP_Ka["Lebensräume"]:
                                        Zusatz_LR.append(Lr)
                            for Lr in LW_Karte.Lebensraum:
                                if Lr == LR_Karte.Art or Lr == "Alle":
                                    Art_Test = True
                                    break
                            for Lr in Zusatz_LR:
                                if Lr == LR_Karte.Art or Lr == "Alle":
                                    Art_Test = True
                                    break
                            if Art_Test == False:
                                Info_Text("Dieser Lebensraum ist für das Lebewesen nicht geeignet")
                            #Hinzufügen?
                            if Voll_Test == True and Art_Test == True:
                                Feld[Spieler][LR_Karte].append(LW_Karte)
                                if Extra_List[0][1] == "Ablage":
                                    Ablage[Spieler].remove(LW_Karte)
                                    Spieler_Zug = True
                                else:
                                    Counter = 0
                                    for Lr in Feld[Spieler]:
                                        if Counter == Alt_LR_Pos:
                                            Feld[Spieler][Lr].remove[LW_Karte]
                                            break
                                        Counter += 1
                        else:
                            Info_Text("Der Lebensraum muss sich auf dem Feld befinden")
                        Clear()
                    else:
                        Info_Text("Wähle einen Lebensraum")
            #normal Text am Rand ausgeben
            else:
                if Kategorie == "Feld_Übersicht":
                    Ausgabe(Spieler, Feld_Surf, range(0, 6), Num)
                    if Modus == "Punkte":
                        Info_Text(Karte.Name + "\n" + Karte.Beschreibung + "\n" + "Punkte: " + str(Karte.Punkte))
                    else:
                        Info_Text(Karte.Name + "\n" + Karte.Beschreibung)
                else:
                    Info_Text(Karte.Name + "\n" + Karte.Beschreibung)

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
    global Spieler_Zug
    Neue_Karte = False
    Ein_Di_SP = Einmal_Dict[Spieler]
    for Karte in Ein_Di_SP:
        Ein_Di_SP[Karte] = True
    Werteverbesserung_Anzahl[Spieler] = Werteverbesserung_Anzahl[Spieler]
    Verbesserung[Spieler] = Verbesserung[Spieler]
    E_Karte = Karten_Liste[0]
    Andere_Karte = Karten_Liste[1]
    Gesuchte_Kombi_1 = E_Karte.Name + "+" + Andere_Karte.Name
    Gesuchte_Kombi_2 = Andere_Karte.Name + "+" + E_Karte.Name
    #Ort und Besitz?
    Lr_1 = False
    Lr_2 = False
    LR_Neu = False
    #E_Karte
    Ort_1 = False
    for Liste in Feld[Spieler]:
        if E_Karte in Feld[Spieler][Liste]:
            Lr_1 = Liste
            Ort_1 = Feld[Spieler][Liste]
            break
    if Ort_1 == False:
        if E_Karte in Feld[Spieler]:
            Ort_1 = Feld[Spieler]
    if Ort_1 == False:
        if E_Karte in Ablage[Spieler]:
            Ort_1 = Ablage[Spieler]
    #Andere_Karte
    Ort_2 = False
    #Doppelte Karte/Karte 1 = Karte 2
    if E_Karte == Andere_Karte:
        for Liste in Feld[Spieler]:
            if Andere_Karte in Feld[Spieler][Liste]:
                if not Ort_1 == Feld[Spieler][Liste]:
                    Lr_2 = Liste
                    Ort_2 = Feld[Spieler][Liste]
                    break
                else:
                    Counter = 0
                    for Krt in Feld[Spieler][Liste]:
                        if Krt == Andere_Karte:
                            Counter += 1
                    if Counter >= 2:
                        Lr_2 = Liste
                        Ort_2 = Feld[Spieler][Liste]
                        break
        if Ort_2 == False:
            if Andere_Karte in Feld[Spieler]:
                if not Ort_1 == Feld[Spieler]:
                    Ort_2 = Feld[Spieler]
                else:
                    Counter = 0
                    for Krt in Feld[Spieler]:
                        if Krt == Andere_Karte:
                            Counter += 1
                    if Counter >= 2:
                        Ort_2 = Feld[Spieler]
        if Ort_2 == False:
            if Andere_Karte in Ablage[Spieler]:
                if not Ort_1 == Ablage[Spieler]:
                    Ort_2 = Ablage[Spieler]
                else:
                    Counter = 0
                    for Krt in Ablage[Spieler]:
                        if Krt == Andere_Karte:
                            Counter += 1
                    if Counter >= 2:
                        Ort_2 = Ablage[Spieler]
    #Nicht doppelt
    else:
        for Liste in Feld[Spieler]:
            if Andere_Karte in Feld[Spieler][Liste]:
                Lr_2 = Liste
                Ort_2 = Feld[Spieler][Liste]
                break
        if Ort_2 == False:
            if Andere_Karte in Feld[Spieler]:
                Ort_2 = Feld[Spieler]
        if Ort_2 == False:
            if Andere_Karte in Ablage[Spieler]:
                Ort_2 = Ablage[Spieler]
    Counter_Add = 0
    for Karte in Karten.Alle_Karten:
        Counter_Add += 1
        #Kombi
        if Gesuchte_Kombi_1 in Karte.Kombi or Gesuchte_Kombi_2 in Karte.Kombi:
            Neue_Karte = Karte
            #Lr
            if E_Karte in Karten.Alle_Lebensraum or Andere_Karte in Karten.Alle_Lebensraum:
                if E_Karte in Karten.Alle_Lebensraum:
                    LR_Karte = E_Karte
                    Andere_Karte = Andere_Karte
                else:
                    LR_Karte = Andere_Karte
                    Andere_Karte = E_Karte
                #Lr + Lr
                if Andere_Karte in Karten.Alle_Lebensraum:
                    #min. eine Feld
                    if Ort_1 == Feld[Spieler] or Ort_2 == Feld[Spieler]:
                        Neue_LW = []
                        if Ort_1 == Feld[Spieler]:
                            Lw_1 = Feld[Spieler][E_Karte]
                            for Lw in Lw_1:
                                Neue_LW.append(Lw)
                            del Feld[Spieler][E_Karte]
                        else:
                            Ablage[Spieler].remove(E_Karte)
                        if Ort_2 == Feld[Spieler]:
                            Lw_2 = Feld[Spieler][Andere_Karte]
                            for Lw in Lw_2:
                                Neue_LW.append(Lw)
                            del Feld[Spieler][Andere_Karte]
                        else:
                            Ablage[Spieler].remove(Andere_Karte)
                        Feld[Spieler].update({Neue_Karte:[]})
                        if not Neue_LW == []:
                            for Lw in Neue_LW:
                                Feld[Spieler][Neue_Karte].append(Lw)
                        Spieler_Zug = True
                        break
                    #beide Ablage
                    elif Ort_1 == Ablage[Spieler] and Ort_2 == Ablage[Spieler]:
                        Ablage[Spieler].remove(E_Karte)
                        Ablage[Spieler].remove(Andere_Karte)
                        Ablage[Spieler].append(Neue_Karte)
                        Spieler_Zug = True
                        break
                #Lr + E
                elif Andere_Karte in Karten.Alle_Elemente:
                    #Lr in Feld
                    if LR_Karte in Feld[Spieler]:
                        Feld[Spieler].update({Neue_Karte:[]})
                        for Lw in Feld[Spieler][LR_Karte]:
                            Feld[Spieler][Neue_Karte].append(Lw)
                        del Feld[Spieler][LR_Karte]
                        Ablage[Spieler].remove(Andere_Karte)
                        Spieler_Zug = True
                        break
                    #Lr in Ablage
                    elif LR_Karte in Ablage[Spieler]:
                        Ablage[Spieler].remove(E_Karte)
                        Ablage[Spieler].remove(Andere_Karte)
                        Ablage[Spieler].append(Neue_Karte)
                        Spieler_Zug = True
                        break
            #Lw
            elif E_Karte in Karten.Alle_Lebewesen or Andere_Karte in Karten.Alle_Lebewesen:
                if E_Karte in Karten.Alle_Lebewesen:
                    LW_Karte = E_Karte
                    Andere_Karte = Andere_Karte
                else:
                    LW_Karte = Andere_Karte
                    Andere_Karte = E_Karte
                #Lw + Lw
                if Andere_Karte in Karten.Alle_Lebewesen:
                    #beide Ablage oder beide selber Lr
                    if Ort_1 == Ort_2:
                        Ort_1.remove(E_Karte)
                        Ort_2.remove(Andere_Karte)
                        Ort_1.append(Neue_Karte)
                        Spieler_Zug = True
                        break
                    #unterschiedliche LRs
                    else:
                        #Falsch
                        if Lr_1 == False or Lr_2 == False:
                            Info_Text("Du kannst nur innerhalb des Feldes oder der Ablage kombinieren.")
                            break
                        #Ort/geeigneter Lr
                        Fertig = False
                        Lebensräume = []
                        for Lr in Neue_Karte.Lebensraum:
                            Lebensräume.append(Lr)
                        if Neue_Karte in Ein_Di_SP:
                            if Ein_Di_SP[Neue_Karte] == True:
                                VB_SP_Ka = Verbesserung[Spieler][Neue_Karte]
                                for Lr in VB_SP_Ka["Lebensräume"]:
                                    Lebensräume.append(Lr)
                        for Lr in Lebensräume:
                            if Lr == Lr_1.Art or Lr == "Alle":
                                Ort_1.append(Neue_Karte)
                                Ort_1.remove(E_Karte)
                                Ort_2.remove(Andere_Karte)
                                Fertig = True
                                Spieler_Zug = True
                                LR_Neu = Lr_1
                                break
                            elif Lr == Lr_2.Art:
                                Ort_2.append(Neue_Karte)
                                Ort_1.remove(E_Karte)
                                Ort_2.remove(Andere_Karte)
                                Fertig = True
                                Spieler_Zug = True
                                LR_Neu = Lr_2
                                break
                        if Spieler_Zug == True:
                            break
                        if Fertig == False:
                            Info_Text("Keiner der beiden Lebensräume ist geeignet für das neue Lebewesen.")
                            break
                #Lw + E
                elif Andere_Karte in Karten.Alle_Elemente:
                    #in Ablage
                    if LW_Karte in Ablage[Spieler]:
                        Ablage[Spieler].remove(LW_Karte)
                        Ablage[Spieler].remove(Andere_Karte)
                        Ablage[Spieler].append(Neue_Karte)
                        Spieler_Zug = True
                        break
                    #Lw auf Feld/in Lr
                    else:
                        Lebensräume = []
                        for Lr in Neue_Karte.Lebensraum:
                            Lebensräume.append(Lr)
                        if Neue_Karte in Ein_Di_SP:
                            if Ein_Di_SP[Neue_Karte] == True:
                                VB_SP_Ka = Verbesserung[Spieler][Neue_Karte]
                                for Lr in VB_SP_Ka["Lebensräume"]:
                                    Lebensräume.append(Lr)
                        if LW_Karte == E_Karte:
                            for Lr in Lebensräume:
                                if Lr == Lr_1.Art or Lr == "Alle":
                                    Ort_1.append(Neue_Karte)
                                    Ort_1.remove(E_Karte)
                                    Ablage[Spieler].remove(Andere_Karte)
                                    Spieler_Zug = True
                                    LR_Neu = Lr_1
                                    break
                            if Spieler_Zug == False:
                                Info_Text("Der Lebensraum ist nicht geeignet für das neue Lebewesen.")
                                break
                            break
                        elif LW_Karte == Andere_Karte:
                            for Lr in Lebensräume:
                                if Lr == Lr_2.Art or Lr == "Alle":
                                    Ort_2.append(Neue_Karte)
                                    Ort_2.remove(Andere_Karte)
                                    Ablage[Spieler].remove(Andere_Karte)
                                    Spieler_Zug = True
                                    LR_Neu = Lr_2
                                    break
                            if Spieler_Zug == False:
                                Info_Text("Der Lebensraum ist nicht geeignet für das neue Lebewesen.")
                                break
                            break
            #E + E
            elif E_Karte in Karten.Alle_Elemente and Andere_Karte in Karten.Alle_Elemente:
                Ablage[Spieler].append(Neue_Karte)
                Ablage[Spieler].remove(E_Karte)
                Ablage[Spieler].remove(Andere_Karte)
                Spieler_Zug = True
                break
        #Keine Kombi möglich
        elif Counter_Add == len(Karten.Alle_Karten):
            Info_Text("Diese Karten lassen sich nicht kombinieren.")
    #Verbesserungen
    if Spieler_Zug == True:
        Info_Text("Neue Karte: " + Neue_Karte.Name)
        #Weitergabe Verbesserungen
        if Neue_Karte in Karten.Alle_Lebensraum:
            Counter = 0
            if E_Karte in Karten.Alle_Lebensraum and E_Karte in Verbesserung[Spieler]:
                Counter += Verbesserung[Spieler][E_Karte]
                del Verbesserung[Spieler][E_Karte]
            if Andere_Karte in Karten.Alle_Lebensraum and Andere_Karte in Verbesserung[Spieler]:
                Counter += Verbesserung[Spieler][Andere_Karte]
                del Verbesserung[Spieler][E_Karte]
            if not Counter == 0:
                if not Neue_Karte in Verbesserung[Spieler]:
                    Counter_Dict[Spieler].update({Neue_Karte:False})
                    Einmal_Dict[Spieler].update({Neue_Karte:False})
                    Verbesserung[Spieler].update({Neue_Karte:0})
                Verbesserung[Spieler][Neue_Karte] += Counter
        elif Neue_Karte in Karten.Alle_Lebewesen:
            Counter_P = 0
            Counter_A = 0
            Counter_V = 0
            if E_Karte in Karten.Alle_Lebewesen and E_Karte in Verbesserung[Spieler]:
                VB_SP_Ka = Verbesserung[Spieler][E_Karte]
                Counter_P += VB_SP_Ka["Punkte"]
                Counter_A += VB_SP_Ka["Angriff"]
                Counter_V += VB_SP_Ka["Verteidigung"]
                del Verbesserung[Spieler][E_Karte]
            if Andere_Karte in Karten.Alle_Lebewesen and Andere_Karte in Verbesserung[Spieler]:
                VB_SP_Ka = Verbesserung[Spieler][Andere_Karte]
                Counter_P += VB_SP_Ka["Punkte"]
                Counter_A += VB_SP_Ka["Angriff"]
                Counter_V += VB_SP_Ka["Verteidigung"]
                del Verbesserung[Spieler][Andere_Karte]
            if not (Counter_P == 0 and Counter_A == 0 and Counter_V == 0):
                if not Neue_Karte in Verbesserung[Spieler]:
                    Counter_Dict[Spieler].update({Neue_Karte:False})
                    Einmal_Dict[Spieler].update({Neue_Karte:False})
                    Verbesserung[Spieler].update({Neue_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                VB_SP_Ka = Verbesserung[Spieler][Neue_Karte]
                VB_SP_Ka["Punkte"] += Counter_P
                VB_SP_Ka["Angriff"] += Counter_A
                VB_SP_Ka["Verteidigung"] += Counter_V
    Clear(False)

def Extra_Func(Liste):
    global Spieler_Zug
    Neue_Karte = False
    Ein_Di_SP = Einmal_Dict[Spieler]
    for Karte in Ein_Di_SP:
        Ein_Di_SP[Karte] = True
    E_Karte = Liste[0]
    Dings = Liste[1]
    Andere_Karte = None
    for Karte in Karten.Alle_Karten:
        if Dings == Karte:
            Andere_Karte = Karte
            break
    #Ort und Besitz?
    Lr_1 = False
    Lr_2 = False
    LR_Neu = False
    #E_Karte
    Ort_1 = False
    for Liste in Feld[Spieler]:
        if E_Karte in Feld[Spieler][Liste]:
            Lr_1 = Liste
            Ort_1 = Feld[Spieler][Liste]
            break
    if Ort_1 == False:
        if E_Karte in Feld[Spieler]:
            Ort_1 = Feld[Spieler]
    if Ort_1 == False:
        if E_Karte in Ablage[Spieler]:
            Ort_1 = Ablage[Spieler]
    Ort = Ort_1
    if not Andere_Karte == None:
        #Andere_Karte
        Ort_2 = False
        #Doppelte Karte/Karte 1 = Karte 2
        if E_Karte == Andere_Karte:
            for Liste in Feld[Spieler]:
                if Andere_Karte in Feld[Spieler][Liste]:
                    if not Ort_1 == Feld[Spieler][Liste]:
                        Lr_2 = Liste
                        Ort_2 = Feld[Spieler][Liste]
                        break
                    else:
                        Counter = 0
                        for Krt in Feld[Spieler][Liste]:
                            if Krt == Andere_Karte:
                                Counter += 1
                        if Counter >= 2:
                            Lr_2 = Liste
                            Ort_2 = Feld[Spieler][Liste]
                            break
            if Ort_2 == False:
                if Andere_Karte in Feld[Spieler]:
                    if not Ort_1 == Feld[Spieler]:
                        Ort_2 = Feld[Spieler]
                    else:
                        Counter = 0
                        for Krt in Feld[Spieler]:
                            if Krt == Andere_Karte:
                                Counter += 1
                        if Counter >= 2:
                            Ort_2 = Feld[Spieler]
            if Ort_2 == False:
                if Andere_Karte in Ablage[Spieler]:
                    if not Ort_1 == Ablage[Spieler]:
                        Ort_2 = Ablage[Spieler]
                    else:
                        Counter = 0
                        for Krt in Ablage[Spieler]:
                            if Krt == Andere_Karte:
                                Counter += 1
                        if Counter >= 2:
                            Ort_2 = Ablage[Spieler]
        #Nicht doppelt
        else:
            for Liste in Feld[Spieler]:
                if Andere_Karte in Feld[Spieler][Liste]:
                    Lr_2 = Liste
                    Ort_2 = Feld[Spieler][Liste]
                    break
            if Ort_2 == False:
                if Andere_Karte in Feld[Spieler]:
                    Ort_2 = Feld[Spieler]
            if Ort_2 == False:
                if Andere_Karte in Ablage[Spieler]:
                    Ort_2 = Ablage[Spieler]
        Anderer_Ort = Ort_2
        Anderer_LR = Lr_2
    else:
        Andere_Karte = Dings
    #Start#
    if E_Karte in Werteverbesserung_Anzahl[Spieler]:
        WV_An_SP_Ka = Werteverbesserung_Anzahl[Spieler][E_Karte]
    #Tränke
    if "Trank" in E_Karte.Name:
        #Lebensraum-Tränke
        if "Lebensraum" in E_Karte.Beschreibung or E_Karte == Karten.Duftender_Trank:
            if Andere_Karte in Karten.Alle_Lebensraum:
                #Vergrößerungs-Trank
                if E_Karte == Karten.Vergrößerungs-Trank:
                    if not Andere_Karte in Verbesserung[Spieler]:
                        Counter_Dict[Spieler].update({Andere_Karte:False})
                        Einmal_Dict[Spieler].update({Andere_Karte:False})
                        Verbesserung[Spieler].update({Andere_Karte:0})
                    Verbesserung[Spieler][Andere_Karte] += 1
                    Spieler_Zug = True
                    Ablage[Spieler].remove(E_Karte)
                    Info_Text("Größe des Lebensraums " + Karte.Name + " um 1 verbessert")
                #Duftender Trank
                elif E_Karte == Karten.Duftender_Trank:
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
                        Feld[Spieler].update({Neue_Karte:[]})
                        for Lw in Feld[Spieler][Andere_Karte]:
                            Feld[Spieler][Neue_Karte].append(Lw)
                        del Feld[Spieler][Andere_Karte]
                    elif Andere_Karte in Ablage[Spieler]:
                        Ablage[Spieler].append(Neue_Karte)
                        Ablage[Spieler].remove(Andere_Karte)
                    Spieler_Zug = True
                    Ablage[Spieler].remove(E_Karte)
                    Info_Text(Andere_Karte.Name + " durch " + Neue_Karte.Name + " ersetzt")
            else:
                Info_Text("Du kannst diesen Trank nur auf Lebensräume anwenden.")
        #Lebewesen-Tränke     
        elif "Lebewesen" in E_Karte.Beschreibung:
            if Andere_Karte in Karten.Alle_Lebewesen:
                Mehr_LRs_Tränke = {Karten.Heißer_Trank:"Wüste", Karten.Wässriger_Trank:"See", Karten.Matschiger_Trank:"Wald", Karten.Blubbernder_Trank:"Berge", Karten.Verkohlter_Trank:"Alle"}
                Werte_Tränke = {Karten.Güldener_Trank:3, Karten.Level_Up_Trank:5, Karten.Glitzernder_Trank:7, Karten.Himmlischer_Trank:10}
                #Mehr Lr Tränke
                if E_Karte in Mehr_LRs_Tränke:
                    Lr = Mehr_LRs_Tränke[E_Karte]
                    if not Andere_Karte in Verbesserung[Spieler]:
                        Counter_Dict[Spieler].update({Andere_Karte:False})
                        Einmal_Dict[Spieler].update({Andere_Karte:False})
                        Verbesserung[Spieler].update({Andere_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                    VB_SP_Ka = Verbesserung[Spieler][Andere_Karte]
                    if not Lr in VB_SP_Ka["Lebensräume"]:
                        VB_SP_Ka["Lebensräume"].append(Lr)
                    Spieler_Zug = True
                    Ablage[Spieler].remove(E_Karte)
                    if Lr == "Alle":
                        Lr = "Alle Lebensräume"
                    Info_Text(Andere_Karte.Name + " kann jetzt hier leben: " + Lr)
                #Werte Tränke
                elif E_Karte in Werte_Tränke:
                    Wert = Werte_Tränke[E_Karte]
                    if not Andere_Karte in Verbesserung[Spieler]:
                        Counter_Dict[Spieler].update({Andere_Karte:False})
                        Einmal_Dict[Spieler].update({Andere_Karte:False})
                        Verbesserung[Spieler].update({Andere_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                    VB_SP_Ka = Verbesserung[Spieler][Andere_Karte]
                    VB_SP_Ka["Punkte"] += Wert
                    VB_SP_Ka["Angriff"] += Wert
                    VB_SP_Ka["Verteidigung"] += Wert
                    Spieler_Zug = True
                    Ablage[Spieler].remove(E_Karte)
                    Info_Text("Alle Werte der Karte " + Andere_Karte.Name + " um " + str(Wert) + " verbessert")
                #Dolly Trank
                elif E_Karte.Name == "Dolly Trank":
                    Ablage[Spieler].append(Andere_Karte)
                    Spieler_Zug = True
                    Ablage[Spieler].remove(E_Karte)
                    Info_Text("Neue Karte: " + Andere_Karte.Name)
            else:
                Info_Text("Du kannst diesen Trank nur auf Lebenwesen anwenden.")
    #Parasit
    elif E_Karte == Karten.Parasit:
        if Andere_Karte in Karten.Alle_Lebewesen:
            if WV_An_SP_Ka[0] > 0:
                Punkte = Andere_Karte.Punkte
                Angriff = Andere_Karte.Angriff
                Verteidigung = Andere_Karte.Verteidigung
                if Andere_Karte in Verbesserung[Spieler]:
                    Punkte += Verbesserung[Spieler][Andere_Karte]["Punkte"]
                    Angriff += Verbesserung[Spieler][Andere_Karte]["Angriff"]
                    Verteidigung += Verbesserung[Spieler][Andere_Karte]["Verteidigung"]
                else:
                    Counter_Dict[Spieler].update({Andere_Karte:False})
                    Einmal_Dict[Spieler].update({Andere_Karte:False})
                    Verbesserung[Spieler].update({Andere_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                if not E_Karte in Verbesserung[Spieler]:
                    Counter_Dict[Spieler].update({E_Karte:False})
                    Einmal_Dict[Spieler].update({E_Karte:False})
                    Verbesserung[Spieler].update({E_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                VB_SP_Ka = Verbesserung[Spieler][E_Karte]
                VB_SP_Ka["Punkte"] += Punkte
                VB_SP_Ka["Angriff"] += Angriff
                VB_SP_Ka["Verteidigung"] += Verteidigung                    
                VB_SP_Ka = Verbesserung[Spieler][Andere_Karte]
                VB_SP_Ka["Punkte"] -= 4
                VB_SP_Ka["Angriff"] -= 4
                VB_SP_Ka["Verteidigung"] -= 4
                WV_An_SP_Ka[0] -= 1
                Spieler_Zug = True
                Info_Text("Parasit um die Werte von der Karte " + Andere_Karte.Name + " verbessert, " + Andere_Karte.Name + "um 4 verschlechtert")
            else:
                Info_Text("Fähigkeit kann nur einmal angewandt werden, Parasit muss auf dem Feld platziert sein.")
        else:
            Info_Text("Kann nur die Werte von Lebewesen aufnehmen.")
    #Werteverbesserungskarte
    elif E_Karte in Karten.Werteverbesserung_Übersicht:
        if Andere_Karte in Karten.Alle_Lebewesen:
            if WV_An_SP_Ka[0] > 0:
                if not Andere_Karte in Verbesserung[Spieler]:
                    Counter_Dict[Spieler].update({Andere_Karte:False})
                    Einmal_Dict[Spieler].update({Andere_Karte:False})
                    Verbesserung[Spieler].update({Andere_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                VB_SP_Ka = Verbesserung[Spieler][Andere_Karte]
                Wert = Karten.Werteverbesserung_Übersicht[E_Karte]
                VB_SP_Ka["Punkte"] += Wert
                VB_SP_Ka["Angriff"] += Wert
                VB_SP_Ka["Verteidigung"] += Wert
                WV_An_SP_Ka[0] -= 1
                Spieler_Zug = True
                Info_Text("Alle Werte der Karte " + Andere_Karte.Name + " um " + str(Wert) + "verbessert")
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
                for Lr in Andere_Karte.Lebensraum:
                    Gesamt_LRs.append(Lr)
                if Andere_Karte in Verbesserung[Spieler]:
                    VB_SP_Ka = Verbesserung[Spieler][Andere_Karte]
                    for Lr in VB_SP_Ka["Lebensräume"]:
                        Gesamt_LRs.append(Lr)
                if "Alle" in Gesamt_LRs:
                    Info_Text("Dieses Lebewesen kann bereits in allen Lebensräumen leben.")
                else:
                    #Zufall
                    Spieler_Zug = True
                    if ExtraLRs[E_Karte] == "Zufall":
                        LRs_Kopie = Karten.LRs.copy()
                        for Lr in Gesamt_LRs:
                            if not Lr == "Wonderland":
                                LRs_Kopie.remove(Lr)
                        Neu = random.choice(LRs_Kopie)
                    else:
                        Neu = ExtraLRs[E_Karte]
                    if not Andere_Karte in Verbesserung[Spieler]:
                        Counter_Dict[Spieler].update({Andere_Karte:False})
                        Einmal_Dict[Spieler].update({Andere_Karte:False})
                        Verbesserung[Spieler].update({Andere_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                    VB_SP_Ka = Verbesserung[Spieler][Andere_Karte]
                    VB_SP_Ka["Lebensräume"].append(Neu)
                    Test_Liste = []
                    for Lr in Andere_Karte.Lebensraum:
                        if not Lr == "Wonderland":
                            Test_Liste.append(Lr)
                    for Lr in VB_SP_Ka["Lebensräume"]:
                        Test_Liste.append(Lr)
                    if len(Test_Liste) >= 4:
                        VB_SP_Ka["Lebensräume"] = ["Alle"]
                        Neu = "Alle Lebensräume"
                    if Neu == "Alle":
                        Neu = "Alle Lebensräume"                    
                    Info_Text("Die Karte " + Andere_Karte.Name + " kann jetzt hier leben: " + Neu)
            else:
                Info_Text("Platziere Lebewesen auf dem Feld, um ihre Extrafunktion zu nutzen.")
        else:
            Info_Text("Kann nur auf Lebewesen angewandt werden.")
    #Friedensengel
    elif E_Karte == Karten.Friedensengel:
        if Andere_Karte in Karten.Alle_Lebensraum:
            if WV_An_SP_Ka[0] > 0:
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
                    Feld[Spieler].update({Neue_Karte:[]})
                    for Lw in Feld[Spieler][Andere_Karte]:
                        Feld[Spieler][Neue_Karte].append(Lw)
                    del Feld[Spieler][Andere_Karte]
                elif Andere_Karte in Ablage[Spieler]:
                    Ablage[Spieler].append(Neue_Karte)
                    Ablage[Spieler].remove(Andere_Karte)
                Spieler_Zug = True
                WV_An_SP_Ka[0] -= 1
                Info_Text("Lebensraum " + Andere_Karte.Name + " durch " + Neue_Karte.Name + " ersetzt")
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
                Ablage[Spieler].append(Neue_Karte)
                Ablage[Spieler].remove(Andere_Karte)
                Spieler_Zug = True
                Info_Text("Neue Karte: " + Neue_Karte.Name)
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
                Ablage[Spieler].append(Neue_Karte)
                Ablage[Spieler].remove(Andere_Karte)
                Spieler_Zug = True
                Info_Text("Neue Karte: " + Neue_Karte.Name)
            else:
                Info_Text("Platziere den Dunklen Magier im Feld um seine Funktion zu nutzen.")
        else:
            Info_Text("Dunkler Magier kann nur Elemente in Gifte verwandeln.")
    #Urwolf
    elif E_Karte == Karten.Urwolf:
        if Andere_Karte in Karten.Alle_Lebewesen:
            if WV_An_SP_Ka[0] > 0:
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
                    if Andere_Karte in Verbesserung[Spieler]:
                        if not Werwolf in Verbesserung[Spieler]:
                            Counter_Dict[Spieler].update({Werwolf:False})
                            Einmal_Dict[Spieler].update({Werwolf:False})
                            Verbesserung[Spieler].update({Werwolf:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                        VB_SP_Ka = Verbesserung[Spieler][Werwolf]
                        VB_SP_Ka["Punkte"] += Werteverbesserung_Übersicht[Andere_Karte]
                        VB_SP_Ka["Angriff"] += Werteverbesserung_Übersicht[Andere_Karte]
                        VB_SP_Ka["Verteidigung"] += Werteverbesserung_Übersicht[Andere_Karte]
                        del Verbesserung[Spieler][Andere_Karte]
                    Spieler_Zug = True
                    WV_An_SP_Ka[0] -= 1
                    Info_Text(Andere_Karte.Name + "in Werwolf verwandelt")
            else:
                Info_Text("Kann nur einmal im Spiel angewandt werden, Karte muss auf dem Feld platziert sein.")
        else:
            Info_Text("Kann nur auf Lebewesen angewandt werden.")
    #Joker
    elif E_Karte == Karten.Joker:
        if WV_An_SP_Ka[0] > 0:
            Neue_Karte = None
            if Andere_Karte == "Lw":
                Neue_Karte = random.choice(Karten.Start_Lebewesen)
            elif Andere_Karte == "Lr":
                Neue_Karte = random.choice(Karten.Start_Lebensraum)
            elif Andere_Karte == "E":
                Neue_Karte = random.choice(Karten.Start_Elemente)
            Ablage[Spieler].append(Neue_Karte)
            Spieler_Zug = True
            WV_An_SP_Ka[0] -= 1
            Info_Text("Neue Karte: " + Neue_Karte.Name)
        else:
            Info_Text("Kann nur einmal pro Runde angewandt werden, Karte muss auf dem Feld platziert sein.")
    #Gifte bzw Gefrorener Trank oder Diebische Elster
    elif "Gift" in E_Karte.Name or E_Karte == Karten.Gefrorener_Trank or E_Karte == Karten.Schwarzer_Trank or E_Karte == Karten.Diebische_Elster:
        Werte_Gifte = {Karten.Elementares_Gift:3, Karten.Pampiges_Gift:5, Karten.Schwarzer_Trank:5, Karten.Trügerisches_Gift:7, Karten.Blutiges_Gift:10}
        Aussetzen_Gifte = {Karten.Magisches_Gift:1, Karten.Lähmendes_Gift:3, Karten.Gefrorener_Trank:3, Karten.Eisiges_Gift:5}
        Zerstörungs_Gifte = [Karten.Reines_Gift, Karten.Gift_des_Vergessens]
        Gegner = Andere_Karte
        #Werte Gifte
        if E_Karte in Werte_Gifte:
            #Lw zufällig wählen
            Gegner_LW = []
            for Lw in Ablage[Gegner]:
                if Lw in Karten.Alle_Lebewesen:
                    Gegner_LW.append(Lw)
            for Lr in Feld[Gegner]:
                for Lw in Feld[Gegner][Lr]:
                    Gegner_LW.append(Lw)
            Gewähltes_Lw = random.choice(Gegner_LW)
            #Werte verschlechtern
            if not Gewähltes_Lw in Verbesserung[Gegner]:
                Counter_Dict[Gegner].update({Gewähltes_Lw:False})
                Einmal_Dict[Gegner].update({Gewähltes_Lw:False})
                Verbesserung[Gegner].update({Gewähltes_Lw:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
            Verbesserung[Gegner][Gewähltes_Lw]["Punkte"] -= Werte_Gifte[E_Karte]
            Verbesserung[Gegner][Gewähltes_Lw]["Angriff"] -= Werte_Gifte[E_Karte]
            Verbesserung[Gegner][Gewähltes_Lw]["Verteidigung"] -= Werte_Gifte[E_Karte]
            Spieler_Zug = True
            Ablage[Spieler].remove(E_Karte)
            Info_Text("Die Karte " + Gewähltes_Lw.Name + " des Spielers " + Gegner + " um " + str(Werte_Gifte[E_Karte]) + " verschlechtert")
        #Aussetzen Gifte
        elif E_Karte in Aussetzen_Gifte:
            Aussetzen_Dict[Gegner] += Aussetzen_Gifte[E_Karte]
            Ablage[Spieler].remove(E_Karte)
            Spieler_Zug = True
            Info_Text(Gegner + " setzt " + "einen Zug" if Aussetzen_Gifte[E_Karte] == 1 else (str(Aussetzen_Gifte[E_Karte]) + " Züge") + " aus")
        #Zerstörungs Gifte
        elif E_Karte in Zerstörungs_Gifte or E_Karte == Karten.Diebische_Elster:
            #Lebewesen nach Werten (Punkten) ordnen
            for Lw in Einmal_Dict[Gegner]:
                Einmal_Dict[Gegner][Lw] = True
            Gegner_LW = {}
            Werte_Liste = []
            Listen = [Ablage[Gegner]]
            for Lr in Feld[Gegner]:
                Listen.append([Feld][Gegner][Lr])
            for Liste in Listen:
                for Lw in Listen:
                    if Lw in Karten.Alle_Lebewesen:
                        Wert = Lw.Punkte
                        if Lw in Verbesserung[Gegner]:
                            if Einmal_Dict[Gegner][Lw] == True:
                                Einmal_Dict[Gegner][Lw] = False
                                Wert = Lw.Punkte + Verbesserung[Gegner][Lw]["Punkte"]
                        if Wert in Gegner_LW:
                            Gegner_LW[Wert].append(Lw)
                        else:
                            Gegner_LW.update({Wert:[Lw]})
                            Werte_Liste.append(Wert)
            if Gegner_LW == {}:
                Info_Text("Dieser Gegner besitzt keine Lebewesen")
                Clear(False)
                return
            #Lebewesen für Trank auswählen
            Werte_Liste.sort()
            if E_Karte == Karten.Reines_Gift or E_Karte == Karten.Diebische_Elster:
                Löschen_Karte = random.choice(Gegner_LW[Werte_Liste[0]])
            elif E_Karte == Karten.Gift_des_Vergessens:
                Löschen_Karte = random.choice(Gegner_LW[Werte_Liste[-1]])
            #Ort finden
            if Löschen_Karte in Ablage[Gegner]:
                Ort = Ablage[Gegner]
            else:
                for Lr in Feld[Gegner]:
                    if Löschen_Karte in Feld[Gegner][Lr]:
                        Ort = Feld[Gegner][Lr]
                        break
            #Ausführen
            if E_Karte in Zerstörungs_Gifte:
                Ort.remove(Löschen_Karte)
                Ablage[Spieler].remove(E_Karte)
                Spieler_Zug = True
                Info_Text("Lebewesen " + Löschen_Karte.Name + " des Spielers " + Gegner + " wurde zerstört")
            elif E_Karte == Karten.Diebische_Elster:
                if WV_An_SP_Ka[0] > 0:
                    Ort.remove(Löschen_Karte)
                    Ablage[Spieler].append(Löschen_Karte)
                    if Löschen_Karte in Verbesserung[Gegner]:
                        if not Löschen_Karte in Verbesserung[Spieler]:
                            Counter_Dict[Spieler].update({Löschen_Karte:False})
                            Einmal_Dict[Spieler].update({Löschen_Karte:False})
                            Verbesserung[Spieler].update({Löschen_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                        Verbesserung[Spieler][Löschen_Karte]["Punkte"] += Verbesserung[Gegner][Löschen_Karte]["Punkte"]
                        Verbesserung[Spieler][Löschen_Karte]["Angriff"] += Verbesserung[Gegner][Löschen_Karte]["Angriff"]
                        Verbesserung[Spieler][Löschen_Karte]["Verteidigung"] += Verbesserung[Gegner][Löschen_Karte]["Verteidigung"]
                        for Lr in Verbesserung[Gegner][Löschen_Karte]["Lebensräume"]:
                            Verbesserung[Spieler][Löschen_Karte]["Lebensräume"].append(Lr)
                        del Verbesserung[Gegner][Löschen_Karte]
                        del Counter_Dict[Gegner][Löschen_Karte]
                        del Einmal_Dict[Gegner][Löschen_Karte]
                        Spieler_Zug = True
                        WV_An_SP_Ka[0] -= 1
                        Info_Text("Lebewesen " + Löschen_Karte.Name + " vom Spieler " + Gegner + " gestohlen")
                else:
                    Info_Text("Fähigkeit kann nur 3 Mal angewandt werden, Diebische Elster muss auf dem Feld platziert sein.")
    #Aussetzen
    elif E_Karte in Karten.Aussetzen_Karten:
        if WV_An_SP_Ka[0] > 0:
            Gegner = Andere_Karte
            Wert = Karten.Aussetzen_Karten[E_Karte]
            Aussetzen_Dict[Gegner] += Wert
            Str = "einen Zug" if Wert == 1 else str(Wert) + " Züge"         
            Spieler_Zug = True
            WV_An_SP_Ka[0] -= 1
            Info_Text(Gegner + " setzt " + Str + " aus")
        else:
            Info_Text("Extrafunktion kann nur einmal pro Runde angewandt werden, Karte muss auf dem Feld platziert sein")
    #Lebensraum vergrößern
    elif E_Karte in Karten.Lr_Vergrößern:
        if WV_An_SP_Ka[0] > 0:
            if Andere_Karte in Karten.Alle_Lebensraum:
                if not Andere_Karte in Verbesserung[Spieler]:
                    Counter_Dict[Spieler].update({Andere_Karte:False})
                    Einmal_Dict[Spieler].update({Andere_Karte:False})
                    Verbesserung[Spieler].update({Andere_Karte:0})
                Verbesserung[Spieler][Andere_Karte] += Karten.Lr_Vergrößern[E_Karte]
                Spieler_Zug = True
                WV_An_SP_Ka[0] -= 1
                Info_Text("Größe des Lebensraums " + Andere_Karte.Name + " um " + str(Karten.Lr_Vergrößern[E_Karte]) + " verbessert")
            else:
                Info_Text("Kann nur auf Lebensräume angewandt werden")
        else:
            Info_Text("Extrafunktion kann nur einmal pro Runde angewandt werden, Karte muss auf dem Feld platziert sein")
    #Goldstück oder Goldkessel von Verrückter Gnom bzw. Kobold
    elif E_Karte == Karten.Goldstück or E_Karte == Karten.Kessel_voller_Gold:
        if Andere_Karte in Karten.Alle_Lebewesen:
            if E_Karte == Karten.Goldstück:
                Wert = 3
            else:
                Wert = 5
            if not Andere_Karte in Verbesserung[Spieler]:
                Counter_Dict[Spieler].update({Andere_Karte:False})
                Einmal_Dict[Spieler].update({Andere_Karte:False})
                Verbesserung[Spieler].update({Andere_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
            VB_SP_Ka = Verbesserung[Spieler][Andere_Karte]
            VB_SP_Ka["Punkte"] += Wert
            VB_SP_Ka["Angriff"] += Wert
            VB_SP_Ka["Verteidigung"] += Wert
            Spieler_Zug = True
            Ablage[Spieler].remove(E_Karte)
            Info_Text("Lebewesen " + Andere_Karte.Name + " um " + str(Wert) + " verbessert")
        elif Andere_Karte in Karten.Alle_Lebensraum:
            if E_Karte == Karten.Goldstück:
                Wert = 1
            else:
                Wert = 3
            if not Andere_Karte in Verbesserung[Spieler]:
                Counter_Dict[Spieler].update({Andere_Karte:False})
                Einmal_Dict[Spieler].update({Andere_Karte:False})
                Verbesserung[Spieler].update({Andere_Karte:0})
            Verbesserung[Spieler][Andere_Karte] += Wert
            Spieler_Zug = True
            Ablage[Spieler].remove(E_Karte)
            Info_Text("Lebensraum " + Andere_Karte.Name + " um " + str(Wert) + " verbessert")
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
        return SMaxG(Alle_Spieler[Num], 110, 45)
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
    Coun_Di_SP = Counter_Dict[Spieler]
    Surf.fill((255, 255, 255))
    global Feld_Übersicht_Alt_Range
    if Surf == Ablage_Surf or Surf == Feld_Surf:
        #Ablage
        if Surf == Ablage_Surf:
            y_Surf = 482
            x_Surf = 452
            List = Ablage[Spieler]
            #für Buttons
            global Ablage_Alt_Range
            Ablage_Alt_Range = Range
            #Ausgabe von Verbesserungen, alt
            for Karte in Coun_Di_SP:
                Coun_Di_SP[Karte] = False
                Test = True
                for Lr in Feld[Spieler]:
                    if Karte == Lr or Karte in Feld[Spieler][Lr]:
                        Test = False
                if Test == True and Karte in Ablage[Spieler]:
                    Coun_Di_SP[Karte] = True
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
            Num = Feld_Übersicht_Alt_Range[LR_Pos]
            Counter = 0
            for Key in Feld[Spieler]:
                if Counter == Num:
                    Lr = Key
                    break
                Counter += 1
            List = Feld[Spieler][Lr]
            #für Buttons
            global Feld_Alt_Range
            Feld_Alt_Range = Range
            global Alt_LR_Pos
            Alt_LR_Pos = LR_Pos
            #Ausgabe von Verbesserung, dont touch
            #Couter, Magisch, Stärker Dicts
            Coun_Di_SP = Counter_Dict[Spieler]
            Magi_Di_SP = Magisch_Dict[Spieler]
            Stä_Di_SP = Stärker_Dict[Spieler]
            for Karte in Coun_Di_SP:
                Coun_Di_SP[Karte] = False
                for Lr in Feld[Spieler]:
                    if Karte == Lr or Karte in Feld[Spieler][Lr]:
                        Coun_Di_SP[Karte] = True
            for Karte in Magi_Di_SP:
                Magi_Di_SP[Karte] = 0
            for Karte in Stä_Di_SP:
                Stä_Di_SP[Karte] = 0
            for Lr in Feld[Spieler]:
                for Lw in Feld[Spieler][Lr]:
                    if "Magisch" in Lr.Name:
                        if Lw in Magi_Di_SP:
                            Magi_Di_SP[Lw] += 1
                        else:
                            Magi_Di_SP.update({Lw:1})
                    if Lw in Karten.Stärker_LR[Lr.Art]:
                        if not Lw in Stä_Di_SP:
                            Stä_Di_SP.update({Lw:1})
                        else:
                            Stä_Di_SP[Lw] += 1
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
        Sortieren(List)
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
        Feld_Übersicht_Alt_Range = Range
        Range_1 = range(Range[0], Range[0] + 8)
        #Surface zusammensetzen
        Dings_a = 90
        Dings = pg.Surface((Dings_a, 42))
        y = 4
        x = 35
        for Num in Range_1:
            if len(Feld[Spieler]) >= (Num + 1):
                Counter = 0
                for Key in Feld[Spieler]:
                    if Counter == Num:
                        Lr = Key
                        break
                    Counter += 1
                Mod_Größe = Lr.Größe
                if Lr in Coun_Di_SP:
                    Verbesserung[Spieler] = Verbesserung[Spieler]
                    Verbesserung_Karte = Verbesserung[Spieler][Lr]
                    Add_Größe = Verbesserung_Karte
                    Mod_Größe = Lr.Größe + Add_Größe
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
                Inside = SMaxG(str(len(Feld[Spieler][Lr])) + " / " + str(Mod_Größe), Dings_a, 19)
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
def Druck(Karte, Spieler, Auswahl = False):
    if Auswahl == False:
        Coun_Di_SP = Counter_Dict[Spieler]
        Magi_Di_SP = Magisch_Dict[Spieler]
        Stä_Di_SP = Stärker_Dict[Spieler]
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
        #altes repr, dont touch (yeah I did now)
        Mod_Punkte = Karte.Punkte
        Mod_Angriff = Karte.Angriff
        Mod_Verteidigung = Karte.Verteidigung
        Mod_Lebensraum_ = []
        for Lr in Karte.Lebensraum:
            if not Lr == "Wonderland":
                Mod_Lebensraum_.append(Lr)
        Mod_Lebensraum = ""
        for Lr in Mod_Lebensraum_:
            Mod_Lebensraum = Mod_Lebensraum + Lr + ", "
        Mod_Lebensraum = Mod_Lebensraum.strip(", ")
        if Auswahl == False:
            if Karte in Coun_Di_SP:
                if Coun_Di_SP[Karte] == True:
                    Verbesserung[Spieler] = Verbesserung[Spieler]
                    Verbesserung_Karte = Verbesserung[Spieler][Karte]
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
                    for Lr in Verbesserung_Karte["Lebensräume"]:
                        if not Lr in Mod_Lebensraum_:
                            Mod_Lebensraum_.append(Lr)
                    if "Alle" in Mod_Lebensraum_:
                        Mod_Lebensraum = "Alle"
                    else:
                        Mod_Lebensraum = ""
                        for Lr in Mod_Lebensraum_:
                            Mod_Lebensraum = Mod_Lebensraum + Lr + ", "
                        Mod_Lebensraum = Mod_Lebensraum.strip(", ")
                    Coun_Di_SP[Karte] = False
            if Karte in Magisch_Dict[Spieler]:
                if Magi_Di_SP[Karte] > 0:
                    Mod_Angriff += 1
                    Mod_Verteidigung += 1
                    Mod_Punkte += 1
                    Magi_Di_SP[Karte] -= 1
            if Karte in Stärker_Dict[Spieler]:
                if Stä_Di_SP[Karte] > 0:
                    Mod_Angriff += 2
                    Mod_Verteidigung += 2
                    Mod_Punkte += 2
                    Stä_Di_SP[Karte] -= 1
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
        #altes repr, dont touch (I did it again)
        Mod_Größe = Karte.Größe
        if Auswahl == False:
            if Karte in Coun_Di_SP:
                if Coun_Di_SP[Karte] == True:
                    Verbesserung[Spieler] = Verbesserung[Spieler]
                    Verbesserung_Karte = Verbesserung[Spieler][Karte]
                    Add_Größe = Verbesserung_Karte
                    Mod_Größe = Karte.Größe + Add_Größe
                    Coun_Di_SP[Karte] = False
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
    if Spieler[-1] == "s" or Spieler[-1] == "S" or Spieler[-1] == "X" or Spieler[-1] == "x":
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
        Ablage.update({Spieler:[Karten.Zeitfee]})
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
        Aussetzen_Dict.update({Spieler:0})
        Werteverbesserung_Anzahl.update({Spieler:{Karten.Parasit:[0, 0],
                                                  Karten.Friedensengel:[0, 0],
                                                  Karten.Diebische_Elster:[0, 0],
                                                  Karten.Joker:[0, 0],
                                                  Karten.Urwolf:[0, 0]}})
        for Karte in Karten.Werteverbesserung_Übersicht:
            Werteverbesserung_Anzahl[Spieler].update({Karte:[0, 0]})
        for Karte in Karten.Aussetzen_Karten:
            Werteverbesserung_Anzahl[Spieler].update({Karte:[0, 0]})
        for Karte in Karten.Lr_Vergrößern:
            Werteverbesserung_Anzahl[Spieler].update({Karte:[0, 0]})
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

#Listen sortieren: Lebewesen, Lebensraum, Element + gleiche nebeneinander
def Sortieren(Liste):
    Dict = {"Lw":{}, "Lr":{}, "E":{}}
    for Karte in Liste:
        if Karte in Karten.Alle_Lebewesen:
            Key = "Lw"
        if Karte in Karten.Alle_Lebensraum:
            Key = "Lr"
        if Karte in Karten.Alle_Elemente:
            Key = "E"
        if Karte in Dict[Key]:
            Dict[Key][Karte] += 1
        else:
            Dict[Key].update({Karte:1})
    Liste.clear()
    for Art in Dict:
        for Karte in Dict[Art]:
            while Dict[Art][Karte] > 0:
                Liste.append(Karte)
                Dict[Art][Karte] -= 1

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

#Nach letzter Runde
def Ende():
    if Modus == "Punkte":
        screen.fill((255, 255, 255))
        Auswertung = {}
    for Spieler in Alle_Spieler:
        Auswertung.update({Spieler:0})
        #Verbesserung durch Lr
        for Karte in Magisch_Dict[Spieler]:
            Magisch_Dict[Spieler][Karte] = 0
        for Karte in Stärker_Dict[Spieler]:
            Stärker_Dict[Spieler][Karte] = 0
        for Lr in Feld_Spieler:
            for Lw in Feld_Spieler[Lr]:
                if "Magisch" in Lr.Name:
                    if Lw in Magisch_Dict[Spieler]:
                        Magisch_Dict[Spieler][Lw] += 1
                    else:
                        Magisch_Dict[Spieler].update({Lw:1})
                if Lw in Stärker_LR[Lr.Art]:
                    if not Lw in Stärker_Dict[Spieler]:
                        Stärker_Dict[Spieler].update({Lw:1})
                    else:
                        Stärker_Dict[Spieler][Lw] += 1                
        #Lebensraum
        for Lr in Feld_Spieler:
            Auswertung[Spieler] += Lr.Punkte
            #Lebewesen darin
            for Lw in Feld_Spieler[Lr]:
                Ende_Punkte = Lw.Punkte
                if Lw in Verbesserung_Spieler:
                    VSK = Verbesserung_Spieler[Lw]
                    Add_Punkte = VSK["Punkte"]
                    if Add_Punkte < 0:
                        Add_Punkte = 0
                    Ende_Punkte += Add_Punkte
                    Verbesserung_Spieler.remove(Lw)
                if Lw in Magisch_Dict[Spieler]:
                    if Magisch_Dict[Spieler] > 0:
                        Ende_Punkte += 1
                        MSD -= 1
                if Lw in Stärker_Dict[Spieler]:
                    if Stärker_Dict[Spieler] > 0:
                        Ende_Punkte += 2
                        Stärker_Dict[Spieler] -= 1
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

#Events
Spieler_Zug = False #Zug Ende
Aus = True #Ausgabe nach Zugende ja oder nein
Input = False #Input Box Einstellungen
done = False
########Löschen wenn fertig###############
Spiel()
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