import gym 
import numpy as np 
import requests


def random(env):

	obs  = env.reset()

	totalreward = 0 

	for episode in range(10000):

		env.render()
		action  = env.action_space.sample()

		print "the action to be taken",action 

		obs , reward , do , inf = env.step(action)    # stochastic actions  -- no policy 

		totalreward =  totalreward + reward

		print "the reward at this step is" ,reward
		print "the total reward till now is ",totalreward

# a non random policy model 

def run_episode(env , param):

	obs = env.reset()

	totalreward = 0 

	explore = 2000

	for steps in range(explore):  ## run an episode for a given number of time steps 

		if np.matmul(param,obs) < 0 :
			action  = 0 
		else :
			action  = 1 

		obs , rew , done, inf = env.step(action)

		print "the action taken is ",action 
		print "the reward is" ,rew 

		totalreward += rew

	print "the overall reward is",totalreward

	return totalreward


## a random search policy 

def random_search(env):
	
	bestparams = 0
	bestreward  = 0 

	for episodes in range(10000):

		parameters = np.random.rand(4)  
		reward = run_episode(env , parameters)

		if reward > bestreward:
			
			bestreward    = reward
			bestparams = parameters


	print "best reward till now are", bestreward
	print "best params till now are ",bestparams 




def hill_climbing(env):

	alpha = 0.1     ## hyper parameter could vary that as well 
	params = np.random.rand(4)

	bestreward = 0  

	for episodes in range(10000):  
		newparams = params + (np.random.rand(4))*alpha

	reward = run_episode(env,newparams)

	if reward > bestreward:
		bestreward = reward
		params = newparams

	print "best reward obtained is",bestreward
	print "best params till now are",params 


if __name__ == "__main__":

	env = gym.make('CartPole-v0')

	#policy 1 
	random(env)

	#policy 2 
	random_search(env)

	#policy 3 
	hill_climbing(env)














