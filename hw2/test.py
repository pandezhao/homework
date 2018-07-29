import gym

env_name='CartPole-v0'

env = gym.make(env_name)

max_path_length = env.spec.max_episode_steps

print('test')