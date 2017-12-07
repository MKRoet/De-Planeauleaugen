import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from houseclasses import *
from functions import *

#-----------------------------------------------------------------------------

# size of the window
plt.figure(figsize=(7,7), dpi=100)

# represents subplot and length of the axes
ax = plt.subplot(111, aspect='equal')
ax.plot()
ax.axis([0,180,0,160])

# as labels
plt.xlabel('180 meter')
plt.ylabel('160 meter')

# intervals of the grid lines of the x and y axes
major_ticksy = np.arange(0, 170, 10)
major_ticksx = np.arange(0, 190, 10)
ax.set_yticks(major_ticksy)
ax.set_xticks(major_ticksx)
ax.minorticks_on()
ax.set_axisbelow(True)

# asks which type of floor plan should be displayed
total_buildings = int(input("Hoeveel huizen moeten er op de plattegrond? (20, 40, 60)\n"))
if not total_buildings in [20, 40, 60]:
    print("Het aantal huizen moet 20, 40 of 60 zijn")
    exit()

# gets access to the houselist
houses = HouseList(total_buildings)

# iteration over all houses in the houselist and creates for every house a patch
for i in range(houses.getTotal_buildings()):
    house = houses.draw()
    temp = patches.Rectangle((house.x,house.y), house.width, house.height, facecolor=house.color, edgecolor='black')
    ax.add_patch(temp)

# gets acces to the plotmap function
PlotMap()
