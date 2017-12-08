#-------------------------------------------------------------------------------
# File name: functions.py
#
# Authors: Jet van den Berg, Maurice Roet, Chantal Stangenberger
#
# Course: Heuristics
#
# This program generates random coordinates, and plots the floor map with grid.
#-------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import random

#-------------------------------------------------------------------------------

# Creates random coordinates.
def getRandom_coordinates():
    x = random.randint(0,180)
    y = random.randint(0,160)
    return ((x,y))

# Plots grid and graph.
def PlotMap():
    plt.grid()
    plt.show()
