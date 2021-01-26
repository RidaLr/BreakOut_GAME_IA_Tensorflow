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
        self.speed = 2
        self.velocity = [randint(2,2),randint(-2,2)]
        self.rect = self.image.get_rect()
        self.rect.x = 540
        self.rect.y = 550
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if (self.rect.y + self.velocity[1]) == self.rect.y:
            if self.rect.y>30:
                self.rect.y-=2

        print("balle y = ",self.rect.y)
        print("velocity y = ", self.velocity[1])

          
    def rebound(self):
        self.velocity[0] = -self.velocity[0]
        x = randint(-2, 2)
        while True:
            x = randint(-2, 2)
            if x != 0:
                self.velocity[1] = x
                break



        #self.velocity[1] = randint(-2,2)

