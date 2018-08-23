import random
import pygame as pg
pg.init()
import Karten
import pygame_textinput as textinput

#Startbildschirm
screen = pg.display.set_mode((1600, 900), pg.FULLSCREEN)
pg.display.set_caption("Klumpen")
screen.fill((255, 255, 210)) #hellgelbe Füllung

#Bilder laden
Bilder = {}
def get_image(path):
	global Bilder
	Bild = Bilder.get(path)
	if Bild == None:
		Bild = pg.image.load(path).convert()
		Bilder.update({Bild:path})
	return Bild

#Text erstellen
def get_Text(Schrift, Größe, Farbe = (0, 0, 0)):
    return (pg.font.Font(None, Größe)).render(Schrift, True, Farbe)

#Buttons
Buttons = []
class Button:
	def __init__(self, Rect, Funktion, Bild = None, Text = None, Bild_2 = None, Füllung = None, Maus_Pos = False):
		self.Rect = Rect
		self.Funktion = Funktion
		self.Bild = Bild
		self.Text = Text
		self.Bild_2 = Bild_2
		self.Füllung = Füllung
		self.Maus_Pos = Maus_Pos
		if not Bild_2 == None:
			self.Switch = False

	def create_button(self):
		Oberfläche = pg.Surface((self.Rect[2], self.Rect[3]))
		if self.Füllung == None:
		    Oberfläche.fill((255, 0, 255))
		    Oberfläche.set_colorkey((255, 0, 255))
		else:
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
		Oberfläche = pg.Surface((self.Rect[2], self.Rect[3]))
		Oberfläche.fill((255, 0, 255))
		Oberfläche.set_colorkey((255, 0, 255))
        #anderes Bild und Text in die Mitte des Buttons
		Oberfläche.blit(Change_Bild, (Oberfläche.get_width() / 2 - Change_Bild.get_width() / 2, Oberfläche.get_height() / 2 - Change_Bild.get_height() / 2))
		if not self.Text == None:
		    Oberfläche.blit(self.Text, (Oberfläche.get_width() / 2 - self.Text.get_width() / 2, Oberfläche.get_height() / 2 - self.Text.get_height() / 2))
		screen.blit(Oberfläche, (self.Rect[0], self.Rect[1]))

#Buttons und Funktionen
Einstellungen = [None, None, None, None] #[Modus, Spieler, Runden, Züge]
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
def Input_Box():
	In_Feld = textinput.TextInput()
	while True:
		In_Feld.update(pg.event.get())
		screen.blit(In_Feld.get_surface(), (900, 350))
Input_Button = Button(pg.Rect(900, 350, 420, 50), Input_Box, None, None, None, (255, 255, 255))
def Spieler_Hinzu():
	if Spieler_Hinzu_Button.Switch == True:
		pass
Spieler_Hinzu_Button = Button(pg.Rect(1400, 350, Kleiner_Haken.get_width(), Kleiner_Haken.get_height()), Spieler_Hinzu, Kleiner_Haken_Blass, None, Kleiner_Haken)

#Regeln
def Regeln():
	pass
Regeln_Bild = get_image("regeln.png")
Text_R = get_Text("Regeln", 50)
Regeln_Rect = pg.Rect(600 - Regeln_Bild.get_width(), 500, Regeln_Bild.get_width(), Regeln_Bild.get_height())
Regeln_Button = Button(Regeln_Rect, Regeln, Regeln_Bild, Text_R)

#Start
def Start():
	global Buttons
	Buttons = []
	screen.fill((255, 255, 210))
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
	screen.blit(Text, (screen.get_width() / 2 - Text.get_width() / 2, 280))
	Spieler_Hinzu_Button.create_button()
	Input_Button.create_button()
Start_Bild = get_image("start.png")
Text_S = get_Text("Start", 50)
Start_Rect = pg.Rect(1000, 500, Start_Bild.get_width(), Start_Bild.get_height())
Start_Button = Button(Start_Rect, Start, Start_Bild, Text_S)

#Startbildschirm
#Klumpen
Klecks_Blau = get_image("klecksblau.png")
screen.blit(Klecks_Blau, (screen.get_width() / 2 - Klecks_Blau.get_width() / 2, screen.get_height() / 2 - Klecks_Blau.get_height() / 2 - 100)) #mittig von Schrift
Text_K = get_Text("Klumpen", 70)
screen.blit(Text_K, (screen.get_width() / 2 - Text_K.get_width() / 2, screen.get_height() / 2 - Text_K.get_height() / 2 - 100)) #mittig, etwas nach oben verschoben
#Regeln
Regeln_Button.create_button()
#Start
Start_Button.create_button()

#Events
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

    pg.display.flip()