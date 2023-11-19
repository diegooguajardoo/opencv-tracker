import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import sin
import random

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'ro')

data = (random.randint(0, 50))

def init():
    ax.set_xlim(0, 50)
    ax.set_ylim(-50, 50)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(frame)
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=data, interval=500,
                    init_func=init, blit=True)
plt.show()