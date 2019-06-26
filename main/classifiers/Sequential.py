import tensorflow as tf
from tensorflow import keras

import numpy as np


class Sequential:
    """A simple Sequential neural network made of 3 layers"""

    def __init__(self, input_size, output_size):
        """Constructs the network with input layer, output layer and 1 hidden layers wich number of nodes is an average
        between the number of the input layer nodes and the number of the output layer nodes."""

        hidden_layer_size = int((input_size+output_size)/2)

        self._model = keras.Sequential([
            keras.layers.Dense(input_size, activation=tf.nn.relu),
            keras.layers.Dense(hidden_layer_size, activation=tf.nn.relu),
            keras.layers.Dense(output_size, activation=tf.nn.softmax)
        ])

        # Compilation parameters are used when training:
        #   optimizer: this object specifies the training procedure
        #   loss: the loss function of the neural network that has to be minimized
        #   metrics: used to monitor training
        self._model.compile(#optimizer=tf.train.GradientDescentOptimizer(learning_rate=1),
                            optimizer=tf.compat.v1.train.AdamOptimizer(0.001),
                            loss=tf.compat.v1.losses.mean_squared_error,
                            metrics=['accuracy'])

    def fit(self, x_train, y_train, epochs=1):
        """Trains the neural network"""
        self._model.fit(x_train, y_train, epochs=epochs, steps_per_epoch=epochs)

    def predict(self, x_test):
        """Returns prediction for the given testing set"""
        confidences = self._model.predict(x_test)
        predictions = list()

        for confidence in confidences:
            if confidence[0] > confidence[1]:
                predictions.append(0)
            else:
                predictions.append(1)

        return predictions
