import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x1 = [1,2,3,4]
y1 = [2,4,6,8]

x2 = np.arange(0,5,0.25)



plt.title("I'm Crashing Out", fontdict = {"fontsize": 20})
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.plot(x1,y1, color = "red", marker = '.', markersize = '10')
plt.plot(x2[:5],x2[:5] ** (1/2), "b.-")
plt.plot(x2[4:],x2[4:] ** (1/2), "b--")
#Shorthand: 'r.-'

plt.show()