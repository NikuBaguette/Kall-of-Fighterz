import pygame
class New_Players:
    count = 0
    def __init__(self,flip:bool,data:list,sprite_sheet,animation_steps:list,x:int=0,y:int=0):
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.Load_images(sprite_sheet,animation_steps)
        self.act = 0 #0:Iddle  1:Run  2:Jump  3:fall  4:TakeHit  5:Dash  6:Death  7:Attack* (in test)
        self.frame_index = 0
        self.image = self.animation_list[self.act][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.vel = 0
        self.running = False
        self.jumping = False
        self.HurtBox = data[3]
        self.HurtBox = pygame.Rect(x,y-self.HurtBox[1],self.HurtBox[0],self.HurtBox[1])
        self.attack_type = 0
        self.isAttacking = False
        self.health = 1000
    
    def Load_images(self,sprite_sheet,animation_steps):
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list
        

    def Movement(self, height:int, width:int, surface:tuple, target):
        sp = 10
        grv = 4
        dx = 0
        dy = 0
        self.running = False
        key = pygame.key.get_pressed()

        if self.isAttacking == False:
            
            if key[pygame.K_q]:
                dx=-sp
                self.running = True
            
            if key[pygame.K_d]:
                dx=sp
                self.running = True

            if self.jumping == False and key[pygame.K_z]:
                self.jumping = True
                self.vel = -50
                
            if key[pygame.K_u] or key[pygame.K_i]:
                if key[pygame.K_u]:
                    self.attack_type = 2
                if key[pygame.K_i]:
                    self.attack_type = 3
                if key[pygame.K_u] and self.jumping:
                    self.attack_type = 1
                self.Attack(surface,target)
                
        
        self.vel += grv
        dy += self.vel
        
        if self.HurtBox.left + dx < 0:
            dx = -self.HurtBox.left
        
        if self.HurtBox.right + dx > width:
            dx = width - self.HurtBox.right
        
        if self.HurtBox.bottom + dy > height - 80:
            self.vel = 0
            dy = height - 80 - self.HurtBox.bottom
            self.jumping = False
        
        if self.HurtBox.centerx < target.HurtBox.centerx:
            self.flip = False
        else:
            self.flip = True
        
        self.HurtBox.x += dx
        self.HurtBox.y += dy
        
    def Update(self):
        if self.jumping:
            if self.vel > 0:
                self.Update_action(3)
            else:
                self.Update_action(2)
        elif self.running:
            self.Update_action(1)
        elif self.isAttacking:
            if self.attack_type+6 >= len(self.animation_list):
                self.Update_action(7)
            else:
                self.Update_action(6+self.attack_type)
        else:
            self.Update_action(0)
        cooldown = 60
        self.image = self.animation_list[self.act][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animation_list[self.act]):
            self.frame_index = 0
        
    def Attack(self,surface:tuple,target):
        self.isAttacking = True
        Hitbox = pygame.Rect(self.HurtBox.centerx - (2 * self.HurtBox.width * self.flip), self.HurtBox.y, 2 * self.HurtBox.width, self.HurtBox.height)
        if Hitbox.colliderect(target.HurtBox):
            target.health -= 150
    
    def Update_action(self, new_action:int):
        if new_action != self.act:
            self.act = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def Draw(self,surface:tuple):
        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(surface,(255,0,0),self.HurtBox)
        surface.blit(img, (self.HurtBox.left - (self.offset[0] * self.image_scale), self.HurtBox.y - (self.offset[1] - self.image_scale)))

class Button:
    def __init__(self, x:int, y:int, width:int = 150, height:int = 60, label:str = "Empty"):
        self.Rect = pygame.Rect(x,y,width,height)
        self.label = label
    
    def draw(self, screen:tuple, color:tuple = (255,0,0), overcolor = (135,206,235)):
        if self.mouseOver():
            pygame.draw.rect(screen, overcolor, self.Rect)
        else:
            pygame.draw.rect(screen, color, self.Rect)
        

    def mouseOver(self):
        mouse = pygame.mouse.get_pos()
        if mouse[0] >= self.Rect.left and mouse[0] <= self.Rect.right and mouse[1] >= self.Rect.top and mouse[1] <= self.Rect.bottom:
            return True
        else:
            return False
    
    def Button1Click(self):
        key = pygame.key.get_pressed()
        if self.mouseOver() and key[pygame.K_h] is True:
            return True
        else:
            return False