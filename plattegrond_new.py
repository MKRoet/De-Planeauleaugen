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

# roept
fh = Familyhouse()
bgl = Bungalow()
ms = Maison()
wtr = Water()

    # creeert eengezinswoning
    for p in [
        patches.Rectangle(
            (fh.x_coordinate, fh.y_coordinate),
            fh.width, fh.depth,
            hatch=pattern1[i],
            facecolor="orange"
        ) for i in range(len(pattern1))
    ]:
        ax.add_patch(p)

    # creeert bungalow
    for g in [
        patches.Rectangle(
            (bgl.x_coordinate, bgl.y_coordinate),
            bgl.width, bgl.depth,
            hatch=pattern2[i],
            facecolor="pink"
        ) for i in range(len(pattern2))
    ]:
        ax.add_patch(g)

    # creeert maison
    for q in [
        patches.Rectangle(
            (ms.x_coordinate, ms.y_coordinate),
            ms.width, ms.depth,
            hatch=pattern3[i],
            facecolor="yellow"
        ) for i in range(len(pattern3))
    ]:
        ax.add_patch(q)

    # creeert water
    for t in [
        patches.Rectangle(
            (wtr.x_coordinate, wtr.y_coordinate),
            wtr.width, wtr.depth,
            fill="blue"
        )
    ]:
        ax.add_patch(t)


plt.grid()
plt.show()
