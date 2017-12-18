#-------------------------------------------------------------------------------
# File name: plotmap.py
#
# Authors: Jet van den Berg, Maurice Roet, Chantal Stangenberger
#
# Course: Heuristics
#
# This file contains a GenerateMap function that generates the ObjectList from
# the objectclasses.py and a PlotMap function that plots the floor plan with use
# of matplotlib.
#-------------------------------------------------------------------------------

from Data_structure.objectclasses import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
from matplotlib.patches import BoxStyle
from matplotlib.path import Path
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------

# Returns the whole ObjectList from objectclasses.py.
def generateMap(total_houses):
    return ObjectList(total_houses)

# Plot the floor plans.
def plotMap(objects, title):

    # Calls getScore from objectclasses.py.
    sumScore = objects.getScore(objects)

    # Size of plot window.
    plt.figure(figsize=(7,7), dpi=600)

    # Represents subplot and length of axes.
    ax = plt.subplot(111, aspect='equal')
    ax.plot
    ax.axis([0,180,0,160])

    # Sets titles of labels.
    plt.suptitle('AmstelHaege - De Planeauleaugen', fontsize=16)
    plt.title('Score: € {}'.format(int(sumScore)), fontsize=12)
    plt.xlabel('180 meter')
    plt.ylabel('160 meter')

    # Creates a map legend.
    mediumseagreen_patch = patches.Patch(color='mediumseagreen', label='Familyhouse')
    gold_patch = patches.Patch(color='gold', label='Bungalow')
    lightcoral_patch = patches.Patch(color='lightcoral', label='Maison')
    lightskyblue_patch = patches.Patch(color='lightskyblue', label='Water')
    ax.legend(handles=[mediumseagreen_patch] + [gold_patch] + [lightcoral_patch]\
        + [lightskyblue_patch], loc='center left', bbox_to_anchor=(1, 0.5))

    # Intervals of grid lines of x and y axes.
    major_ticksy = np.arange(0, 170, 10)
    major_ticksx = np.arange(0, 190, 10)
    ax.set_axisbelow(True)
    ax.set_yticks(major_ticksy)
    ax.set_xticks(major_ticksx)

    # Iterates over all houses and water in the objectList and creates a patch
    # for every house/water in list. Uses Rectangle-patch to create house and
    # distance with round corners on map.
    for object_type in objects.objectList:
        plotDetached = patches.FancyBboxPatch((object_type.x, object_type.y),\
            object_type.width, object_type.height,\
            boxstyle=BoxStyle.Round(pad=object_type.detached),\
            color=object_type.color, alpha = 0.4)
        ax.add_patch(plotDetached)

        objectPlot = patches.Rectangle((object_type.x, object_type.y),\
            object_type.width, object_type.height, facecolor=object_type.color,)
        ax.add_patch(objectPlot)

    # Plots the floor plan en prints the corresponding score.
    plt.grid()
    plt.savefig(title, bbox_inches='tight')
    plt.cla()
    print("Score: € {}".format(int(sumScore)))
    plt.close()
