import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from Woningen import *
import math
import random

def Randomize():
    x = random.randint(0,180)
    y = random.randint(0,160)

def PlotMap():
    plt.grid()
    plt.show()


# def drawHouses():
#     print(house_lists)
#
    # for house in house_lists:
    #
    #     if house == 'fh':
    #         house_type = Familyhouse
    #         color = 'green'
    #
    #     if house == 'bgl':
    #         house_type = Bungalow
    #         color = 'yellow'
    #
    #     if house == 'ms':
    #         house_type = Maison
    #         color = 'pink'
    #
    #     temp = patches.Rectangle((Randomize()), house_type.width, house_type.depth, facecolor=color, edgecolor='black')
    #     ax.add_patch(temp)





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
#
#     def draw(self):
#         pass # ....
#
# def contraintCheck(self,houseList):
#     for h in houseList:
#         if self.name!=h.name:
#             pass
#             #distance=....
#     return True
#
# def getShortestDistance(self,HL):
#     shortestDistance=9999999999
#     for h2 in HL.houseList:
#         d=self.getDistane(h2)
#         if d<shortestDistance:
#             shortestDistance=d
#     return shortestDistance
#
#
# def getDistance(self,h2):
#
#     return 347
#
# def getScore(self):
#     return 129
#
# # Geeft een string terug met het huistype
# @abstractmethod
# def house_type(self):
#     pass

# def getX():

# from classes import *
# from plattegrondMatplotlib import *
#
# def contraintCheck(self,houseList):
#     for h in houseList:
#         if self.name != h.name:
#             pass
#             #distance=....
#     return True
#
# def overlapCheck(x, y, width, height, House):
#     overlapCheck = False
#     for House in house_lists:
#
#         # Check if space between x.begin and x.end are overlapping
#         # Check between two houses: self and House(nr)
#         xStartSelf = self.x
#         xEndSelf = self.x + self.width
#         lengthSelf = xEndSelf - xStartSelf
#
#         yStartSelf = self.y
#         yEndSelf = self.y + self.height
#         depthSelf = yEndSelf - yStartSelf
#
#         if xStartSelf <= x <= xEndSelf \
#         and yStartself <= y <= yEndSelf
#             overlapCheck = True
#
#     return overlapCheck
#
#         # if x > House.x - House.width
#         # and
#         # x < House.x + House.width
#         # and
#         # y >
#         # and
#         # y <
