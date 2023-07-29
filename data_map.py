import costmap
import matplotlib.pyplot as plt
from a_star import indexToWorld


my_data = costmap.my_costmap
print ("my_costmap:", my_data)


map_width = 74 
map_height = 74

map_2d = [[0]*map_width for _ in range(map_height)]
print("Map:", map_2d, len(map_2d), len(map_2d[6])) ## perfect 

for x in range(map_width):
    for y in range(map_height):
        map_2d[x][y] = my_data[((x*74)+y)]

## debug
'''print ("XY:",map_2d )
counter =0
for x in range (74):
    for y in range (74):
        if map_2d[x][y] == my_data[(((x*74)+y))]:
            counter = counter +1


print ("Counter: ",counter )'''

new_data = []
for i in range (73, -1, -1):
    for j in range (74):
        new_data.append(my_data[i*74+j])
print ("len", len(new_data))
        
xy_new_data = [0] * len (new_data)

for i in range (len(new_data)):
    xy_new_data[i] = indexToWorld(new_data[i], 74, 0.2 , [0,0])

x_new_data = [0] * len(new_data)
y_new_data = [0] * len(new_data)

for i in range (len(new_data)):
    x_new_data[i] = round(xy_new_data[i][0],2)
    y_new_data[i] = round(xy_new_data[i][1],2)



for i in range (74):
    for j in range (74):
        print (i,j, my_data[i*74+j], new_data[i*74+j])
#plt.plot(x_new_data,y_new_data,"o")
#plt.show()


### Extracting obstacle 

static_obstacle = []

for i in range (len(new_data)):
    if (new_data[i] == 254 or new_data[i] == 255):
        static_obstacle.append(i)

print("static_obstacle:", static_obstacle, len(static_obstacle))

##  We got the obstacle index 
## convert it into XY world 

alg_width = 74
alg_resolution =0.2
alg_origin = [0,0]

x_static_obs = [0] * len (static_obstacle)
y_static_obs = [0] * len (static_obstacle)
xy_static_obs = [0] * len (static_obstacle)


for i in range (len(static_obstacle)):
    xy_static_obs[i] = indexToWorld(static_obstacle[i], alg_width, alg_resolution, alg_origin)
print ("xy_obstacel:", xy_static_obs, len(xy_static_obs), "lop")

for i in range (len(static_obstacle)):
    x_static_obs[i] = round(xy_static_obs[i][0],2)
    y_static_obs[i] = round(xy_static_obs[i][1],2)

##plots2 
plt.plot(x_static_obs, y_static_obs, 'o')
plt.show()