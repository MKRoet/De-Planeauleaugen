#!/usr/apps/Python/bin/python
import matplotlib, sys
matplotlib.use('TkAgg')
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from tkinter import *

master = Tk()
master.title("Plattegrond Planeauleaugen")
#-------------------------------------------------------------------------------

f = Figure(figsize=(10,10), dpi=100)
a = f.add_subplot(111)
a.plot()
a.axis([0,18,0,16])
a.set_facecolor('green')

dataPlot = FigureCanvasTkAgg(f, master=master)
dataPlot.show()
dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
#-------------------------------------------------------------------------------
master.mainloop()

# test van BAS
