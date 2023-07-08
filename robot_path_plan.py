""" This is .py file is used for robot Path planning. It contains all the functions required
for the proposed algorithm.

Parameters :   
Initial location (tuple), Destination Location (tuple)  

Return Value :
Waypoints (List of Tuples)

"""
import random
from distance_funs import euclidean_distance, manhatten_distance 
from random_location import a_random_position

def Combining_the_X_and_Y_cordinate (X_list, Y_list):
    """This function is used to Create the waypoints of Robot to be traversed
        parameters   : X_list (List of X-cordinates), Y_list(List of Y-cordinates )
        Return Value : Waypoints (List of Tuple)
    """
    Waypoint_list = [0] * len(X_list)

    for i in range(len(Waypoint_list)):
        Waypoint_list[i]=(X_list[i],Y_list[i])

    #print("Waypoint_LIst:", Waypoint_list)

    return Waypoint_list






def robot_path_planning (source_loc, destination_loc):

    print("\n\n********Funtion starts********")
    print ("Debug:Manhatten: ",manhatten_distance(source_loc,destination_loc)) # The Manhatten is choosen 
    print("Source Location: ", source_loc)
    print("Destination LOcation", destination_loc)
    

    no_of_waypoints = manhatten_distance(source_loc, destination_loc)

    temp_X = [0] * no_of_waypoints
    temp_Y = [0] * no_of_waypoints
    
    for i in range(len(temp_X)):
        temp_X[i] = round( random.uniform(source_loc[0], destination_loc[0]), 2)
    
    temp_X [0]=source_loc[0]
    temp_X [len(temp_X)-1]=destination_loc[0]
    #print("Debug : Temp_X: ", temp_X) 

    for i in range(len(temp_Y)):
        temp_Y[i] = round(random.uniform( source_loc[1], destination_loc[1]), 2 )
    
    temp_Y[0]=source_loc[1]
    temp_Y[len(temp_Y)-1]=destination_loc[1]
    #print("Debug : Temp_Y: ", temp_Y) 

    temp_X.sort()
    temp_Y.sort()

    Waypoint_Array = Combining_the_X_and_Y_cordinate(temp_X,temp_Y)
    print("Debug: Waypoint Array:\n", Waypoint_Array)
    print("******Function Exits*******\n\n")
    return Waypoint_Array

if __name__ == "__main__":
    a = a_random_position(20,20)
    b = a_random_position(20,20)
    my_array = robot_path_planning(a,b)
    print("Debug: Working OK!")
    print("my_array", my_array)