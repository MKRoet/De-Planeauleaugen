#-------------------------------------------------------------------------------
# File name: main.py
#
# Authors: Jet van den Berg, Maurice Roet, Chantal Stangenberger
#
# Course: Heuristics
#
# This program creates a floor plan in which 20, 40 or 60 houses are placed.
# Uses the other file 'houseclasses.py' to generate the
# necessary data.
#-------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
from matplotlib.patches import BoxStyle
from matplotlib.path import Path
import numpy as np
import sys
from houseclasses import *

#-------------------------------------------------------------------------------

# global variable
bestScore = 0

#-------------------------------------------------------------------------------

def main():

    # Command line argument: total runs of the algorithm.
    runs_algorithm = int(sys.argv[2])

    for i in range(runs_algorithm):
        PlotMap()

def PlotMap():

    # Command line argument: which type of floor plan should be displayed.
    total_houses = int(sys.argv[1])
    if not total_houses in [20, 40, 60]:
        print("The amount of houses has to be 20, 40 or 60.")
        exit()

    # Size of window.
    plt.figure(figsize=(7,7), dpi=600)

    # Represents subplot and length of axes.
    ax = plt.subplot(111, aspect='equal')
    ax.plot
    ax.axis([0,180,0,160])

    # Calls HouseList with its values.
    global objects
    global sumScore
    objects = ObjectList(total_houses)
    sumScore = objects.getScore(objects)

    # Sets titles of labels.
    plt.suptitle('Amstelhaege - De Planeauleaugen', fontsize=16)
    plt.title('Score: € {}'.format(int(sumScore)), fontsize=12)
    plt.xlabel('180 meter')
    plt.ylabel('160 meter')
    mediumseagreen_patch = patches.Patch(color='mediumseagreen', label='Familyhouse')
    gold_patch = patches.Patch(color='gold', label='Bungalow')
    lightcoral_patch = patches.Patch(color='lightcoral', label='Maison')
    lightskyblue_patch = patches.Patch(color='lightskyblue', label='Water')
    ax.legend(handles=[mediumseagreen_patch] + [gold_patch] + [lightcoral_patch] \
     + [lightskyblue_patch], loc='center left', bbox_to_anchor=(1, 0.5))

    # Intervals of grid lines of x and y axes.
    major_ticksy = np.arange(0, 170, 10)
    major_ticksx = np.arange(0, 190, 10)
    ax.set_axisbelow(True)
    ax.set_yticks(major_ticksy)
    ax.set_xticks(major_ticksx)

    # Iterates over all houses and water in objectlist and creates a patch for
    # every house/water in list. Uses Rectangle-patch to create house and distance with round corners on map.
    for object_type in objects.objectList:
        plotDetached = patches.FancyBboxPatch((object_type.x, object_type.y), \
        object_type.width, object_type.height, boxstyle=BoxStyle.Round(pad=object_type.detached), \
        color=object_type.color, alpha = 0.4)
        ax.add_patch(plotDetached)

        objectPlot = patches.Rectangle((object_type.x, object_type.y), \
        object_type.width, object_type.height, facecolor=object_type.color)
        ax.add_patch(objectPlot)

    # Print the bestScore of the floor plan and plot/save the best floor plan.
    global bestScore
    if sumScore > bestScore:
        bestScore = sumScore
        plt.grid()
        plt.savefig('map.png', bbox_inches='tight')
        plt.cla()
    print("Score: € {}".format(int(bestScore)))
    plt.close()

if __name__ == '__main__':
    main()
