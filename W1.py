from abc import ABCMeta, abstractmethod
#import random
from F1 import *


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

class HouseList:

    def __init__(self, total_buildings):
        self.houseList=[]
        self.fh_amount = int(float(total_buildings) * 0.6)
        self.bgl_amount = int(float(total_buildings) * 0.25)
        self.ms_amount = int(float(total_buildings) * 0.15)

        for i in range(self.fh_amount):
            x,y = Randomize()
            house_type = Familyhouse(x,y)
            self.houseList.append(house_type)
        for i in range(self.bgl_amount):
            x,y = Randomize()
            house_type = Bungalow(x,y)
            self.houseList.append(house_type)
        for i in range(self.ms_amount):
            x,y = Randomize()
            house_type = Maison(x,y)
            self.houseList.append(house_type)

    def getTotal_buildings(self):
        return len(self.houseList)

    def draw(self):
        return self.houseList.pop()

class House(object):

    __metaclass__ = ABCMeta

    base_sale_price = 0
    width = 0
    depth = 0
    detached = 0
    x = 0
    y = 0

    def __init__(self, x, y):
        #self.house_type = house_type
        #self.leftLowerX = x
        #self.leftLowerY = y

        #self.rightLowerX = leftLowerX + width
        #self.rightLowerY = y

        #self.leftUpperX = x
        #self.leftUpperY = y + depth

        #self.rightUpperX = x + width
        #self.rightUpperY = y + depth
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


class Familyhouse(House):

    def __init__(self,x,y):
         super(Familyhouse,self).__init__(x,y)

    base_sale_price = 285000
    width = 8
    depth = 8
    detached = 2
    color = 'green'

    def house_type(self):
        return 'familyhome'

class Bungalow(House):

    def __init__(self,x,y):
         super(Bungalow,self).__init__(x,y)

    base_sale_price = 399000
    width = 10
    depth = 7.5
    detached = 3
    color = 'yellow'

    def house_type(self):
        return 'bungalow'

class Maison(House):

    def __init__(self,x,y):
         super(Maison,self).__init__(x,y)

    base_sale_price = 610000
    width = 11
    depth = 10.5
    detached = 6
    color = 'pink'

    def house_type(self):
        return 'maison'

class Water(House):

    # def __init__(self):
    #     House.__init__(self)

    width = 48
    depth = 120
    color = 'blue'
