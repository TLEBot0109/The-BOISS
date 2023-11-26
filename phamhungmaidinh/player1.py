import pygame
moving_sprites = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, wi, he, color,health,delay):
        super().__init__()
        self.x = x
        self.y = y
        self.wi = wi
        self.he = he
        self.color = color
        self.rec = (x, y, wi, he)
        self.vel = 3
        self.health=health
        self.max_health=health
        self.delay=delay
        self.sprites=[]
        self.sprites.append(pygame.image.load('random1.jpg'))
        self.sprites.append(pygame.image.load('random2.jpg'))
        self.sprites.append(pygame.image.load('random3.jpg'))
        self.sprites.append(pygame.image.load('random4.jpg'))
        self.sprites.append(pygame.image.load('random5.jpg'))
        self.sprites.append(pygame.image.load('random6.jpg'))
        self.sprites.append(pygame.image.load('random7.jpg'))
        self.sprites.append(pygame.image.load('random8.jpg'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        #self.rect.topleft = [x+50,y+50]
        moving_sprites.add(self)
    def update_image(self):
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
    
    def draw(self, win):
        #pygame.draw.rect(win, self.color, self.rec)
        moving_sprites.draw(win)
        pygame.draw.line(win,(255,0,0),(self.x-25,self.y-30), 
                         (self.x-25+50*(self.health/self.max_health),self.y-30),3)
        if(self.health < self.max_health):
            pygame.draw.line(win,(255,255,255),
                         (self.x-25+50*(self.health/self.max_health)+1,self.y-30), (self.x+25,self.y-30),3)
    def Update(self):      
        self.rec = (self.x - self.wi/2, self.y - self.he/2, self.wi, self.he)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rec[0],self.rec[1]]
    def move(self): 
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]: 
            self.x -= self.vel
            if self.x <0 :
                self.x = 0
            elif self.x >500:
                self.x = 500
            
        if keys[pygame.K_RIGHT]: 
            self.x += self.vel
            if self.x <0 :
                self.x = 0
            elif self.x >500:
                self.x = 500
            
        if keys[pygame.K_UP]: 
            self.y -= self.vel
            if self.y <0 :
                self.y = 0
            elif self.y >500:
                self.y = 500
        
        if keys[pygame.K_DOWN]: 
            self.y += self.vel
            if self.y <0 :
                self.y = 0
            elif self.y >500:
                self.y = 500
        self.Update()