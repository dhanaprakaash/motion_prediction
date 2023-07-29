#! /usr/bin/env python
from a_star import indexToWorld


def oneDtotwoD(oneDlist):
    xy_cordinates = [0] * len(oneDlist)
    x_cordinates =  [0] * len (oneDlist)
    y_cordinates =  [0] * len (oneDlist)

    ## converting index to cordinates: 
    for i in range (len(oneDlist)):
        xy_cordinates[i] = indexToWorld(oneDlist[i], 74, 0.2, [0,0])

    ## into two list 
    for i in range (len(xy_cordinates)):
        x_cordinates[i] = round(xy_cordinates[i][0], 2)
        y_cordinates[i] = round(xy_cordinates[i][1], 2)
    
    #print("len", len(x_cordinates))
    return x_cordinates, y_cordinates

