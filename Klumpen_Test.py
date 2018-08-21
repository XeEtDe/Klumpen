import random
import pygame as pg
pg.init()
pg.event.set_allowed(None)
pg.event.set_allowed([pg.MOUSEMOTION, pg.MOUSEBUTTONUP, pg.MOUSEBUTTONDOWN, pg.QUIT])
import Karten

#Buttons
Buttons = []
class Button:
	def __init__(self, Rect, Funktion, Bild = None, Text = None, Oberfläche = None, Maus_Pos = False):
		self.Rect = Rect
		self.Funktion = Funktion
		self.Maus_Pos = Maus_Pos
		self.Bild = None
		self.Text = None
		self.Oberfläche = pg.Surface((Rect[2], Rect[3]), pg.SRCALPHA)
        screen.blit(Oberfläche, (Rect[0], Rect[1]))
        #Bild und Text in die Mitte des Buttons
		if not Bild == None:
			screen.blit(Bild, (Oberfläche.get_width() / 2 - Bild.get_width() / 2, Oberfläche.get_height() / 2 - Bild.get_height() / 2))
		if not Text == None:
			screen.blit(Text, (Oberfläche.get_width() / 2 - Text.get_width() / 2, Oberfläche.get_height() / 2 - Text.get_height() / 2))
		Buttons.append(self)

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
	print("Regeln")

def Start():
	global Buttons
	Buttons = []
	screen.fill((255, 255, 210))

#Startbildschirm
screen = pg.display.set_mode((800, 600))
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
Regeln_Rect = Rect(screen.get_width() * 1/4 - Regeln_Bild.get_width() / 2, screen.get_height() / 2 - Regeln_Bild.get_height() / 2 + 150, Regeln_Bild.get_width(), Regeln_Bild.get_height())
Regeln_Button = Button(Regeln_Rect, Regeln, Regeln_Bild, Text_R)
#Start
Start_Bild = get_image("start.png")
screen.blit(Start_Bild, (screen.get_width() * 3/4 - Start_Bild.get_width() / 2, screen.get_height() / 2 - Start_Bild.get_height() / 2 + 150))
Text_S = (pg.font.Font(None, 50)).render("Start", True, (0, 0, 0)) #"Start" in Standartschrift, Größe 50, Farbe schwarz
screen.blit(Text_S, (screen.get_width() * 3/4 - Text_S.get_width() / 2, screen.get_height() / 2 - Text_S.get_height() / 2 + 150))

#Start_Rect = pg.Rect(screen.get_width() * 3/4 - Start_Bild.get_width() / 2, screen.get_height() / 2 - Start_Bild.get_height() / 2 + 150, Start_Bild.get_width(), Start_Bild.get_height())
#Start_Button = Button(Start_Rect, Start)

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