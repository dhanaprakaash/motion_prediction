#! /usr/bin/env python

# imports 
import matplotlib.pyplot as plt
import random
#import costmap
from transition_vectors import create_transition_vector
from next_state_to_index import next_state_to_index
from distance_funs import euclidean_distance,manhatten_distance
import a_star

# 

# total number of grids = height * width
# resolution = meters / pixel
# here, resolution is 0.2
cm_height = 74
cm_width  = 74

# costmap occupancy (static Obstacle)
## value 254, 255 indicates the definite obstacle 
## value less 128 indicates it the freespace 
### value 128 to 253 indicates the possicility of collision inflation layer in the obstacle, the robot can move in these grids.

my_costmap = (255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 255, 255, 255, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 255, 255, 254, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203,203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 254, 255, 255, 255, 254, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 254, 255, 255, 254, 203, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74,74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 203, 254, 255, 255, 255, 254, 203, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 74, 74, 203, 254, 255, 255,254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 203, 203, 203, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 74, 203, 254, 255, 255, 255, 254, 254, 254, 254, 254, 254, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255,255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 254,254, 254, 254, 254, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 254, 255, 255,254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,74, 74, 74, 74, 74, 74, 74, 74, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203,74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 134, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254,255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255,255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255,254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255,255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203,74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203,203, 203, 203, 203, 203, 134, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 0, 0, 0, 74, 203, 254, 255,255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 134, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203,254, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 203, 203, 203, 203, 134, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 255, 255, 255, 254, 203, 203, 203, 203, 203, 134, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 254, 255, 255, 255, 254, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 74, 74, 74, 74, 74, 74, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255,255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 74, 74, 74, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255,254, 203, 74, 0, 74, 203, 254, 254, 254, 254, 254, 254, 255, 255, 255, 254, 203, 203, 203, 203, 203, 134, 0, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 254, 255, 255, 255, 254, 203, 74, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 134, 203, 203, 203, 203, 203, 254, 255, 255, 255, 254, 254, 254, 254, 254, 254, 203, 74, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 74, 74, 74, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 74, 74, 74, 74, 74, 74, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255,255, 255, 254, 203, 74, 0, 74, 203, 254, 254, 254, 254, 254, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 134, 203, 203, 203, 203, 203, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255,255, 254, 203, 74, 0, 0, 0, 74, 74, 74, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203,74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0,0, 0, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 254, 254, 254, 254, 254, 254, 255, 255,254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 203, 203, 203, 203, 254,255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 74, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255,254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 134, 0, 0, 0, 0, 0,0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74,74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 203, 254, 255, 255, 255, 254, 203, 74, 74, 74, 203, 254, 255, 255, 254, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 254, 255,255, 255, 254, 203, 203, 203, 203, 203, 254, 255, 255, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 255, 255, 255, 254, 254, 254, 254, 254, 254, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255)


## Importing from robot plan from A star 
### Planning the robot plan using A* algorithm (file: a_star.py)
my_start_index=2050
my_goal_index= 2345
my_resolution= 0.2
my_origin = [-7.4, -7.4, 0]
### a_star(start_index, goal_index, width, height, costmap, resolution, origin)
#(input 2 for a risk event detector)
robot_plan = a_star.a_star(my_start_index, my_goal_index, cm_width, cm_height,my_costmap, my_resolution, my_origin)

'''input_1 = [0] * len(predicted_human_trajectory) ## Dummy Input 

for i in range(len(input_1)): 
    input_1[i] =random.randint(0,74*74)'''

cost_map_values =set()
for i in range(len(my_costmap)):
    cost_map_values.add(my_costmap[i])
print("cost_map_values=", cost_map_values)

### create occupancy Probability matrix for humans : 

occupancy_human = [0] * len(my_costmap)
#print("debug", occupancy_probability_human)
#print ("DEbug:", len(occupancy_probability_human))

for i in range(len(occupancy_human)):
    occupancy_human[i] = random.randint(0,100)
print("debug", occupancy_human)

### occupancy probability 
total_steps = sum (occupancy_human)
human_occupancy_probability = [0] * len(my_costmap)

for i in range (len(human_occupancy_probability)):
    human_occupancy_probability[i] = occupancy_human[i]/ total_steps
print("human_occupancy_probability", human_occupancy_probability)

# Create Transition Probability Matrix for humans: 
# initialized
transition_probability_tensor = [] 

#some internal variables 
count_normal = 0
corner1 = []
corner2 = []
corner3 = []
corner4 = []

edges_right =[]
edges_left = []
edges_upper = []
edges_lower = []

normal = []

# create masks for the corners and edges
# different index have differnet transition vector depends on the location of the grid.
# Masks takes care of this 
# eg. corner grids have only 4 transitions possible out of 9 total
mask_corner1 = [0,0,0,0,1,1,0,1,1]
mask_corner2 = [0,0,0,1,1,0,1,1,0]
mask_corner3 = [0,1,1,0,1,1,0,0,0]
mask_corner4 = [1,1,0,1,1,0,0,0,0]

mask_edge_left = [1,1,1,1,1,1,0,0,0]
mask_edge_right = [0,0,0,1,1,1,1,1,1]
mask_edge_upper = [1,1,0,1,1,0,1,1,0]
mask_edge_lower = [0,1,1,0,1,1,0,1,1]

normal_mask = [1,1,1, 1,1,1, 1,1,1]

for i in range(cm_width* cm_height):
    if (i == 0):
        print("corner 1")
        print(i)
        corner1.append(i)
        transition_probability_tensor.append(create_transition_vector (mask_corner1))
    elif (i == cm_height -1):
        print ("corner2")
        print(i)
        corner2.append(i)
        transition_probability_tensor.append(create_transition_vector (mask_corner2))
    elif (i == cm_height*cm_width - cm_width):
        print("corner 3")
        print(i)
        corner3.append(i)
        transition_probability_tensor.append(create_transition_vector (mask_corner3))
    elif (i == cm_width*cm_height - 1):
        print("corner 4")
        print(i)
        corner4.append(i)
        transition_probability_tensor.append(create_transition_vector (mask_corner4))
    elif (i>0 and i<cm_height-1): # good 
        print("right_edges")
        print(i)
        edges_right.append(i)
        transition_probability_tensor.append(create_transition_vector (mask_edge_right))
        
    elif (i%cm_width ==0):  # good
        print("lower_egdes")
        print(i)
        edges_lower.append(i)
        transition_probability_tensor.append(create_transition_vector (mask_edge_lower))
        
    elif ((i%cm_height) == (cm_width-1)): # good 
        print("upper_edges")
        print(i)
        edges_upper.append(i)
        transition_probability_tensor.append(create_transition_vector (mask_edge_upper))
        
    elif (i>((cm_height*cm_width)-cm_height) and i<=((cm_height*cm_width)-1)): #good
        print("left_edges")
        print(i)
        edges_left.append(i)
        transition_probability_tensor.append(create_transition_vector (mask_edge_left))
        
    else:
        count_normal =+ 1
        normal.append(i)
        transition_probability_tensor.append(create_transition_vector (normal_mask))
        

print(count_normal)
print("corner1 :", corner1,len(corner1))
print("corner2 :", corner2,len(corner2))
print("corner3 :", corner3,len(corner3))
print("corner4 :", corner4,len(corner4))

print("left:",edges_left,len(edges_left) )
print("lower:",edges_lower,len(edges_lower))
print("right:",edges_right,len(edges_right))
print("upper",edges_upper,len(edges_upper))

print ("normal:", normal, len(normal))



# create masks for the corners and edges
mask_corner1 = [0,0,0,0,1,1,0,1,1]
mask_corner2 = [0,0,0,1,1,0,1,1,0]
mask_corner3 = [0,1,1,0,1,1,0,0,0]
mask_corner4 = [1,1,0,1,1,0,0,0,0]

mask_edge_left = [1,1,1,1,1,1,0,0,0]
mask_edge_right = [0,0,0,1,1,1,1,1,1]
mask_edge_upper = [1,1,0,1,1,0,1,1,0]
mask_edge_lower = [0,1,1,0,1,1,0,1,1]


print ("Mega Debug !!!!! ")

### Prints all the data genrated so far in step fashion 
for i in range(len(transition_probability_tensor)):
    print (i,":", human_occupancy_probability[i], transition_probability_tensor[i], "sum: ",sum(transition_probability_tensor[i]))

print("cost_map_values=", cost_map_values)


### Human Trajectory Prediction
### checking the length of the costmap which has the height = 74, width =74 and len in 1d = height * width

print ("len(my_costmap)", len(my_costmap))

### Rounding off the Occupancy Matrix  

for i in range(len(human_occupancy_probability)):
    human_occupancy_probability[i] = round(human_occupancy_probability[i],4)

print("occupancy Matrix:", human_occupancy_probability)

print("1:",transition_probability_tensor[1], sum(transition_probability_tensor[1]))
print("0:",transition_probability_tensor[0], sum(transition_probability_tensor[0]))
print("last:",transition_probability_tensor[74*74-1], sum(transition_probability_tensor[74*74-1]))
print("5:",transition_probability_tensor[5], sum(transition_probability_tensor[5]))


### Now, data is availble in the form of occupancy probability matrix and transition probability matrix
### Do predicction given the current index 

human_initial_index = random.randint(0, 74*74)

#printing the transition vector for this index 100
print ("100: ",transition_probability_tensor[human_initial_index], 
      ",sum: ", round(sum(transition_probability_tensor[human_initial_index]),3), 
       ",max_value: ", max(transition_probability_tensor[human_initial_index]))

# select the index of the transition vector that has the maximum value

next_state = transition_probability_tensor[human_initial_index].index(max(transition_probability_tensor[human_initial_index]))
next_state =+ 1

print("next state = ", next_state)
# The next state is obtained using the argmax of the transition matrix 
# the convert the state into actual index in the map
# at t = 0, human location (index) is given by the variable huamn_initial_index

next_index = next_state_to_index(45, 9)
print("next_index::", next_index)

predicted_human_trajectory = [human_initial_index]

for i in range(len(robot_plan)): ## for time steps = len(robot_plan)
    next_state=transition_probability_tensor[predicted_human_trajectory[i]].index(max(transition_probability_tensor[predicted_human_trajectory[i]]))
    next_state = next_state + 1
    next_index = next_state_to_index(predicted_human_trajectory[i],next_state)
    predicted_human_trajectory.append(next_index)

#print("predicted_human_trajectory:", predicted_human_trajectory, len(predicted_human_trajectory))

print ("Printing Trajectory Details:")
print ("intial human index:", predicted_human_trajectory[0])
print("predicted_human_trajectory:", predicted_human_trajectory, len(predicted_human_trajectory))
print ("time:", len(predicted_human_trajectory))

human_occupied_gird = set()


### Printing for Debugging!!
for i in range (len(predicted_human_trajectory)):
    human_occupied_gird.add(predicted_human_trajectory[i])
print("grids occupied:", human_occupied_gird, len(human_occupied_gird))



### Risk event Detection:
# Inputs : planned Robot Trajectory, Predicted Human Trajectory
# output: Human safe robot trajectory

### predicted trajectory 
#(input 1 for risk detector)
human_plan = predicted_human_trajectory

'''## Importing from robot plan from A star 
### Planning the robot plan using A* algorithm (file: a_star.py)
my_start_index=2050
my_goal_index= 2345
my_resolution= 0.2
my_origin = [-7.4, -7.4, 0]
### a_star(start_index, goal_index, width, height, costmap, resolution, origin)
#(input 2 for a risk event detector)
robot_plan = a_star.a_star(my_start_index, my_goal_index, cm_width, cm_height,my_costmap, my_resolution, my_origin)'''

'''input_1 = [0] * len(predicted_human_trajectory) ## Dummy Input 

for i in range(len(input_1)): 
    input_1[i] =random.randint(0,74*74)'''


robot_plan_1 =[]
robot_plan_1.append(my_start_index)

for i in range(1, len(robot_plan)+1):
    robot_plan_1.append(robot_plan[i-1])

robot_plan = robot_plan_1
print("ROBOT PLAN:", robot_plan)
print("HUMAN PLAN:", human_plan)

### rHuman Safe Path-planning
### Risk event detector 
### if risk is found  -> update costmap with spatio-temporal obstacle, do a replan 
### if no risk is founf  -> no change in robot's plan 

## Risk Event Detector 
robot_plan_xy = []
human_plan_xy = []

for i in range(len(robot_plan)):
    robot_plan_xy.append(a_star.indexToWorld(robot_plan[i], cm_width, my_resolution, my_origin))
    human_plan_xy.append(a_star.indexToWorld(human_plan[i], cm_width, my_resolution, my_origin))


print ("human XY:", human_plan_xy, len(human_plan_xy))
print ("Robot XY:", robot_plan_xy, len(robot_plan_xy))

safe_threshold = 3 
distance_vector = [0] * len (robot_plan_xy)


for i in range(len(robot_plan)):
    distance_vector[i]  = euclidean_distance( robot_plan_xy[i], human_plan_xy[i])

for i in range(len(distance_vector)):
    distance_vector[i] = round(distance_vector[i],2)

### Distance Vector  Distance vector elements tells about the distance between robot and human at time instances 
print("Distance Vector:", distance_vector)

def find_spatio_temporal_risk (distance_vector, safe_threshold =4, risk_index = robot_plan): ## verified, need to change the structure at last!!
    is_risk_detected = False
    risk_index_wrt_human = 0
    for i in range (1,len(distance_vector)):
        if (distance_vector[i] < safe_threshold):
            is_risk_detected = True
            risk_index_wrt_human = risk_index[i]
            break
    print("risk_index_wrt_human:", risk_index_wrt_human)
    return is_risk_detected, risk_index_wrt_human

Risk_Detected, Spatio_temp_obstacle  = find_spatio_temporal_risk (distance_vector)
#print("Risk detected (Human pos and robot pos coincides ) in xy: ", a_star.indexToWorld(Spatio_temp_obstacle,cm_width,my_resolution, my_origin))
print("results:", Risk_Detected, Spatio_temp_obstacle)

def update_costmap (costmap_to_process, obstcle_loc): ## verified
    print("Function:   update_costmap: ")
    a= obstcle_loc
    print("obstacel_loc:", obstcle_loc)
    modified_map = list(costmap_to_process)
    '''obstacle_list  = [  a+76+74, a+76, a+2 ,a-72, a-72-74,
                        a+75+74, a+75, a+1, a-73, a-73-74,
                        a+74+74, a+74, a, a-74, a-74-74,
                        a+73+74, a+73, a-1, a-75, a-75-74,
                        a+72+74, a+72, a-2, a-76, a-76-74   ]'''
    obstacle_list = [a+75, a+1, a-73, a+74, a, a-74, a+73, a-1, a-75]
    for i in range(len(obstacle_list)):
        modified_map[obstacle_list[i]] = 255 ### Adding obstacle in the costmap (obstacle is added exactly at the location and neighbouring cells surrounding them)
    ypdated_map =tuple(modified_map)
    debug_costmap = []
    for i in range(len(ypdated_map)):
        print("i=", i , costmap_to_process[i], ypdated_map[i])
    for i in range (len(ypdated_map)):
        if (costmap_to_process[i]!= ypdated_map[i]):
            debug_costmap.append(i)
    print("debug_costmap:", debug_costmap)
    print("===========================")
    return ypdated_map

### status is True indicates , Spatio-temporal collision is predicted, 
### costmap map should be updates with the dected obstacle 
### again, plan has to be done for robot 
def update_the_plan(status, human_obstacle_index, costmap_to_process = my_costmap , intiail_robot_paln = robot_plan):
    print("Inside : update_the_plan_function")
    print("Status:", status)
    if (status):
        print("intial plan:", intiail_robot_paln)
        updated_costmap = update_costmap(costmap_to_process , human_obstacle_index)
        print("updated_costmap:", update_costmap)
        updated_safe_plan= a_star.a_star(intiail_robot_paln[0], intiail_robot_paln[len(intiail_robot_paln)-1], width=74, height=74, costmap= updated_costmap, resolution=0.2, origin=[-7.4, -7.4, 0])
        print("index:", human_obstacle_index)
        print("intial plan:", intiail_robot_paln)
        print("update plan 2:", updated_safe_plan)
        print("exiting 2: update_the_plan_function")
        return updated_safe_plan
    else:
        print("intitial plan:", intiail_robot_paln)
        updated_safe_plan = intiail_robot_paln
        print ("no replan")
        print("update plan 1: ", updated_safe_plan)
        print("exiting 1: update_the_plan_function")
        return updated_safe_plan



### Human-Safe Path Planning 
Human_Safe_Planning = update_the_plan(Risk_Detected, Spatio_temp_obstacle)
print("##Human safe Planning:", Human_Safe_Planning)


Human_Safe_Planning[0] =robot_plan[0]

'''robot_plan_11=[]
robot_plan_11.append(robot_plan[0])

### Appening the start index to the plan at index : 0 
for i in range(len(robot_plan)):
    robot_plan_11.append(Human_Safe_Planning[i-1])

Human_Safe_robot_Plan = robot_plan_11 '''


#print("Human-safe-path:::", Human_Safe_robot_Plan)

print("\n\n")
print ("*****Summary*****")

print("Planned Robot Path:", robot_plan)
print("Predicted HUman Path:", human_plan)
print("Risk Detected: ", Risk_Detected)
print("spatio temporal" , Spatio_temp_obstacle)
print("Human- Safe Path Plan:", Human_Safe_Planning)
print("==============")


# plotting index to world 
here_width = 74
here_resolution= 0.2
here_origin = [0, 0]

# robot_plan
index_plan = [0]* len(robot_plan)
for i in range(len(robot_plan)):
    index_plan[i] = a_star.indexToWorld(robot_plan[i],here_width,here_resolution, here_origin)

print("indexed :", index_plan)

#plotting 

x_plot_robot_plan = [0]*len(robot_plan)
y_plot_robot_plan = [0] *len(robot_plan)


for i in range(len(index_plan)):
    x_plot_robot_plan[i] = round(index_plan[i][0],2)
    y_plot_robot_plan[i] = round(index_plan[i][1],2)

print("x_plot_robot:", x_plot_robot_plan)
print("y_plot_robot:", y_plot_robot_plan)

plt.plot(x_plot_robot_plan, y_plot_robot_plan)

### plotting human safe 

index_plan_safe = [0]* len(Human_Safe_Planning)
for i in range(len(Human_Safe_Planning)):
    index_plan_safe[i] = a_star.indexToWorld(Human_Safe_Planning[i],here_width,here_resolution, here_origin)

print("indexed :", index_plan_safe)

#plotting 

x_plot_robot_plan_safe = [0]*len(Human_Safe_Planning)
y_plot_robot_plan_safe = [0] *len(Human_Safe_Planning)


for i in range(len(index_plan_safe)):
    x_plot_robot_plan_safe[i] = round(index_plan_safe[i][0],2)
    y_plot_robot_plan_safe[i] = round(index_plan_safe[i][1],2)

print("x_plot_robot:", x_plot_robot_plan_safe)
print("y_plot_robot:", y_plot_robot_plan_safe)

plt.plot(x_plot_robot_plan_safe, y_plot_robot_plan_safe)
plt.plot(x_plot_robot_plan[0], y_plot_robot_plan[0], 'o')
plt.plot(x_plot_robot_plan[len(x_plot_robot_plan)-1], y_plot_robot_plan[len(y_plot_robot_plan)-1], 'o')

## plotting spatio-temporal obstacle :

##radius 3 

dynamic_obstacle = [] 
print("dynamic_obs:" , dynamic_obstacle)
#[a+75, a+1, a-73, a+74, a, a-74, a+73, a-1, a-75]
if Risk_Detected:
    list_obs = []
    list_obs.append(Spatio_temp_obstacle+75)
    list_obs.append(Spatio_temp_obstacle+1)
    list_obs.append(Spatio_temp_obstacle-73)
    list_obs.append(Spatio_temp_obstacle+74)
    list_obs.append(Spatio_temp_obstacle)
    list_obs.append(Spatio_temp_obstacle-74)
    list_obs.append(Spatio_temp_obstacle+73)
    list_obs.append(Spatio_temp_obstacle-1)
    list_obs.append(Spatio_temp_obstacle-75)
    dynamic_obstacle = list_obs
print("dynamic:", dynamic_obstacle)

## plotting dynamic obstacel : 

xy_dynamic = [0] * len(dynamic_obstacle)

for i in range (len(xy_dynamic)):
    xy_dynamic[i] = a_star.indexToWorld(dynamic_obstacle[i], here_width, here_resolution, here_origin)

x_dynamic = [0] * len(xy_dynamic)
y_dynamic = [0] * len (xy_dynamic)

for i in range (len(xy_dynamic)):
    x_dynamic[i] = round(xy_dynamic[i][0], 2)
    y_dynamic[i] = round (xy_dynamic[i][1], 2)

#print("x_dynamic", "y_dynamic" , x_dynamic, y_dynamic)
if Risk_Detected:
    plt.plot(x_dynamic[4], y_dynamic[4], 'o')







print("Planned Robot Path:", robot_plan)
print("Predicted HUman Path:", human_plan)
print("Risk Detected: ", Risk_Detected)
print("spatio temporal" , Spatio_temp_obstacle)## not neede 
print("Human- Safe Path Plan:", Human_Safe_Planning)
print ("obstacle_lsit ", )
print("==============")





plt.show()



'''


# plotting costmap 

xy_costmap = [0] * len (my_costmap)

for i in range (len(my_costmap)):
    xy_costmap[i] = a_star.indexToWorld(my_costmap[i],here_width,here_resolution, here_origin)

print ("xy_costmap: ", xy_costmap)

x_plot_my_costmap = [0] * len(my_costmap)
y_plot_my_costmap = [0] * len(my_costmap)

for i in range (len(my_costmap)):
    x_plot_my_costmap[i] = round(xy_costmap[i][0],2)
    y_plot_my_costmap[i] = round(xy_costmap[i][0],2)


# debug 

print ("x_plot:", x_plot_my_costmap)
print ("y_plot", y_plot_my_costmap)




# plotting static obstacles 


obstacles_index = []

for i in range(len(my_costmap)):
    if (my_costmap[i] == 254 or my_costmap[i] == 255):
        obstacles_index.append(i)

print ("obstacle index: ", obstacles_index , "len: ",len(obstacles_index))


##plotting obstacles 

# convert into xy 
xy_obstacles_list = [0] * len (obstacles_index)

for i in range(len(obstacles_index)):
    xy_obstacles_list[i] = a_star.indexToWorld( obstacles_index[i] , here_width, here_resolution, here_origin)    

print("obstacle_list :", xy_obstacles_list, len(obstacles_index))



x_obstacle_list = [0] * len(obstacles_index)
y_obstacle_list = [0] * len (obstacles_index)


for i in range (len(obstacles_index)):
    x_obstacle_list[i] = round (xy_obstacles_list[i][0], 2)
    y_obstacle_list[i] = round (xy_obstacles_list[i][1], 2)

print("x_obstacle: ", x_obstacle_list)
print("y_obstacle:" ,y_obstacle_list)


plt.plot(x_obstacle_list, y_obstacle_list)
plt.show()'''