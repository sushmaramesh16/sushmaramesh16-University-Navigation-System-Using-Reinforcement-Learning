class Trainer:
    def __init__(self, agent, environment, episodes=1000):
        self.agent = agent
        self.environment = environment
        self.episodes = episodes

    def train(self):
        for episode in range(self.episodes):
            state = self.environment.start
            done = False
            while not done:
                action = self.agent.choose_action(state)
                reward = self.environment.get_reward(state, action)
                next_state = (state[0] + action[0], state[1] + action[1])
                self.agent.update_Q(state, action, reward, next_state)
                if next_state == self.environment.end:
                    done = True
                state = next_state
