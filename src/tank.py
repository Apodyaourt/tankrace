#-*- coding: utf-8 -*-

__author__ = 'Christophe Taillan'
__email__ = 'christophe.taillan@cnes.fr'
__version__ = ''
__date__ = '28/02/2018'
__last_modified__ = '28/02/2018'

import os
import logging
from sklearn.neural_network import MLPClassifier

logger = logging.getLogger(__name__)


class Car():
    def __init__(self):
        """
        Constructor of the Car class
        """
        #: Velocity of the car
        self.velocity = 0.

        # Position of the car
        #: x position
        self.x = 0. 
        #: y position
        self.y = 0. 

        #: Radius of the circle car
        self.radius = 1. 

        #: Neural network associated to the car
        self.neural_network = MLPClassifier()

        #: Distance runned by the car
        self.distance = 0.


    def update_position(self, a, b, c):
        self.neural_network.predict()
        self.x = 0.
        self.y = 0.
