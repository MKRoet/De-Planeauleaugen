import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from classesnew import *

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

# verschillende soorten huizen
fh = Familyhouse()
bgl = Bungalow()
ms = Maison()
wtr = Water()

list = []

total_buildings = int(input("Hoeveel huizen moeten er op de plattegrond? (20, 40, 60)\n"))
if total_buildings != 20: #40 en 60 moeten erbij
    print("Het aantal huizen moet 20, 40 of 60 zijn")
    exit()

fh_amount = float(total_buildings) * 0.6
bgl_amount = float(total_buildings) * 0.25
ms_amount = float(total_buildings) * 0.15

fh_list = ['fh'] * int(fh_amount)
bgl_list = ['bgl'] * int(bgl_amount)
ms_list = ['ms'] * int(ms_amount)

list.append(fh_list + bgl_list + ms_list)

for i in range int(fh_amount):
    if 'fh':
        temp = patches.Rectangle((fh.x_coordinate, fh.y_coordinate),fh.width, fh.depth)
        ax.add_patch(temp)

# # # creëert eengezinswoning
# # ax.add_patch(
# #     patches.Rectangle(
# #         (fh.x_coordinate, fh.y_coordinate),
# #         fh.width, fh.depth,
# #         )
# # ) for i in range()
#
# # creëert bungalow
# for g in [
#     patches.Rectangle(
#         (bgl.x_coordinate, bgl.y_coordinate),
#         bgl.width, bgl.depth,
#         hatch=pattern2[i],
#         facecolor="pink"
#     )
# ]:
#     ax.add_patch(g)
#
# # creëert maison
# for q in [
#     patches.Rectangle(
#         (ms.x_coordinate, ms.y_coordinate),
#         ms.width, ms.depth,
#         hatch=pattern3[i],
#         facecolor="yellow"
#     ) for i in range(len(pattern3))
# ]:
#     ax.add_patch(q)
#
# # creëert water
# for t in [
#     patches.Rectangle(
#         (wtr.x_coordinate, wtr.y_coordinate),
#         wtr.width, wtr.depth,
#         fill="blue"
#     )
# ]:
#     ax.add_patch(t)

plt.grid()
plt.show()
