import pygame
from player import Player
from player2 import Player2
from bullet import Bullet

width = int(500)
height = int(500)
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("client")   

def Win(win, Player, Player2):
    win.fill((0, 0, 0))
    Player.draw(win)
    Player2.draw(win)
    pygame.display.update()
    
def main():
    run = True
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
    bullets_p1 = []
    bullets_p2 = []
    p_1 = Player(25, 25, 50, 50, (0, 255, 0))
    p_2 = Player2(500, 500, 50, 50, (0, 0, 255))
    clock = pygame.time.Clock()
    
    while run == True:
        clock.tick(60)
        mouse_button = pygame.mouse.get_pressed(num_buttons = 3)
        key = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()     
        Win(win, p_1, p_2) 
        if mouse_button[0]:
            bullets_p1.append(Bullet(p_1.x,p_1.y,9))
        if mouse_button[2]:
            bullets_p2.append(Bullet(p_2.x,p_2.y,9))
                
        for bullets in bullets_p1[:]:
            bullets.update(bullets_p1)
        for bullets in bullets_p2[:]:
            bullets.update(bullets_p2)
            

        for bullet in bullets_p1:
            bullet.draw(win)
        for bullet in bullets_p2:
            bullet.draw(win)
             
        p_1.move()
        p_2.move()
        pygame.display.flip()

main()