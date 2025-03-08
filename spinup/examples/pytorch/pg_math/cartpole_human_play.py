import gym
import pygame
import random

import numpy as np

np.bool8 = np.bool_  # Temporary fix

def main():
    env = gym.make("CartPole-v1", render_mode="human")  # Enable rendering
    obs, _ = env.reset()
    
    pygame.init()

    clock = pygame.time.Clock()
    
    running = True
    action_count = 0

    print("game will start in 3 seconds")
    pygame.time.delay(3000)
    
    while running:       
        pygame.time.delay(400)

        action = random.choice([0, 1])  # Default to a random action
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            print("Moving right...")
            action = 1  # Move right
        elif keys[pygame.K_LEFT]:
            print("Moving left...")
            action = 0  # Move left
        else:
            print("random action")
        
        obs, _, done, _, _ = env.step(action)  # Step in the environment
        action_count += 1

        if done:
            print(f"Episode ended after {action_count} actions.")
            break

    env.close()
    pygame.quit()

if __name__ == "__main__":
    main()
