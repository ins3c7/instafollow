#!/usr/bin/python2
# coding:utf-8
#
# Seguir pessoas no Instagram
#
# ins3c7, 6 nov, 2016

# bro.find_elements_by_xpath("//span[@class='_fbms8 _e616g']")[0].click()

import time, os, random, re
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

os.system('clear')

bro = webdriver.Chrome()
bro.set_window_size(1090,1050)
bro.set_window_position(830, 30)
bro.get('http://www.instagram.com/')

while 1:
  i=0;num=len(bro.find_elements_by_xpath("//a[@class='_8mlbc _vbtk2 _t5r8b']"));print str(num),'carregados..'
  for x in range(num):
    i+=1
    try:
      bro.find_elements(By.XPATH, '//button[text()="Seguir"]')[0].click()
      print str(i),'de',num, '- Seguindo!'
      time.sleep(1)
    except Exception, e:
      print str(i),'de',num, '- Já segue.'
      # print str(e)
      pass
    try:
      if random.randrange(2):
        bro.find_elements_by_xpath("//span[@class='_soakw coreSpriteHeartOpen']")[0].click()
      elif random.randrange(3) == 0:
        bro.find_elements_by_xpath("//input[@class='_7uiwk _qy55y']")[0].send_keys(random.choice(['top! segue?', 'top.. segue?', 'ei, segue? :)', ':)',';)']))
        bro.find_elements_by_xpath("//input[@class='_7uiwk _qy55y']")[0].send_keys(Keys.RETURN)
    except Exception, e:
      pass
    try:
      bro.find_elements_by_xpath("//a[@class='_de018 coreSpriteRightPaginationArrow']")[0].click()
      time.sleep(0.5)
    except Exception, e:
      # print 'NEXT:', str(e)
      pass

  num = raw_input('Pressione ENTER para continuar. or 0 to exit.')
  if num == int(0):
    break
  else:
    continue
