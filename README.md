# Q-Learning Algorithm

## Introduction
This repository contains an implementation of the Q-learning algorithm, a reinforcement learning method that allows an agent to learn optimal decisions by interacting with its environment. The agent learns to maximize a cumulative reward by updating a Q-table that estimates the action values in different states.

## Basic Concepts

1. **Agent**: Entity that makes decisions.
2. **Environment**: The space where the agent performs actions.
3. **State (S)**: The situation in which the agent finds itself at a given moment.
4. **Action (A)**: Movements or decisions the agent can make.
5. **Reward (R)**: Feedback the agent receives after taking an action.
6. **Policy (π)**: The strategy the agent follows to choose actions based on the state.
7. **Q-Value (Q)**: A function that estimates the quality of an action in a specific state, representing the expected long-term reward.

## Q-Learning Algorithm

Q-learning is a reinforcement learning algorithm based on the Bellman equation. The Q-value update equation is:

$$
Q(s, a) \leftarrow Q(s, a) + \alpha \left[R(s, a) + \gamma \max_{a'} Q(s', a') - Q(s, a)\right]
$$

Where:
- \(Q(s, a)\) is the current Q-value for state \(s\) and action \(a\).
- \(\alpha\) is the learning rate.
- \(R(s, a)\) is the reward received after taking action \(a\) in state \(s\).
- \(\gamma\) is the discount factor.
- \(\max_{a'} Q(s', a')\) is the maximum Q-value for the next state \(s'\).

## Implementation

### Requirements

- Python 3.x
- Numpy

### Installation

Clone this repository and navigate to the main directory:
```bash
git clone https://github.com/your-username/q-learning.git](https://github.com/luisfelipedussan/Q-Learning-and-Applications.git)


