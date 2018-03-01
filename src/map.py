#-*- coding: utf-8 -*-

__author__ = 'Christophe Taillan'
__email__ = 'christophe.taillan@cnes.fr'
__version__ = ''
__date__ = '28/02/2018'
__last_modified__ = '28/02/2018'

import os
import logging
import importlib

logger = logging.getLogger(__name__)


class Map():
    def __init__(self):
        """
        Constructeur de la classe Product

        :param id: Identifiant du produit pour le projet
        """
        self.velocity = 1.
        
