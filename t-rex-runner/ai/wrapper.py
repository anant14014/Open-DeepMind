import pyautogui as pg 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Chrome()  ##some appropriate setting for it 

url = "http://rawgit.com/anant14014/Open-DeepMind/master/t-rex-runner/index.html"


def jump():
	pg.press('space')

def down():
	pg.press('down')


def getVals():

	cookies = driver.get_cookies()

    speed, obs_dist, obs_size, passed, score, crashed = 0, 0, 0, 0, 0, 0

    for i in range(6):

        cookie = cookies[i]

        if cookie['name'] == u'speed':
            speed = float(cookie['value'])

        if cookie['name'] == u'obs_dist':
            obs_dist = int(cookie['value'])

        if cookie['name'] == u'obs_size':
            obs_size = int(cookie['value'])

        if cookie['name'] == u'passed':
            passed_obs = int(cookie['value'])

        if cookie['name'] == u'score':
            score = int(cookie['value'])

        if cookie['name'] == u'crashed':
            crashed = (cookie['value'] == u'true')

    return speed, obs_dist, obs_size, passed_obs, score, crashed

