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


def gibbs_sampled_trajectory (no_smaples = 5, epoch_length =10, map =costmap.my_costmap):
    init_location= human_start_index()
    gibbs_trajextories = [0]*no_smaples
    for i in range(no_smaples):
        iter_trajectory = []
        iter_trajectory.append(init_location)
        states = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while(len(iter_trajectory)!=epoch_length):
            step = random.choice(states)
            temp = 0
            if (step==1):
                temp = iter_trajectory[-1] -75

            elif(step==2):
                temp = iter_trajectory[-1] -74

            elif(step==3):
                temp = iter_trajectory[-1] -73
            elif(step==4):
                temp = iter_trajectory[-1] -1
            elif(step==5):
                temp = iter_trajectory[-1]

            elif(step==6):
                temp = iter_trajectory[-1] +1
            elif(step==7):
                temp = iter_trajectory[-1] + 73

            elif(step==8):
                temp = iter_trajectory[-1] + 74
            elif(step==9):
                temp = iter_trajectory[-1] + 75

            if (map[temp]<128):
                iter_trajectory.append(temp)
        gibbs_trajextories[i]=iter_trajectory
    return gibbs_trajextories




if __name__=="__main__":
    element = human_start_index()
    print("element:" , element)
    my_list = genHumTrajectory()
    print("trajectory:", my_list, len(my_list))

    for i in range (len(my_list)):
        e = my_list[i]
        print ("i=", i ,e, costmap.my_costmap[e])

    trajec = gibbs_sampled_trajectory()
    print("traject:",trajec)
    print(len(trajec), len(trajec[0]))