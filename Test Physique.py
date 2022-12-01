import pygame
from random import randint
class Projectile:
    def __init__(self, x:int, y:int, width:int, height:int, frottement:float = 1.1, vx = 20, vy = -10):
        self.box = pygame.Rect(x,y,width,height)
        self.vy = vy
        self.vx = vx
        self.frot = frottement

    def mov(self,width,height,liste:list):
        gravity = 2
        frot = self.frot
        dx = 0
        dy = 0
        
        self.vy += gravity
        dy += self.vy
        dx += self.vx

        for i in liste:
            if self != i:
                if self.box.left - dx <= i.box.right and self.box.right + dx > i.box.left and self.box.top - dy <= i.box.bottom and self.box.bottom + dx > i.box.top:
                    if self.box.y >=  i.box.y:
                        self.vy = abs(self.vy)/frot
                        dy = abs(dy)
                    else:
                        self.vy = -self.vy/frot
                        dy = -abs(dy)
                    self.vx = -self.vx/frot
                    
                    dx = -dx

        if self.box.left + dx < 0:
            self.vx = abs(self.vx)/frot
            dx = 0
        
        if self.box.right + dx > width:
            self.vx = -abs(self.vx)/frot
            dx = 0
        
        if self.box.bottom + dy > height - 50:
            if abs(self.vx) <= 0.3:
                self.vx = 0
            self.vx = self.vx/frot
            self.vy = -self.vy//gravity
            dy = height - 50 - self.box.bottom

        self.box.x += dx
        self.box.y += dy

    def draw(self, surface):
        pygame.draw.rect(surface, (200,0,0), self.box)

pygame.init()

screen = (800,600)
surface = pygame.display.set_mode(screen)
time = pygame.time.Clock()
keys = pygame.key.get_pressed()
sky = (135,206,235)
game = True

a = [Projectile(randint(0,770), randint(0,400), 30, 30, 1 + (randint(1,50)/100), randint(-50,50), randint(-20, 0)) for _ in range(0)]
a.append(Projectile(300,400,30,30, vx=0))
a.append(Projectile(300,200,30,30, vx=0))
def movProjo(liste:list):
    for i in liste:
        i.mov(800,600,liste)

def drawProjo(liste:list):
    for i in liste:
        i.draw(surface)

while game:
    surface.fill(sky)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    movProjo(a)
    drawProjo(a)
    
    pygame.display.update()
    time.tick(60)

pygame.quit()
