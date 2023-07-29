from random import randint, choice
import costmap

def get_freespace(map=costmap.my_costmap):
    
    freespace_list =[]
    for i in range (len(map)):
        if (map[i] <254):
            freespace_list.append(i)
    #print(len(freespace_list))
    return freespace_list




def giveIndex( ):
    freespace = get_freespace()
    return choice(freespace)


if __name__ == "__main__":
    #my_list = get_freespace()
    #print (len(my_list))
    element = giveIndex()
    print ("index:", element, "value: ", costmap.my_costmap[element])