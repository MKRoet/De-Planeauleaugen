#-------------------------------------------------------------------------------
# File name: houseclasses.py
#
# Authors: Jet van den Berg, Maurice Roet, Chantal Stangenberger
#
# Course: Heuristics
#
# This program creates classes for HouseList and House (with the child classes
# Familyhouse, Bungalow and Maison). Both have their own methods to check for
# overlap, distance and score.
#-------------------------------------------------------------------------------

from functions import *
import math

#-------------------------------------------------------------------------------

width_map = 180
height_map = 160
percentage_familyhouse = 0.6
percentage_bungalow = 0.25
percentage_maison = 0.15

#-------------------------------------------------------------------------------

class HouseList:
    """HouseList holds and updates the houseList, calculates amount of
    house types, and checks for map bounds and overlap for every house in list.
    Returns distance and score for total of houseList."""

    # Initializes class HouseList, computes total amount of each house type.
    def __init__(self, total_houses):
        self.houseList=[]
        self.fh_amount = int(float(total_houses) * percentage_familyhouse)
        self.bgl_amount = int(float(total_houses) * percentage_bungalow)
        self.ms_amount = int(float(total_houses) * percentage_maison)

        # Iterates over every house type, generates random coordinates,
        # sets coordinates for house type, checks for map bounds and overlap.
        # When True, adds house type to houseList.
        for i in range(self.fh_amount):
            while True:
                x,y = getRandom_coordinates()
                house_type = Familyhouse(x,y)
                if self.MapBounds(house_type) and not self.overlap(house_type):
                    break
            self.houseList.append(house_type)
        for i in range(self.bgl_amount):
            while True:
                x,y = getRandom_coordinates()
                house_type = Bungalow(x,y)
                if self.MapBounds(house_type) and not self.overlap(house_type):
                    break
            self.houseList.append(house_type)
        for i in range(self.ms_amount):
            while True:
                x,y = getRandom_coordinates()
                house_type = Maison(x,y)
                if self.MapBounds(house_type) and not self.overlap(house_type):
                    break
            self.houseList.append(house_type)
            self.getScore(house_type)

    # Checks if house is within map.
    def MapBounds(self, house_type):
        if (house_type.x - house_type.detached < 0):
            return False
        if (house_type.x + house_type.width + house_type.detached > width_map):
            return False
        if (house_type.y - house_type.detached < 0):
            return False
        if (house_type.y + house_type.height + house_type.detached > height_map):
            return False
        return True

    # Checks for every house in houseList if overlap exists.
    def overlap(self, house_type):
        for h in self.houseList:
            if house_type.overlap(h):
                return True
        return False

    # Returns length of houseList.
    def getTotal_houses(self):
        return len(self.houseList)

    # Checks for every house the distance to another house, returns shortest
    # distance.
    def getDistance(self, house_type):
        shortestDistance = 99999999
        for h in self.houseList:
            if h is not house_type:
                free_space = house_type.getDistance(h)
                if free_space < shortestDistance:
                    shortestDistance = free_space
        return shortestDistance

    # Calculates score for every house in houseList, updates sum of score after
    # iteration over every house in houseList.
    def getScore(self, house_type):
        sumScore = 0
        for h in self.houseList:
            if h is not house_type:
                score = House.getScore(self, h)
                sumScore += score
        return sumScore

class House(object):
    """A House checks for overlap and distance to another house, and calculates
    score based on extra detached distance from other houses. Houses have the
    following properties:

    Attributes:
        base_sale_price: An integer representing the house's price.
        width: The house's width in meters.
        height: The house's heigth (depth) in meters.
        detached: The house's required free space in meters.
        percentage_addedvalue: A float representing the house's added value per
            meter extra detached distance.
    """

    base_sale_price = 0
    width = 0
    height = 0
    detached = 0
    percentage_addedvalue = 0

    # Initializes class House with x and y.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    # Checks for house if other houses on right, left, top and bottom do not
    # overlap and has correct detached distance to other houses.
    def overlap(self,h):
        if h.x + h.width + h.detached <= self.x and \
           self.x - self.detached >= h.x + h.width:
            return False
        if h.x - h.detached >= self.x + self.width and \
           self.x + self.width + self.detached <= h.x:
            return False
        if h.y + h.height + h.detached <= self.y and \
           self.y - self.detached >= h.y + h.height:
            return False
        if h.y - h.detached >= self.y + self.height and \
           self.y + self.height + self.detached <= h.y:
            return False
        return True

    # Checks what the distance is between walls and corners of houses, returns
    # distance.
    def getDistance(self, house):
        global distance

        # Checks for overlap on horizontal axis.
        if self.y <= house.y <= (self.y + self.height) or \
           self.y <= (house.y + house.height) <= (self.y + self.height):
            if self.x > house.x:  # Left side
                distance = (self.x - house.x) - house.width
            elif self.x < house.x:  # Right side
                distance = (house.x - self.x) - self.width

        # Checks for overlap on vertical axis.
        elif self.x <= house.x <= (self.x + self.width) or \
             self.x <= (house.x + house.width) <= (self.x + self.width):
                if self.y < house.y:  # Top side
                    distance = (house.y - self.y) - self.height
                elif self.y > house.y:  # Bottom side
                    distance = (self.y - house.y) - house.height

        # Checks for overlap on top corners of house using Pythagorean theorem.
        elif (self.y + self.height) < house.y:
            if self.x > house.x:  # Left side
                ab = house.y - (self.y + self.height)
                bc = self.x - (house.x + house.width)
                ac = ab**2 + bc**2
                distance = math.sqrt(ac)
            elif self.x < house.x:  # Right side
                ab = house.y - (self.y + self.height)
                bc = house.x - (self.x + self.width)
                ac = ab**2 + bc**2
                distance = math.sqrt(ac)

        # Checks for overlap on bottom corners of house using Pythagorean
        # theorem.
        elif self.y > (house.y + house.height):
            if self.x > house.x:  # Left side
                ab = self.y - (house.y + house.height)
                bc = self.x - (house.x + house.width)
                ac = ab**2 + bc**2
                distance = math.sqrt(ac)
            elif self.x < house.x:  # Right side
                ab = self.y - (house.y + house.height)
                bc = house.x - (self.x + self.width)
                ac = ab**2 + bc**2
                distance = math.sqrt(ac)

        return distance

    # Calculates score for house based on distance from another house.
    def getScore(self, house):
        detached_extra = HouseList.getDistance(self, house) - house.detached
        totalpercentage_addedvalue = detached_extra * house.percentage_addedvalue
        addedvalue = house.base_sale_price * totalpercentage_addedvalue
        score = house.base_sale_price + addedvalue
        return score

class Familyhouse(House):
    """A Familyhouse of type House, with its own values."""

    def __init__(self,x,y):
         super(Familyhouse,self).__init__(x,y)

    base_sale_price = 285000
    width = 8
    height = 8
    detached = 2
    percentage_addedvalue = 0.03
    color = 'green'

class Bungalow(House):
    """A Bungalow of type House, with its own values."""

    def __init__(self,x,y):
         super(Bungalow,self).__init__(x,y)

    base_sale_price = 399000
    width = 10
    height = 7.5
    detached = 3
    percentage_addedvalue = 0.04
    color = 'yellow'

class Maison(House):
    """A Maison of type House, with its own values."""

    def __init__(self,x,y):
         super(Maison,self).__init__(x,y)

    base_sale_price = 610000
    width = 11
    height = 10.5
    detached = 6
    percentage_addedvalue = 0.06
    color = 'pink'
