import random
import pygame as pg
pg.init()
pg.event.set_allowed(None)
pg.event.set_allowed([pg.MOUSEMOTION, pg.MOUSEBUTTONUP, pg.MOUSEBUTTONDOWN, pg.QUIT])
import Karten

#Buttons
Buttons = []
class Button:
	def __init__(self, Rect, Funktion, Bild = None, Text = None, Bild_2 = None, Maus_Pos = False):
		self.Rect = Rect
		self.Funktion = Funktion
		self.Bild = Bild
		self.Text = Text
		self.Bild_2 = Bild_2
		self.Maus_Pos = Maus_Pos
		Oberfläche = pg.Surface((Rect[2], Rect[3]))
		Oberfläche.fill((255, 0, 255))
		Oberfläche.set_colorkey((255, 0, 255))
        #Bild und Text in die Mitte des Buttons
		if not Bild == None:
			Oberfläche.blit(Bild, (Oberfläche.get_width() / 2 - Bild.get_width() / 2, Oberfläche.get_height() / 2 - Bild.get_height() / 2))
		if not Bild_2 == None:
			Switch = False
		if not Text == None:
			Oberfläche.blit(Text, (Oberfläche.get_width() / 2 - Text.get_width() / 2, Oberfläche.get_height() / 2 - Text.get_height() / 2))
		screen.blit(Oberfläche, (Rect[0], Rect[1]))
		Buttons.append(self)

		def Change(self):
			if Switch == False:
				Change_Bild = self.Bild_2
				Switch = True
			elif Switch == True:
				Change_Bild = self.Bild_1
				Switch = False
			Oberfläche = pg.Surface((Rect[2], Rect[3]))
			Oberfläche.fill((255, 0, 255))
			Oberfläche.set_colorkey((255, 0, 255))
            #anderes Bild und Text in die Mitte des Buttons
			Oberfläche.blit(Change_Bild, (Oberfläche.get_width() / 2 - Change_Bild.get_width() / 2, Oberfläche.get_height() / 2 - Change_Bild.get_height() / 2))
			if not self.Text == None:
			    Oberfläche.blit(self.Text, (Oberfläche.get_width() / 2 - self.Text.get_width() / 2, Oberfläche.get_height() / 2 - self.Text.get_height() / 2))
			    screen.blit(Oberfläche, (Rect[0], Rect[1]))

#Bilder laden
Bilder = {}
def get_image(path):
	global Bilder
	Bild = Bilder.get(path)
	if Bild == None:
		Bild = pg.image.load(path).convert()
		Bilder.update({Bild:path})
	return Bild

#Funktionen
def Regeln():
	pass

def Start():
	global Buttons
	Buttons = []
	screen.fill((255, 255, 210))
	#Modus
	Text = (pg.font.Font(None, 50)).render("Modus?", True, (0, 0, 0))
	screen.blit(Text, (screen.get_width() / 2 - Text.get_width() / 2, 10))
	Kreis_Bild = get_image("kreisbild.png")
	Kreis_Bild_2 = get_image("kreisbild2.png")
	def Punkte_Funk():
		pass
	Punkte_Rect = pg.Rect(300 - Kreis_Bild.get_width(), 50, Kreis_Bild.get_width(), Kreis_Bild.get_height())
	Punkte_Button = Button(Punkte_Rect, Punkte_Funk, Kreis_Bild, None, Kreis_Bild_2)
	#Spieler
	Text = (pg.font.Font(None, 50)).render("Spieler?", True, (0, 0, 0))
	screen.blit(Text, (screen.get_width() / 2 - Text.get_width() / 2, screen.get_height() / 3))



#Startbildschirm
screen = pg.display.set_mode((1600, 900), pg.FULLSCREEN)
pg.display.set_caption("Klumpen")
screen.fill((255, 255, 210)) #hellgelbe Füllung
#Klumpen
Klecks_Blau = get_image("klecksblau.png")
screen.blit(Klecks_Blau, (screen.get_width() / 2 - Klecks_Blau.get_width() / 2, screen.get_height() / 2 - Klecks_Blau.get_height() / 2 - 100)) #mittig von Schrift
Text_K = (pg.font.Font(None, 70)).render("Klumpen", True, (0, 0, 0)) #"Klumpen" in Standartschrift, Größe 70, Farbe schwarz
screen.blit(Text_K, (screen.get_width() / 2 - Text_K.get_width() / 2, screen.get_height() / 2 - Text_K.get_height() / 2 - 100)) #mittig, etwas nach oben verschoben
#Regeln
Regeln_Bild = get_image("regeln.png")
Text_R = (pg.font.Font(None, 50)).render("Regeln", True, (0, 0, 0)) #"Regeln" in Standartschrift, Größe 50, Farbe schwarz
Regeln_Rect = pg.Rect(600 - Regeln_Bild.get_width(), 500, Regeln_Bild.get_width(), Regeln_Bild.get_height())
Regeln_Button = Button(Regeln_Rect, Regeln, Regeln_Bild, Text_R)
#Start
Start_Bild = get_image("start.png")
Text_S = (pg.font.Font(None, 50)).render("Start", True, (0, 0, 0)) #"Start" in Standartschrift, Größe 50, Farbe schwarz
Start_Rect = pg.Rect(1000, 500, Start_Bild.get_width(), Start_Bild.get_height())
Start_Button = Button(Start_Rect, Start, Start_Bild, Text_S)

#Events
done = False
while done == False:
        for event in pg.event.get():
                if event.type == pg.QUIT:
                        done = True
                        break
                if event.type == pg.MOUSEMOTION:
                	for Button in Buttons:
                		if Button.Rect.collidepoint(pg.mouse.get_pos()):
                			Button.Maus_Pos = True
                		else:
                			Button.Maus_Pos = False
                if event.type == pg.MOUSEBUTTONDOWN:
                	for Button in Buttons:
                		if Button.Maus_Pos == True:
                		    Button.Funktion()

        pg.display.flip()