import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from matplotlib.animation import FuncAnimation
from queue import PriorityQueue

# Define the grid size and create an empty grid map with a step size of 1m
grid_size = (200, 200)  # Define grid size (rows, columns) with 1m step size
grid_map = np.zeros(grid_size)  # Initialize an empty grid map

# Define obstacles in the grid map (set cells to 1 for obstacles) with 1m step size
obstacles = []

# Define a bigger circular obstacle: (center row, center column, radius)
bigger_circle_obstacle = (100, 100, 12)  # Adjusted for 1m step size

center_row, center_col, radius = bigger_circle_obstacle
for i in range(grid_size[0]):
    for j in range(grid_size[1]):
        if (i - center_row)**2 + (j - center_col)**2 <= radius**2:
            grid_map[i, j] = 1

# Add bigger obstacles with different shapes and sizes in 1m step size
bigger_obstacles = [(40, 45, 20, 15), (110, 75, 22, 15), (85, 163, 18, 12), (175, 147, 12, 32)]

# Add a border wall around the grid map as obstacles with 1m step size
border_thickness = 5  # Thickness of the border wall in cells
border_obstacles = []
for i in range(border_thickness, grid_size[0] - border_thickness):
    border_obstacles.append((i, border_thickness))
    border_obstacles.append((i, grid_size[1] - border_thickness - 1))
for j in range(border_thickness, grid_size[1] - border_thickness):
    border_obstacles.append((border_thickness, j))
    border_obstacles.append((grid_size[0] - border_thickness - 1, j))

for obstacle in border_obstacles:
    grid_map[obstacle] = 1  # Set border wall obstacle cells to 1 in the grid map

for obstacle in obstacles:
    grid_map[obstacle] = 1  # Set small obstacle cells to 1 in the grid map

for obstacle in bigger_obstacles:
    top_left_row, top_left_col, height, width = obstacle
    grid_map[top_left_row:top_left_row + height, top_left_col:top_left_col + width] = 1  # Set bigger obstacle cells to 1 in the grid map

# Define a function to generate random positions for the robot within the 1m step size grid
def generate_random_position():
    while True:
        x = np.random.randint(grid_size[1])
        y = np.random.randint(grid_size[0])
        if grid_map[y, x] == 0:  # Check if the position is not an obstacle
            return y, x

# Define the robot's initial position with 1m step size
initial_position = generate_random_position()  # Initial position of the robot (row, column) with 1m step size
## add the path planning algorithms here 

# Define the goal position similar to the initial position with 1m step size
goal_position = generate_random_position()  # Goal position of the robot (row, column) similar to initial position

# A* Algorithm Implementation
def heuristic(node, goal):
    return np.sqrt((node[0] - goal[0])**2 + (node[1] - goal[1])**2)

def astar(grid, start, goal):
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

        for next_node in neighbors(current_node):
            new_cost = cost_so_far[current_node] + 1  # Assuming cost of moving to adjacent cell is 1

            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(next_node, goal)
                open_list.put((priority, next_node))
                came_from[next_node] = current_node

    path = reconstruct_path(came_from, start, goal)
    return path

def neighbors(node):
    row, col = node
    all_neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    valid_neighbors = [(r, c) for r, c in all_neighbors if 0 <= r < grid_size[0] and 0 <= c < grid_size[1] and grid_map[r, c] == 0]
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

# Find path using A* algorithm
path = astar(grid_map, initial_position, goal_position)

print ("Some Output:")
print ("INitial Position: ", initial_position )
print ("Goal Position:", goal_position)
print("a-satr:", path)

# Initialize plot
fig, ax = plt.subplots(figsize=(10, 10))  # Set plot size
ax.set_xlim(0, grid_size[1])  # Set x-axis limits based on grid size
ax.set_ylim(0, grid_size[0])  # Set y-axis limits based on grid size
ax.set_aspect('equal')  # Set aspect ratio to equal for square plot
ax.grid(True)  # Show grid

# Plot obstacles as squares in the grid map with 1m step size
for obstacle in obstacles:
    ax.add_patch(Rectangle((obstacle[1] - 1, obstacle[0] - 1), 2, 2, color='cyan'))  # Gray squares for small obstacles

# Plot bigger obstacles with different shapes and sizes in 1m step size
for obstacle in bigger_obstacles:
    top_left_row, top_left_col, height, width = obstacle
    ax.add_patch(Rectangle((top_left_col - 1, top_left_row - 1), width, height, color='orange'))  # Orange rectangles for bigger obstacles

# Plot the border wall obstacles as squares in the grid map with 1m step size
for border_obstacle in border_obstacles:
    ax.add_patch(Rectangle((border_obstacle[1], border_obstacle[0]), 1, 1, color='black'))  # Black squares for border wall

# Plot the bigger circular obstacle as a circle in the grid map with 1m step size
ax.add_patch(Circle((center_col, center_row), radius, color='red'))

# Plot the initial position of the robot as a red circle marker with 1m step size
robot_marker, = ax.plot([initial_position[1]], [initial_position[0]], 'ro', markersize=10)  # Red circle marker for robot

# Plot the goal position of the robot as a green circle marker with 1m step size
goal_marker, = ax.plot([goal_position[1]], [goal_position[0]], 'go', markersize=10)  # Green circle marker for goal

# Plot the path found by A* algorithm as a blue line with 1m step size
path_points = np.array(path)
ax.plot(path_points[:, 1], path_points[:, 0], 'b-', lw=2)  # Blue line for path

# Show plot
plt.xlabel('Columns')
plt.ylabel('Rows')
plt.title('Grid-based Robot Movement with Bigger Obstacles (Step Size: 1m) and A* Path Finding')
plt.show()
