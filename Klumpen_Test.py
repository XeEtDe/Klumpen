import random
import pygame as pg
pg.init()
import Karten

#Bilder laden
Bilder = {}
def get_image(path):
	global Bilder
	Bild = Bilder.get(path)
	if Bild == None:
		Bild = pg.image.load(path).convert()
		Bilder.update({Bild:path})
	return Bild

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Klumpen")
screen.fill((255, 255, 210)) #hellgelbe Füllung

#Startbildschirm
#Klumpen
Klecks_Blau = get_image("klecksblau.png")
screen.blit(Klecks_Blau, (screen.get_width() / 2 - Klecks_Blau.get_width() / 2, screen.get_height() / 2 - Klecks_Blau.get_height() / 2 - 100)) #mittig von Schrift
Text_K = (pg.font.Font(None, 70)).render("Klumpen", True, (0, 0, 0)) #"Klumpen" in Standartschrift, Größe 70, Farbe schwarz
screen.blit(Text_K, (screen.get_width() / 2 - Text_K.get_width() / 2, screen.get_height() / 2 - Text_K.get_height() / 2 - 100)) #mittig, etwas nach oben verschoben
#Regeln
Regeln_Bild = get_image("regeln.png")
screen.blit(Regeln_Bild, (screen.get_width() * 1/4 - Regeln_Bild.get_width() / 2, screen.get_height() / 2 - Regeln_Bild.get_height() / 2 + 150))
Text_R = (pg.font.Font(None, 50)).render("Regeln", True, (0, 0, 0)) #"Regeln" in Standartschrift, Größe 50, Farbe schwarz
screen.blit(Text_R, (screen.get_width() * 1/4 - Text_R.get_width() / 2, screen.get_height() / 2 - Text_R.get_height() / 2 + 150))
#Start
Start_Bild = get_image("start.png")
screen.blit(Start_Bild, (screen.get_width() * 3/4 - Start_Bild.get_width() / 2, screen.get_height() / 2 - Start_Bild.get_height() / 2 + 150))
Text_S = (pg.font.Font(None, 50)).render("Start", True, (0, 0, 0)) #"Start" in Standartschrift, Größe 50, Farbe schwarz
screen.blit(Text_S, (screen.get_width() * 3/4 - Text_S.get_width() / 2, screen.get_height() / 2 - Text_S.get_height() / 2 + 150))

done = False
while done == False:
        for event in pg.event.get():
                if event.type == pg.QUIT:
                        done = True

        pg.display.flip()