import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from classesnew import *

#-----------------------------------------------------------------------------

# Verschillende patronen
pattern1 = ['*']
pattern2 = ['x']
pattern3 = ['.']

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

# coordinaten gelinkt met classes
buildingF = Familyhome(30,30)
buildingB = Bungalow(30,90)
buildingM = Maison(30,60)
water = Water(132,0)

# creëert eengezinswoning
for p in [
    patches.Rectangle(
        (buildingF.x_coordinate, buildingF.y_coordinate),
        buildingF.width, buildingF.depth,
        hatch=pattern1[i],
        facecolor="orange"
    ) for i in range(len(pattern1))
]:
    ax.add_patch(p)

# creëert bungalow
for g in [
    patches.Rectangle(
        (buildingB.x_coordinate, buildingB.y_coordinate),
        buildingB.width, buildingB.depth,
        hatch=pattern2[i],
        facecolor="pink"
    ) for i in range(len(pattern2))
]:
    ax.add_patch(g)

# creëert maison
for q in [
    patches.Rectangle(
        (buildingM.x_coordinate, buildingM.y_coordinate),
        buildingM.width, buildingM.depth,
        hatch=pattern3[i],
        facecolor="yellow"
    ) for i in range(len(pattern3))
]:
    ax.add_patch(q)

# # creëert water
for t in [
    patches.Rectangle(
        (water.x_coordinate, water.y_coordinate),
        water.width, water.depth,
        fill="blue"
    )
]:
    ax.add_patch(t)

plt.grid()
plt.show()
