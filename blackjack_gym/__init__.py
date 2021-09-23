from gym.envs.registration import register

register(
  id='BlackjackEnv-v0',
  entry_point='blackjack_gym.envs.blackjack_env:BlackjackEnv',
)