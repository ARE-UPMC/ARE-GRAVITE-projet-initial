import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))

size = 0.1
xcenter = 5
ycenter = 5
radius = 3

patch = plt.Circle((0,0), size, fc='b')

def init():
    ax.add_patch(patch)
    return patch,

def animate(t):
    x, y = patch.center
    x = xcenter + radius * np.sin(np.radians(t))
    y = ycenter + radius * np.cos(np.radians(t))
    patch.center = (x, y)
    return patch,

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=360, 
                               interval=20,
                               blit=True)
plt.show()
