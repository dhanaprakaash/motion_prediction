import numpy as np
import random

def generate_transistion_matrix ():

    markov_transistion_matrix = np.zeros((9,9))
    temp_sum = np.zeros(9)
    for i in range(len(markov_transistion_matrix[0])):
        for j in range(len(markov_transistion_matrix[0])):
            markov_transistion_matrix[i,j] = random.randint(1,9)
            temp_sum[i] += markov_transistion_matrix[i,j]
        
        #print("temp_sum", temp_sum[i])
        #print("temp_vector",temp_sum)


    for i in range (len(markov_transistion_matrix[0])):
        markov_transistion_matrix[i]=markov_transistion_matrix[i]/temp_sum[i]
    #print("Markov_Transistion_Chain",markov_transistion_matrix)

    '''for i in range(len(markov_transistion_matrix[0])):
        print(i, np.sum(markov_transistion_matrix[i])) '''

    for i in range(len(markov_transistion_matrix[0])):
        for j in range (len(markov_transistion_matrix[0])):
            markov_transistion_matrix[i,j] = round(markov_transistion_matrix[i, j], 3)
    
    final_matrix = markov_transistion_matrix.transpose() # Correct Matrix ! Dont be Confused!
    return final_matrix



if __name__=="__main__":
    matrix= generate_transistion_matrix()
    print(matrix)
    for i in range(9):
        print("row:", i,np.sum(matrix[i]))
    matrix_2 = np.zeros(9)
    matrix_2[3] = 1

    new_matrix = np.dot(matrix, matrix_2)
    print("Eurekha!",new_matrix,np.sum(new_matrix))
    
    
    for i in range(9):
        print(i, np.sum(new_matrix[i]))
    new = matrix.transpose()  # Wrong Method!
    new_matrix_2 = np.dot(new, matrix_2)
    for i in range(9):
        print(i,np.sum(new[i]))
    print(new_matrix_2, np.sum(new_matrix_2))