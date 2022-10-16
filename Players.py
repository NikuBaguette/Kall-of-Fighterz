import pygame
class New_Players:
    count = 0
    def __init__(self,flip,data,sprite_sheet,animation_steps,width=100,height=160,x=0,y=0):
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.Load_images(sprite_sheet,animation_steps)
        self.act = 4 #0:Attack1  1:dash  2:death  3:fall  4:iddle  5:jump  6:run  7:TakeHit (in test)
        self.frame_index = 0
        self.image = self.animation_list[self.act][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.vel = 0
        self.running = False
        self.jumping = False
        self.HurtBox = pygame.Rect(x,y-height,width,height)
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
        

    def Movement(self, height, width, surface, target):
        sp = 10
        grv = 3
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
                self.vel = -40
                
            if key[pygame.K_r] or key[pygame.K_f]:
                self.Attack(surface,target)
                if key[pygame.K_r]:
                    self.attack_type = 1
                if key[pygame.K_f]:
                    self.attack_type = 2
        
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
            self.Update_action(5)
        elif self.running:
            self.Update_action(6)
        else:
            self.Update_action(4)
        cooldown = 60
        self.image = self.animation_list[self.act][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animation_list[self.act]):
            self.frame_index = 0
        
    def Attack(self,surface,target):
        self.isAttacking = True
        Hitbox = pygame.Rect(self.HurtBox.centerx - (2 * self.HurtBox.width * self.flip), self.HurtBox.y, 2 * self.HurtBox.width, self.HurtBox.height)
        
        if Hitbox.colliderect(target.HurtBox):
            target.health -= 150
        pygame.draw.rect(surface,(0,250,0),Hitbox)
    
    def Update_action(self, new_action):
        if new_action != self.act:
            self.act = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def Draw(self,surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(surface,(255,0,0),self.HurtBox)
        surface.blit(img, (self.HurtBox.x - (self.offset[0] * self.image_scale), self.HurtBox.y - (self.offset[1] - self.image_scale)))
