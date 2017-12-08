#-------------------------------------------------------------------------------
# File name: main.py
#
# Authors: Jet van den Berg, Maurice Roet, Chantal Stangenberger
#
# Course: Heuristics
#
# This program creates a floor plan in which 20, 40 or 60 houses are placed.
# Uses other files names 'houseclasses.py' and 'functions.py' to generate the
# necessary data.
#-------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from houseclasses import *
from functions import *

#-------------------------------------------------------------------------------

# Size of window.
plt.figure(figsize=(7,7), dpi=100)

# Represents subplot and length of axes.
ax = plt.subplot(111, aspect='equal')
ax.plot()
ax.axis([0,180,0,160])

# Sets titles of labels.
plt.title('Amstelhaege - De Planeauleaugen', fontsize=16)
plt.xlabel('180 meter')
plt.ylabel('160 meter')

# Intervals of grid lines of x and y axes.
major_ticksy = np.arange(0, 170, 10)
major_ticksx = np.arange(0, 190, 10)
ax.set_axisbelow(True)
ax.set_yticks(major_ticksy)
ax.set_xticks(major_ticksx)

# Asks which type of floor plan should be displayed.
total_houses = int(input("How many houses should be on the floor plan? (20, 40, 60)\n"))
if not total_houses in [20, 40, 60]:
    print("The amount of houses has to be 20, 40 or 60.")
    exit()

# Gets access to houseList.
houses = HouseList(total_houses)

# Iterates over all houses in house list and creates every house in list.
for i in range(houses.getTotal_houses()):
    house = houses.draw()
    housePlot = patches.Rectangle((house.x,house.y), house.width, house.height,\
        facecolor=house.color, edgecolor='black')
    ax.add_patch(housePlot)

# Calls function to plot map.
PlotMap()
