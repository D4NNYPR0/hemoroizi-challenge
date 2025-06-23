import sys 
import pygame as pag
from playergaina import Gainaplayer

ALBASTRU = (0, 0, 10)
pag.init()

WIDTH, HEIGHT = 1000, 1000
screen = pag.display.set_mode((WIDTH, HEIGHT))
pag.display.set_caption("Nu pot sa codez asa ca am facut un cacatel de chicken invaders")

FPS = pag.time.Clock()

gaina = Gainaplayer()
grupul_gaina = pag.sprite.GroupSingle()
grupul_gaina.add(gaina)







while True:
    for event in pag.event.get():
        if event.type == pag.QUIT:
            pag.quit()
            sys.exit()
            
    grupul_gaina.update()


    
    screen.fill(ALBASTRU)
    grupul_gaina.draw(screen)
    grupul_gaina.sprite.oul.draw(screen)
 

    pag.display.update()
    FPS.tick(60)