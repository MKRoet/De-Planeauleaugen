from abc import ABCMeta, abstractmethod
import random
from Functions import *


# class HouseList:
#
#     def __init__(self):
#         self.houseList=[]
#
#     def addHouse(self,house):
#         self.houseList.append(house)
#
#     def getScore(self):
#         sumScore=0
#         for h in self.houseList:
#             sumScore+=h.getScore()
#         return sumScore
#
#
#     def draw(self):
#         pass # ....

class House(object):

    __metaclass__ = ABCMeta

    base_sale_price = 0
    width = 0
    depth = 0
    base_detached = 0
    x = 0
    y = 0

    def __init__(self, x, y):
        self.house_type = house_type
        self.leftLowerX = x
        self.leftLowerY = y

        self.rightLowerX = leftLowerX + width
        self.rightLowerY = y

        self.leftUpperX = x
        self.leftUpperY = y + depth

        self.rightUpperX = x + width
        self.rightUpperY = y + depth

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
        return 'familyhome'

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
