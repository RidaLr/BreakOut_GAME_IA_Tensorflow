# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 21:18:27 2020

@author: Rida
"""
import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"
import pygame
import math
import random
import numpy as np
from ball import Ball
from brick import Brick
from paddle import Paddle
from player import Player
from ai import Ai
from tensorflow import keras
from random import randint
import tensorflow as tf
from tensorflow import keras

import keras
import pydot
import pydotplus
from pydotplus import graphviz
from keras.utils.vis_utils import plot_model
from keras.utils.vis_utils import model_to_dot
from tensorflow.keras.callbacks import TensorBoard

keras.utils.vis_utils.pydot = pydot


class Game:

    def __init__(self):
        # Call the parent class (Sprite) constructor
        self.is_playing = False
        self.is_playing_tensorflow = False
        self.ball = Ball()
        self.paddle = Paddle()
        self.player = Player()
        self.tensorflowIA = Ai(self)
        self.epsilon = 1

    def score(self, screen):
        font = pygame.font.Font(None, 74)
        score = font.render("Score: " + str(self.player.score), 1, (255, 255, 255))
        screen.blit(score, (20, 10))

    def lives(self, screen):
        # draw score on the canvas
        font = pygame.font.Font(None, 74)
        lives = font.render("Lives: " + str(self.player.lives), 1, (255, 255, 255))
        screen.blit(lives, (650, 10))

    def game_over(self, screen):

        font = pygame.font.Font(None, 74)
        game_over = font.render("GAME OVER", 1, (255, 255, 255))
        screen.blit(game_over, (250, 300))

    def win_game(self, screen):

        font = pygame.font.Font(None, 74)
        game_over = font.render("You won the game", 1, (255, 255, 255))
        screen.blit(game_over, (250, 300))

    def draw_menu(self, screen, logo, play_button, play_button_rect, play_button_tensorflow, play_button_rect2):
        screen.blit(logo, (345, 150))
        screen.blit(play_button, play_button_rect)
        screen.blit(play_button_tensorflow, play_button_rect2)

    def draw(self, all_bricks, brick_list, ball, paddle):

        all_sprites_list = pygame.sprite.Group()

        y = 60
        for obj in brick_list:
            for i in range(14):
                rand = random.randint(1, 9)
                if rand == 1:
                    brick = Brick('assets/brick_1.jpg')
                elif rand == 2:
                    brick = Brick('assets/brick_2.jpg')
                elif rand == 3:
                    brick = Brick('assets/brick_3.jpg')
                elif rand == 4:
                    brick = Brick('assets/brick_4.jpg')
                elif rand == 5:
                    brick = Brick('assets/brick_5.jpg')
                elif rand == 6:
                    brick = Brick('assets/brick_6.jpg')
                elif rand == 7:
                    brick = Brick('assets/brick_7.jpg')
                elif rand == 8:
                    brick = Brick('assets/brick_8.jpg')
                elif rand == 9:
                    brick = Brick('assets/brick_9.jpg')
                brick.rect.x = 10 + i * 75
                brick.rect.y = y
                if brick.image_src == 'assets/brick_1.jpg':
                    brick.incassable = 1

                all_sprites_list.add(brick)
                all_bricks.add(brick)

            y += 27

        # Add the paddle to the list of sprites
        all_sprites_list.add(paddle)
        all_sprites_list.add(ball)

        return all_sprites_list

    def play_music(self):
        pygame.mixer.music.load("assets/music/ctr_ingame.mp3")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

    def prepare_data(self, data_hash):
        array = list(data_hash.values())[:3]
        numpy_array = np.array(array)
        return numpy_array

    def update_epsilon(self):
        if self.epsilon > 0.1:
            self.epsilon -= 0.00001

    def get_reward(self):
        if self.player.lives - self.player.old_lives > 0:
            reward = -700
            self.player.old_lives = self.player.lives
        elif self.ball.rect.colliderect(self.paddle):
            reward = 700
            self.player.old_lives = self.player.lives
        else:
            reward = 0
        return reward

    def output_data(self):
        output = {"r": self.paddle.rect.x,
                  "bx": self.ball.rect.x,
                  "by": self.ball.rect.y,
                  "score": self.player.lives}
        return output

    def run(self, screen, background, all_sprites_list, logo, play_button, play_button_rect, play_button_tensorflow,
            play_button_rect2, paddle, ball, all_bricks):
        running = True
        tf.keras.backend.clear_session()

        # Launch the graph in a session.
        #sess = tf.compat.v1.Session()
        # Create a summary writer, add the 'graph' to the event file.


        # self.play_music()
        action = -1
        is_starting = True
        self.ball = ball
        self.paddle = paddle

        while running:

            # stores the (x,y) coordinates into a tuple
            mouse = pygame.mouse.get_pos()

            # if the game not started yet we show those images
            screen.blit(background, (0, 0))

            # else we will show the game interface and desable those images
            if self.is_playing:
                self.paddle.velocity = 2
                print("is player true")
                all_sprites_list.draw(screen)
                all_sprites_list.update()

                # Check if the ball is rebounding against any of the 4 walls:
                if self.ball.rect.x >= 1040:
                    self.ball.velocity[0] = -self.ball.velocity[0]
                if self.ball.rect.x <= 0:
                    self.ball.velocity[0] = -self.ball.velocity[0]
                if self.ball.rect.y > 580:

                    self.ball.rect.x = 540
                    self.ball.rect.y = 550
                    self.paddle.rect.x = 510
                    self.paddle.rect.y = 580

                    self.player.lives -= 1
                    is_starting = True

                    if self.player.lives == 0:
                        # Display Game Over Message
                        self.game_over(screen)
                        pygame.display.flip()
                        # Wait 5 seconds before closing the game
                        pygame.time.wait(5000)
                        # Stop the Game
                        running = False

                if self.ball.rect.y < 40:
                    self.ball.velocity[1] = -self.ball.velocity[1]

                # Detect collisions between the ball and the paddle
                if pygame.sprite.collide_mask(self.ball, self.paddle):
                    self.ball.rect.x -= self.ball.velocity[0]
                    self.ball.rect.y -= self.ball.velocity[1]
                    self.ball.rebound()

                # Detect the collisions between the ball and the bricks 
                brick_collision_list = pygame.sprite.spritecollide(self.ball, all_bricks, False)
                for brick in brick_collision_list:

                    if brick.incassable == 0:
                        self.ball.rebound()
                        self.player.score += 1
                        brick.kill()
                    else:
                        self.ball.rebound()

                # Check if there is no bricks
                if len(all_bricks) == 0:
                    print(len(all_bricks))
                    # Display 'you won the game' message
                    self.win_game(screen)
                    pygame.display.flip()
                    # Wait 5 seconds before closing the game
                    pygame.time.wait(5000)
                    # Stop the Game
                    running = False

                # Draw the score
                self.score(screen)
                # Draw the lives 
                self.lives(screen)

                # updates the frames of the game  
                pygame.display.update()

                # wait to press space key to launch the game
                while is_starting:
                    pygame.display.update()
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN:
                        is_starting = False
                        continue

            # else we will show the game interface and desable those images
            elif self.is_playing_tensorflow:
                # self.tensorflowIA.model = keras.models.load_model('test.h5')
                self.paddle.velocity = 50
                self.tensorflowIA.receive_state(self.prepare_data(self.output_data()), self.epsilon)

                all_sprites_list.draw(screen)
                all_sprites_list.update()

                # Check if the ball is rebounding against any of the 4 walls:
                if self.ball.rect.x >= 1040:
                    self.ball.velocity[0] = -self.ball.velocity[0]
                if self.ball.rect.x <= 0:
                    self.ball.velocity[0] = -self.ball.velocity[0]
                if self.ball.rect.y > 580:
                    self.ball.velocity[1] = -self.ball.velocity[1]
                    self.player.lives -= 1
                    if self.player.lives == 0:
                        # Display Game Over Message
                        self.game_over(screen)
                        pygame.display.flip()
                        # Wait 5 seconds before closing the game
                        pygame.time.wait(5000)
                        # Stop the Game
                        self.tensorflowIA.model.save('dqn_model_breakout.h5')
                        running = False

                if self.ball.rect.y < 40:
                    self.ball.velocity[1] = -self.ball.velocity[1]

                # Detect collisions between the ball and the paddle
                if pygame.sprite.collide_mask(self.ball, paddle):
                    self.ball.rect.x -= self.ball.velocity[0]
                    self.ball.rect.y -= self.ball.velocity[1]
                    self.ball.rebound()

                # Detect the collisions between the ball and the bricks
                brick_collision_list = pygame.sprite.spritecollide(self.ball, all_bricks, False)
                for brick in brick_collision_list:
                    if brick.incassable == 0:
                        self.ball.rebound()
                        self.player.score += 1
                        brick.kill()
                    else:
                        self.ball.rebound()

                """
                # Check if there is no bricks
                if len(all_bricks) == 0:
                    print(len(all_bricks))
                    # Display 'you won the game' message
                    self.win_game(screen)
                    pygame.display.flip()
                    # save the model
                    self.tensorflowIA.model.save('dqn_model_breakout.h5')
                    # Wait 5 seconds before closing the game
                    pygame.time.wait(5000)
                    # Stop the Game
                    running = False
                """

                # Draw the score
                self.score(screen)
                # Draw the lives
                self.lives(screen)
                # updates the frames of the game
                pygame.display.update()

                self.tensorflowIA.update_state(self.prepare_data(self.output_data()))
                self.update_epsilon()
                print(self.epsilon)
                print(self.output_data())
                # print("PaddleX : ", self.paddle.rect.x)
                # print("PaddleY : ", self.paddle.rect.y)

                # updates the frames of the game
                pygame.display.update()

                # The game is not already started, show the menu  
            else:
                self.draw_menu(screen, logo, play_button, play_button_rect, play_button_tensorflow, play_button_rect2)

            pygame.display.flip()
            pygame.key.set_repeat(1, 1)

            # check if the mouse is clicked on the quit button in the quit button of the window
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running == False

                    dot_img_file = 'model_1.png'
                    tf.keras.utils.plot_model(self.tensorflowIA.model, to_file=dot_img_file, show_shapes=True)
                    #self.writer = tf.summary.create_file_writer('tensorflow/logdir')

                    self.tensorflowIA.model.save('dqn_model_breakout.h5')
                    pygame.quit()

                # checks if a mouse is clicked
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # if the mouse is clicked on the Play button the game will start
                    if (play_button_rect.collidepoint(event.pos)):
                        # Start the game
                        self.is_playing = True

                    if (play_button_rect2.collidepoint(event.pos)):
                        # Start the game
                        self.is_playing_tensorflow = True

                # check if the player touch a key button
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.is_playing = False
                        self.is_playing_tensorflow = False
                    if event.key == pygame.K_RIGHT:
                        self.paddle.move_right()
                    if event.key == pygame.K_LEFT:
                        self.paddle.move_left()

        pygame.quit()
