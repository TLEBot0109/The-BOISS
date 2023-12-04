import pygame
from network import Network
from Player import player
from bullet import Bullet

width = int(500)
height = int(500)
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("client")

clientNumber = 0

def drawWindow(win, Player , Player2):
    win.fill((255, 255, 255))
    Player.draw(win)
    Player2.draw(win)
    pygame.display.update()

                                                                                                                                                                                          
def main():
    run = True
    n=Network()
    p1 = n.getP()
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        p2 = n.send(p1)

        for e in p1.bul:
            Bullet.update(e)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        for e in p1.bul:
            Bullet.draw(e)
            
        p1.move()
        drawWindow(win, p1 , p2)


main()