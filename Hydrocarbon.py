import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("TkAgg")

light = 20
heavy = 20
container_size = 1
particles_speed = 0.1
target_y = 0.5

light_pos = np.random.rand(light, 2) * container_size
lightV = np.array([[0, particles_speed] for _ in range(light)])
heavy_pos = np.random.rand(heavy, 2) * container_size
heavyV = np.zeros((heavy, 2))

for i in range(heavy):
    heavyV[i, 1] = (target_y - heavy_pos[i, 1]) * particles_speed  # Move towards target y

collisions = []

fig, ax = plt.subplots()
light_scatter = ax.scatter(light_pos[:, 0], light_pos[:, 1], color="grey", marker="o")
heavy_scatter = ax.scatter(heavy_pos[:, 0], heavy_pos[:, 1], color="grey", marker="_")
ax.set_xlim(0, container_size)
ax.set_ylim(0, container_size)
plt.gca().set_aspect("equal", adjustable="box")

plt.xticks([])
plt.yticks([])

for steps in range(50):
    light_pos += lightV
    heavy_pos += heavyV
    num_collision = 0

    for a in range(light):
        for b in range(2):
            if light_pos[a, b] < 0 or light_pos[a, b] > 1:
                lightV[a, b] *= -1
                num_collision += 1

    for c in range(heavy):
        for d in range(2):
            if heavy_pos[c, d] < 0 or heavy_pos[c, d] > 1:
                heavyV[c, d] *= -1
                num_collision += 1

    collisions = np.append(collisions, num_collision)

    light_scatter.set_offsets(light_pos)
    heavy_scatter.set_offsets(heavy_pos)
    plt.pause(0.1)

lightV[:, 1] = -particles_speed
heavyV[:, 1] = -particles_speed

while True:
    light_pos += lightV
    heavy_pos += heavyV
    num_collision = 0

    for a in range(light):
        for b in range(2):
            if light_pos[a, b] < 0 or light_pos[a, b] > 1:
                lightV[a, b] *= -1
                num_collision += 1

    for c in range(heavy):
        for d in range(2):
            if heavy_pos[c, d] < 0 or heavy_pos[c, d] > 1:
                heavyV[c, d] *= -1
                num_collision += 1

    collisions = np.append(collisions, num_collision)

    light_scatter.set_offsets(light_pos)
    heavy_scatter.set_offsets(heavy_pos)
    plt.pause(0.1)

    if np.all(light_pos[:, 1] <= 0) and np.all(heavy_pos[:, 1] <= 0):
        break

plt.show()