import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, dimensions, color, health, delay, controls, 
                 pre_time_moving,walking_way):
        #0=right 1=left
        super().__init__()
        self.moving_sprites = pygame.sprite.Group()
        self.moving_sprites.add(self)
        self.x = dimensions[0]
        self.y = dimensions[1]
        self.wi = dimensions[2]
        self.he = dimensions[3]
        self.color = color
        self.rec = dimensions
        self.vel = 3
        self.health=health
        self.max_health=health
        self.delay=delay
        self.controls=controls
        self.pre_time_moving=pre_time_moving
        self.walking_way=walking_way
        
        
        self.sprites=[[],[]]
        self.sprites[0].append(pygame.image.load('knight_move_right1.png'))
        self.sprites[0].append(pygame.image.load('knight_move_right2.png'))
        self.sprites[0].append(pygame.image.load('knight_move_right3.png'))
        self.sprites[0].append(pygame.image.load('knight_move_right4.png'))
        self.sprites[0].append(pygame.image.load('knight_move_right5.png'))
        self.sprites[0].append(pygame.image.load('knight_move_right6.png'))
        self.sprites[0].append(pygame.image.load('knight_move_right7.png'))
        self.sprites[0].append(pygame.image.load('knight_move_right8.png'))
        self.sprites[1].append(pygame.image.load('knight_move_left1.png'))
        self.sprites[1].append(pygame.image.load('knight_move_left2.png'))
        self.sprites[1].append(pygame.image.load('knight_move_left3.png'))
        self.sprites[1].append(pygame.image.load('knight_move_left4.png'))
        self.sprites[1].append(pygame.image.load('knight_move_left5.png'))
        self.sprites[1].append(pygame.image.load('knight_move_left6.png'))
        self.sprites[1].append(pygame.image.load('knight_move_left7.png'))
        self.sprites[1].append(pygame.image.load('knight_move_left8.png'))
        
        
        self.current_sprite = 0
        self.image = self.sprites[walking_way][self.current_sprite]

        self.rect = self.image.get_rect()

    def update_image(self):
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.walking_way][self.current_sprite]
    
    def draw(self, win):
        #pygame.draw.rect(win, self.color, self.rec)
        self.moving_sprites.draw(win)
        p=-5
        start=self.x-15+p
        end=self.x+15+p
        pygame.draw.line(win,(255,0,0),(start,self.y-25), 
                         (start+(end-start+1)*(self.health/self.max_health),self.y-25),3)
        if(self.health < self.max_health):
            pygame.draw.line(win,(255,255,255),
                         (start+(end-start+1)*(self.health/self.max_health)+1,self.y-25), 
                         (end,self.y-25),3)
    
    def delete_from_spirte(self):
        self.moving_sprites.remove(self)
    
    def Update(self):      
        #self.rec = (self.x - self.wi/2, self.y - self.he/2, self.wi, self.he)
        self.rec = (self.x , self.y , self.wi, self.he)
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rec[0]-30,self.rec[1]-30]
    def move(self): 
        keys = pygame.key.get_pressed()
        change_image = False
        min_x=29
        max_x=500-18
        min_y=27
        max_y=500-63
        if keys[self.controls[2]]:
            self.x -= self.vel
            if self.x < min_x:
                self.x = min_x
            elif self.x > max_x:
                self.x = max_x
            change_image = True
            self.walking_way=1

        if keys[self.controls[3]]:
            self.x += self.vel
            if self.x < min_x:
                self.x = min_x
            elif self.x > max_x:
                self.x = max_x
            change_image = True
            self.walking_way=0

        if keys[self.controls[0]]:
            self.y -= self.vel
            if self.y < min_y:
                self.y = min_y
            elif self.y > max_y:
                self.y = max_y
            change_image = True

        if keys[self.controls[1]]:
            self.y += self.vel
            if self.y < min_y:
                self.y = min_y
            elif self.y > max_y:
                self.y = max_y
            change_image = True
        
        if change_image == True:
            current_time= pygame.time.get_ticks()
            if(current_time-self.pre_time_moving>250):
                self.update_image()
                self.pre_time_moving=current_time
        else:
            self.current_sprite=0
            self.image = self.sprites[self.walking_way][self.current_sprite]
        self.Update()
