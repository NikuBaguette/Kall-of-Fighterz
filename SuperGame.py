import pygame as pg
import Players
pg.init()


size = (1280,720)
sky = (135,206,235)
black = (1,1,1)
grey = (120,120,120)

screen = pg.display.set_mode(size)
width = screen.get_width()
height = screen.get_height()

time = pg.time.Clock()

bg_image = pg.image.load("Call Of Fighters\img\screen pratique.jpg").convert_alpha()

def background():
    scaled_bg = pg.transform.scale(bg_image,size)
    screen.blit(scaled_bg,(0,0))

player1=Players.New_Players()

game_on = True


while game_on:
    player1.Movement(screen,height,width)
    background()
    player1.Draw(screen)

    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
              game_on = False
        elif event.type==pg.KEYDOWN:
                if event.key==pg.K_ESCAPE:
                     game_on=False 
    mouse = pg.mouse.get_pos()
    pg.display.update()
    time.tick(60)

pg.quit()