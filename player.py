# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 20:13:08 2020

@author: Rida LAKSIR
"""
import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.score = 100
        self.lives = 3