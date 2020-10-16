# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 23:39:23 2020

@author: Rida LAKSIR
"""

import pygame
 

class Brick(pygame.sprite.Sprite):
   
    def __init__(self, image_brick):
     
        super().__init__()
        # Set the brick image
        self.image = pygame.image.load(image_brick) 
        self.rect = self.image.get_rect()