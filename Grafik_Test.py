import pygame as pg

pg.init()
sreen = pg.display.set_mode((300, 200))
pg.display.set_caption("Klumpen")
clock = pg.time.Clock()


done = False
while done == False:
        for event in pg.event.get():
                if event.type == pg.QUIT:
                        done = True

        pg.display.flip()
        clock.tick(60)