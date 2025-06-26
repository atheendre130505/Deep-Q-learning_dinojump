import torch
import time
import pygame
from dino2 import DinoEnv
from agent import agent
from replay_buffer import replay_buffer

state_dim = 5  # Example state dimension
action_dim = 3  # Example action dimension (jump, duck, do nothing)
replay_buffer_size = 10000
agent = agent(action_dim, state_dim, replay_buffer(replay_buffer_size))

def train_agent(episodes=1000):
    env = DinoEnv()
    total_rewards = []

    for episode in range(episodes):
        state = env.reset()
        done = False
        total_reward = 0

        while not done:
            action = agent.select_action(state)
            next_state, reward, done = env.step(action)
            agent.replay_buffer.add((state, action, reward, next_state, done))
            agent.train()
            state = next_state
            total_reward += reward

        if episode % 50 == 0:
            agent.update_target_network()

        if episode % 100 == 0:
            print(f"Episode {episode}, Total Reward: {total_reward}, Epsilon: {agent.epsilon:.2f}")


    return total_rewards
def train_from_checkpoint(episodes=1000):
    agent.policy_net.load_state_dict(torch.load("dqn_dino.pth"))
    agent.update_target_network()
    return train_agent(episodes)

def test_agent():
    env = DinoEnv()
    state = env.reset()
    done = False
    total_reward = 0

    agent.epsilon = 0.0  # Full exploitation
    agent.policy_net.eval()

    while not done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()

        action = agent.select_action(state)
        next_state, reward, done = env.step(action)
        env.draw()
        time.sleep(0.03)

        state = next_state
        total_reward += reward

    print(f"Test completed. Total reward: {total_reward}")

if __name__ == "__main__":
    train_agent(episodes=10000)
    torch.save(agent.policy_net.state_dict(), "dqn_dino.pth")
    print("Training complete. Starting visual test...")
    test_agent()
