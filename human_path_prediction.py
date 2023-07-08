import numpy as np
from numpy.core.fromnumeric import argmax

from generate_transistion_probability_matrix import generate_transistion_matrix
from update_loc import update_loc


def update_location(argmax):
    argmax += 1
    loc_delta =(0,0)
    if argmax == 1:
        loc_delta=(-1,-1)
        return loc_delta
    elif argmax == 2:
        loc_delta = (0,-1)
        return loc_delta
    elif argmax == 3:
        loc_delta = (1,-1)
        return loc_delta
    elif argmax == 4:
        loc_delta = (-1,0)
        return loc_delta
    elif argmax == 5:
        loc_delta = (0,0)
        return loc_delta
    elif argmax == 6:
        loc_delta = (1,0)
        return loc_delta
    elif argmax == 7:
        loc_delta = (-1,1)
        return loc_delta
    elif argmax == 8:
        loc_delta = (0,1)
        return loc_delta
    elif argmax == 9:
        loc_delta = (1,1)
        return loc_delta
    else:
        print("Error!")




def human_path_prediction(source_loc, time_taken):


    print("Source", source_loc[0],source_loc[1])


    matrix_transistion = np.zeros((40,40,9,9))
    initial_state = np.zeros(9)

    for i in range(40):
        for j in range(40):
            matrix_transistion[i,j] = generate_transistion_matrix()
    print("Matrix Generated Succuessfully!")
    

    initial_state[5] = 1
    
    path_vector = [0]*time_taken
    current_state = initial_state
    print("Current_State", current_state, current_state.shape)
    updated_loc = source_loc
    print("updated_loc", updated_loc)
    T_mat = matrix_transistion[source_loc[0],source_loc[1]]
    print("T_mat",T_mat)
    print("T_max Succewssfull!")
    for i in range (len(path_vector)):
        next_state = np.dot(T_mat, current_state)
        print("****")
        print("next_state", next_state, "size:",np.sum(next_state))
        path_vector[i]= argmax(next_state)
        print("Path_Vector", path_vector)
        current_state = next_state   # the vector got updated 
        updated_loc = update_location(path_vector[i])  # updating the matrix
        print(updated_loc)
        a= source_loc[0] + updated_loc[0]
        b= source_loc[1] + updated_loc[1]
        T_mat = matrix_transistion[a,b]

    print("Won!", path_vector)
    for i in range(len(path_vector)):
        path_vector[i] += 1
    return path_vector


if __name__ == "__main__":
    src = (2,5)
    path = human_path_prediction(src,20)
    print(path)


# Output :
# States 1, 2, 3, 4, 5, 6, 7, 8, 9 

