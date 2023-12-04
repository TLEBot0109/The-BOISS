import pygame
from bullet import Bullet

def border(number):
        if number < 0:
            return 0
        elif number > 500:
            return 500
        else: 
            return number
        
class player():
    def __init__(self, x, y, wi, he, color):
        self.x = x
        self.y = y
        self.wi = wi
        self.he = he
        self.color = color
        self.rec = (x, y, wi, he)
        self.vel = 3
        self.bul=[]
  
    def draw(self, win):
        pygame.draw.ellipse(win, self.color, self.rec)
    
    def update(self):
        self.rec = (border(self.x) - self.wi/2, border(self.y) - self.he/2, self.wi, self.he)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= self.vel
            
        if keys[pygame.K_d]:
            self.x += self.vel

        if keys[pygame.K_w]:
            self.y -= self.vel

        if keys[pygame.K_s]:
            self.y += self.vel

        if keys[pygame.MOUSEBUTTONDOWN]:
            b1=Bullet(border(self.x),border(self.y),100)
            self.bul.append(b1)

        if keys[pygame.K_ESCAPE]:
            run = False
            pygame.quit()
    
        self.update()