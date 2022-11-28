import pygame as pg
import Players
import Main_menu

Hero_Knight_Size = 140
Hero_Knight_Scale = 4
Hero_Knight_Offset = [58,176]
Hero_Knight_Base_Hurtbox = [90,160] # width, height
Hero_Knight_Data = [Hero_Knight_Size, Hero_Knight_Scale, Hero_Knight_Offset, Hero_Knight_Base_Hurtbox]
Fantasy_Warrior_Size = 162
Fantasy_Warrior_Scale = 4
Fantasy_Warrior_Offset = [70,238] 
Fantasy_Warrior_Base_Hurtbox = [90,170]# width, height
Fantasy_Warrior_Data = [Fantasy_Warrior_Size, Fantasy_Warrior_Scale, Fantasy_Warrior_Offset, Fantasy_Warrior_Base_Hurtbox]

Hero_Knight_Animation_Steps = [11,8,4,4,4,4,9,6]
Fantasy_Warrior_Steps = [10,8,3,3,3,0,7,7,7,8]

pg.init()
pg.mixer.init()

size = (1280,720)
sky = (135,206,235)
yeepee = (220,175,0)

screen = pg.display.set_mode(size)
width = screen.get_width()
height = screen.get_height()
pg.display.set_caption("Kall Of Fighterz")
time = pg.time.Clock()

bg_image = pg.image.load("dassets\dbackgroud\Heyo.jpg").convert_alpha()

Hero_Knight_sheet = pg.image.load("dassets\Hero Knight 2\Sprites\Hero_Knight_2.png").convert_alpha()
Fantasy_Warrior_sheet = pg.image.load("dassets\Fantasy Warrior\Sprites\Fantasy_Warrior.png").convert_alpha()

def background():
    scaled_bg = pg.transform.scale(bg_image,size)
    screen.blit(scaled_bg,(0,0))

def healthbar(health,x,y,plr=0):
    pg.draw.rect(screen,(100,100,100),(x-3,y-3,556,26))
    pg.draw.rect(screen,(15,15,15),(x,y,550,20))
    imagine_lost_hp = health / 1000
    if plr == 1:
        pg.draw.rect(screen,yeepee,(x+(551-550*imagine_lost_hp),y,550*imagine_lost_hp,20))
    else:
        pg.draw.rect(screen,yeepee,(x,y,550*imagine_lost_hp,20))

player1=Players.New_Players(1, False, Hero_Knight_Data, Hero_Knight_sheet, Hero_Knight_Animation_Steps, x=150, y=640)
player2=Players.New_Players(2, True, Fantasy_Warrior_Data, Fantasy_Warrior_sheet, Fantasy_Warrior_Steps, x=980, y=640)



game_on = True if Main_menu.start() else False
if game_on == True:
    pg.mixer.music.load("dassets\sounds\musics\Revolution Mario.mp3")
    pg.mixer.music.set_volume(0.5)
pg.mixer.music.play()
while game_on:
    player2.Movement(height,width,screen,player1)
    player1.Movement(height,width,screen,player2)
    background()
    healthbar(player1.health,25,20,1)
    healthbar(player2.health,width-575,20)
    
    player2.Update()
    player1.Update()
    
    player2.Draw(screen)
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
