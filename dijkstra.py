from queue import PriorityQueue

def dijkstra(grid, start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not open_list.empty():
        current_cost, current_node = open_list.get()

        if current_node == goal:
            break

        for next_node in neighbors(current_node, grid):
            new_cost = cost_so_far[current_node] + 1  # Assuming cost of moving to adjacent cell is 1

            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                open_list.put((new_cost, next_node))
                came_from[next_node] = current_node

    path = reconstruct_path(came_from, start, goal)
    return path

def neighbors(node, grid):
    row, col = node
    all_neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    valid_neighbors = [(r, c) for r, c in all_neighbors if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0]
    return valid_neighbors

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path
