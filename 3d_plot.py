# importing mplot3d toolkits, numpy and matplotlib
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

# syntax for 3-D projection
ax = plt.axes(projection ='3d')

# defining all 3 axes
z = [1,2,3,4]
x = [1,1,1,1]
y =  [1,2,3,4]

# plotting
ax.plot3D(x, y, z, 'green')
ax.scatter(x, y, z)
ax.set_title('3D line plot geeks for geeks')
plt.show()


#Occupancy Matrix 

