#! /usr/bin/env python

height = 74

def next_state_to_index(current_index,next_state):
    if next_state == 1:
        #print("1")
        print("inside current_index:",current_index)
        print ("inside height:", height)
        current_index = current_index - height
        print("current_index:", current_index)
        current_index = current_index -1

        print("inside current:", current_index)
    if next_state == 2:
        #print("2")
        current_index = current_index - height
    if next_state == 3:
        #print("3")
        current_index = current_index - height
        current_index = current_index + 1
    if next_state == 4:
        #print("4")
        current_index = current_index - 1
    if next_state == 5:
        #print("5")
        current_index = current_index
    if next_state == 6:
        #print("6")
        current_index = current_index + 1
    if next_state == 7:
        #print("7")
        current_index = current_index + height
        current_index = current_index -1
    if next_state == 8:
        #print("8")
        current_index = current_index + height
    if next_state == 9:
        #print("9")
        current_index = current_index + height
        current_index = current_index + 1
    return current_index
    
if __name__ == "__main__":
    next_index = next_state_to_index(34, 1)
    print(next_index)
    next_index = next_state_to_index(34, 2)
    print(next_index)
    next_index = next_state_to_index(34, 3)
    print(next_index)
    next_index = next_state_to_index(34, 4)
    print(next_index)
    next_index = next_state_to_index(34, 5)
    print(next_index)
    next_index = next_state_to_index(34, 6)
    print(next_index)
    next_index = next_state_to_index(34, 7)
    print(next_index)
    next_index = next_state_to_index(34, 8)
    print(next_index)
    next_index = next_state_to_index(34, 9)
    print(next_index)