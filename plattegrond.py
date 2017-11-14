#!/usr/apps/Python/bin/python
import matplotlib, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.patches as patches
from tkinter import *

master = Tk()
master.title("Plattegrond Planeauleaugen")
#-------------------------------------------------------------------------------
pattern1 = ['*']
pattern2 = ['x']
pattern3 = ['.']

f = Figure(figsize=(10,10), dpi=100)
a = f.add_subplot(111, aspect='equal')
a.plot()
a.axis([0,18,0,16])
a.set_facecolor('#8DDA00')
for p in [
    patches.Rectangle(
        (3.0, 3.0),
        0.8,
        0.8,
        hatch=pattern1[i],
        facecolor="orange"
    ) for i in range(len(pattern1))
]:
    a.add_patch(p)

for g in [
    patches.Rectangle(
        (3.0, 9.0),
        1.0,
        0.75,
        hatch=pattern2[i],
        facecolor="pink"
    ) for i in range(len(pattern2))
]:
    a.add_patch(g)

for q in [
    patches.Rectangle(
        (3.0, 6.0),
        1.1,
        1.05,
        hatch=pattern3[i],
        facecolor="yellow"
    ) for i in range(len(pattern3))
]:
    a.add_patch(q)

for t in [
    patches.Rectangle(
        (13.2, 0.0),
        4.8,
        12.0,
        fill="blue"
    )
]:
    a.add_patch(t)


dataPlot = FigureCanvasTkAgg(f, master=master)
dataPlot.show()
dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
#-------------------------------------------------------------------------------
master.mainloop()

# yo
