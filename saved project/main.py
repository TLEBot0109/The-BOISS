#!/usr/bin/env python3
import pygame
from player import Player
from bullet import Bullet
import sys

pygame.init()
width = int(500)
height = int(500)
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Retard game") 
BG1 = pygame.transform.scale(pygame.image.load("player1_win.jpg"),(width, height))
def draw_p1_win():
    win.blit(BG1,(0,0))
    pygame.display.update()

BG2 = pygame.transform.scale(pygame.image.load("player2_win.jpg"),(width, height))
def draw_p2_win():
    win.blit(BG2,(0,0))
    pygame.display.update()

def draw_start_menu():
    win.fill((0, 0, 0))
    font = pygame.font.SysFont('arial',40)
    title = font.render('My Game', True, (255, 255, 255))
    start_button = font.render('Start', True, (255, 255, 255))
    win.blit(title, (width/2 - title.get_width()/2, 
                     height/2 - title.get_height()/2-30))
    win.blit(start_button, (width/2 - start_button.get_width()/2, 
                            height/2 + start_button.get_height()/2-30))
    pygame.display.update()

def draw_game_over_screen():
   font = pygame.font.SysFont('arial', 40)
   restart_button = font.render('R - Restart', True, (0, 255, 255))
   win.blit(restart_button, (width/2 - restart_button.get_width()/2, height/1.9 + restart_button.get_height()))
   pygame.display.update()

def Win(win, Player, Player2):
    win.fill((0, 0, 0))
    Player.draw(win)
    Player2.draw(win)
    pygame.display.update()
    
def check(bullet, player):
    if(bullet.pos[0]>=player.x-28 and bullet.pos[0]<=player.x+28 
        and bullet.pos[1]>=player.y-28 and bullet.pos[1]<=player.y+28):
            bullet.pos=(1000,1000)
            player.health -= bullet.damage

#def final_screen() :
def main():
    gameRunning = True
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
    bullets_p1 = []
    bullets_p2 = []
    p_1 = Player(50, 50, 50, 50, (0, 255, 0),200,100)
    p_2 = Player(450, 450, 50, 50, (0, 0, 255),200,100)
    clock = pygame.time.Clock()
    pre_time1=pygame.time.get_ticks()
    pre_time2=pygame.time.get_ticks()
    game_state="start_menu"
    draw_start_menu()
    end = False

    while gameRunning:
        clock.tick(60)
        mouse_button = pygame.mouse.get_pressed(num_buttons = 3)
        key = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False
                pygame.quit()

        if game_state == "start_menu":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                game_state = "game"
            else:
                continue

        if key[pygame.K_ESCAPE]:
            pygame.quit() 
            exit()

        if end == True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                gameRunning = True
                bullets_p1 = []
                bullets_p2 = []
                p_1 = Player(50, 50, 50, 50, (0, 255, 0),200,100)
                p_2 = Player(450, 450, 50, 50, (0, 0, 255),200,100)
                pre_time1=pygame.time.get_ticks()
                pre_time2=pygame.time.get_ticks()
                game_state="start_menu"
                draw_start_menu()
                end = False
            continue
                

        Win(win, p_1, p_2) 
        if mouse_button[0]:
            cur_time1=pygame.time.get_ticks()
            if(cur_time1-pre_time1>p_1.delay):
                pre_time1=cur_time1
                bullets_p1.append(Bullet(p_1.x,p_1.y,10))
        if mouse_button[2]:
            cur_time2=pygame.time.get_ticks()
            if(cur_time2-pre_time2>p_2.delay):
                pre_time2=cur_time2
                bullets_p2.append(Bullet(p_2.x,p_2.y,10))
                

        for bullets in bullets_p1[:]:
            check(bullets, p_2)
            bullets.update(bullets_p1)
            
        for bullets in bullets_p2[:]:
            check(bullets, p_1)
            bullets.update(bullets_p2)
            

        

        for bullet in bullets_p1:
            bullet.draw(win)
        for bullet in bullets_p2:
            bullet.draw(win)
             
        p_1.move()
        p_2.move()
        pygame.display.flip()
        if(p_1.health<=0 or p_2.health<=0):
            end = True
            if(p_1.health<=0):
                draw_p2_win()
            else:
                draw_p1_win()
            draw_game_over_screen()

if __name__ == "__main__":
    main()