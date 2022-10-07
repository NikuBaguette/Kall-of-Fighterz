import pygame as pg
pg.init()




size = (1920,1080)
sky = (135,206,235)
Keys = pg.key.get_pressed()

window = pg.display.set_mode(size)
game_on = True
pg.display.set_caption("Bagarre")
time = pg.time.Clock()
while game_on == True:
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
              carryOn = False 
        elif event.type==pg.KEYDOWN:
                if event.key==pg.K_f: 
                     carryOn=False  
        pg.display.update()
        
    window.fill(sky)
    pg.display.flip()
    time.tick(60)
pg.quit()