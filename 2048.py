# Write a program that will open the game at https://gabrielecirulli.github.io/2048/ and keep sending up, right, down, and left keystrokes to automatically play the game.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')
x = 1

for i in range(0,100):
    htmlElem.send_keys(Keys.UP)
    time.sleep(x)
    htmlElem.send_keys(Keys.RIGHT)
    time.sleep(x)
    htmlElem.send_keys(Keys.DOWN)
    time.sleep(x)
    htmlElem.send_keys(Keys.DOWN)