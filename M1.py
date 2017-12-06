import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from W1 import *
from F1 import *
import math

#-----------------------------------------------------------------------------
# hoe groot het venster is dat geopend wordt
f = plt.figure(figsize=(7,7), dpi=100)

# weergeeft subplot en lengte van de assen
ax = plt.subplot(111, aspect='equal')
ax.plot()
ax.axis([0,180,0,160])

# as labels
plt.xlabel('180 meter')
plt.ylabel('160 meter')

# intervallen van de grid lines van de x- en y-as
major_ticksy = np.arange(0, 170, 10)
major_ticksx = np.arange(0, 190, 10)
ax.set_yticks(major_ticksy)
ax.set_xticks(major_ticksx)

# vraagt om welk type plattegrond
total_buildings = int(input("Hoeveel huizen moeten er op de plattegrond? (20, 40, 60)\n"))
if not total_buildings in [20, 40, 60]:
    print("Het aantal huizen moet 20, 40 of 60 zijn")
    exit()

# haalt de houselist op
houses = HouseList(total_buildings)

# loopt over alle huizen in de house list en creert een patch
for i in range(houses.getTotal_buildings()):
    house = houses.draw()
    temp = patches.Rectangle((house.x,house.y), house.width, house.depth, facecolor=house.color, edgecolor='black')
    ax.add_patch(temp)

# roept plot functie aan
PlotMap()
