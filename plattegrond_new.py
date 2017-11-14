import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

#-----------------------------------------------------------------------------

# Verschillende patronen
pattern1 = ['*']
pattern2 = ['x']
pattern3 = ['.']

# hoe groot het venster is dat geopend wordt
f = plt.figure(figsize=(7,7), dpi=100)

#
a = plt.subplot(111, aspect='equal')
a.plot()
a.axis([0,180,0,160])

# as labels
plt.xlabel('180 meter')
plt.ylabel('160 meter')

# intervallen van de grid lines van de x- en y-as
major_ticksy = np.arange(0, 170, 10)
major_ticksx = np.arange(0, 190, 10)
a.set_yticks(major_ticksy)
a.set_xticks(major_ticksx)

# creëert eengezinswoning
for p in [
    patches.Rectangle(
        (30, 30),
        8.0,
        8.0,
        hatch=pattern1[i],
        facecolor="orange"
    ) for i in range(len(pattern1))
]:
    a.add_patch(p)

# creëert bungalow
for g in [
    patches.Rectangle(
        (30, 90),
        10.0,
        7.5,
        hatch=pattern2[i],
        facecolor="pink"
    ) for i in range(len(pattern2))
]:
    a.add_patch(g)

# creëert maison
for q in [
    patches.Rectangle(
        (30, 60),
        11.0,
        10.5,
        hatch=pattern3[i],
        facecolor="yellow"
    ) for i in range(len(pattern3))
]:
    a.add_patch(q)

# creëert water
for t in [
    patches.Rectangle(
        (132, 0.0),
        48.0,
        120.0,
        fill="blue"
    )
]:
    a.add_patch(t)

plt.grid()
plt.show()
