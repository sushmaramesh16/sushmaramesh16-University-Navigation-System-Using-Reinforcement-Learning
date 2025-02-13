import random

# Define actions: up, down, left, right
actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Agent:
    def __init__(self, grid_size, epsilon=0.1, learning_rate=0.1, discount_factor=0.9):
        self.epsilon = epsilon
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.Q_table = np.zeros((grid_size, grid_size, len(actions)))

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(actions)
        else:
            state_index = state[0], state[1]
            action_index = np.argmax(self.Q_table[state_index])
            return actions[action_index]

    def update_Q(self, state, action, reward, next_state):
        state_index = state[0], state[1]
        next_state_index = next_state[0], next_state[1]
        action_index = actions.index(action)
        best_future_q = np.max(self.Q_table[next_state_index])
        self.Q_table[state_index][action_index] += self.learning_rate * (reward + self.discount_factor * best_future_q - self.Q_table[state_index][action_index])
