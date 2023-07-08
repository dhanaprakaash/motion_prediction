import numpy as np
import matplotlib.pyplot as plt
import random

x_grids_max = 100 
y_grids_max = 100

#Occupancy Matrix: 
occu_matrix = np.zeros((x_grids_max,y_grids_max))
occu_matrix = occu_matrix.astype(int)
transition_matrix = np.zeros((x_grids_max*y_grids_max,9))
transition_matrix = transition_matrix.astype(int)
transition_matrix[ 20*100, 3 ] = 5

def randomwalk2D(n, x_init, y_init):
    # [0, 0, 0, ... ,0]
    x = np.zeros(n)
    y = np.zeros(n)
    x[0]= x_init
    y[0]= y_init
    states = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(1, n):
        # Pick a direction at random
        step = random.choice(states)
        
        # Move the object according to the direction
        if step == "1":
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1] + 1
        elif step == "2":
            x[i] = x[i - 1] 
            y[i] = y[i - 1] + 1
        elif step == "3":
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1] + 1
        elif step == "4":
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1] 
        elif step == "5":
            x[i] = x[i - 1] 
            y[i] = y[i - 1]
        elif step == "6":
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
        elif step == "7":
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1] - 1
        elif step == "8":
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1
        elif step == "9":
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1] - 1
    # Return all the x and y positions of the object
    
    # tests
    for i in range(n):
        print(i, ": ",x[i], y[i])
    return x, y


if __name__=="__main__":
    Iter_val= 10
    while(Iter_val):    
        x_start = random.randint(1,x_grids_max)#input("Enter the starting X cordinate (less than 100): ")
        y_start = random.randint(1,y_grids_max)#input("Enter the starting Y cordinate: (less than 100)")


        time_duration = 50#int(input ("ENter the time duration "))
        time_axis = []
        for i in range(time_duration):
            time_axis.append(i)
        print("time_axis", time_axis)
        x_data, y_data = randomwalk2D(time_duration, int(x_start), int(y_start))
        # Add data to the occupancy Matrix:
        for i in range (len(x_data)):
            occu_matrix[int(x_data[i]),int(y_data[i])] += 1
        print("Occupancy Matrix", occu_matrix)
        for i in range(100): 
            print("Occupancy Matrix ", i, occu_matrix[i])
        
        # Transition Matrix 
        x_data = x_data.astype(int)
        y_data = y_data.astype(int)
        print(type(x_data[0]))
        print("X_data:", x_data) 
        print("Y_data:", y_data)


        for i in range(len(x_data)-1):
            if ((x_data[i+1]-x_data[i] == 0 ) and (y_data[i+1]-y_data[i] == 0)): #  (0,0)    #4
                transition_matrix[x_data[i]*100+y_data[i],4] += 1 #transition_matrix[x_data*100+y_data,4] + 1
            elif ((x_data[i+1]-x_data[i] == 1 ) and (y_data[i+1]-y_data[i] == 0)): # (1,0)   #5
                transition_matrix[x_data[i]*100+y_data[i],5] += 1 # transition_matrix[x_data*100+y_data,5] + 1
            elif ((x_data[i+1]-x_data[i] == -1 ) and (y_data[i+1]-y_data[i] == 0)): # (-1,0) #3 
                transition_matrix[x_data[i]*100+y_data[i],3] += 1 # transition_matrix[x_data*100+y_data,3] + 1
            
            elif ((x_data[i+1]-x_data[i] == 0 ) and (y_data[i+1]-y_data[i] == 0)): # (0,1) # 1  
                transition_matrix[x_data[i]*100+y_data[i],1] += 1 #transition_matrix[x_data*100+y_data,1] + 1
            elif ((x_data[i+1]-x_data[i] == 0 ) and (y_data[i+1]-y_data[i] == 0)): # (1,1) # 2
                transition_matrix[x_data[i]*100+y_data[i],2] += 1 # transition_matrix[x_data*100+y_data,2] + 1
            elif ((x_data[i+1]-x_data[i] == 0 ) and (y_data[i+1]-y_data[i] == 0)): # (-1,1) # 0
                transition_matrix[x_data[i]*100+y_data[i],0] += 1 #  transition_matrix[x_data*100+y_data,0] + 1
            
            elif ((x_data[i+1]-x_data[i] == 0 ) and (y_data[i+1]-y_data[i] == 0)):#(0,-1)  # 7 
                transition_matrix[x_data[i]*100+y_data[i],7] += 1# transition_matrix[x_data*100+y_data,7] + 1
            elif ((x_data[i+1]-x_data[i] == 0 ) and (y_data[i+1]-y_data[i] == 0)):#(1.-1)  # 8
                transition_matrix[x_data[i]*100+y_data[i],8] += 1 # transition_matrix[x_data*100+y_data,8] + 1
            elif ((x_data[i+1]-x_data[i] == 0 ) and (y_data[i+1]-y_data[i] == 0)): #(-1,-1) # 6
                transition_matrix[x_data[i]*100+y_data[i],6] += 1# transition_matrix[x_data*100+y_data,6] + 1



        print("TRansition Matrix:" , transition_matrix)
        print("size " , transition_matrix.shape)
        for i in range(10000):
            print("I=", i, transition_matrix[i])
        for i in range (10000):
            for j in range(9):
                if (transition_matrix[i,j] != 0):
                    print( i, j ,"found non zero")
                    print("\n")
        '''plt.title("Walking MOdel in Warehouse")

        plt.scatter(ix_data[0], y_data[0], c="red") # start
        #plt.legend("start")
        plt.plot(x_data, y_data)
        #plt.legend("path_traversde")
        plt.scatter(x_data[-1], y_data[-1], c="green") #end
        plt.legend(("path traversed","start point","end point"))'''


        ax = plt.axes(projection ='3d')
        z = time_axis
        x = x_data
        y = y_data
        ax.plot3D(x, y, z, 'green')
        ax.scatter(x, y, z)
        ax.set_title('Spatio-temporal Visualization of human trajectory')
        ax.set_xlabel('X', fontsize=10)
        ax.set_ylabel('Y')
        ax.set_zlabel('time ', fontsize=10)
        
        
        plt.show()
        x_same =[]
        y_same =[]
    
        for i in range(1,time_duration):
            if (x_data[i]==x_data[i-1] and y_data[i] == y_data[i-1]):
                x_same.append(x_data[i])
                y_same.append(y_data[i])

        # same print 
        print("Test Data:")
        for i in range (len(x_same)):
            print(i, "Debug: ", x_same[i], y_same[i])

        Iter_val -= 1
        print("This Loop Over!!")
    print("occupancy : Sum", np.sum(occu_matrix))

    print("Final Occupancy Matrix")
    occu_matrix = occu_matrix/np.sum(occu_matrix)
    print("Occupancy Matrix", occu_matrix)

    print("Final Transition Matrix ")
    for i in range(1000):
        sum_value = np.sum(transition_matrix[i])
        for j in range(9):
            if (transition_matrix[i,j] != 0):
                transition_matrix[i,j] = transition_matrix[i,j]/ sum_value
    print("Transition Matrix")
    for i in range(1000):
        for j in range(9):
            if(transition_matrix[i,j] != 0):
                print(transition_matrix[i,j])
#Occupancy Matrix: 
#occu_matrix = np.zeros((x_grids_max,y_grids_max))
#transition_matrix = np.zeros((x_grids_max*y_grids_max,9))


