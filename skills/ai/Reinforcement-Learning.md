---
title: "Reinforcement Learning"
category: "AI"
level: 3
description: "Aprendizado por reforco para agentes que aprendem politicas otimas via interacao e recompensas. Inclui PPO, DQN e exemplos Gymnasium."
projects:
  - "JARVIS Core"
related_skills:
  - "MLOps"
  - "Generative Models"
  - "Engenharia de Prompts"
resources:
  - "Sutton & Barto - Reinforcement Learning: An Introduction"
  - "PPO paper (Schulman et al., 2017)"
  - "Human-level control through DRL (Mnih et al., 2015)"
date: 2026-04-29
tags: [skills, ai, reinforcement-learning]
updated: 2026-06-05
---

# Reinforcement Learning

RL ensina agentes a tomar decisoes otimas por meio de interacao sequencial com um ambiente e recompensas. Este documento cobre implementacoes praticas com Gymnasium, PPO, DQN, templates de funcao de recompensa e loops de treinamento.

## Gymnasium — Ambiente Basico

```python
import gymnasium as gym
import numpy as np

env = gym.make("CartPole-v1", render_mode="rgb_array")
state, info = env.reset()

for step in range(200):
    action = env.action_space.sample()  # acao aleatoria
    next_state, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        state, info = env.reset()
```

### Ambiente Customizado

```python
from gymnasium import Env
from gymnasium.spaces import Discrete, Box

class SearchEnv(Env):
    def __init__(self, documents: list[str]):
        super().__init__()
        self.documents = documents
        self.action_space = Discrete(len(documents))
        self.observation_space = Box(
            low=0, high=1, shape=(384,), dtype=np.float32
        )

    def step(self, action: int):
        relevancia = self._calcular_relevancia(self.documents[action])
        reward = 1.0 if relevancia > 0.8 else -0.1
        terminated = relevancia > 0.9
        return self._get_obs(), reward, terminated, False, {}

    def reset(self, seed=None):
        return self._get_obs(), {}
```

## Template de Funcao de Recompensa

```python
def reward_function(context: dict) -> float:
    """Template para definicao de recompensa multi-objetivo."""
    score = 0.0

    # Recompensa positiva por relevancia
    if context.get("relevancia", 0) > 0.7:
        score += 1.0

    # Penalidade por tempo excessivo
    if context.get("tempo_gasto", 0) > 30:
        score -= 0.5 * (context["tempo_gasto"] - 30) / 30

    # Bonus por acao correta na primeira tentativa
    if context.get("primeira_tentativa", False):
        score += 2.0

    # Penalidade por erros
    score -= 0.2 * context.get("erros", 0)

    return np.clip(score, -5, 5)
```

## PPO (Proximal Policy Optimization)

```python
import torch
import torch.nn as nn

class PPOMemory:
    def __init__(self):
        self.states = []
        self.actions = []
        self.rewards = []
        self.dones = []
        self.log_probs = []

    def store(self, state, action, reward, done, log_prob):
        self.states.append(state)
        self.actions.append(action)
        self.rewards.append(reward)
        self.dones.append(done)
        self.log_probs.append(log_prob)

class ActorCritic(nn.Module):
    def __init__(self, state_dim: int, action_dim: int):
        super().__init__()
        self.shared = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU()
        )
        self.actor = nn.Linear(64, action_dim)
        self.critic = nn.Linear(64, 1)

    def forward(self, state: Tensor):
        features = self.shared(state)
        action_probs = torch.softmax(self.actor(features), dim=-1)
        value = self.critic(features)
        return action_probs, value

class PPOAgent:
    def __init__(self, state_dim: int, action_dim: int, lr: float = 3e-4):
        self.model = ActorCritic(state_dim, action_dim)
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)
        self.memory = PPOMemory()
        self.gamma = 0.99
        self.eps_clip = 0.2

    def update(self, batch_size: int = 64):
        states = torch.FloatTensor(self.memory.states)
        actions = torch.LongTensor(self.memory.actions)
        rewards = torch.FloatTensor(self.memory.rewards)
        dones = torch.FloatTensor(self.memory.dones)
        old_log_probs = torch.FloatTensor(self.memory.log_probs)

        # Calcular retornos
        returns = []
        G = 0
        for reward, done in zip(reversed(rewards), reversed(dones)):
            G = reward + self.gamma * G * (1 - done)
            returns.insert(0, G)
        returns = torch.FloatTensor(returns)

        for _ in range(10):  # K epochs PPO
            for i in range(0, len(states), batch_size):
                batch = slice(i, i + batch_size)
                action_probs, values = self.model(states[batch])
                dist = torch.distributions.Categorical(action_probs)
                new_log_probs = dist.log_prob(actions[batch])

                ratio = torch.exp(new_log_probs - old_log_probs[batch])
                advantages = returns[batch] - values.squeeze()

                surr1 = ratio * advantages
                surr2 = torch.clamp(ratio, 1 - self.eps_clip, 1 + self.eps_clip) * advantages
                actor_loss = -torch.min(surr1, surr2).mean()
                critic_loss = nn.MSELoss()(values.squeeze(), returns[batch])
                loss = actor_loss + 0.5 * critic_loss

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

        self.memory = PPOMemory()
```

## DQN (Deep Q-Network)

```python
class DQNAgent:
    def __init__(self, state_dim: int, action_dim: int):
        self.q_network = nn.Sequential(
            nn.Linear(state_dim, 128), nn.ReLU(),
            nn.Linear(128, 64), nn.ReLU(),
            nn.Linear(64, action_dim)
        )
        self.target_network = copy.deepcopy(self.q_network)
        self.optimizer = torch.optim.Adam(self.q_network.parameters(), lr=1e-3)
        self.memory = deque(maxlen=10000)
        self.epsilon = 1.0
        self.gamma = 0.99

    def act(self, state: np.ndarray) -> int:
        if np.random.random() < self.epsilon:
            return np.random.randint(self.q_network[-1].out_features)
        state = torch.FloatTensor(state).unsqueeze(0)
        return self.q_network(state).argmax().item()

    def train(self, batch_size: int = 64):
        if len(self.memory) < batch_size:
            return
        batch = random.sample(self.memory, batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)

        states = torch.FloatTensor(states)
        actions = torch.LongTensor(actions)
        rewards = torch.FloatTensor(rewards)
        next_states = torch.FloatTensor(next_states)
        dones = torch.FloatTensor(dones)

        q_values = self.q_network(states).gather(1, actions.unsqueeze(1)).squeeze()
        next_q = self.target_network(next_states).max(1)[0].detach()
        target = rewards + self.gamma * next_q * (1 - dones)

        loss = nn.MSELoss()(q_values, target)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
```

## Loop de Treinamento Completo

```python
env = gym.make("CartPole-v1")
agent = PPOAgent(state_dim=4, action_dim=2)
num_episodes = 1000

for episode in range(num_episodes):
    state, _ = env.reset()
    episode_reward = 0

    for t in range(500):
        action_probs, _ = agent.model(torch.FloatTensor(state))
        dist = torch.distributions.Categorical(action_probs)
        action = dist.sample()
        log_prob = dist.log_prob(action)

        next_state, reward, terminated, truncated, _ = env.step(action.item())
        done = terminated or truncated

        agent.memory.store(state, action.item(), reward, done, log_prob.item())
        episode_reward += reward
        state = next_state

        if done:
            break

    agent.update()
    if episode % 100 == 0:
        print(f"Episodio {episode}, Recompensa: {episode_reward}")
```

## Referencias

- [[skills/ai/MLOps|MLOps]] — Pipeline de treino e deploy de agentes RL
- [[skills/ai/Engenharia-de-Prompts|Engenharia de Prompts]] — RL para otimizacao de prompts (RLHF)
- [[skills/04-knowledge-systems/memory-management|Gestao de Memoria]] — Buffer de replay e memoria episodica
- [[Conhecimento-Geral/Neurociencia/Sistemas-de-Memoria|Sistemas de Memoria]] — Inspiracao biologica para RL
