import pygame

class test:
    def __init__(self,x=10,y=700,width=150,height=280):
        self.position_x = x
        self.position_y = y
        self.velocity_y = 0
        self.jumping = False
        self.HurtBox = pygame.Rect((x,y,width,height))
    
    def Draw(self,surface,color=(255,0,0)):
        pygame.draw.rect(surface,color,self.HurtBox)
    
    def Move(self,width,height):
        sp = 10
        grv = 4
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_q]:
            dx=-sp
        
        if key[pygame.K_d]:
            dx=sp
        
        if self.jumping == False and key[pygame.K_z]:
            self.jumping = True
            self.velocity_y = -50
        
        self.velocity_y += grv
        dy += self.velocity_y 
        
        if self.HurtBox.left + dx < 0:
            dx = -self.HurtBox.left
        
        if self.HurtBox.right + dx > width:
            dx = width - self.HurtBox.right
        
        if self.HurtBox.bottom + dy > height - 200:
            self.velocity_y = 0
            dy = height - 200 - self.HurtBox.bottom
            self.jumping = False
        
        self.HurtBox.x += dx
        self.HurtBox.y += dy
