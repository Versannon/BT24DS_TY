# Topic 3: Reinforcement Learning

A paradigm where an agent takes actions in an environment to maximize cumulative reward.
- **Q-Learning**: An off-policy algorithm learning state-action values (Q-values) using Bellman update:
  $$Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]$$
- **Deep Q-Networks (DQNs)**: Approximates Q-values using neural networks in large state spaces.
- **Policy Gradient Methods**: Directly optimizes policy actions via gradient ascent.
