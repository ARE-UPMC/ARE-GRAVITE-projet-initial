import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(-20, 20), ylim=(-20, 20))

size = 0.2
xcenter = 0
ycenter = 0
radius = 1

n = 10

patch_list = []
for i in range(n):
    patch = plt.Circle((0,0), size, fc = 'r')
    patch_list.append(patch)
for p in patch_list:
    ax.add_patch(p)

def init():
    return patch_list

def animate(t):
    i = 1
    for p in patch_list:
        x, y = p.center
        x = xcenter + i*radius * np.sin(np.radians(t*i/5))
        y = ycenter + i*radius * np.cos(np.radians(t*i/5))
        p.center = (x, y)
        i=i+1
    return patch_list

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=360, 
                               interval=20,
                               blit=True)
plt.show()
