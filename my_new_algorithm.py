import costmap
import matplotlib.pyplot as plt
from a_star import indexToWorld,a_star


my_data = costmap.my_costmap
print ("my_costmap:", my_data)

## Parameters for the a_star.indextoworld function
alg_width = 74
alg_resolution = 0.2
alg_origin = [0,0]

x_data = [0] * len(my_data)
y_data = [0] * len(my_data)


temp_xy_data = []

for i in range (len(my_data)):
    temp_xy_data.append(indexToWorld(my_data[i], alg_width, alg_resolution, alg_origin))

print ("temp_XY:", temp_xy_data, len (temp_xy_data), 74*74)


## Now differing the x and y 

for i in range (len(temp_xy_data)):
    x_data[i] = round (temp_xy_data[i][0],2)
    y_data[i] = round (temp_xy_data[i][1],2)

### debugging the 

for i in range (len(x_data)):
    print ("i=", i , x_data[i] , y_data[i])

### Above line is not needed 


static_obstacle = []

for i in range (len(my_data)):
    if (my_data[i] == 254 or my_data[i] == 255):
        static_obstacle.append(i)

print("static_obstacle:", static_obstacle, len(static_obstacle))

##  We got the obstacle index 
## convert it into XY world 

x_static_obs = [0] * len (static_obstacle)
y_static_obs = [0] * len (static_obstacle)
xy_static_obs = [0] * len (static_obstacle)


for i in range (len(static_obstacle)):
    xy_static_obs[i] = indexToWorld(static_obstacle[i], alg_width, alg_resolution, alg_origin)
print ("xy_obstacel:", xy_static_obs, len(xy_static_obs), "lop")

for i in range (len(static_obstacle)):
    x_static_obs[i] = round(xy_static_obs[i][0],2)
    y_static_obs[i] = round(xy_static_obs[i][1],2)


## debug 

for i in range (len(xy_static_obs)):
    print ("i:", i, x_static_obs[i], y_static_obs[i])


## plotting obstacles 
#plt.plot(x_static_obs, y_static_obs, 'o')
#plt.show()
my_width=74
my_height= 74
my_start_index= 2050
my_goal_index= 2345
my_resolution= 0.2
my_origin = [-7.4, -7.4, 0]


path = a_star(my_start_index, my_goal_index, my_width,my_height, costmap=my_data, resolution=my_resolution, origin=my_origin )

print ("Path:", path)

xy_path = [0] * len(path)


for i in range (len(xy_path)):
    xy_path[i] = indexToWorld(path[i], 74, 0.2, [0,0])

x_path = [0]*len(xy_path)
y_path = [0]*len(xy_path)

for i in range (len(xy_path)):
    x_path[i]= round(xy_path[i][0],2)
    y_path[i]= round(xy_path[i][0],2)
plt.plot(x_path[0], y_path[0])
plt.plot(x_path[len(x_path)-1], y_path[len(y_path)-1],'o')
plt.plot(x_path,y_path)
plt.show()
