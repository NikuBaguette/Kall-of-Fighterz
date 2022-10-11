import pygame

class test:
    def __init__(self,x=0,y=700,width=50,height=80):
        self.position_x = x
        self.position_y = y
        self.HurtBox = pygame.Rect((x,y,width,height))
    
    def Draw(self,surface,color=(255,0,0)):
        pygame.draw.rect(surface,color,self.HurtBox)
    
    def Move(self):
        sp = 15
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_q]:
            dx=-sp
        if key[pygame.K_d]:
            dx=sp
        self.HurtBox.x += dx
        self.HurtBox.y += dy
