from abc import ABCMeta, abstractmethod
import random

class House(object):

    __metaclass__ = ABCMeta

    base_sale_price = 0
    width = 0
    depth = 0
    base_detached = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def house_type(self):
        pass

class Familyhouse(House):

    # def __init__(self):
    #     House.__init__(self)

    base_sale_price = 285000
    width = 8
    depth = 8
    base_detached = 2

    def house_type(self):
        return 'familyhouse'

class Bungalow(House):

    # def __init__(self):
    #     House.__init__(self)

    base_sale_price = 399000
    width = 10
    depth = 7.5
    base_detached = 3

    def house_type(self):
        return 'bungalow'

class Maison(House):

    # def __init__(self):
    #     House.__init__(self)

    base_sale_price = 610000
    width = 11
    depth = 10.5
    base_detached = 6

    def house_type(self):
        return 'maison'

class Water(House):

    # def __init__(self):
    #     House.__init__(self)

    width = 48
    depth = 120
