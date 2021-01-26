import random
import numpy as np

from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import RMSprop
from tensorflow.keras.callbacks import TensorBoard


class Ai:

    def __init__(self, game):
        self.NAME = "Test2"
        self.tensorboard = TensorBoard(log_dir="tensorflow/logdir/{}".format(self.NAME), histogram_freq=0,
                                       write_graph=True,
                                       write_images=False,
                                       update_freq="epoch",
                                       profile_batch=2,
                                       embeddings_freq=0,
                                       embeddings_metadata=None
                                       )
        self.game = game
        self.gamma = 0.9
        self.game_over = 0
        self.model = Sequential()
        self.model.add(Dense(150, kernel_initializer='lecun_uniform'))
        self.model.add(Activation('relu'))
        self.model.add(Dense(168, kernel_initializer='lecun_uniform'))
        self.model.add(Activation('relu'))
        self.model.add(Dense(2, kernel_initializer='lecun_uniform'))
        self.model.add(Activation('linear'))
        self.rms = RMSprop()
        self.model.compile(loss='mse', optimizer=self.rms)
        self.qval = None
        self.action = None

    def receive_state(self, state, epsilon):
        # Set up qval by adding current state to the model
        self.qval = self.model.predict(state.reshape(1, 3), batch_size=1, callbacks=[self.tensorboard])
        # We set an epsilon - an ever decreasing number
        # If a random number is less than the epsilon we do a random action
        # If greater we use the qval to decide the action
        # Epsilon stops decreasing at 0.1 so there is always chance of a random action
        # Te random chance means novel action can still happen
        if random.random() < epsilon:
            self.action = np.random.randint(0, 2)
        else:
            self.action = (np.argmax(self.qval))
        # Take an action now based on the above
        self.take_action(self.action)
        print(f"Qval is {self.qval}")

    def update_state(self, state):
        # Now we check the reward for our action
        reward = self.game.get_reward()
        # Lets find the maximum qvalue that was in the array
        max_q = np.max(self.qval)
        # If no reward (no win or lose this cycle)
        # Set the update to be based on the maximum Q value (a decreased value)
        if reward == 0:
            update = reward + (self.gamma * max_q)
            self.game_over = 0
        # If not the reward itself is the update
        else:
            update = reward
            self.game_over = 1
        # create an empty numpy array y
        y_val = np.zeros((1, 2))
        # make y a copy of qval (original model output)
        y_val[:] = self.qval[:]
        # update the up or down value of the qval with the update value calculated above
        # Makes the qval based on the reward
        y_val[0][self.action] = update
        # Update the model based on this
        self.model.fit(state.reshape(1, 3), y_val, batch_size=10, epochs=1, verbose=1, callbacks=[self.tensorboard])
        print(f"Yval is {y_val}")
        print(update)
        print('-' * 50)

    def take_action(self, action):
        if action == 0:
            self.game.paddle.move_right()
        else:
            self.game.paddle.move_left()
