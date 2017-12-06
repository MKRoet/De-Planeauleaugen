import matplotlib.pyplot as plt
import random

#-------------------------------------------------------------------------------

def getRandom_coordinates():

    # creates random coordinates
    x = random.randint(0,180)
    y = random.randint(0,160)
    return ((x,y))

def PlotMap():

    # plot grid and graph
    plt.grid()
    plt.show()
