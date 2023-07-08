import numpy as np
from generate_transistion_probability_matrix import generate_transistion_matrix


#  2 matries of Dimension 40 x 40 x 9 x 9
#  Each one for robots and HUmans
#  This is will get continously updated   
#  The Robot path planning is influenced by the transistion matrix 
#  The Human Path is predicted with the help of the matrix 



env_robot_trans_matrix = np.zeros((40,40,9,9))

for i in range(40):
    for j in range(40):
        env_robot_trans_matrix[i,j] = generate_transistion_matrix()

print("\n\nn\n")
print("sixe check", env_robot_trans_matrix[0].shape)
print(env_robot_trans_matrix[1][4][5])


env_human_trans_matrix = np.zeros((40,40,9,9))

for i in range(40):
    for j in range(40):
        env_human_trans_matrix[i,j] = generate_transistion_matrix()

print("Human",env_human_trans_matrix)
print("HUman")

path_vector_human = [1,2,3,4,5,6,7,8]
path_vector_robot = [4,3,5,6,7]


time_active_human = [0] * len(path_vector_human)
time_active_robot = [0] * len(path_vector_robot)



risk_matrix_human = np.zeros((len(path_vector_human),40,40))
risk_matrix_robot = np.zeros((len(path_vector_robot),40,40))

print(risk_matrix_human.shape)
print(risk_matrix_robot.shape)

