import random 

def a_random_position(x_max, y_max):
    x_max -= 1
    y_max -= 1
    x=round(random.uniform(0,x_max),2)
    y=round(random.uniform(0,y_max),2)
    return (x,y)



if __name__== "__main__":
    pos = a_random_position(20,20)
    print(pos)