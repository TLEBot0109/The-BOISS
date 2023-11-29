import pygame

class Button():
    def __init__(self, x, y, wi, he, color, contex):
        self.x = x
        self.y = y
        self.wi = wi
        self.he = he
        self.color = color
        self.contex = contex
        
        
    def get_clicked(self):
        mouse_button = pygame.mouse.get_pressed(num_buttons = 3)
        mouse_pos = pygame.mouse.get_pos()
        if (mouse_button[0] and mouse_pos >= self.x - self.wi and mouse_pos <= self.x 
            and mouse_pos >= self.y - self.he and mouse_pos <= self.y):
            return True
        else: 
            return False 
            