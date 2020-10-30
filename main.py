# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:51:54 2020

@author: Rida
"""

import pygame
import math
import sys
from player import Player
from ball import Ball
from game import Game
from paddle import Paddle
from brick import Brick


pygame.init()


# Create graphic interface 
pygame.display.set_caption("BreakOut Game")
screen = pygame.display.set_mode((1080, 620))

#import the background of our game
background = pygame.image.load('assets/bg.jpg')

#import the play button
play_button = pygame.image.load('assets/start.png')
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.55)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# create a surface object for the logo image 
logo = pygame.image.load('assets/logo.png') 

# stores the width of the screen into a variable called width  
width = screen.get_width()  
  
# stores the height of the screen into a variable called height  
height = screen.get_height() 

#Load player
player = Player()

#Load bricks
brick1 = Brick('assets/brick_1.jpg')
brick2 = Brick('assets/brick_2.jpg')
brick3 = Brick('assets/brick_3.jpg')
brick4 = Brick('assets/brick_4.jpg')
brick5 = Brick('assets/brick_5.jpg')
brick6 = Brick('assets/brick_6.jpg')
brick7 = Brick('assets/brick_7.jpg')
brick8 = Brick('assets/brick_8.jpg')
brick9 = Brick('assets/brick_9.jpg')

#A list of bricks objects
brick_list = []

#Add all the bricks into this list
brick_list.append(brick1)
brick_list.append(brick2)
brick_list.append(brick3)
brick_list.append(brick4)
brick_list.append(brick5)
brick_list.append(brick6)
brick_list.append(brick7)
brick_list.append(brick8)
brick_list.append(brick9)
    
    
#Paddle
paddle = Paddle()

#Ball
ball = Ball()

#This will be a list that will contain all the sprites we intend to use in our game.
sprites_list = pygame.sprite.Group()
 
bricks = pygame.sprite.Group()
       
#Load game party
game = Game()

#Draw the objects 
sprites_list = game.draw(bricks ,brick_list, ball, paddle)


#The main
if __name__ == '__main__':
    game.run(screen, background, sprites_list, logo, play_button, play_button_rect, paddle, ball, bricks)
   