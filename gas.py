import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("TkAgg")



num_particles = 100
container_size = 1
time_steps = 1000
particles_speed = 0.1

positions = np.random.rand(num_particles, 2) * container_size
velocity = np.random.rand(num_particles, 2) * particles_speed

fig,ax = plt.subplots()
scatter = ax.scatter(positions[:,0], positions[:,1], color = "#63C6EA", marker = "o")
ax.set_xlim(0, container_size)
ax.set_ylim(0, container_size)
plt.gca().set_aspect("equal", adjustable = "box")

for steps in range(time_steps):
    positions += velocity

    for i in range(num_particles):
        for j in range(2):
            if positions[i,j] < 0 or positions[i,j] > 1:
                velocity[i,j] *= -1

    scatter.set_offsets(positions)
    plt.pause(0.1)

plt.show()