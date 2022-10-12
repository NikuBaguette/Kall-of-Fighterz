import pygame
class New_Players:
    count = 0
    def __init__(self,width=150,height=200,x=0,y=0):
        self.x = x
        self.y = y
        self.vel = 0
        self.jumping = False
        self.HurtBox = pygame.Rect(x,y,width,height)
        
    def Draw(self,surface):
        pygame.draw.rect(surface,(255,0,0),self.HurtBox)
    
    def Attack(self,surface):
        Hitbox = pygame.Rect(self.HurtBox.centerx,self.HurtBox.y,2*self.HurtBox.width,self.HurtBox.height)
        pygame.draw.rect(surface,(0,255,0),Hitbox)

    def Movement(self,surface,height,width):
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
            self.vel = -50

        self.vel += grv
        dy += self.vel 

        if key[pygame.K_r]:
            self.Attack(surface)
        
        if self.HurtBox.left + dx < 0:
            dx = -self.HurtBox.left
        
        if self.HurtBox.right + dx > width:
            dx = width - self.HurtBox.right
        
        if self.HurtBox.bottom + dy > height - 100:
            self.vel = 0
            dy = height - 100 - self.HurtBox.bottom
            self.jumping = False
        
        self.HurtBox.x += dx
        self.HurtBox.y += dy
    
    