from turtle import color
#from matplotlib.lines import _LineStyle
import numpy as np 
import matplotlib.pyplot as plt
import random
from human_path_prediction import human_path_prediction
from new_path import new_path
from random_location import a_random_position
from numpy.core.fromnumeric import shape
from robot import Robot
from human import Human
from robot_path_plan import robot_path_planning
from distance_funs import manhatten_distance
from new_path import new_path
from minimin import minimum


# initial Environment 

dimension = 40
no_of_static_obstacles = 8

map = np.zeros((dimension,dimension))
obstacle = np.full((3,3),255)

#initial State 
print(map)
print(obstacle)
print("Length: ",len(map[0]))
print("FIrst row: ", map[0])

print("\n\n\n")

# ALGORITHM FOR CREATING THE OBSTACLES : 

number_of_obstacle = 0

while (number_of_obstacle < no_of_static_obstacles):
        i = random.randint(0,dimension-1)
        j = random.randint(0,dimension-1)
        print("DEbug", i,j)
        try:
            map[i,j]=  obstacle[1,1] 
        except IndexError:
            pass
        try:
            map[i,j+1]= obstacle[1,2]
        except IndexError:
            pass
        try:
            map[i,j-1]= obstacle[1,0]
        except IndexError:
            pass
        try:
            map[i-1,j]= obstacle[0,1]
        except IndexError:
            pass
        try:
            map[i+1,j]= obstacle[2,1]
        except IndexError:
            pass
        try:
            map[i-1,j-1]= obstacle[0,0]
        except IndexError:
            pass
        try:
            map[i+1,j-1]= obstacle[2,0]
        except IndexError:
            pass
        try:
            map[i-1,j+1]= obstacle[0,2] 
        except IndexError:
            pass
        try:
            map[i+1,j+1]= obstacle[2,2]
        except IndexError:
            pass
        number_of_obstacle += 1
#print("Dimension: ",shape(map))
print("After", map)  




R1 = Robot ("Robot_1")
H1 = Human ("Human_1")

R1.set_init_loc( a_random_position(dimension,dimension))
R1.set_dest_loc(a_random_position(dimension,dimension))
r1_src = R1.get_init_loc()
r1_dst = R1.get_dest_loc()
r1_path = robot_path_planning(r1_src, r1_dst)
R1.set_planned_path(r1_path)
check = R1.get_path_robot()

print("Check: ",check)


H1.set_init_loc(a_random_position(dimension,dimension))
H1.set_dst_loc(a_random_position(dimension,dimension))


# Human Path Prediction 
h1_src_loc = H1.get_init_loc()
h1_dst_loc = H1.get_dst_loc()

h1_src_loc  = (round(h1_src_loc[0]), round(h1_src_loc[1]))

time_taken =  manhatten_distance(h1_src_loc,h1_dst_loc)
print("HI source",h1_src_loc)
H1.print_details()
R1.print_details()

transistion_vector = human_path_prediction(h1_src_loc, time_taken)
print ("*****new path****** ",transistion_vector)


human_path = new_path(h1_src_loc, transistion_vector)
H1.set_path(human_path)
print("Human Path",human_path)

plt.imshow(map, interpolation='none')
#plt.matshow(a)
#plt.show()


print("robot_Path and Humsn Path\n", r1_path, human_path)

# PLOTTING HUMAN AND ROBOT PATH:

time_axis_robot = np.zeros(len(r1_path))
time_axis_human = np.zeros(len(human_path))

for i in range(len(time_axis_robot)):
    time_axis_robot[i] = i

for i in range(len(time_axis_human)):
    time_axis_human[i] = i

print("time_axis_robot",time_axis_robot)
print("time_axis_human", time_axis_human)

robot_x_axis = [0] * len(r1_path)
robot_y_axis = [0] * len(r1_path)
human_x_axis = [0] * len(human_path)
human_y_axis = [0] * len(human_path)


for i in range(len(r1_path)):
    robot_x_axis[i] = r1_path[i][0]
    robot_y_axis[i] = r1_path[i][1]

print ("ra_path", r1_path)

for i in range(len(human_path)):
    human_x_axis[i] = human_path[i][0]
    human_y_axis[i] = human_path[i][1]


print ("robot_y",robot_y_axis, "robot_x",robot_x_axis, "human_x",human_x_axis, "human_y",human_y_axis)
print("*****\n\n\n\n\n")  
'''

plt.plot(r1_path,time_axis_robot)
plt.plot(human_path,time_axis_human)

plt.show()


plt.scatter(robot_x_axis,robot_y_axis)
plt.scatter(human_x_axis, human_y_axis)

plt.show()
'''
print("Debug: ","Human Path", "Robot Path")
print("HUman:", human_path)
print("Robot:", r1_path)

x_axis_human = [0] * len(human_path)
y_axis_human = [0] * len(human_path)

x_axis_robot = [0] * len(r1_path)
y_axis_robot = [0] * len(r1_path)

for i in range(len(human_path)):
    x_axis_human[i] = human_path[i][0]
    y_axis_human[i] = human_path[i][1]

print("x_axis: ", x_axis_human)
print("y_axis: ",y_axis_human )

for i in range(len(r1_path)):
    x_axis_robot[i] = r1_path[i][0]
    y_axis_robot[i] = r1_path[i][1]

print("x_axis: ", x_axis_robot)
print("y_axis: ",y_axis_robot )


plot1 = plt.figure(1)
ax = plt.subplot()
for i in range(len(human_path)):
    plt.scatter(x_axis_human[i], y_axis_human[i])
for i in range(len(r1_path)):  
    plt.scatter(x_axis_robot[i], y_axis_robot[i])
plt.plot(x_axis_human, y_axis_human, label="Human motion")
plt.plot(x_axis_robot, y_axis_robot, label="Robot motion")
plt.grid()
plt.legend()
#plt.show()



print("Debug: Robot and Human Path")
print("Robot:", r1_path)
print("Human: ", human_path)


print ("\n\n\n")
print("\t\t\t\t\t\t****  Details ****")


H1.print_details()
R1.print_details()
print()
### *** End of the ENvironemental Details *** 

### The Risk assessment 

print ("#### Risk Assessment! ####")
human_path_test = H1.get_path_human()
length_human = len(human_path_test)

print("\n\n\n\thuman_path_test",human_path_test, "length= ", length_human)

robot_path_test = R1.get_path_robot()
length_robot = len(robot_path_test)

print ("\n\n\n\tRobot_test", robot_path_test, "length = ", length_robot)


# Matrix for finding the probability 

# For Humans 

human_presence_matrix = np.zeros((dimension,dimension))
robot_presence_matrix = np.zeros((dimension,dimension))


print("human_presence_matrix", human_presence_matrix)


sum_human_matrix = 0 
for i in range(len(human_presence_matrix[0])):
    for j in range (len(human_presence_matrix[1])):
        human_presence_matrix[i,j]= random.randint(0,40)
        sum_human_matrix = sum_human_matrix + human_presence_matrix[i,j]


print("human_presence_matrix", human_presence_matrix)
print("sum_human_matrix", sum_human_matrix)

sum_robot_matrix = 0
for i in range (len(robot_presence_matrix[0])):
    for j in range (len(robot_presence_matrix[1])):
        robot_presence_matrix[i,j]=random.randint(0,40)
        sum_robot_matrix = sum_robot_matrix + robot_presence_matrix[i,j]

print("robot_presence_matrix", robot_presence_matrix)
print("sum_robot_matrix", sum_robot_matrix)


# Probability Matrix
# for HUmans 

for i in range (len(human_presence_matrix[0])):
    for j in range (len(human_presence_matrix[1])):
        human_presence_matrix[i,j] = human_presence_matrix[i,j]/ sum_human_matrix

for i in range (len(robot_presence_matrix[0])):
    for j in range (len(robot_presence_matrix[1])):
        robot_presence_matrix[i,j] = robot_presence_matrix[i,j]/ sum_robot_matrix 


# printing the final matrix 

print ("human probability matrix: ", human_presence_matrix)
print ("robot probability matrix: ", robot_presence_matrix)

## testing the test_sum

test_sum = 0 

for i in range (len(human_presence_matrix[0])):
    for j in range (len(human_presence_matrix[1])):
        test_sum = test_sum + human_presence_matrix[i,j]

print("Human test", test_sum)

# For Robot

time_length = minimum( len(human_path_test), len(robot_path_test))
distance_vector = [0] * time_length
risk_vector = [0] * time_length

for i in range(time_length):
    distance_vector[i] = manhatten_distance(human_path_test[i],robot_path_test[i])

print("distance vector",distance_vector)

threshold_distance = 30
for i in range (time_length):
    if (distance_vector[i] < threshold_distance):
        risk_vector[i]=1
    else:
        risk_vector[i]=0

print("risk_vector",risk_vector)

# Risk Matrix 

risk_matrix = np.zeros((time_length,40,40))
probability_risk = [0] * time_length
print("Time Length", time_length)
print("shape of risk matrix",np.shape(risk_matrix) )
print("***Probability_risk***", probability_risk)

### ALGORITHM FOR RISK CALCULATION 


count_c1 = 0
count_c2 = 0
count_c3 = 0
count_c4 = 0
count_c5 = 0
count_c6 = 0
count_c7 = 0
count_c8 = 0
count_c9 = 0


for k in range(time_length):
    if(risk_vector[k]==1):
        for i in range(40):
            for j in range(40):
                if (i==0 and j==0):
                    count_c1 = count_c1 +1 
                    risk_matrix[k,i,j]=human_presence_matrix[i, j] * robot_presence_matrix[i,j]
                    risk_matrix[k,i+1,j]=human_presence_matrix[i+1, j] * robot_presence_matrix[i+1, j]
                    risk_matrix[k,i,j+1]=human_presence_matrix[i, j+1] * robot_presence_matrix[i, j+1]
                    risk_matrix[k,i+1, j+1]=human_presence_matrix[i+1, j+1] * robot_presence_matrix[i+1, j+1]
                    print("case 1",risk_matrix[k,i,j], risk_matrix[k,i+1,j], risk_matrix[k,i,j+1], risk_matrix[k,i+1,j+1],"==",risk_matrix[k,i,j]+ risk_matrix[k,i+1,j]+ risk_matrix[k,i,j+1]+risk_matrix[k,i+1, j+1] )
                    probability_risk[k] = risk_matrix[k,i,j]+risk_matrix[k,i+1,j]+risk_matrix[k,i,j+1]+risk_matrix[k,i+1, j+1]

                elif (i==39 and j == 0):
                    count_c2 = count_c2 +1
                    risk_matrix[k,i,j]=human_presence_matrix[i, j] * robot_presence_matrix[i,j]
                    risk_matrix[k,i-1,j]=human_presence_matrix[i-1, j] * robot_presence_matrix[i-1, j]
                    risk_matrix[k,i-1,j+1]=human_presence_matrix[i-1,j+1] * robot_presence_matrix[i-1, j+1]
                    risk_matrix[k,i,j+1]=human_presence_matrix[i, j+1] * robot_presence_matrix[i, j+1]
                    print("case 2 ", risk_matrix[k, i, j]+ risk_matrix[k, i-1, j]+risk_matrix[k, i-1, j+1] +risk_matrix[k, i, j+1])
                    probability_risk[k] = risk_matrix[k, i, j]+ risk_matrix[k, i-1, j]+risk_matrix[k, i-1, j+1] +risk_matrix[k, i, j+1]
                elif (i==0 and j ==39):
                    count_c3 = count_c3 +1
                    risk_matrix[k,i,j]=human_presence_matrix[i, j] * robot_presence_matrix[i,j]
                    risk_matrix[k,i,j-1]=human_presence_matrix[i, j-1] * robot_presence_matrix[i, j-1]
                    risk_matrix[k,i+1,j]=human_presence_matrix[i+1, j] * robot_presence_matrix[i+1, j]
                    risk_matrix[k,i+1, j]=human_presence_matrix[i+1, j] * robot_presence_matrix[i+1, j]
                    print("Case 3:",risk_matrix[k, i, j]+ risk_matrix[k, i, j-1]+risk_matrix[k, i+1, j] + risk_matrix[k, i+1, j] )
                    probability_risk[k] = risk_matrix[k, i, j]+ risk_matrix[k, i, j-1]+risk_matrix[k, i+1, j] + risk_matrix[k, i+1, j]
                    
                elif(i==39 and j ==39):
                    count_c4 = count_c4 +1
                    risk_matrix[k,i,j]=human_presence_matrix[i, j] * robot_presence_matrix[i,j]
                    risk_matrix[k,i-1,j]=human_presence_matrix[i-1, j] * robot_presence_matrix[i-1, j]
                    risk_matrix[k,i,j-1]=human_presence_matrix[i, j-1] * robot_presence_matrix[i, j-1]
                    risk_matrix[k,i-1,j-1]=human_presence_matrix[i-1,j-1] * robot_presence_matrix[i-1,j-1]
                    print("case 4 ",risk_matrix[k, i, j]+ risk_matrix[k, i-1, j]+risk_matrix[k, i, j-1] + risk_matrix[k, i-1, j-1] )
                    probability_risk[k] = risk_matrix[k, i, j]+ risk_matrix[k, i-1, j]+risk_matrix[k, i, j-1] + risk_matrix[k, i-1, j-1]

                elif (j==0 and (i !=0 and i !=39)):# correct
                    count_c5 = count_c5 +1 
                    risk_matrix[k,i,j]=human_presence_matrix[i, j] * robot_presence_matrix[i,j]
                    risk_matrix[k,i-1,j]=human_presence_matrix[i-1, j] * robot_presence_matrix[i-1, j]
                    risk_matrix[k,i+1,j]=human_presence_matrix[i+1, j] * robot_presence_matrix[i+1, j]
                    risk_matrix[k,i-1,j+1] = human_presence_matrix[i-1,j+1] * robot_presence_matrix[i-1, j+1]
                    risk_matrix[k,i,j+1]=human_presence_matrix[i, j+1] * robot_presence_matrix[i, j+1]
                    risk_matrix[k,i+1, j+1]=human_presence_matrix[i+1, j+1] * robot_presence_matrix[i+1, j+1]
                    print("case 5", risk_matrix[k, i, j] + risk_matrix[k, i-1, j] + risk_matrix[k, i+1, j] + risk_matrix[k,i-1, j+1] +risk_matrix[k, i,j+1] +risk_matrix[k, i+1,j+1])
                    probability_risk[k] = risk_matrix[k, i, j] + risk_matrix[k, i-1, j] + risk_matrix[k, i+1, j] + risk_matrix[k,i-1, j+1] +risk_matrix[k, i,j+1] +risk_matrix[k, i+1,j+1]
                    
                elif (j==39 and (i !=0 and i !=39)): # correct
                    count_c6 = count_c6 +1 
                    risk_matrix[k,i,j]=human_presence_matrix[i, j] * robot_presence_matrix[i,j]
                    risk_matrix[k,i-1,j]=human_presence_matrix[i-1, j] * robot_presence_matrix[i-1, j]
                    risk_matrix[k,i+1,j]=human_presence_matrix[i+1, j] * robot_presence_matrix[i+1, j]
                    risk_matrix[k,i-1,j-1]=human_presence_matrix[i-1][j-1] * robot_presence_matrix[i-1][j-1]
                    risk_matrix[k,i,j-1]=human_presence_matrix[i, j-1] * robot_presence_matrix[i, j-1]
                    risk_matrix[k,i+1,j-1]=human_presence_matrix[i+1,j-1] * robot_presence_matrix[i+1,j-1]
                    print("case 6" , risk_matrix[k, i, j]+ risk_matrix[k, i-1, j]+risk_matrix[k, i+1, j] +risk_matrix[k, i-1, j-1] +risk_matrix[k, i,j-1] +risk_matrix[k, i+1,j-1])
                    probability_risk[k] = risk_matrix[k, i, j]+ risk_matrix[k, i-1, j]+risk_matrix[k, i+1, j] +risk_matrix[k, i-1, j-1] +risk_matrix[k, i,j-1] +risk_matrix[k, i+1,j-1]

                elif(i==0 and (j!=0 and j!=39)):
                    count_c7 = count_c7 +1
                    risk_matrix[k,i,j]=human_presence_matrix[i, j] * robot_presence_matrix[i,j]
                    risk_matrix[k,i+1,j]=human_presence_matrix[i+1, j] * robot_presence_matrix[i+1, j]
                    risk_matrix[k,i,j+1]=human_presence_matrix[i, j+1] * robot_presence_matrix[i, j+1]
                    risk_matrix[k,i+1, j+1]=human_presence_matrix[i+1, j+1] * robot_presence_matrix[i+1, j+1]
                    risk_matrix[k,i,j-1]=human_presence_matrix[i, j-1] * robot_presence_matrix[i, j-1]
                    risk_matrix[k,i+1,j-1]=human_presence_matrix[i+1,j-1] * robot_presence_matrix[i+1,j-1]
                    print("case 7", risk_matrix[k, i, j]+ risk_matrix[k, i+1, j]+risk_matrix[k, i, j+1] +risk_matrix[k, i+1, j+1] +risk_matrix[k, i,j-1] +risk_matrix[k, i+1,j-1])
                    probability_risk[k] = risk_matrix[k, i, j]+ risk_matrix[k, i+1, j]+risk_matrix[k, i, j+1] +risk_matrix[k, i+1, j+1] +risk_matrix[k, i,j-1] +risk_matrix[k, i+1,j-1]
                    
                elif (i==39 and (j !=0 and j !=39)) :
                    count_c8 = count_c8 +1
                    risk_matrix[k,i,j]=human_presence_matrix[i, j] * robot_presence_matrix[i,j]
                    risk_matrix[k,i-1,j]=human_presence_matrix[i-1, j] * robot_presence_matrix[i-1, j]
                    risk_matrix[k,i-1,j+1] = human_presence_matrix[i-1,j+1] * robot_presence_matrix[i-1, j+1]
                    risk_matrix[k,i,j+1]=human_presence_matrix[i, j+1] * robot_presence_matrix[i, j+1]
                    risk_matrix[k,i-1,j-1]=human_presence_matrix[i-1][j-1] * robot_presence_matrix[i-1][j-1]
                    risk_matrix[k,i,j-1]=human_presence_matrix[i, j-1] * robot_presence_matrix[i, j-1]
                    print("case 8", risk_matrix[k, i, j]+ risk_matrix[k, i-1, j]+risk_matrix[k, i-1, j+1] + risk_matrix[k, i, j+1] +risk_matrix[k, i-1,j-1] +risk_matrix[k, i,j-1])
                    probability_risk[k] = risk_matrix[k, i, j]+ risk_matrix[k, i-1, j]+risk_matrix[k, i-1, j+1] + risk_matrix[k, i, j+1] +risk_matrix[k, i-1,j-1] +risk_matrix[k, i,j-1]
                    
                else:
                    count_c9 = count_c9 +1
                    risk_matrix[k,i,j]=human_presence_matrix[i, j] * robot_presence_matrix[i,j]
                    risk_matrix[k,i-1,j]=human_presence_matrix[i-1, j] * robot_presence_matrix[i-1, j]
                    risk_matrix[k,i+1,j]=human_presence_matrix[i+1, j] * robot_presence_matrix[i+1, j]
                    
                    risk_matrix[k,i-1,j+1] = human_presence_matrix[i-1,j+1] * robot_presence_matrix[i-1, j+1]
                    risk_matrix[k,i,j+1]=human_presence_matrix[i, j+1] * robot_presence_matrix[i, j+1]
                    risk_matrix[k,i+1, j+1]=human_presence_matrix[i+1, j+1] * robot_presence_matrix[i+1, j+1]
                
                    risk_matrix[k,i-1,j-1]=human_presence_matrix[i-1][j-1] * robot_presence_matrix[i-1][j-1]
                    risk_matrix[k,i,j-1]=human_presence_matrix[i, j-1] * robot_presence_matrix[i, j-1]
                    risk_matrix[k,i+1,j-1]=human_presence_matrix[i+1,j-1] * robot_presence_matrix[i+1,j-1]
                    print("case 9",risk_matrix[k, i, j]+ risk_matrix[k, i-1, j]+risk_matrix[k, i+1, j] + risk_matrix[k, i-1, j+1] +risk_matrix[k, i,j+1] +risk_matrix[k, i+1,j+1] + risk_matrix[k, i-1,j-1] + risk_matrix[k, i,j-1] + risk_matrix[k,i+1,j-1] )
                    probability_risk[k] = risk_matrix[k, i, j]+ risk_matrix[k, i-1, j]+risk_matrix[k, i+1, j] + risk_matrix[k, i-1, j+1] +risk_matrix[k, i,j+1] +risk_matrix[k, i+1,j+1] + risk_matrix[k, i-1,j-1] + risk_matrix[k, i,j-1] + risk_matrix[k,i+1,j-1]

        print ("Probabi;lity ",probability_risk[k])

print ("count cas 1: ", count_c1)
print ("count cas 2: ", count_c2)
print ("count cas 3: ", count_c3)
print ("count cas 4: ", count_c4)
print ("count cas 5: ", count_c5)
print ("count cas 6: ", count_c6)
print ("count cas 7: ", count_c7)
print ("count cas 8: ", count_c8)
print ("count cas 9: ", count_c9)
print ("Total: ", count_c1+count_c2+count_c3+count_c4+count_c5+count_c6+count_c7+count_c8+count_c9)
print("expected : ", time_length * 40 *40)


print("risk_vector",risk_vector)


                

print("risk_matrix", risk_matrix)
print("Risk_Matrix_shape", risk_matrix.shape)
print ("the end!")

temp_count = 0
for i in range(time_length):
    for j in range(40):
        for k in range(40):
            if (risk_matrix[i,j,k]!=0):
                print (i, j, k , risk_matrix[i,j,k])
                print("\n")
                temp_count = temp_count +1

print (temp_count,(time_length*40*40))
print ("probability risk")


for i in range (len(probability_risk)):
    probability_risk[i]=np.sum(risk_matrix[i])
    print(probability_risk[i])


for k in range (time_length):
    print ("k= ", k )
    print("\n")
    for i in range (40):
        print(risk_matrix[k,i])
print ("#### Debug ####")

print("risk_matrix[0]", risk_matrix[0])

print("Probability Risk",len(probability_risk),probability_risk)
print("distance_vector",len(distance_vector), distance_vector)
print("risk_vector",len(risk_vector) ,risk_vector)



## Debugging 

# human presence matrix 

for i in range(40):
    for j in range(40):
        print("i=",i, "j=", j, human_presence_matrix[i][j], robot_presence_matrix[i][j])    



## probability _new _risk 


print (np.shape(risk_matrix))
print (np.shape(risk_matrix[1]))
print (np.shape(risk_matrix[1][2]))
print (np.shape(risk_matrix[1][2][3]))


risk_sum = [0] * time_length
for i in range(time_length):
    risk_sum[i] = np.sum(risk_matrix[i])


print ("risk_matrix", risk_sum)

### Calculating the risk 


print ("human_path_test" , human_path_test)
print ("robot_path_test", robot_path_test)





collision_matrix = np.zeros((time_length, 40, 40))

for k in range (time_length):
    if (risk_vector[k]):
        try: 
            collision_matrix[k,round(human_path_test[k][0], None), round(human_path_test[k][1], None)] = 1
        except IndexError as e:
            print (e)
            print ("Run Again!")


print ("collision Matrix" , collision_matrix) 

for i in range (time_length):
    print("i=", i , np.sum(collision_matrix[i]))

print("end")

collision_probability  = np.zeros((time_length, 40, 40))

collision_probability = np.multiply(collision_matrix, risk_matrix)

for k in range(time_length):
    for i in range (40):
        for j in range(40):
            if(collision_matrix[k,i,j] == 1):
                print(k,i,j,"|", "c=",collision_probability[k,i,j], "a=", collision_matrix[k,i,j], "b=", risk_matrix[k,i,j] )


risk_prob_time = [0] * time_length
print("collision Probability!")
for k in range (time_length):
    risk_prob_time[k] = np.sum(collision_probability[k])
    print("k:",k,risk_prob_time[k])


## plotting 

risk_x_axis = [0] * time_length

for i in range(len(risk_x_axis)):
    risk_x_axis[i] = i

risk_y_axis = [0] * time_length 

for i in range (len(risk_y_axis)):
    risk_y_axis[i] = risk_prob_time[i]
plot_risk = plt.figure()
plt.plot(risk_x_axis, risk_y_axis, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
plt.xlabel('Time instants')
plt.ylabel('Probability of collision')
plt.title('Probability of Collision Vs Time')

#plt.show()
print (human_path_prediction)
print("human_path",human_path)
print("risk_vector", risk_vector)

### Verification of ALgorithm 
### Using Monte Carlo Methods 

print(" \t\t\t ###Verification!### ")

verification_para = 100
ver_human_src_loc = H1.get_init_loc()
ver_human_dst_loc = H1.get_dst_loc()

ver_time_taken = time_taken
ver_robot_path = R1.get_path_robot()
ver_human_path_test = H1.get_path_human()

ver_human_src_loc=(round(ver_human_src_loc[0]), round(ver_human_src_loc[1]))
random_walk_human = [0] * verification_para



for i in range (verification_para):
    ver_transisition_vector = human_path_prediction(ver_human_src_loc,ver_time_taken)
    ver_human_path = new_path(ver_human_src_loc, ver_transisition_vector)
    random_walk_human[i] = ver_human_path 

print(ver_human_path_test)
print(ver_human_path)

for i in range (len(random_walk_human)):
    print("i=", i, random_walk_human[i])
print("end!")

### verification monte carlo 

ver_probability_vector = [0] * time_length

for i in range (verification_para):
    for j in range(time_length):
        if (manhatten_distance(random_walk_human[i][j], ver_robot_path[j]) < threshold_distance):
            ver_probability_vector[j] += (1/16) * (1 / 16)


for i in range (len(ver_probability_vector)):
    ver_probability_vector[i] = (ver_probability_vector[i] / verification_para)
print("ver_prob",ver_probability_vector) 
print("risk_prob",risk_prob_time)

for i in range (len(ver_probability_vector)):
    print("i=", i ,risk_prob_time[i], ver_probability_vector[i])




risk_x_axis = [0] * time_length

for i in range(len(risk_x_axis)):
    risk_x_axis[i] = i

risk_y_axis = [0] * time_length 
ver_y_axis = [0] * time_length

for i in range (len(risk_y_axis)):
    risk_y_axis[i] = risk_prob_time[i]
    ver_y_axis[i] = ver_probability_vector[i]

plot_risk = plt.figure()
plt.plot(risk_x_axis, risk_y_axis, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
plt.plot(risk_x_axis, ver_y_axis, color= "red" )
plt.xlabel('Time instants')
plt.ylabel('Probability of collision')
plt.title('Probability of Collision Vs Time')

plt.show()
