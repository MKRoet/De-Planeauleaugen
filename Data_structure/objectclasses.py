#-------------------------------------------------------------------------------
# File name: objectclasses.py
#
# Authors: Jet van den Berg, Maurice Roet, Chantal Stangenberger
#
# Course: Heuristics
#
# This file creates classes for ObjectList and MapObjects (with the child
# classes Familyhouse, Bungalow, Maison and Water). Both have their own methods
# to check for overlap, distance and score.
#-------------------------------------------------------------------------------

import random
import math

#-------------------------------------------------------------------------------

# global variables
width_map = 180
height_map = 160
percentage_familyhouse = 0.6
percentage_bungalow = 0.25
percentage_maison = 0.15
percentage_watersurface = 0.2
max_distance = 99999999

#-------------------------------------------------------------------------------

class ObjectList:
    """ObjectList holds and updates the objectList, calculates amount of
    house types and water, generate random coordinates for houses and water in
    the objectList, checks for map bounds and overlap for every house and water
    in the list. Returns distance and score for total of objectList."""

    # Initializes class ObjectList, computes total amount of each house type and
    # water.
    def __init__(self, total_houses):
        self.objectList = []
        self.fh_amount = int(float(total_houses) * percentage_familyhouse)
        self.bgl_amount = int(float(total_houses) * percentage_bungalow)
        self.ms_amount = int(float(total_houses) * percentage_maison)
        self.amount_waterbodies = Water.amount_waterbodies

        # Iterates over every house type and water, generates random coordinates,
        # sets coordinates for house type and water, checks for map bounds and
        # overlap. When True, adds house type or water to objectList.
        for i in range(self.amount_waterbodies):
            while True:
                x,y = self.getRandom_coordinates()
                object_type = Water(x,y)
                if self.mapBounds(object_type) and not self.overlap(object_type):
                    break
            self.objectList.append(object_type)
        for i in range(self.ms_amount):
            while True:
                x,y = self.getRandom_coordinates()
                object_type = Maison(x,y)
                if self.mapBounds(object_type) and not self.overlap(object_type):
                    break
            self.objectList.append(object_type)
        for i in range(self.bgl_amount):
            while True:
                x,y = self.getRandom_coordinates()
                object_type = Bungalow(x,y)
                if self.mapBounds(object_type) and not self.overlap(object_type):
                    break
            self.objectList.append(object_type)
        for i in range(self.fh_amount):
            while True:
                x,y = self.getRandom_coordinates()
                object_type = Familyhouse(x,y)
                if self.mapBounds(object_type) and not self.overlap(object_type):
                    break
            self.objectList.append(object_type)
            self.getScore(object_type)

    # Creates random coordinates.
    def getRandom_coordinates(self):
        x = random.randint(0,180)
        y = random.randint(0,160)
        return ((x,y))

    # Checks if house or water is within map.
    def mapBounds(self, object_type):
        if (object_type.x - object_type.detached < 0):
            return False
        if (object_type.x + object_type.width + object_type.detached > width_map):
            return False
        if (object_type.y - object_type.detached < 0):
            return False
        if (object_type.y + object_type.height + object_type.detached > height_map):
            return False
        return True

    # Checks for every house or water in objectList if overlap exists.
    def overlap(self, object_type):
        for i in self.objectList:
            if i is not object_type:
                if object_type.overlap(i):
                    return True
        return False

    # Checks for every house the distance to another house, returns shortest
    # distance.
    def getDistance(self, object_type):
        shortestDistance = max_distance
        for h in self.objectList:
            if h is not object_type:
                if not isinstance(h,Water):
                    free_space = object_type.getDistance(h)
                    if free_space < shortestDistance:
                        shortestDistance = free_space
        return shortestDistance

    # Calculates score for every house in objectList, updates sum of score after
    # iteration over every house in objectList.
    def getScore(self, object_type):
        sumScore = 0
        for h in self.objectList:
            if h is not object_type:
                if not isinstance(h,Water):
                    score = MapObjects.getScore(self, h)
                    sumScore += score
        return sumScore

class MapObjects(object):
    """A MapObjects checks for overlap and distance to another house, and
    calculates score based on extra detached distance from other houses.
    MapObjects have the following properties:

    Attributes:
        base_sale_price: An integer representing the house's price.
        width: The house's width in meters.
        height: The house's heigth (depth) in meters.
        detached: The house's required free space in meters.
        percentage_addedvalue: A float representing the house's added value per
            meter extra detached distance.
        color: The color of a specific house or water.
    """

    base_sale_price = 0
    width = 0
    height = 0
    detached = 0
    percentage_addedvalue = 0

    # Initializes class MapObjects with x and y.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    # Checks for house or water (self) if other houses or water (item) on right,
    # left, top, bottom and corners do not overlap and has correct detached
    # distance to other houses or water. False = no overlap.
    def overlap(self, item):
        if self.x + self.width + self.detached <= item.x and \
            item.x - item.detached >= self.x + self.width:
            return False
        if self.x - self.detached >= item.x + item.width and \
            item.x + item.width + item.detached <= self.x:
            return False
        if self.y + self.height + self.detached <= item.y and \
            item.y - item.detached >= self.y + self.height:
            return False
        if self.y - self.detached >= item.y + item.height and \
            item.y + item.height + item.detached <= self.y:
            return False

        # Gets distance between corners of two houses.
        distanceHouses = self.getDistance(item)

        # Checks between left upper corner (self) and right lower corner (item)
        # for overlap and correct distance per house.
        if self.x >= item.x + item.width and self.y + self.height <= item.y:
            if distanceHouses >= self.detached and distanceHouses >= item.detached:
                return False

        # Checks between right upper corner (self) and left lower corner (item)
        # for overlap and correct distance per house.
        if self.x + self.width <= item.x and self.y + self.height >= item.y:
            if distanceHouses >= self.detached and distanceHouses >= item.detached:
                return False

        # Checks between left lower corner (self) and right upper corner (item)
        # for overlap and correct distance per house.
        if self.x >= item.x + item.width and self.y >= item.y + item.height:
            if distanceHouses >= self.detached and distanceHouses >= item.detached:
                return False

        # Checks between right lower corner (self) and left upper corner (item)
        # for overlap and correct distance per house.
        if self.x + self.width <= item.x and self.y >= item.y + item.height:
            if distanceHouses >= self.detached and distanceHouses >= item.detached:
                return False

        return True

    # Checks what the distance is between walls and corners of houses, returns
    # distance.
    def getDistance(self, house):
        distance = 0.0

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
                if self.y < house.y:  # Upper side
                    distance = (house.y - self.y) - self.height
                elif self.y > house.y:  # Lower side
                    distance = (self.y - house.y) - house.height

        # Checks for overlap on upper corners of house using Pythagorean theorem.
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

        # Checks for overlap on lower corners of house using Pythagorean
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
        detached_extra = ObjectList.getDistance(self, house) - house.detached
        totalpercentage_addedvalue = detached_extra * house.percentage_addedvalue
        addedvalue = house.base_sale_price * totalpercentage_addedvalue
        score = house.base_sale_price + addedvalue
        return score

class Familyhouse(MapObjects):
    """A Familyhouse of type MapObjects, with its own values."""

    base_sale_price = 285000
    width = 8
    height = 8
    detached = 2
    percentage_addedvalue = 0.03
    color = 'mediumseagreen'
    edgecolor = 'black'

    def __init__(self, x,y):
        super(Familyhouse, self).__init__(x,y)

class Bungalow(MapObjects):
    """A Bungalow of type MapObjects, with its own values."""

    base_sale_price = 399000
    width = 10
    height = 7.5
    detached = 3
    percentage_addedvalue = 0.04
    color = 'gold'
    edgecolor = 'black'

    def __init__(self, x,y):
        super(Bungalow, self).__init__(x,y)

class Maison(MapObjects):
    """A Maison of type MapObjects, with its own values."""

    base_sale_price = 610000
    width = 11
    height = 10.5
    detached = 6
    percentage_addedvalue = 0.06
    color = 'lightcoral'
    edgecolor = 'black'

    def __init__(self, x,y):
        super(Maison, self).__init__(x,y)

class Water(MapObjects):
    """Water of type MapObjects, with its own values."""

    # Random amount of waterbodies, between 1 and 4.
    amount_waterbodies = random.randint(1,4)

    # Surface for every individual waterbody, is 20% of total surface of map.
    surface_waterbody = (((width_map * height_map) * percentage_watersurface) \
        / amount_waterbodies)

    # Generates the ratio for the waterbodies, ratio can be 1:1, 1:2, 1:3 or 1:4.
    generate_ratio = random.randint(1,4)

    width = math.sqrt(surface_waterbody/generate_ratio)
    height = width * generate_ratio
    color = 'lightskyblue'
    edgecolor = None

    def __init__(self, x,y):
        super(Water, self).__init__(x,y)
