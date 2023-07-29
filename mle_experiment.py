#! /usr/bin/env python

import costmap
import matplotlib.pyplot as plt
from oneDtotwoD import oneDtotwoD
from a_star import a_star,indexToWorld,manhattan_distance,euclidean_distance,find_neighbors
import dijkstra
from giveIndex import giveIndex
from genHumTrajectory import genHumTrajectory, human_start_index

map = costmap.my_costmap


obstacles = []

for i in range(len(map)):
    if (map[i]== 254 or map[i] == 255):
        obstacles.append(i) ### important : it is index, not the value !!!!



x_obstacles, y_obstacles = oneDtotwoD(obstacles)



#plt_no: 1
plt.plot(x_obstacles, y_obstacles,'o')
plt.legend(['Static Obstacles'])
#show_no:1
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


robot_plan1 = [my_start_index]


for i in range(len(robot_plan)):
    robot_plan1.append(robot_plan[i])
robot_plan = robot_plan1
print("Robot plan:", robot_plan, "len:",len(robot_plan))
x_robot_plan, y_robot_plan = oneDtotwoD(robot_plan)



xy_start_index =indexToWorld(my_start_index, 74, 0.2, [0,0])
xy_goal_index = indexToWorld(my_goal_index,74,0.2,[0,0])

#plt_no 2,3,4




# Human Presence 


### write this function 
### human_start 
human_trajectory = genHumTrajectory(epoch_lenggth=len(robot_plan))

print ("Human Trajectory:", human_trajectory, "len: ",len(human_trajectory))

x_human_trajectory, y_human_trajectory= oneDtotwoD(human_trajectory)




### so far 
### Risk Event Detection
### Spatio-temporal Collision Detection:

spatio_temporal_collisions_euclidean = []
spatio_temporal_collisions_manhatten = []
spatio_temporal_collisions_dijkstra = []


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

distance_vector_dijkstra = distance_shortest_path_length

safeThreshold_manhantten = 3
safeThreshold_Euclidean = 3
safeThreshold_Dijkstra = 10



time_instants_euclidean = []
time_instants_manhatten = []
time_instants_dijkstra = []

## euclidean 
for i in range (len(distance_vector_euclidean)):
    if (distance_vector_euclidean[i]< safeThreshold_Euclidean):
        spatio_temporal_collisions_euclidean.append(human_trajectory[i]) ## important!!!
        time_instants_euclidean.append(i)

print ("spatio-temporal-collisions_euclidean:", spatio_temporal_collisions_euclidean)
print ("time instants_euclidean: ", time_instants_euclidean)

##Manhatten 
for i in range (len(distance_vector_manhatten)):
    if (distance_vector_manhatten[i]< safeThreshold_manhantten):
        spatio_temporal_collisions_manhatten.append(human_trajectory[i]) ## important!!!
        time_instants_manhatten.append(i)

print ("spatio-temporal-collisions_manhatten:", spatio_temporal_collisions_manhatten)
print ("time instants_manhatten: ", time_instants_manhatten)

##Dijkstra

for i in range (len(distance_vector_dijkstra)):
    if (distance_vector_dijkstra[i]< safeThreshold_Dijkstra):
        spatio_temporal_collisions_dijkstra.append(human_trajectory[i]) ## important!!!
        time_instants_dijkstra.append(i)

print ("spatio-temporal-collisions_dijkstra:", spatio_temporal_collisions_dijkstra)
print ("time instants_dijkstra: ", time_instants_dijkstra)






## euclidean 
if (len(spatio_temporal_collisions_euclidean)==0):
    print ("No collision")
else :
    print("How many collisions?(euclidean)",len(spatio_temporal_collisions_euclidean))

##Manhatten:
if (len(spatio_temporal_collisions_manhatten)==0):
    print ("No collision")
else :
    print("How many collisions?(manhatten)",len(spatio_temporal_collisions_manhatten))

##Dijkstra:
if (len(spatio_temporal_collisions_dijkstra)==0):
    print ("No collision")
else :
    print("How many collisions?(dijkstra)",len(spatio_temporal_collisions_dijkstra))


## updating the costmap: 

dynamic_obstacles_euclidean = []
dynamic_obstacles_manhatten = []
dynamic_obstacles_dijkstra = []

## converting tuple into list 
my_map_euclidean = list(map)
my_map_manhatten = list(map)
my_map_dijkstra = list(map)

## euclidean 
## Updating the dynamic Obstacle 

for i in range(len(spatio_temporal_collisions_euclidean)):
    if (spatio_temporal_collisions_euclidean[i]-75 < 5476):
        my_map_euclidean[spatio_temporal_collisions_euclidean[i]-75] =255
        dynamic_obstacles_euclidean.append(spatio_temporal_collisions_euclidean[i]-75)

    if (spatio_temporal_collisions_euclidean[i]-74 < 5476):
        my_map_euclidean[spatio_temporal_collisions_euclidean[i]-74] =255
        dynamic_obstacles_euclidean.append(spatio_temporal_collisions_euclidean[i]-74)

    if (spatio_temporal_collisions_euclidean[i]-73 < 5476):
        my_map_euclidean[spatio_temporal_collisions_euclidean[i]-73] = 255
        dynamic_obstacles_euclidean.append(spatio_temporal_collisions_euclidean[i]-75)
    
    if (spatio_temporal_collisions_euclidean[i]-1 < 5476):
        my_map_euclidean[spatio_temporal_collisions_euclidean[i]-1] =255
        dynamic_obstacles_euclidean.append(spatio_temporal_collisions_euclidean[i]-1)

    if (spatio_temporal_collisions_euclidean[i] < 5476):
        my_map_euclidean[spatio_temporal_collisions_euclidean[i]]   = 255
        dynamic_obstacles_euclidean.append(spatio_temporal_collisions_euclidean[i])

    if (spatio_temporal_collisions_euclidean[i]+1 < 5476):
        my_map_euclidean[spatio_temporal_collisions_euclidean[i]+1] = 255
        dynamic_obstacles_euclidean.append(spatio_temporal_collisions_euclidean[i]+1) 

    if (spatio_temporal_collisions_euclidean[i]+73 < 5476):
        my_map_euclidean[spatio_temporal_collisions_euclidean[i]+73] = 255
        dynamic_obstacles_euclidean.append(spatio_temporal_collisions_euclidean[i]+73) 

    if (spatio_temporal_collisions_euclidean[i]+74 < 5476):
        my_map_euclidean[spatio_temporal_collisions_euclidean[i]+74] = 255
        dynamic_obstacles_euclidean.append(spatio_temporal_collisions_euclidean[i]+74) 

    if (spatio_temporal_collisions_euclidean[i]+75 < 5476):
        my_map_euclidean[spatio_temporal_collisions_euclidean[i]+75] = 255
        dynamic_obstacles_euclidean.append(spatio_temporal_collisions_euclidean[i]+75)

goal_neighbours = find_neighbors(robot_plan[-1],74,74,map,0.2)
print("goal neighbours:", goal_neighbours)
remove_nodes = [0] * len(goal_neighbours)

for i in range (len(remove_nodes)):
    remove_nodes[i] = goal_neighbours[i][0]

print("Remove nodes:", remove_nodes)

for i in range (len(remove_nodes)):
    if (remove_nodes[i] in dynamic_obstacles_euclidean):
        dynamic_obstacles_euclidean.remove(remove_nodes[i])


goal_neighbours = find_neighbors(robot_plan[-2],74,74,map,0.2)
print("goal neighbours:", goal_neighbours)
remove_nodes = [0] * len(goal_neighbours)

for i in range (len(remove_nodes)):
    remove_nodes[i] = goal_neighbours[i][0]

print("Remove nodes:", remove_nodes)

for i in range (len(remove_nodes)):
    if (remove_nodes[i] in dynamic_obstacles_euclidean):
        dynamic_obstacles_euclidean.remove(remove_nodes[i])



updated_map_euclidean =tuple(my_map_euclidean)

##Algorithm : Euclidean 

if (len(spatio_temporal_collisions_euclidean) == 0):
    updated_robot_plan_euclidean = robot_plan
else:
    updated_robot_plan_euclidean = [my_start_index]
    temp = a_star(start_index = my_start_index, goal_index = my_goal_index,width = 74, height= 74, 
                            costmap = updated_map_euclidean,resolution=my_resolution, origin=my_origin)
    for i in range (len(temp)):
        updated_robot_plan_euclidean.append(temp[i])

if (len(updated_robot_plan_euclidean)==1):
    updated_robot_plan_euclidean=robot_plan



## Manhatten
## Updating the Dynamic Obstacle

for i in range(len(spatio_temporal_collisions_manhatten)):
    if (spatio_temporal_collisions_manhatten[i]-75 < 5476):
        my_map_manhatten[spatio_temporal_collisions_manhatten[i]-75] =255
        dynamic_obstacles_manhatten.append(spatio_temporal_collisions_manhatten[i]-75)

    if (spatio_temporal_collisions_manhatten[i]-74 < 5476):
        my_map_manhatten[spatio_temporal_collisions_manhatten[i]-74] =255
        dynamic_obstacles_manhatten.append(spatio_temporal_collisions_manhatten[i]-74)

    if (spatio_temporal_collisions_manhatten[i]-73 < 5476):
        my_map_manhatten[spatio_temporal_collisions_manhatten[i]-73] = 255
        dynamic_obstacles_manhatten.append(spatio_temporal_collisions_manhatten[i]-75)
    
    if (spatio_temporal_collisions_manhatten[i]-1 < 5476):
        my_map_manhatten[spatio_temporal_collisions_manhatten[i]-1] =255
        dynamic_obstacles_manhatten.append(spatio_temporal_collisions_manhatten[i]-1)

    if (spatio_temporal_collisions_manhatten[i] < 5476):
        my_map_manhatten[spatio_temporal_collisions_manhatten[i]]   = 255
        dynamic_obstacles_manhatten.append(spatio_temporal_collisions_manhatten[i])

    if (spatio_temporal_collisions_manhatten[i]+1 < 5476):
        my_map_manhatten[spatio_temporal_collisions_manhatten[i]+1] = 255
        dynamic_obstacles_manhatten.append(spatio_temporal_collisions_manhatten[i]+1) 

    if (spatio_temporal_collisions_manhatten[i]+73 < 5476):
        my_map_manhatten[spatio_temporal_collisions_manhatten[i]+73] = 255
        dynamic_obstacles_manhatten.append(spatio_temporal_collisions_manhatten[i]+73) 

    if (spatio_temporal_collisions_manhatten[i]+74 < 5476):
        my_map_manhatten[spatio_temporal_collisions_manhatten[i]+74] = 255
        dynamic_obstacles_manhatten.append(spatio_temporal_collisions_manhatten[i]+74) 

    if (spatio_temporal_collisions_manhatten[i]+75 < 5476):
        my_map_manhatten[spatio_temporal_collisions_manhatten[i]+75] = 255
        dynamic_obstacles_manhatten.append(spatio_temporal_collisions_manhatten[i]+75)

goal_neighbours1 = find_neighbors(robot_plan[-1],74,74,map,0.2)
print("goal neighbours:", goal_neighbours1)
remove_nodes1 = [0] * len(goal_neighbours1)

for i in range (len(remove_nodes1)):
    remove_nodes1[i] = goal_neighbours1[i][0]

print("Remove nodes:", remove_nodes1)

for i in range (len(remove_nodes1)):
    if (remove_nodes1[i] in dynamic_obstacles_manhatten):
        dynamic_obstacles_manhatten.remove(remove_nodes1[i])


goal_neighbours2 = find_neighbors(robot_plan[-2],74,74,map,0.2)
print("goal neighbours:", goal_neighbours2)
remove_nodes2 = [0] * len(goal_neighbours2)

for i in range (len(remove_nodes2)):
    remove_nodes2[i] = goal_neighbours2[i][0]

print("Remove nodes:", remove_nodes2)

for i in range (len(remove_nodes2)):
    if (remove_nodes2[i] in dynamic_obstacles_manhatten):
        dynamic_obstacles_manhatten.remove(remove_nodes2[i])



updated_map_manhatten =tuple(my_map_manhatten)


##Algorithm : Manhatten

if (len(spatio_temporal_collisions_manhatten) == 0):
    updated_robot_plan_manhatten = robot_plan
else:
    updated_robot_plan_manhatten = [my_start_index]
    temp = a_star(start_index = my_start_index, goal_index = my_goal_index,width = 74, height= 74, 
                            costmap = updated_map_manhatten, resolution=my_resolution, origin=my_origin)
    for i in range (len(temp)):
        updated_robot_plan_manhatten.append(temp[i])

if (len(updated_robot_plan_manhatten)==1):
    updated_robot_plan_manhatten=robot_plan

##Dijkstra 
## updating the dynamic Obstacle

for i in range(len(spatio_temporal_collisions_dijkstra)):
    if (spatio_temporal_collisions_dijkstra[i]-75 < 5476):
        my_map_dijkstra[spatio_temporal_collisions_dijkstra[i]-75] =255
        dynamic_obstacles_dijkstra.append(spatio_temporal_collisions_dijkstra[i]-75)

    if (spatio_temporal_collisions_dijkstra[i]-74 < 5476):
        my_map_dijkstra[spatio_temporal_collisions_dijkstra[i]-74] =255
        dynamic_obstacles_dijkstra.append(spatio_temporal_collisions_dijkstra[i]-74)

    if (spatio_temporal_collisions_dijkstra[i]-73 < 5476):
        my_map_dijkstra[spatio_temporal_collisions_dijkstra[i]-73] = 255
        dynamic_obstacles_dijkstra.append(spatio_temporal_collisions_dijkstra[i]-75)
    
    if (spatio_temporal_collisions_dijkstra[i]-1 < 5476):
        my_map_dijkstra[spatio_temporal_collisions_dijkstra[i]-1] =255
        dynamic_obstacles_dijkstra.append(spatio_temporal_collisions_dijkstra[i]-1)

    if (spatio_temporal_collisions_dijkstra[i] < 5476):
        my_map_dijkstra[spatio_temporal_collisions_dijkstra[i]]   = 255
        dynamic_obstacles_dijkstra.append(spatio_temporal_collisions_dijkstra[i])

    if (spatio_temporal_collisions_dijkstra[i]+1 < 5476):
        my_map_dijkstra[spatio_temporal_collisions_dijkstra[i]+1] = 255
        dynamic_obstacles_dijkstra.append(spatio_temporal_collisions_dijkstra[i]+1) 

    if (spatio_temporal_collisions_dijkstra[i]+73 < 5476):
        my_map_dijkstra[spatio_temporal_collisions_dijkstra[i]+73] = 255
        dynamic_obstacles_dijkstra.append(spatio_temporal_collisions_dijkstra[i]+73) 

    if (spatio_temporal_collisions_dijkstra[i]+74 < 5476):
        my_map_dijkstra[spatio_temporal_collisions_dijkstra[i]+74] = 255
        dynamic_obstacles_dijkstra.append(spatio_temporal_collisions_dijkstra[i]+74) 

    if (spatio_temporal_collisions_dijkstra[i]+75 < 5476):
        my_map_dijkstra[spatio_temporal_collisions_dijkstra[i]+75] = 255
        dynamic_obstacles_dijkstra.append(spatio_temporal_collisions_dijkstra[i]+75)

goal_neighbours = find_neighbors(robot_plan[-1],74,74,map,0.2)
print("goal neighbours:", goal_neighbours)
remove_nodes = [0] * len(goal_neighbours)

for i in range (len(remove_nodes)):
    remove_nodes[i] = goal_neighbours[i][0]

print("Remove nodes:", remove_nodes)

for i in range (len(remove_nodes)):
    if (remove_nodes[i] in dynamic_obstacles_dijkstra):
        dynamic_obstacles_dijkstra.remove(remove_nodes[i])


goal_neighbours = find_neighbors(robot_plan[-2],74,74,map,0.2)
print("goal neighbours:", goal_neighbours)
remove_nodes = [0] * len(goal_neighbours)

for i in range (len(remove_nodes)):
    remove_nodes[i] = goal_neighbours[i][0]

print("Remove nodes:", remove_nodes)

for i in range (len(remove_nodes)):
    if (remove_nodes[i] in dynamic_obstacles_dijkstra):
        dynamic_obstacles_dijkstra.remove(remove_nodes[i])



updated_map_dijkstra =tuple(my_map_dijkstra)


##Algorithm: Dijkstra 

if (len(spatio_temporal_collisions_dijkstra) == 0):
    updated_robot_plan_dijkstra = robot_plan
else:
    updated_robot_plan_dijkstra = [my_start_index]
    temp = a_star(start_index = my_start_index, goal_index = my_goal_index,width = 74, height= 74, 
                            costmap = updated_map_dijkstra, resolution=my_resolution, origin=my_origin)
    for i in range (len(temp)):
        updated_robot_plan_dijkstra.append(temp[i])

if (len(updated_robot_plan_dijkstra)==1):
    updated_robot_plan_dijkstra = robot_plan



print ('##### Experiment Summary#####')
print("robot_plan:", robot_plan , len(robot_plan))
print("human trajectory:", human_trajectory, len(human_trajectory))


## euclidean 
print("             ###Euclidean ")
print("Distance Vector: euclidean:", distance_vector_euclidean, len(distance_vector_euclidean) )
print("Spatio-temporal-obstacles :euclidean", spatio_temporal_collisions_euclidean , len(spatio_temporal_collisions_euclidean))
print ("time instants euclidean:", time_instants_euclidean, len(time_instants_euclidean))

print ("safe Threshold: ", safeThreshold_Euclidean)
print ("updated robot path : euclidean: ", updated_robot_plan_euclidean, len(updated_robot_plan_euclidean))

## manhatten

print ("         ### Manhatten         ")
print("Distance Vector: manhatten:", distance_vector_manhatten, len(distance_vector_manhatten) )
print("Spatio-temporal-obstacles :manhatten", spatio_temporal_collisions_manhatten , len(spatio_temporal_collisions_manhatten))
print ("time instants manhatten:", time_instants_manhatten, len(time_instants_manhatten))

print ("safe Threshold: ", safeThreshold_manhantten)
print ("updated robot path : manhatten: ", updated_robot_plan_manhatten, len(updated_robot_plan_manhatten))

## DIjkstra

print ("            ### dijkstra's    ")
print("Distance Vector: dijkstra:", distance_vector_dijkstra, len(distance_vector_dijkstra) )
print("Spatio-temporal-obstacles :dijkstra", spatio_temporal_collisions_dijkstra , len(spatio_temporal_collisions_dijkstra))
print ("time instants dijkstra:", time_instants_dijkstra, len(time_instants_dijkstra))

print ("safe Threshold: ", safeThreshold_Dijkstra)
print ("updated robot path : dijkstra ", updated_robot_plan_dijkstra, len(updated_robot_plan_dijkstra))

print ("################ THanks ! ####################")

#Graph: 2
plt.plot(xy_start_index[0],xy_start_index[1],'o')
plt.plot(xy_goal_index[0], xy_goal_index[1],'o')
plt.plot(x_robot_plan,y_robot_plan)
plt.plot(x_human_trajectory[0], y_human_trajectory[0],'o')
plt.plot(x_human_trajectory, y_human_trajectory)
plt.plot(x_human_trajectory[-1], y_human_trajectory[-1],'o')
plt.legend(['robot:start', 'robot:goal', 'robot:path','human:start','human:path','human:goal'])
plt.plot(x_obstacles, y_obstacles,'o')
plt.show()


#Graph:3
plt.plot(x_obstacles, y_obstacles,'o')
plt.plot(xy_start_index[0],xy_start_index[1],'o')
plt.plot(xy_goal_index[0], xy_goal_index[1],'o')
plt.plot(x_robot_plan,y_robot_plan)
plt.plot(x_human_trajectory[0], y_human_trajectory[0],'o')
plt.plot(x_human_trajectory, y_human_trajectory)
plt.plot(x_human_trajectory[-1], y_human_trajectory[-1],'o')
plt.legend(['obstacles','robot:start', 'robot:goal', 'robot:path','human:start','human:path','human:goal'])

for i in range (len(time_instants_euclidean)):
    x_cor, y_cor = oneDtotwoD([robot_plan[time_instants_euclidean[i]],human_trajectory[time_instants_euclidean[i]]])
    plt.plot(x_cor, y_cor)
plt.show()


# Graph 4 

x_dynamic_obstacles,y_dynamic_obstacles = oneDtotwoD(dynamic_obstacles_euclidean)
x_updated_path, y_updated_path = oneDtotwoD(updated_robot_plan_euclidean)

plt.plot(x_obstacles,y_obstacles,'o')
plt.plot(x_dynamic_obstacles, y_dynamic_obstacles,'o')
plt.plot(x_updated_path, y_updated_path,'o')
plt.plot(x_human_trajectory,y_human_trajectory)
plt.plot(x_robot_plan, y_robot_plan)
plt.show()


### Mnahatten 
#Graph:3
plt.plot(x_obstacles, y_obstacles,'o')
plt.plot(xy_start_index[0],xy_start_index[1],'o')
plt.plot(xy_goal_index[0], xy_goal_index[1],'o')
plt.plot(x_robot_plan,y_robot_plan)
plt.plot(x_human_trajectory[0], y_human_trajectory[0],'o')
plt.plot(x_human_trajectory, y_human_trajectory)
plt.plot(x_human_trajectory[-1], y_human_trajectory[-1],'o')
plt.legend(['obstacles','robot:start', 'robot:goal', 'robot:path','human:start','human:path','human:goal'])

for i in range (len(time_instants_manhatten)):
    x_cor, y_cor = oneDtotwoD([robot_plan[time_instants_manhatten[i]],human_trajectory[time_instants_manhatten[i]]])
    plt.plot(x_cor, y_cor)
plt.show()


# Graph 4 

x_dynamic_obstacles,y_dynamic_obstacles = oneDtotwoD(dynamic_obstacles_manhatten)
x_updated_path, y_updated_path = oneDtotwoD(updated_robot_plan_manhatten)

plt.plot(x_obstacles,y_obstacles,'o')
plt.plot(x_dynamic_obstacles, y_dynamic_obstacles,'o')
plt.plot(x_updated_path, y_updated_path,'o')
plt.plot(x_human_trajectory,y_human_trajectory)
plt.plot(x_robot_plan, y_robot_plan)
plt.show()

#DIjkstra 
#Graph:5
plt.plot(x_obstacles, y_obstacles,'o')
plt.plot(xy_start_index[0],xy_start_index[1],'o')
plt.plot(xy_goal_index[0], xy_goal_index[1],'o')
plt.plot(x_robot_plan,y_robot_plan)
plt.plot(x_human_trajectory[0], y_human_trajectory[0],'o')
plt.plot(x_human_trajectory, y_human_trajectory)
plt.plot(x_human_trajectory[-1], y_human_trajectory[-1],'o')
plt.legend(['obstacles','robot:start', 'robot:goal', 'robot:path','human:start','human:path','human:goal'])

for i in range (len(time_instants_dijkstra)):
    x_cor, y_cor = oneDtotwoD([robot_plan[time_instants_dijkstra[i]],human_trajectory[time_instants_dijkstra[i]]])
    plt.plot(x_cor, y_cor)
plt.show()


# Graph 6

x_dynamic_obstacles,y_dynamic_obstacles = oneDtotwoD(dynamic_obstacles_dijkstra)
x_updated_path, y_updated_path = oneDtotwoD(updated_robot_plan_dijkstra)

plt.plot(x_obstacles,y_obstacles,'o')
plt.plot(x_dynamic_obstacles, y_dynamic_obstacles,'o')
plt.plot(x_updated_path, y_updated_path,'o')
plt.plot(x_human_trajectory,y_human_trajectory)
plt.plot(x_robot_plan, y_robot_plan)
plt.show()
