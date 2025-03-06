import torch
import torch.nn as nn
from torch.distributions.categorical import Categorical
from torch.optim import Adam
import numpy as np
import gym
from gym.spaces import Discrete, Box

np.bool8 = np.bool_  # Temporary fix

# make environment, check spaces, get obs / act dims
env = gym.make('CartPole-v1', render_mode="human")

obs, _ = env.reset()  
env.render()

assert isinstance(env.observation_space, Box), \
    "This example only works for envs with continuous state spaces."
assert isinstance(env.action_space, Discrete), \
    "This example only works for envs with discrete action spaces."

obs_dim = env.observation_space.shape[0]
n_acts = env.action_space.n

print(env.action_space)

action_num = 0
action_rewards = []
while True:
    # rendering
    env.render()
    # save obs

    action = np.random.choice([0,1])
    obs, rew, done, truncated, info = env.step(action)
    print(obs)
    action_reward = (action_num, rew)
    action_rewards.append(action_reward)
    action_num += 1

    if done:
        break

print(action_rewards)
