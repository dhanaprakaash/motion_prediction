#! /usr/bin/env python

import costmap
import matplotlib.pyplot as plt
from oneDtotwoD import oneDtotwoD
from a_star import a_star,indexToWorld,manhattan_distance,euclidean_distance
import dijkstra
from giveIndex import giveIndex
from genHumTrajectory import genHumTrajectory, human_start_index

map = costmap.my_costmap
#print ("map:", map, len(map))

obstacles = []

for i in range(len(map)):
    if (map[i]== 254 or map[i] == 255):
        obstacles.append(i) ### important : it is index, not the value !!!!

#print ("obstacles: ", obstacles, len(obstacles))

x_obstacles, y_obstacles = oneDtotwoD(obstacles)

#print ("x_obstacles: ", x_obstacles, len(x_obstacles))
#sprint ("y_obstacles:", y_obstacles, len(y_obstacles))

##ploting the map and obstacles
#plt_no:1
plt.plot(x_obstacles, y_obstacles,'o')
#plt.show()

### Robot path planning 

my_start_index = giveIndex()# giveIndex() # generate random location in map giveIndex(obstacles)
my_goal_index = giveIndex()
#constants : dont change for the experiments 
my_width = 74 
my_height = 74
my_resolution= 0.2
my_origin = [-7.4, -7.4, 0]


robot_plan = a_star(start_index=my_start_index, goal_index=my_goal_index, width=my_width, height=my_height, 
                    costmap=map, resolution=my_resolution, origin=my_origin)

if (len(robot_plan)==0):
    print("not a possible path!")
    exit()
#print ("Robot Plan: ", robot_plan , len(robot_plan))

robot_plan1 = [my_start_index]
#print("robot_plan1:", robot_plan1)

for i in range(len(robot_plan)):
    robot_plan1.append(robot_plan[i])
robot_plan = robot_plan1
print("Robot plan:", robot_plan, "len:",len(robot_plan))
x_robot_plan, y_robot_plan = oneDtotwoD(robot_plan)

'''
print ("Algorithm Details: ")
print ("start index:", my_start_index)
print ("goal_index:", my_goal_index) '''

xy_start_index =indexToWorld(my_start_index, 74, 0.2, [0,0])
xy_goal_index = indexToWorld(my_goal_index,74,0.2,[0,0])
#plt_no:2 
plt.plot(xy_start_index[0],xy_start_index[1],'o')
plt.plot(xy_goal_index[0], xy_goal_index[1],'o')
plt.plot(x_robot_plan,y_robot_plan)
plt.legend(['static obstacle','robot:start', 'robot:goal', 'robot:path'])
#plt.show()


# Human Presence 


### write this function 
### human_start 
human_trajectory = genHumTrajectory(epoch_lenggth=len(robot_plan))

print ("Human Trajectory:", human_trajectory, "len: ",len(human_trajectory))

x_human_trajectory, y_human_trajectory= oneDtotwoD(human_trajectory)

#print("x_human:", x_human_trajectory)
#print ("y_human:", y_human_trajectory)

plt.plot(x_human_trajectory[0], y_human_trajectory[0],'o')
plt.plot(x_human_trajectory, y_human_trajectory)
plt.plot(x_human_trajectory[-1], y_human_trajectory[-1],'o')
plt.legend(['static obstacle','robot:start', 'robot:goal', 'robot:path','human:start','human:path','human:goal'])
# plot nus: 7

### Risk Event Detection
### Spatio-temporal Collision Detection:

spatio_temporal_collisions = []


### find the distance vector for 3 different parameters 
distance_vector_manhatten = []
distance_vector_euclidean = []
distance_shortest_path_length = [] #  Dijkstra's 
for i in range(len(robot_plan)):
    distance_vector_manhatten.append(round(manhattan_distance(indexToWorld(robot_plan[i], 74, 0.2, [0,0]),
                                      indexToWorld(human_trajectory[i], 74, 0.2, [0,0])),2))
    distance_vector_euclidean.append(round(euclidean_distance(indexToWorld(robot_plan[i], 74, 0.2, [0,0]),
                                      indexToWorld(human_trajectory[i], 74, 0.2, [0,0])),2))
    distance_shortest_path_length.append(len(dijkstra.dijkstra(robot_plan[i], human_trajectory[i], 74,74,map, 0.2,[0,0])))


print ("Distance Vector: Manhatten", distance_vector_manhatten, len(distance_vector_manhatten))
print ("Distance Vector: Euclidean", distance_vector_euclidean, len(distance_vector_euclidean))
print ("Distance Vector: Shorest Path Length:", distance_shortest_path_length, len(distance_shortest_path_length))


#### Mega Debug 

'''
for i in range(len(distance_shortest_path_length)):
    print ("i=", i , distance_shortest_path_length[i], distance_vector_euclidean[i], distance_vector_manhatten[i])'''
