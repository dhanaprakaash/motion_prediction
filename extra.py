#number of index 
human_init_index = random.randint(0,5476)
print (human_init_index)

print("print:", transition_probability_tensor[human_init_index])
print("print:", max(transition_probability_tensor[human_init_index]))
print("print:",  transition_probability_tensor[human_init_index].index(max(transition_probability_tensor[human_init_index])))
next_state = transition_probability_tensor[human_init_index].index(max(transition_probability_tensor[human_init_index])) + 1
print("next_state:", next_state)


predicted_human_trajectory = [] 

predicted_human_trajectory.append(human_init_index)

def next_state_prediction (transition_vector):
    next_state = transition_vector.index(max(transition_vector))
    print(next_state+1)
    return next_state+1

'''or i in range (10):

    next_state = transition_probability_tensor
    predicted_human_trajectory.append()'''

def human_motion_prediction (init_position, time_steps =10):
    path_vector = []
    path_vector.append(init_position)
    for i in range(time_steps):
        path_vector.append(next_state_to_index(path_vector[i], next_state_prediction(transition_probability_tensor[path_vector[i]] )))
    print ("path_vector:",path_vector)


human_motion_prediction (1234)