import pygame

class Player2():
    def __init__(self, x, y, wi, he, color,health,delay):
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
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rec )
        pygame.draw.line(win,(255,0,0),(self.x-25,self.y-30), 
                         (self.x-25+50*(self.health/self.max_health),self.y-30),3)
        if(self.health < self.max_health):
            pygame.draw.line(win,(255,255,255),
                         (self.x-25+50*(self.health/self.max_health)+1,self.y-30), (self.x+25,self.y-30),3)
        
    def Update(self):      
        self.rec = (self.x - self.wi/2, self.y - self.he/2, self.wi, self.he)
        
    def move(self): 
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]: 
            self.x -= self.vel
            if self.x <0 :
                self.x = 0
            elif self.x >500:
                self.x = 500
            
        if keys[pygame.K_d]: 
            self.x += self.vel
            if self.x <0 :
                self.x = 0
            elif self.x >500:
                self.x = 500
            
        if keys[pygame.K_w]: 
            self.y -= self.vel
            if self.y <0 :
                self.y = 0
            elif self.y >500:
                self.y = 500
        
        if keys[pygame.K_s]: 
            self.y += self.vel
            if self.y <0 :
                self.y = 0
            elif self.y >500:
                self.y = 500
        self.Update()