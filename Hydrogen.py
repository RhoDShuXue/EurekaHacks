import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")

hydro_particles = 500
oxy_particles = 250
container_size =1
particles_speed= 0.1

hydro_pos = np.random.rand(hydro_particles, 2) * container_size
hydroV = np.random.rand(hydro_particles, 2) * particles_speed
oxy_pos = np.random.rand(oxy_particles, 2) * container_size
oxyV = np.random.rand(oxy_particles, 2) * particles_speed

fig, ax= plt.subplots()
hydroScatter = ax.scatter(hydro_pos[:, 0], hydro_pos[:, 1], color = "#63C6EA", marker = "o")
oxyScatter = ax.scatter(oxy_pos[:, 0], oxy_pos[:, 1], color = "#E97225", marker = "o")
ax.set_xlim(0, container_size)
ax.set_ylim(0, container_size)
plt.gca().set_aspect("equal", adjustable = "box")

active_hydro = np.ones(hydro_particles, dtype = bool)
active_oxy = np.ones(oxy_particles, dtype = bool)

plt.xticks([])
plt.yticks([])

redBall = []
max_redBall = 25

for steps in range(1000):
    hydro_pos += hydroV
    oxy_pos += oxyV

    for a in range(hydro_particles):
        if active_hydro[a]:
            for b in range(2):
                if hydro_pos[a, b] < 0 or hydro_pos[a, b] > 1:
                    hydroV[a, b]*= -1

    for c in range(oxy_particles):
        if active_oxy[c]:
            for d in range(2):
                if oxy_pos[c, d] < 0 or oxy_pos[c, d] > 1:
                    oxyV[c, d] *= -1

    for i in range(hydro_particles):
        if active_hydro[i]:
            for j in range(oxy_particles):
                if active_oxy[j]:
                    if np.linalg.norm(hydro_pos[i] - oxy_pos[j]) < 0.02:
                        if max_redBall < (len(redBall)) * 0.6:
                            red_ball_position = (hydro_pos[i] + oxy_pos[j]) / 2
                            redBall.append(red_ball_position)
                            max_redBall += 1
                        active_hydro[i] = False
                        active_oxy[j] = False

    hydro_pos_active = hydro_pos[active_hydro]
    oxy_pos_active = oxy_pos[active_oxy]

    hydroScatter.set_offsets(hydro_pos_active)
    oxyScatter.set_offsets(oxy_pos_active)

    for ball in redBall:
        circle = plt.Circle(ball, 0.01, color = "red", alpha = 0.5)
        ax.add_artist(circle)

    plt.pause(0.2)

red_balls = np.array(redBall)

for _ in range(100):
    ax.collections.clear()
    red_balls[:, 1] -= 0.01
    red_balls[:, 1] = np.maximum(red_balls[:, 1], 0)
    hydroScatter.set_offsets(hydro_pos_active)
    oxyScatter.set_offsets(oxy_pos_active)

    for ball in red_balls:
        circle = plt.Circle(ball, 0.01, color = "red", alpha = 0.5)
        ax.add_artist(circle)

    plt.pause(0.2)
plt.show()