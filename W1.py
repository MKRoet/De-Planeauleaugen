from abc import ABCMeta, abstractmethod
from F1 import *

class HouseList:

    def __init__(self, total_buildings):
        self.houseList=[]
        self.fh_amount = int(float(total_buildings) * 0.6)
        self.bgl_amount = int(float(total_buildings) * 0.25)
        self.ms_amount = int(float(total_buildings) * 0.15)

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

    def MapBounds(self, house_type):
        if (house_type.x - house_type.detached < 0):
            # print("x1:"+str(house_type.x) + " " + str(house_type.detached))
            return False
        if (house_type.x + house_type.width + house_type.detached > 180):
            return False
        if (house_type.y - house_type.detached < 0):
            return False
        if (house_type.y + house_type.depth + house_type.detached > 160):
            return False

        return True

    def overlap(self, house_type):
        for h in self.houseList:
            if house_type.overlap(h):
                return True
        return False

    def getTotal_buildings(self):
        return len(self.houseList)

    def draw(self):
        return self.houseList.pop()

    def getDetached(self):
        return self.houseList

class House(object):

    __metaclass__ = ABCMeta

    base_sale_price = 0
    width = 0
    depth = 0
    detached = 0
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def overlap(self,h):
        # print("h.x:"+str(h.x) + " self.x:" + str(self.x)+" self.width:"+str(self.width))
        # print("h.y:"+str(h.y) + " self.y:" + str(self.y)+" self.depth:"+str(self.depth))
        if h.x+h.width<self.x:
            return False
        if h.x>self.x+self.width:
            return False
        if h.y+h.depth<self.y:
            return False
        if h.y>self.y+self.depth:
            return False
        return True

    def testOverlap():
        m1=Maison(0,0)
        m2=Maison(3,2)
        return m1.overlap(m2)

    # def getShortestDistance(self, HL):
    #
    #     shortestDistance=9999999999
    #     for h2 in HL.houseList:
    #         d=self.getDistance(h2)
    #         if d<shortestDistance:
    #             shortestDistance=d
    #     return shortestDistance
    #
    # def getDistance(self, house):
    #
    #     # Creeer een lijst voor de afstanden
    #     distances = []
    #
    #     # # Ga alle huizen af
    #     # for house in HouseList:
    #
    #     # Overlap horizontale as
    #     if self.y <= house.y <= (self.y + self.depth) or self.y <= (house.y + house.depth) <= (self.y + self.depth):
    #
    #         # Links
    #         if self.x > house.x:
    #             distance = (self.x - house.x) - house.width
    #             distances.append(distance)
    #
    #         # Rechts
    #         elif self.x < house.x:
    #             distance = (house.x - self.x) - self.width
    #             distances.append(distance)
    #
    #     # Overlap verticale as
    #     elif self.x <= house.x <= (self.x + self.width) or self.x <= (house.x + house.width) <= (self.x + self.width):
    #
    #             # Boven
    #             if self.y < house.y:
    #                 distance = (house.y - self.y) - self.depth
    #                 distances.append(distance)
    #
    #             # Onder
    #             elif self.y > house.y:
    #                 distance = (self.y - house.y) - house.depth
    #                 distances.append(distance)
    #
    #     # Schuin boven
    #     elif (self.y + self.depth) < house.y:
    #
    #         # Links
    #         if self.x > house.x:
    #             ab = house.y - (self.y + self.depth)
    #             bc = self.x - (house.x + house.width)
    #             ac = ab**2 + bc**2
    #             distance = math.sqrt(ac)
    #             distances.append(distance)
    #
    #         # Rechts
    #         elif self.x < house.x:
    #             ab = house.y - (self.y + self.depth)
    #             bc = house.x - (self.x + self.width)
    #             ac = ab**2 + bc**2
    #             distance = math.sqrt(ac)
    #             distances.append(distance)
    #
    #     #Schuin Onder
    #     elif self.y > (house.y + house.depth):
    #
    #         # Links
    #         if self.x > house.x:
    #             ab = self.y - (house.y + house.depth)
    #             bc = self.x - (house.x + house.width)
    #             ac = ab**2 + bc**2
    #             distance = math.sqrt(ac)
    #             distances.append(distance)
    #
    #         # Rechts
    #         elif self.x < house.x:
    #             ab = self.y - (house.y + house.depth)
    #             bc = house.x - (self.x + self.width)
    #             ac = ab**2 + bc**2
    #             distance = math.sqrt(ac)
    #             distances.append(distance)
    #
    #     print(distances)

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
