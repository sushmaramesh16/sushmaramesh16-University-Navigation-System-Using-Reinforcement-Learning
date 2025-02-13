from environment import CampusGrid
from agent import Agent
from trainer import Trainer

# Initialize grid and agent
grid_size = 10
env = CampusGrid(size=grid_size)
agent = Agent(grid_size)
trainer = Trainer(agent, env)

# Train the agent
trainer.train()

# Test and visualize the path taken by the agent
state = env.start
path = [state]
while state != env.end:
    action = agent.choose_action(state)
    next_state = (state[0] + action[0], state[1] + action[1])
    path.append(next_state)
    state = next_state

env.visualize(path)
