import random 
import costmap


def human_start_index (data=costmap.my_costmap):
    possible_human_starts = []
    for i in range(len(data)):
        if (data[i] < 128):
            possible_human_starts.append(i)
    return random.choice(possible_human_starts)


def genHumTrajectory (epoch_lenggth =10, map =costmap.my_costmap):
    init_loc = human_start_index()
    #print("INit loc:", init_loc)
    generated_trajectory = []
    generated_trajectory.append(init_loc)
    states = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while(len(generated_trajectory)!=epoch_lenggth):
        step = random.choice(states)
        temp = 0
        if (step==1):
            temp = generated_trajectory[-1] -75

        elif(step==2):
            temp = generated_trajectory[-1] -74

        elif(step==3):
            temp = generated_trajectory[-1] -73
        elif(step==4):
            temp = generated_trajectory[-1] -1
        elif(step==5):
            temp = generated_trajectory[-1]

        elif(step==6):
            temp = generated_trajectory[-1] +1
        elif(step==7):
            temp = generated_trajectory[-1] + 73

        elif(step==8):
            temp = generated_trajectory[-1] + 74
        elif(step==9):
            temp = generated_trajectory[-1] + 75

        if (map[temp]<128):
            generated_trajectory.append(temp)

    return generated_trajectory   



if __name__=="__main__":
    element = human_start_index()
    print("element:" , element)
    my_list = genHumTrajectory()
    print("trajectory:", my_list, len(my_list))

    for i in range (len(my_list)):
        e = my_list[i]
        print ("i=", i ,e, costmap.my_costmap[e])
