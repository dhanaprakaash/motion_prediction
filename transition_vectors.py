

import random


def create_transition_vector (mask):
    transition_vector = [0]*9
    for i in range(len(transition_vector)):
        transition_vector[i] = random.randint(0,20)


    for i in range(len(mask)):
        transition_vector[i]= mask[i] * transition_vector[i]
    
    sum_vector = sum(transition_vector)

    for i in range(len(transition_vector)):
        transition_vector[i]= round(transition_vector[i]/ sum_vector,2)
    #print("debug:",sum(transition_vector))
    
    return transition_vector


if __name__ == "__main__":
    mask = [0,0,0,0,1,1,0,1,1]
    my_vector = create_transition_vector(mask)

    print (my_vector)