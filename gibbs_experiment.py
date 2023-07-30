#! /usr/bin/env python

import costmap
import matplotlib.pyplot as plt
from oneDtotwoD import oneDtotwoD
from a_star import a_star,indexToWorld,manhattan_distance,euclidean_distance,find_neighbors
import dijkstra
from giveIndex import giveIndex
from genHumTrajectory import genHumTrajectory, human_start_index, gibbs_sampled_trajectory


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

### Gibbs Sampled Human Trajectories 

human_trajectories_gibbs = gibbs_sampled_trajectory(no_smaples=4, epoch_length=len(robot_plan))

print("gibbs:",len(human_trajectories_gibbs))


x_trajectories = []
y_trajectories = []
for i in range(len(human_trajectories_gibbs)):
    x_gibbs, y_gibbs = oneDtotwoD(human_trajectories_gibbs[i])
    x_trajectories.append(x_gibbs)
    y_trajectories.append(y_gibbs)

print("S", len(x_trajectories), len(y_trajectories))
print(x_trajectories)
print(y_trajectories)

for i in range(len(human_trajectories_gibbs)):
    plt.plot(x_trajectories[i], y_trajectories[i])
#plt.show()



distance_vector_euclidean = []
for j in range(len(human_trajectories_gibbs)):
    temp =[]
    for i in range(len(human_trajectories_gibbs[j])):
        temp.append(round(euclidean_distance(indexToWorld(robot_plan[i], 74, 0.2, [0,0]),
                                      indexToWorld(human_trajectories_gibbs[j][i], 74, 0.2, [0,0])),2))

    distance_vector_euclidean.append(temp)

print("di:", distance_vector_euclidean)
print("sd:", len(distance_vector_euclidean), len(distance_vector_euclidean[1]))

safeThreshold_Euclidean = 3
safe_distance = safeThreshold_Euclidean

spatio_temporal_collision = set()

for j in range(len(distance_vector_euclidean)):
    for i in range(len(distance_vector_euclidean[j])):
        if (distance_vector_euclidean[j][i] < safe_distance):
            spatio_temporal_collision.add(robot_plan[i])

spatio_temporal_collisions = list(spatio_temporal_collision)

print ("spatil collisons:", spatio_temporal_collisions, len(spatio_temporal_collisions))


### update the map 



dynamic_obstacles_plot = []

## converting tuple into list 
my_map =list(map)
#print("my_map:", type(my_map), len(my_map))

for i in range(len(spatio_temporal_collisions)):
    
    ### regular 
    if (spatio_temporal_collisions[i]-74 < 5476):
        my_map[spatio_temporal_collisions[i]-74] =255
        dynamic_obstacles_plot.append(spatio_temporal_collisions[i]-74)

    if (spatio_temporal_collisions[i]-1 < 5476):
        my_map[spatio_temporal_collisions[i]-1] =255
        dynamic_obstacles_plot.append(spatio_temporal_collisions[i]-1)

    if (spatio_temporal_collisions[i] < 5476):
        my_map[spatio_temporal_collisions[i]]   = 255
        dynamic_obstacles_plot.append(spatio_temporal_collisions[i])

    if (spatio_temporal_collisions[i]+1 < 5476):
        my_map[spatio_temporal_collisions[i]+1] = 255
        dynamic_obstacles_plot.append(spatio_temporal_collisions[i]+1) 

    if (spatio_temporal_collisions[i]+74 < 5476):
        my_map[spatio_temporal_collisions[i]+74] = 255
        dynamic_obstacles_plot.append(spatio_temporal_collisions[i]+74) 


goal_neighbours = find_neighbors(robot_plan[-1],74,74,map,0.2)
print("goal neighbours:", goal_neighbours)
remove_nodes = [0] * len(goal_neighbours)

for i in range (len(remove_nodes)):
    remove_nodes[i] = goal_neighbours[i][0]

print("Remove nodes:", remove_nodes)

for i in range (len(remove_nodes)):
    if (remove_nodes[i] in dynamic_obstacles_plot):
        dynamic_obstacles_plot.remove(remove_nodes[i])


goal_neighbours = find_neighbors(robot_plan[-2],74,74,map,0.2)
print("goal neighbours:", goal_neighbours)
remove_nodes = [0] * len(goal_neighbours)

for i in range (len(remove_nodes)):
    remove_nodes[i] = goal_neighbours[i][0]

print("Remove nodes:", remove_nodes)

for i in range (len(remove_nodes)):
    if (remove_nodes[i] in dynamic_obstacles_plot):
        dynamic_obstacles_plot.remove(remove_nodes[i])


updated_map = tuple(my_map)


if (len(spatio_temporal_collisions) == 0):
    updated_robot_plan = robot_plan
else:
    updated_robot_plan = a_star(start_index = my_start_index, goal_index = my_goal_index,width = 74, height= 74, 
                            costmap = updated_map,resolution=my_resolution, origin=my_origin)
    

print("#### Summary ####")
print("robot start index:",robot_plan[0] )
print("Robot Goal Index:", robot_plan[-1])
print("path length:", len(robot_plan))
print("number od expected coolisions:", len(spatio_temporal_collisions))
if (len(spatio_temporal_collisions)==0):
    print("Updated robot plan:", len(updated_robot_plan))
else:
    print("Updated robot plan:", len(updated_robot_plan))