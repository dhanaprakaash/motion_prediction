#! /usr/bin/env python


import rospy


def find_neighbors(index, width, height, costmap, orthogonal_step_cost):
    """
    Identifies neighbor nodes inspecting the 8 adjacent neighbors
    Checks if neighbor is inside the map boundaries and if is not an obstacle according to a threshold
    Returns a list with valid neighbour nodes as [index, step_cost] pairs
    """
    neighbors = []
    
    diagonal_step_cost = orthogonal_step_cost * 1.41421
    # threshold value used to reject neighbor nodes as they are considered as obstacles [1-254]
    lethal_cost = 1

    upper = index - width
    if upper > 0:
        if costmap[upper] < lethal_cost:
            step_cost = orthogonal_step_cost + costmap[upper]/255
            neighbors.append([upper, step_cost])

    left = index - 1
    if left % width > 0:
        if costmap[left] < lethal_cost:
            step_cost = orthogonal_step_cost + costmap[left]/255
            neighbors.append([left, step_cost])

    upper_left = index - width - 1
    if upper_left > 0 and upper_left % width > 0:
        if costmap[upper_left] < lethal_cost:
            step_cost = diagonal_step_cost + costmap[upper_left]/255
            neighbors.append([index - width - 1, step_cost])

    upper_right = index - width + 1
    if upper_right > 0 and (upper_right) % width != (width - 1):
        if costmap[upper_right] < lethal_cost:
            step_cost = diagonal_step_cost + costmap[upper_right]/255
            neighbors.append([upper_right, step_cost])

    right = index + 1
    if right % width != (width + 1):
        if costmap[right] < lethal_cost:
            step_cost = orthogonal_step_cost + costmap[right]/255
            neighbors.append([right, step_cost])

    lower_left = index + width - 1
    if lower_left < height * width and lower_left % width != 0:
        if costmap[lower_left] < lethal_cost:
            step_cost = diagonal_step_cost + costmap[lower_left]/255
            neighbors.append([lower_left, step_cost])

    lower = index + width
    if lower <= height * width:
        if costmap[lower] < lethal_cost:
            step_cost = orthogonal_step_cost + costmap[lower]/255
            neighbors.append([lower, step_cost])

    lower_right = index + width + 1
    if (lower_right) <= height * width and lower_right % width != (width - 1):
        if costmap[lower_right] < lethal_cost:
            step_cost = diagonal_step_cost + costmap[lower_right]/255
            neighbors.append([lower_right, step_cost])

    return neighbors


def dijkstra(start_index, goal_index, width, height, costmap, resolution, origin, grid_viz):
    ''' 
    Performs Dijkstra's shortes path algorithm search on a costmap with a given start and goal node
    '''

   
    open_list = []

    
    closed_list = set()

    
    parents = dict()

    
    g_costs = dict()

    
    g_costs[start_index] = 0

   
    open_list.append([start_index, 0])

    shortest_path = []

    path_found = False
    rospy.loginfo('Dijkstra: Done with initialization')

    
    while open_list:

        
        open_list.sort(key=lambda x: x[1])
        
        current_node = open_list.pop(0)[0]

        # Close current_node to prevent from visting it again
        closed_list.add(current_node)

       
        grid_viz.set_color(current_node, "pale yellow")

        
        if current_node == goal_index:
            path_found = True
            break

        
        neighbors = find_neighbors(
            current_node, width, height, costmap, resolution)

        
        for neighbor_index, step_cost in neighbors:

            
            if neighbor_index in closed_list:
                continue

            # calculate g_cost of neighbour considering it is reached through current_node
            g_cost = g_costs[current_node] + step_cost

            # Check if the neighbor is in open_list
            in_open_list = False
            for idx, element in enumerate(open_list):
                if element[0] == neighbor_index:
                    in_open_list = True
                    break

            # CASE 1: neighbor already in open_list
            if in_open_list:
                if g_cost < g_costs[neighbor_index]:
                    
                    g_costs[neighbor_index] = g_cost
                    parents[neighbor_index] = current_node
                    
                    open_list[idx] = [neighbor_index, g_cost]

            # CASE 2: neighbor not in open_list
            else:
                
                g_costs[neighbor_index] = g_cost
                parents[neighbor_index] = current_node
                
                open_list.append([neighbor_index, g_cost])

                
                grid_viz.set_color(neighbor_index, 'orange')

    rospy.loginfo('Dijkstra: Done traversing nodes in open_list')

    if not path_found:
        rospy.logwarn('Dijkstra: No path found!')
        return shortest_path

    # Reconstruct path by working backwards from target
    if path_found:
        node = goal_index
        shortest_path.append(goal_index)
        while node != start_index:
            shortest_path.append(node)
            
            node = parents[node]
    # reverse list
    shortest_path = shortest_path[::-1]
    rospy.loginfo('Dijkstra: Done reconstructing path')
    print("Algorithn returns the path: Dijkstra's")
    return shortest_path
