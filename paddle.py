# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:30:09 2020

@author: Rida LAKSIR
"""

import pygame

width = 980

class Paddle(pygame.sprite.Sprite):
    
    def __init__(self):

        super().__init__()
        self.velocity = 50
        self.image = pygame.image.load('assets/paddle.png')      
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 580

    def move_right(self):
        self.rect.x += self.velocity
        
        if self.rect.x > width: 
          self.rect.x = width

    def move_left(self):
        self.rect.x -= self.velocity
	    
        if self.rect.x < 0:
          self.rect.x = 0

    