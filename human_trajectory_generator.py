#! /usr/bin/env python

import costmap
import matplotlib.pyplot as plt
from oneDtotwoD import oneDtotwoD
from a_star import a_star,indexToWorld,manhattan_distance,euclidean_distance,find_neighbors
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

### so far 
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


print ("Distance Vector: Manhatten", distance_vector_manhatten, len(distance_vector_manhatten), "Avg:",
       sum(distance_vector_manhatten)/len(distance_vector_manhatten))
print ("Distance Vector: Euclidean", distance_vector_euclidean, len(distance_vector_euclidean), "Avg:",
       sum(distance_vector_euclidean)/len(distance_vector_euclidean))
print ("Distance Vector: Shorest Path Length:", distance_shortest_path_length, len(distance_shortest_path_length),
       "Avg:",sum(distance_shortest_path_length)/len(distance_shortest_path_length))


#### Mega Debug 

'''
for i in range(len(distance_shortest_path_length)):
    print ("i=", i , distance_shortest_path_length[i], distance_vector_euclidean[i], distance_vector_manhatten[i])'''


safeThreshold_manhantten = 3
safeThreshold_Euclidean = 3
safeThreshold_Dijkstra = 10


distance_vector = distance_vector_euclidean
safe_distance = safeThreshold_Euclidean
time_instants = []

for i in range (len(distance_vector)):
    if (distance_vector[i]< safe_distance):
        spatio_temporal_collisions.append(robot_plan[i]) ## important!!!
        time_instants.append(i)

print ("spatio-temporal-collisions:", spatio_temporal_collisions)
print ("time instants: ", time_instants)
#plt.show()
for i in range (len(time_instants)):
    x_cor, y_cor = oneDtotwoD([robot_plan[time_instants[i]],human_trajectory[time_instants[i]]])
    plt.plot(x_cor, y_cor)

#plt.show()
if (len(spatio_temporal_collisions)==0):
    print ("No collision")
else :
    print("How many collisions?",len(spatio_temporal_collisions))


### two functionalities remaining!!!
### Update the costmap 
### Debug :: 
'''for i in range(len(spatio_temporal_collisions)):
    print ("i=",i , spatio_temporal_collisions[i], map[spatio_temporal_collisions[i]])'''


#print("type:", type(map))

## updating the costmap: 

dynamic_obstacles = []

## converting tuple into list 
my_map =list(map)
#print("my_map:", type(my_map), len(my_map))

for i in range(len(spatio_temporal_collisions)):
    
    '''if (spatio_temporal_collisions[i]-76 < 5476):
        my_map[spatio_temporal_collisions[i]-76] =255
        dynamic_obstacles.append(spatio_temporal_collisions[i]-76)

    if (spatio_temporal_collisions[i]-2 < 5476):
        my_map[spatio_temporal_collisions[i]-2] = 255
        dynamic_obstacles.append(spatio_temporal_collisions[i]-2)
    
    if (spatio_temporal_collisions[i]-72 < 5476):
        my_map[spatio_temporal_collisions[i]-72] =255
        dynamic_obstacles.append(spatio_temporal_collisions[i]-72)

    if (spatio_temporal_collisions[i]+76 < 5476):
        my_map[spatio_temporal_collisions[i]+76] =255
        dynamic_obstacles.append(spatio_temporal_collisions[i]+76)

    if (spatio_temporal_collisions[i]+2 < 5476):
        my_map[spatio_temporal_collisions[i]+2] = 255
        dynamic_obstacles.append(spatio_temporal_collisions[i]+2)
    
    if (spatio_temporal_collisions[i]+72 < 5476):
        my_map[spatio_temporal_collisions[i]+72] =255
        dynamic_obstacles.append(spatio_temporal_collisions[i]+72)
    
    ## right corner
    if (spatio_temporal_collisions[i]-146 < 5476):
        my_map[spatio_temporal_collisions[i]-146] =255
        dynamic_obstacles.append(spatio_temporal_collisions[i]-146)

    if (spatio_temporal_collisions[i]-147 < 5476):
        my_map[spatio_temporal_collisions[i]-147] = 255
        dynamic_obstacles.append(spatio_temporal_collisions[i]-147)
    
    if (spatio_temporal_collisions[i]-148 < 5476):
        my_map[spatio_temporal_collisions[i]-148] =255
        dynamic_obstacles.append(spatio_temporal_collisions[i]-148)

    if (spatio_temporal_collisions[i]-149 < 5476):
        my_map[spatio_temporal_collisions[i]-149]   = 255
        dynamic_obstacles.append(spatio_temporal_collisions[i]-149)

    if (spatio_temporal_collisions[i]-150 < 5476):
        my_map[spatio_temporal_collisions[i]-150] = 255
        dynamic_obstacles.append(spatio_temporal_collisions[i]-150) 

    ## left corner
    if (spatio_temporal_collisions[i]+146 < 5476):
        my_map[spatio_temporal_collisions[i]+146] =255
        dynamic_obstacles.append(spatio_temporal_collisions[i]+146)

    if (spatio_temporal_collisions[i]+147 < 5476):
        my_map[spatio_temporal_collisions[i]+147] = 255
        dynamic_obstacles.append(spatio_temporal_collisions[i]+147)
    
    if (spatio_temporal_collisions[i]+148 < 5476):
        my_map[spatio_temporal_collisions[i]+148] =255
        dynamic_obstacles.append(spatio_temporal_collisions[i]+148)

    if (spatio_temporal_collisions[i]+149 < 5476):
        my_map[spatio_temporal_collisions[i]+149]   = 255
        dynamic_obstacles.append(spatio_temporal_collisions[i]+149)

    if (spatio_temporal_collisions[i]+150 < 5476):
        my_map[spatio_temporal_collisions[i]+150] = 255
        dynamic_obstacles.append(spatio_temporal_collisions[i]+150) '''
    
    ### regular 
    if (spatio_temporal_collisions[i]-75 < 5476):
        my_map[spatio_temporal_collisions[i]-75] =255
        dynamic_obstacles.append(spatio_temporal_collisions[i]-75)

    if (spatio_temporal_collisions[i]-74 < 5476):
        my_map[spatio_temporal_collisions[i]-74] =255
        dynamic_obstacles.append(spatio_temporal_collisions[i]-74)

    if (spatio_temporal_collisions[i]-73 < 5476):
        my_map[spatio_temporal_collisions[i]-73] = 255
        dynamic_obstacles.append(spatio_temporal_collisions[i]-75)
    
    if (spatio_temporal_collisions[i]-1 < 5476):
        my_map[spatio_temporal_collisions[i]-1] =255
        dynamic_obstacles.append(spatio_temporal_collisions[i]-1)

    if (spatio_temporal_collisions[i] < 5476):
        my_map[spatio_temporal_collisions[i]]   = 255
        dynamic_obstacles.append(spatio_temporal_collisions[i])

    if (spatio_temporal_collisions[i]+1 < 5476):
        my_map[spatio_temporal_collisions[i]+1] = 255
        dynamic_obstacles.append(spatio_temporal_collisions[i]+1) 

    if (spatio_temporal_collisions[i]+73 < 5476):
        my_map[spatio_temporal_collisions[i]+73] = 255
        dynamic_obstacles.append(spatio_temporal_collisions[i]+73) 

    if (spatio_temporal_collisions[i]+74 < 5476):
        my_map[spatio_temporal_collisions[i]+74] = 255
        dynamic_obstacles.append(spatio_temporal_collisions[i]+74) 

    if (spatio_temporal_collisions[i]+75 < 5476):
        my_map[spatio_temporal_collisions[i]+75] = 255
        dynamic_obstacles.append(spatio_temporal_collisions[i]+75)

goal_neighbours = find_neighbors(robot_plan[-1],74,74,map,0.2)
print("goal neighbours:", goal_neighbours)
remove_nodes = [0] * len(goal_neighbours)

for i in range (len(remove_nodes)):
    remove_nodes[i] = goal_neighbours[i][0]

print("Remove nodes:", remove_nodes)

for i in range (len(remove_nodes)):
    if (remove_nodes[i] in dynamic_obstacles):
        dynamic_obstacles.remove(remove_nodes[i])


goal_neighbours = find_neighbors(robot_plan[-2],74,74,map,0.2)
print("goal neighbours:", goal_neighbours)
remove_nodes = [0] * len(goal_neighbours)

for i in range (len(remove_nodes)):
    remove_nodes[i] = goal_neighbours[i][0]

print("Remove nodes:", remove_nodes)

for i in range (len(remove_nodes)):
    if (remove_nodes[i] in dynamic_obstacles):
        dynamic_obstacles.remove(remove_nodes[i])

dynamic_obs =set()
#print("Dynamic Obstacle:", dynamic_obstacles , len(dynamic_obstacles))
for i in range(len(dynamic_obstacles)):
    dynamic_obs.add(dynamic_obstacles[i])

#print ("dynamic_set:", dynamic_obs, len(dynamic_obs))
### mega dubugg:
'''counts=0
for i in range (len(my_map)):
    if (map[i]!=my_map[i]):
        counts =counts +1 
print ("counts:", counts)'''
## removing goal index: 
 

### mega dubug 
dynamic_list = list (dynamic_obs)
'''for i in range (len(dynamic_obstacles)):
    print ("i=", i , map[dynamic_obstacles[i]], my_map[dynamic_obstacles[i]])'''

updated_map =tuple(my_map)

#print ("type(updated_map):", type(updated_map))
#print ("type (map):", type(map))
###call the planner again!!!

if (len(spatio_temporal_collisions) == 0):
    updated_robot_plan = robot_plan
else:
    updated_robot_plan = a_star(start_index = my_start_index, goal_index = my_goal_index,width = 74, height= 74, 
                            costmap = updated_map,resolution=my_resolution, origin=my_origin)
  

### printing the final output: 
print ("###Summary###")
print ("Robot PLan: ", robot_plan, len(robot_plan))
print ("updated_robot_plan:", updated_robot_plan, len(updated_robot_plan))

#plt.show()
### plotting the entire scene !!! 
#x_obstacles, y_obstacles
#x_robot_plan,y_robot_plan
#x_human_trajectory,y_human_trajectory


print("#### Summary ####")
print("robot start index:",robot_plan[0] )
print("Robot Goal Index:", robot_plan[-1])
print("path length:", len(robot_plan))
print("number od expected coolisions:", len(spatio_temporal_collisions))
if (len(spatio_temporal_collisions)==0):
    print("Updated robot plan:", len(updated_robot_plan))
else:
    print("Updated robot plan:", len(updated_robot_plan))







x_dynamic_obstacles,y_dynamic_obstacles = oneDtotwoD(dynamic_obstacles)
x_updated_path, y_updated_path = oneDtotwoD(updated_robot_plan)

plt.plot(x_obstacles,y_obstacles,'o')
plt.plot(x_dynamic_obstacles, y_dynamic_obstacles,'o')
plt.plot(x_updated_path, y_updated_path,'o')
plt.plot(x_human_trajectory,y_human_trajectory)
plt.plot(x_robot_plan, y_robot_plan)
#plt.show()