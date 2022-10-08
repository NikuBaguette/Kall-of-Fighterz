import pygame as pg
import Players as plr
pg.init()


size = (1920,1080)
sky = (135,206,235)
black = (1,1,1)
grey = (120,120,120)

screen = pg.display.set_mode(size)
width = screen.get_width()
height = screen.get_height()



game_on = True

time = pg.time.Clock()
while game_on:
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
              game_on = False
        elif event.type==pg.KEYDOWN:
                if event.key==pg.K_ESCAPE:
                     game_on=False 
    mouse = pg.mouse.get_pos()

    pg.display.update()
    screen.fill(sky)
    time.tick(60)
pg.quit()