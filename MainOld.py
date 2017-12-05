import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from Woningen import *
from Functions import *
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

# creeërt een list
house_lists = []

# vraagt om welk type plattegrond
total_buildings = int(input("Hoeveel huizen moeten er op de plattegrond? (20, 40, 60)\n"))
if not total_buildings in [20, 40, 60]:
    print("Het aantal huizen moet 20, 40 of 60 zijn")
    exit()

# berekent het percentage familyhome, bungalow en maison van totaal aantal huizen
fh_amount = float(total_buildings) * 0.6
bgl_amount = float(total_buildings) * 0.25
ms_amount = float(total_buildings) * 0.15

# zorgt dat de verschillende typen huizen worden weergeven als lettercode
fh_list = ['fh'] * int(fh_amount)
bgl_list = ['bgl'] * int(bgl_amount)
ms_list = ['ms'] * int(ms_amount)

# voegt alle huizen toe aan de list
house_lists.extend(fh_list + bgl_list + ms_list)
print(house_lists)

for house in house_lists:

    if house == 'fh':
        house_type = Familyhouse
        color = 'green'

    if house == 'bgl':
        house_type = Bungalow
        color = 'yellow'

    if house == 'ms':
        house_type = Maison
        color = 'pink'

    temp = patches.Rectangle((Randomize()), house_type.width, house_type.depth, facecolor=color, edgecolor='black')
    ax.add_patch(temp)

PlotMap()
