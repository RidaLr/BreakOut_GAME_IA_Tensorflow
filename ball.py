# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:47:17 2020

@author: Rida
"""

import pygame
from random import randint

 
class Ball(pygame.sprite.Sprite):
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()       
        # Set the ball image
        self.image = pygame.image.load('assets/ball.png') 
        self.rect = self.image.get_rect()
        self.radius = 10
        # Game speed    
        self.speed = 8
        self.velocity = [randint(4,8),randint(-8,8)]
        self.rect = self.image.get_rect()
        self.rect.x = 540
        self.rect.y = 550
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
       
          
    def rebound(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

