import pygame
import math
from player1 import Player
from player2 import Player2

class Bullet:
    def __init__(self, x, y, damage):
        self.pos = (x, y)
        self.damage = damage
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        self.speed = 5
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        self.angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
    
    def update(self, array):  
        self.pos = (self.pos[0]+self.dir[0]*self.speed,
                    self.pos[1]+self.dir[1]*self.speed)
        if self.pos[0] > 500 or self.pos[0] < 0 or self.pos[1] > 500 or self.pos[1] < 0:
            array.remove(self)
        
    def draw(self, surf):
        self.bullet = pygame.Surface((9, 4)).convert_alpha()
        self.bullet.fill((0, 255, 255))
        self.bullet = pygame.transform.rotate(self.bullet, self.angle)
        bullet_rect = self.bullet.get_rect(center = self.pos)
        surf.blit(self.bullet, bullet_rect)  

