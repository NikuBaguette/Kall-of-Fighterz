import pygame as pg
import Players
pg.init()

def start():
    size = (1280,720)
    screen = pg.display.set_mode(size)
    width = screen.get_width()
    height = screen.get_height()
    time = pg.time.Clock()
    bg_image = pg.image.load("dassets\dbackgroud\Heyo.jpg").convert_alpha()

    def background():
        scaled_bg = pg.transform.scale(bg_image,size)
        screen.blit(scaled_bg,(0,0))

    game_on = True

    playButton = Players.Button(width//2 - 100,height//2 - 150, 200, 100)
    quitButton = Players.Button(width//2 - 100,height//2 + 50, 200, 100)

    def button(rect:pg.Rect, color = (200,0,0)):
        pg.draw.rect(screen,color,rect)

    while game_on:
        background()
        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                game_on = False
                return False
            elif event.type==pg.KEYDOWN:
                    if event.key==pg.K_ESCAPE:
                        game_on=False
                        return False
        
        playButton.draw(screen,(0,150,0))
        quitButton.draw(screen,(150,0,0))
        if playButton.Button1Click():
            game_on = False
            return True
        if quitButton.Button1Click():
            game_on = False
            return False
        
        pg.display.update()
        time.tick(60)
