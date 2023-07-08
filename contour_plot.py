# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import shape

feature_x = np.arange(0, 50, 2)
feature_y = np.arange(0, 50, 3)

print("feature_X:", feature_x)
print("feature_Y: ", feature_y)
# Creating 2-D grid of features
[X, Y] = np.meshgrid(feature_x, feature_y)


print("X:", X)
print("Y:",Y)
print("Peintrt ",[X,Y])
print(shape(X))
print(shape(Y))
print(shape([X, Y]))
fig, ax = plt.subplots(1, 1)

Z = np.cos(X / 2) + np.sin(Y / 4)

# plots contour lines
ax.contour(X, Y, Z)

ax.set_title('Contour Plot')
ax.set_xlabel('feature_x')
ax.set_ylabel('feature_y')

plt.show()
