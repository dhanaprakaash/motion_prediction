import environment
import matplotlib
import matplotlib.pyplot as plt
import numpy as np



x_axis = [0] * 40
y_axis = [0] * 40 

for i in range(len(x_axis)):
    x_axis[i] = str(i)

for i in range (len(y_axis)):
    y_axis[i] = str(i)
print(x_axis)
print(y_axis)

harvest = environment.risk_matrix[0] * 100

fig, ax = plt.subplots()
im = ax.imshow(harvest)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(x_axis)))
ax.set_yticks(np.arange(len(y_axis)))

ax.set_xticklabels(x_axis)
ax.set_yticklabels(y_axis)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(y_axis)):
    for j in range(len(x_axis)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="b")

ax.set_title("Harvest of local farmers (in tons/year)")
fig.tight_layout()
plt.show()
