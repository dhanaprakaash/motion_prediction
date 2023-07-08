import random 


def new_loc(arg_1, arg_2):

    if (arg_2 == 1):
        arg_1= (arg_1[0] -1, arg_1[1] -1)

    elif(arg_2 == 2):
        arg_1 = (arg_1[0], arg_1[1] -1)
    
    elif(arg_2 == 3):
        arg_1 = (arg_1[0] +1, arg_1[1] -1)

    elif(arg_2 ==4):
        arg_1 = (arg_1[0] -1, arg_1[1])

    elif(arg_2 == 5):
        arg_1 = (arg_1[0] ,arg_1[1])
    
    elif(arg_2 ==6 ):
        arg_1 = (arg_1[0] +1, arg_1[1]) 
    
    elif(arg_2 ==7 ):
        arg_1 = (arg_1[0] -1, arg_1[1] +1)
    
    elif(arg_2 ==8 ):
        arg_1 = (arg_1[0] ,arg_1[1] +1)
    
    elif(arg_2 ==9 ):
        arg_1 = (arg_1[0] +1,arg_1[1] +1)
    
    a = random.uniform(0,1)
    b = random.uniform(0,1)
    arg_1  = (round(arg_1[0]+ a ,2) ,round(arg_1[1]+ b,2))
    return arg_1






def new_path (src_loc, path_vector):
    temp_loc = src_loc
    new_path_vec = [0] * len(path_vector)

    new_path_vec[0] = src_loc
    for i in range(1,len(new_path_vec)):
        new_path_vec[i]= new_loc (temp_loc, path_vector[i])
        temp_loc = new_path_vec[i]

    return new_path_vec



if __name__ == "__main__":
    tst_src_loc = (25,34)
    tst_state_vec = [1,2,3,4,5,6]
   
    test_new_path = new_path(tst_src_loc, tst_state_vec)
     
    print("New Path",test_new_path)
    print(random.uniform(0,1))