import random 
import numpy as np
from distance_funs import manhatten_distance
from random_location import a_random_position
markov_transistion_matrix = np.zeros((9,9))
initial_state_vector = np.zeros(9)
print(markov_transistion_matrix)

""" Given the Initial position and Destination Position
    How to find the Path for Humans
    -> Multiple paths
"""
ini_position = a_random_position(40,40)
dst_position = a_random_position(40,40)

print("INitial Position: ", ini_position, "Destination:", dst_position)

print("markov_matrix:",markov_transistion_matrix[0])
print("Initial_Vector:",initial_state_vector)

temp_sum = np.zeros(9)
for i in range(len(markov_transistion_matrix[0])):
    for j in range(len(markov_transistion_matrix[0])):
        markov_transistion_matrix[i,j] = random.randint(1,9)
        temp_sum[i] += markov_transistion_matrix[i,j]
        
    print("temp_sum", temp_sum[i])
    print("temp_vector",temp_sum)
print(markov_transistion_matrix)

# Creating the Transistion Matrix 

for i in range (len(markov_transistion_matrix[0])):
        markov_transistion_matrix[i]=markov_transistion_matrix[i]/temp_sum[i]

skimmed_Transistion_matrix = markov_transistion_matrix
print("Skimmed TRansistion Matrix",skimmed_Transistion_matrix)

for i in range(len(markov_transistion_matrix[0])):
    for j in range (len(markov_transistion_matrix[0])):
        skimmed_Transistion_matrix[i,j] = round(skimmed_Transistion_matrix[i, j], 3)
#print("After SKimming:")
#print(skimmed_Transistion_matrix)


print("Transistion Matrix:")
print(markov_transistion_matrix)

# The Final Transistion Matrix 
Trans_Mat = skimmed_Transistion_matrix.transpose()

print("Transpose Skimmed")
print( Trans_Mat)

initial_state_vector[5] = 1
#initial_state_vector[5] = 1
# Matrix X Vector MUltiplication 

resultant_2 = np.dot (Trans_Mat, initial_state_vector)
print("Resultant", resultant_2 , "sum:", np.sum(resultant_2))

# Generating the Path:


h1_start_location = a_random_position(40,40)
h1_dest_locatiion = a_random_position(40,40)

print("h1_start","h1_destin", h1_start_location, h1_dest_locatiion)

time_taken = manhatten_distance(h1_start_location, h1_dest_locatiion)

print("time_taken", time_taken)


path_vec = [0] * time_taken
current_state= initial_state_vector
next_state = np.zeros(9)

print(current_state, next_state)
print("Time Loop Starts.....")

for i in range(time_taken):
    next_state = np.dot(Trans_Mat,current_state)
    print(i)
    print("next_state\n",next_state)
    print("sum", np.sum(next_state))
    print("Current_stat\n",current_state)
    print("Sum", np.sum(current_state))
    print("\n")
    path_vec[i] = np.argmax(next_state)
    current_state = next_state

print("Path_Vector", path_vec)
