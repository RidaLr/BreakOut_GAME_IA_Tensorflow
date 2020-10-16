# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:51:54 2020

@author: Rida LAKSIR
"""

#Manage the imports
import pygame
import math
from player import Player
from ball import Ball
from game import Game
from paddle import Paddle
from brick import Brick


pygame.init()


# Create graphic interface 

pygame.display.set_caption("BreakOut Game")
screen = pygame.display.set_mode((1080, 620))

# white color  
color = (255,255,255) 

#import the background of our game
background = pygame.image.load('assets/bg_3.png')

#import the play button
play_button = pygame.image.load('assets/start.png')
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.55)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# create a surface object, logo is drawn on it. 
logo = pygame.image.load('assets/logo.png') 

# stores the width of the screen into a variable called width  
width = screen.get_width()  
  
# stores the height of the screen into a variable called height  
height = screen.get_height() 

#Load player
player = Player()

#Load game party
game = Game()

#Load ball
ball = Ball()

#Load brick
brick = Brick()

#Load paddle
paddle = Paddle()

running = True

while running:
    
    
    # if the game not started yet we show those images
    screen.blit(background, (0, 0))
    screen.blit(logo, (345, 150))
    screen.blit(play_button, play_button_rect)
    screen.blit(game.ball.image, game.ball.rect)
    screen.blit(game.brick.image, game.brick.rect)
    screen.blit(game.paddle.image, game.paddle.rect)
    
    # else we will show the game interface and desable those images
    
    
    
    
    
    
    
    pygame.display.flip()
        
    # stores the (x,y) coordinates into a tuple  
    mouse = pygame.mouse.get_pos() 
    
    #check if the mouse is clicked on the quit button in the quit button of the window
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running == False
            pygame.quit()
    
        #checks if a mouse is clicked  
        if event.type == pygame.MOUSEBUTTONDOWN:  
              
            #if the mouse is clicked on the Play button the game will start  
            if (play_button_rect.collidepoint(event.pos)):
                #Start the game
                #game.is_playing = True
                print("start the game")
                
        #check if the player touch a key button
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game.paddle.move_right()
            if event.key == pygame.K_LEFT:
                game.paddle.move_left()
                
    
    # updates the frames of the game  
    pygame.display.update() 