
from wrapper import * 
import time 

def basic_ai(jump_d):

	driver.get(url)
	time.sleep(10)

	jump()
	jump()

	speed , obs_dist  = getVals()[:2]

	if obs_dist < jump_d :
		jump()


basic_ai(150)


