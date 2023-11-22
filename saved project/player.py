import pygame

class Player():
    def __init__(self, x, y, wi, he, color,):
        self.x = x
        self.y = y
        self.wi = wi
        self.he = he
        self.color = color
        self.rec = (x, y, wi, he)
        self.vel = 3
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rec )
        
    def Update(self):      
        self.rec = (self.x - 25, self.y - 25, self.wi, self.he)
        
    def move(self): 
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]: 
            self.x -= self.vel
            if self.x <0 :
                self.x = 500
            elif self.x >500:
                self.x = 0
            
        if keys[pygame.K_RIGHT]: 
            self.x += self.vel
            if self.x <0 :
                self.x = 500
            elif self.x >500:
                self.x = 0
            
        if keys[pygame.K_UP]: 
            self.y -= self.vel
            if self.y <0 :
                self.y = 500
            elif self.y >500:
                self.y = 0
        
        if keys[pygame.K_DOWN]: 
            self.y += self.vel
            if self.y <0 :
                self.y = 500
            elif self.y >500:
                self.y = 0
        self.Update()