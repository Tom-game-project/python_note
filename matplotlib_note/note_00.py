
import matplotlib.pyplot as plt
import numpy as np

def function_2(x):
    #面倒がらず明示的に
    return x[0]**2 + x[1]**2
x = np.linspace(-3,3,50)
y = np.linspace(-3,3,50)
z = function_2([x,y])

X,Y = np.meshgrid(x, y)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

plt.cla()
#ax.plot(x, y, z, marker='o', markersize=5, color='blue')

X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, function_2([X,Y]), alpha=0.7)

ax.set_xlabel('X-label')
ax.set_ylabel('Y-label')
ax.set_zlabel('Z-label')

plt.show()