# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 20:13:08 2020

@author: Rida
"""
import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.lives = 10000
        self.old_lives = 10000
        self.score = 0