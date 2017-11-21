from abc import ABCMeta, abstractmethod
from randomize import *

# -------------------------------------------------------------------------

# Overkoepelende klasse voor de objecten in het veld.
class House(object):

    # Zorgt ervoor dat er niet een 'House' geinitieerd kan worden.
    __metaclass__ = ABCMeta

    # Vaste kenmerken die ieder huis bezit.
    base_sale_price = 0
    width = 0
    depth = 0
    base_detached = 0

    # Aangeven op welke plek het huis moet komen.
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    # Geeft een string terug met het type huis (familyhome, bungalow of maison).
    @abstractmethod
    def house_type(self):
        pass

# De verschillende subklasses die in het veld komen.
class Familyhome(House):

    base_sale_price = 285000
    width = 8
    depth = 8
    base_detached = 2

def house_type(self):
        return 'familyhome'

class Bungalow(House):

    base_sale_price = 399000
    width = 10
    depth = 7.5
    base_detached = 3

    def house_type(self):
        return 'bungalow'


class Maison(House):

    base_sale_price = 610000
    width = 11
    depth = 10.5
    base_detached = 6

    def house_type(self):
        return 'maison'

class Water(House):

    width = 48
    depth = 120
