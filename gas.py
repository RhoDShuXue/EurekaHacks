import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("TkAgg")



hydro_particles = 100
oxy_particles = 50
container_size = 1
particles_speed = 0.1

hydro_pos = np.random.rand(hydro_particles, 2) * container_size
hydroV = np.random.rand(hydro_particles, 2) * particles_speed
oxy_pos = np.random.rand(oxy_particles, 2) * container_size
oxyV = np.random.rand(oxy_particles, 2) * particles_speed

fig,ax = plt.subplots()
hydroScatter = ax.scatter(hydro_pos[:,0], hydro_pos[:,1], color = "#63C6EA", marker = "o")
oxyScatter = ax.scatter(oxy_pos[:,0], oxy_pos[:,1], color = "#E97225", marker = "o")
ax.set_xlim(0, container_size)
ax.set_ylim(0, container_size)
plt.gca().set_aspect("equal", adjustable = "box")

collisions = []

plt.xticks([])
plt.yticks([])

for steps in range(1000):
    hydro_pos += hydroV
    oxy_pos += oxyV
    num_collision = 0

    for a in range(hydro_particles):
        for b in range(2):
            if hydro_pos[a,b] < 0 or hydro_pos[a,b] > 1:
                hydroV[a,b] *= -1
                num_collision += 1

    for c in range(oxy_particles):
        for d in range(2):
            if oxy_pos[c,d] < 0 or oxy_pos[c,d] > 1:
                oxyV[c,d] *= -1
                num_collision += 1

    collisions = np.append(collisions, num_collision)

    hydroScatter.set_offsets(hydro_pos)
    oxyScatter.set_offsets(oxy_pos)
    plt.pause(0.1)

plt.show()