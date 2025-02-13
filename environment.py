import numpy as np
import matplotlib.pyplot as plt

# Define the campus grid
class CampusGrid:
    def __init__(self, size=10):
        self.size = size
        self.grid = np.zeros((size, size))  # Empty grid
        self.start = (0, 0)
        self.end = (size-1, size-1)
        self.create_obstacles_and_buildings()

    def create_obstacles_and_buildings(self):
        self.grid[4, 4] = 1  # Building 1
        self.grid[6, 6] = 1  # Building 2
        self.grid[2, 7] = 1  # Building 3
        self.grid[5, 3] = -1  # Obstacle

    def print_grid(self):
        print(self.grid)

    def get_reward(self, state, action):
        new_state = (state[0] + action[0], state[1] + action[1])
        if not (0 <= new_state[0] < self.size and 0 <= new_state[1] < self.size):
            return -10
        if self.grid[new_state[0], new_state[1]] == -1:
            return -10
        if new_state == self.end:
            return 100
        return -1

    def visualize(self, path):
        grid_copy = self.grid.copy()
        for point in path:
            grid_copy[point[0], point[1]] = 2
        grid_copy[self.start] = 3
        grid_copy[self.end] = 4
        plt.imshow(grid_copy, cmap='hot', interpolation='nearest')
        plt.colorbar()
        plt.show()
