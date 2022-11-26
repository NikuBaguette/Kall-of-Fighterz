import pygame as pg
import Players
pg.init()
pg.mixer.init()

def start():
    pg.mixer.music.load("dassets\sounds\musics\A-day-in-the-life.mp3")
    pg.mixer.music.set_volume(0.5)
    size = (1280,720)
    screen = pg.display.set_mode(size)
    width = screen.get_width()
    height = screen.get_height()
    time = pg.time.Clock()
    bg_image = pg.image.load("dassets\dbackgroud\Heyo.jpg").convert_alpha()

    def background():
        scaled_bg = pg.transform.scale(bg_image,size)
        screen.blit(scaled_bg,(0,0))

    menu = True

    playButton = Players.Button(width//2 - 100,height//2 - 150, 200, 100)
    quitButton = Players.Button(width//2 - 100,height//2 + 50, 200, 100)
    pg.mixer.music.play()
    while menu:
        background()
        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                menu = False
                return False
            elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        menu = False
                        return False
        
        playButton.draw(screen,(0,150,0))
        quitButton.draw(screen,(150,0,0))
        if playButton.Button1Click():
            menu = False
            return True
        if quitButton.Button1Click():
            menu = False
            return False
        
        pg.display.update()
        time.tick(60)
