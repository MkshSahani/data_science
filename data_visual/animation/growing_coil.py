# growing_coil.py

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)

# initialization function


def init():
    # creating an empty plot/frame
    line.set_data([], [])
    return line,


xdata, ydata = [], []


def animate(i):
    #  t is a paramter
    t = 0.1 * i

    x = t * np.sin(t)
    y = t * np.cos(t)

    xdata.append(x)
    ydata.append(y)

    line.set_data(xdata, ydata)
    return line,


plt.title("Creating a growing coil with matplotlib")
plt.axis('off')

anim = animation.FuncAnimation(
    fig, animate, init_func=init, frames=200, interval=20, blit=True)
plt.pause(10)
