# costmap occupancy (static Obstacle)
## value 254, 255 indicates the definite obstacle 
## value less 128 indicates it the freespace 
### value 128 to 253 indicates the possicility of collision inflation layer in the obstacle, the robot can move in these grids.

my_costmap = (255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 255, 255, 255, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 255, 255, 254, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203,203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 254, 255, 255, 255, 254, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 254, 255, 255, 254, 203, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74,74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 203, 254, 255, 255, 255, 254, 203, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 74, 74, 203, 254, 255, 255,254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 203, 203, 203, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 74, 203, 254, 255, 255, 255, 254, 254, 254, 254, 254, 254, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255,255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 254,254, 254, 254, 254, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 254, 255, 255,254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,74, 74, 74, 74, 74, 74, 74, 74, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203,74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 134, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254,255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255,255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255,254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255,255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203,74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203,203, 203, 203, 203, 203, 134, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 0, 0, 0, 74, 203, 254, 255,255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 134, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203,254, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 203, 203, 203, 203, 134, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 255, 255, 255, 254, 203, 203, 203, 203, 203, 134, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 254, 255, 255, 255, 254, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 74, 74, 74, 74, 74, 74, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255,255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 74, 74, 74, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255,254, 203, 74, 0, 74, 203, 254, 254, 254, 254, 254, 254, 255, 255, 255, 254, 203, 203, 203, 203, 203, 134, 0, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 254, 255, 255, 255, 254, 203, 74, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 134, 203, 203, 203, 203, 203, 254, 255, 255, 255, 254, 254, 254, 254, 254, 254, 203, 74, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 74, 74, 74, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 74, 74, 74, 74, 74, 74, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255,255, 255, 254, 203, 74, 0, 74, 203, 254, 254, 254, 254, 254, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 134, 203, 203, 203, 203, 203, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255,255, 254, 203, 74, 0, 0, 0, 74, 74, 74, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203,74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0,0, 0, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 254, 254, 254, 254, 254, 254, 255, 255,254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 134, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 203, 203, 203, 203, 254,255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 74, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255,254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 203, 74, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 134, 0, 0, 0, 0, 0,0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74, 203, 254, 255, 255, 255, 254, 203, 74, 0, 74, 203, 254, 255, 255, 254, 203, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74,74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 203, 254, 255, 255, 255, 254, 203, 74, 74, 74, 203, 254, 255, 255, 254, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 254, 255,255, 255, 254, 203, 203, 203, 203, 203, 254, 255, 255, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 255, 255, 255, 254, 254, 254, 254, 254, 254, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255)