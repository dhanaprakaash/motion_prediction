from queue import PriorityQueue

def greedy_best_first_search(grid, start, goal):
    open_list = PriorityQueue()
    open_list.put((heuristic(start, goal), start))
    came_from = {}
    came_from[start] = None

    while not open_list.empty():
        _, current_node = open_list.get()

        if current_node == goal:
            break

        for next_node in neighbors(current_node, grid):
            if next_node not in came_from:
                open_list.put((heuristic(next_node, goal), next_node))
                came_from[next_node] = current_node

    path = reconstruct_path(came_from, start, goal)
    return path

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])  # Manhattan distance heuristic

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
