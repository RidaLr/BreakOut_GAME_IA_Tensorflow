# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 21:18:27 2020

@author: Rida
"""
import pygame
from ball import Ball
from brick import Brick
from paddle import Paddle
from player import Player


class Game(pygame.sprite.Sprite):
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()   
        self.ball = Ball()
        self.brick = Brick()
        self.paddle = Paddle()
        self.palyer = Player()
        