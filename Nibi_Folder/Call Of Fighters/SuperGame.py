import pygame as pg
import Players
pg.init()

size = (1280,720)
sky = (135,206,235)
yeepee = (220,175,0)

Hero_Knight_Size = 140
Hero_Knight_Scale = 4
Hero_Knight_Offset = [58,177]
Hero_Knight_Data = [Hero_Knight_Size, Hero_Knight_Scale, Hero_Knight_Offset]
Fantasy_Warrior_Size = 162
Fantasy_Warrior_Scale = 4
Fantasy_Warrior_Offset = [72,156]
Fantasy_Warrior_Data = [Fantasy_Warrior_Size, Fantasy_Warrior_Scale, Fantasy_Warrior_Offset]

screen = pg.display.set_mode(size)
width = screen.get_width()
height = screen.get_height()
pg.display.set_caption("Call Of Fighters")
time = pg.time.Clock()

bg_image = pg.image.load("Batch\game\Call Of Fighters\dassets\dbackgroud\Heyo.jpg").convert_alpha()

Hero_Knight_sheet = pg.image.load("Batch\game\Call Of Fighters\dassets\Hero Knight 2\Sprites\Hero_Knight_2.png").convert_alpha()
Fantasy_Warrior_sheet = pg.image.load("Batch\game\Call Of Fighters\dassets\Fantasy Warrior\Sprites\Fantasy_Warrior.png").convert_alpha()

Hero_Knight_Animation_Steps = [6,4,9,4,11,4,8,4]
Fantasy_Warrior_Steps = [7,7,8,7,3,10,3,8,3]

def background():
    scaled_bg = pg.transform.scale(bg_image,size)
    screen.blit(scaled_bg,(0,0))

def healthbar(health,x,y,plr=0):
    pg.draw.rect(screen,(100,100,100),(x-3,y-3,556,26))
    pg.draw.rect(screen,(15,15,15),(x,y,550,20))
    imagine_lost_hp = health / 1000
    if plr == 1:
        pg.draw.rect(screen,yeepee,(x+(550-550*imagine_lost_hp),y,550*imagine_lost_hp,20))
    else:
        pg.draw.rect(screen,yeepee,(x,y,550*imagine_lost_hp,20))

player1=Players.New_Players(False, Hero_Knight_Data, Hero_Knight_sheet, Hero_Knight_Animation_Steps, x=150, y=640)
player2=Players.New_Players(True, Fantasy_Warrior_Data, Fantasy_Warrior_sheet, Fantasy_Warrior_Steps, x=980, y=640)

game_on = True


while game_on:
    player1.Movement(height,width,screen,player2)
    background()
    healthbar(player1.health,25,20,1)
    healthbar(player2.health,width-575,20)
    
    player1.Update()
    
    player1.Draw(screen)
    player2.Draw(screen)

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