import pygame

class Button():
    def __init__(self, x, y, wi, he, color, ):
        self.x = x
        self.y = y
        self.wi = wi
        self.he = he
        self.color = color
        self.rect=pygame.Rect(x,y,wi,he)
        
    def draw(self,win):
        pygame.draw.rect(win,self.color,self.rect)
    
    def get_clicked(self):
        mouse_button = pygame.mouse.get_pressed(num_buttons = 3)
        mouse_pos = pygame.mouse.get_pos()
        if (mouse_button[0] and 
            self.rect.collidepoint(mouse_pos)):
            return True
        else: 
            return False 
            
