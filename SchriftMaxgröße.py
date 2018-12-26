import pygame as pg
import Karten
pg.init()

def SchriftFunc(Text, Länge = None, Höhe = None, Farbe = (0, 0, 0), Schriftart = None):
    Größe = 1
    Alte_Größe = 0
    while True:
        Schrift = pg.font.Font(Schriftart, Größe).render(Text, True, Farbe)
        if not Länge == None:
            if Schrift.get_width() > Länge:
                break
        if not Höhe == None:
            if Schrift.get_height() > Höhe:
                break
        Alte_Größe = Größe
        Größe += 1
    return pg.font.Font(Schriftart, Alte_Größe).render(Text, True, Farbe)