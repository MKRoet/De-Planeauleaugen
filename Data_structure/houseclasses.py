from functions import *
import math

#-------------------------------------------------------------------------------

height_graph = 160
width_graph = 180
percentage_familyhouse = 0.6
percentage_bungalow = 0.25
percentage_maison = 0.15

#-------------------------------------------------------------------------------

class HouseList:

    def __init__(self, total_buildings):
        self.houseList=[]
        self.fh_amount = int(float(total_buildings) * percentage_familyhouse)
        self.bgl_amount = int(float(total_buildings) * percentage_bungalow)
        self.ms_amount = int(float(total_buildings) * percentage_maison)

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
            return False
        if (house_type.x + house_type.width + house_type.detached > width_graph):
            return False
        if (house_type.y - house_type.detached < 0):
            return False
        if (house_type.y + house_type.height + house_type.detached > height_graph):
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

    def getDistance(self, house_type):
        shortestDistance=99999999
        for h in self.houseList:
            if h is not house_type:
                distance = house_type.getDistance(h)
                if distance < shortestDistance:
                    shortestDistance = distance
        return shortestDistance

    def getScore(self, house_type):
        sumScore = 0
        for h in self.houseList:
                score = house_type.getScore(h)
                sumScore += score
        return sumScore

    # def __getitem__(self, item):
    #     return self.houseList[item]

class House(object):

    base_sale_price = 0
    width = 0
    height = 0
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
        if h.x + h.width + h.detached <= self.x and self.x - self.detached >= h.x + h.width:
            return False
        if h.x - h.detached >= self.x + self.width and self.x + self.width + self.detached <= h.x:
            return False
        if h.y + h.height + h.detached <= self.y and self.y - self.detached >= h.y + h.height:
            return False
        if h.y - h.detached >= self.y + self.height and self.y + self.height + self.detached <= h.y:
            return False
        return True

    def getDistance(self, house):
        # Overlap horizontale as
        if self.y <= house.y <= (self.y + self.height) or self.y <= (house.y + house.height) <= (self.y + self.height):

            # Links
            if self.x > house.x:
                distance = (self.x - house.x) - house.width

            # Rechts
            elif self.x < house.x:
                distance = (house.x - self.x) - self.width

        # Overlap verticale as
        elif self.x <= house.x <= (self.x + self.width) or self.x <= (house.x + house.width) <= (self.x + self.width):

                # Boven
                if self.y < house.y:
                    distance = (house.y - self.y) - self.height

                # Onder
                elif self.y > house.y:
                    distance = (self.y - house.y) - house.height

        # Schuin boven
        elif (self.y + self.height) < house.y:

            # Links
            if self.x > house.x:
                ab = house.y - (self.y + self.height)
                bc = self.x - (house.x + house.width)
                ac = ab**2 + bc**2
                distance = math.sqrt(ac)

            # Rechts
            elif self.x < house.x:
                ab = house.y - (self.y + self.height)
                bc = house.x - (self.x + self.width)
                ac = ab**2 + bc**2
                distance = math.sqrt(ac)

        #Schuin Onder
        elif self.y > (house.y + house.height):

            # Links
            if self.x > house.x:
                ab = self.y - (house.y + house.height)
                bc = self.x - (house.x + house.width)
                ac = ab**2 + bc**2
                distance = math.sqrt(ac)

            # Rechts
            elif self.x < house.x:
                ab = self.y - (house.y + house.height)
                bc = house.x - (self.x + self.width)
                ac = ab**2 + bc**2
                distance = math.sqrt(ac)

        return distance

    def getScore(self):
        detached_extra = House.getDistance(self) - self.detached
        totalpercentage_addedvalue = detached_extra * self.percentage_addedvalue
        addedvalue = self.base_sale_price * totalpercentage_addedvalue
        score = self.base_sale_price + addedvalue
        return score

class Familyhouse(House):

    def __init__(self,x,y):
         super(Familyhouse,self).__init__(x,y)

    base_sale_price = 285000
    width = 8
    height = 8
    detached = 2
    color = 'green'

class Bungalow(House):

    def __init__(self,x,y):
         super(Bungalow,self).__init__(x,y)

    base_sale_price = 399000
    width = 10
    height = 7.5
    detached = 3
    color = 'yellow'

class Maison(House):

    def __init__(self,x,y):
         super(Maison,self).__init__(x,y)

    base_sale_price = 610000
    width = 11
    height = 10.5
    detached = 6
    color = 'pink'
