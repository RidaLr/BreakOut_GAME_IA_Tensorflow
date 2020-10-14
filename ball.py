# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:47:17 2020

@author: Rida LAKSIR
"""

import pygame
from random import randint

 
class Ball(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()       
        # Set the ball image
        self.image = pygame.image.load('assets/ball.png') 
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        # Game speed       
        self.velocity = 5
