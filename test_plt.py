import numpy as np
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
data2D = np.random.random((50, 50))
im = plt.imshow(data2D, cmap="copper_r")
plt.colorbar(im)
plt.show()