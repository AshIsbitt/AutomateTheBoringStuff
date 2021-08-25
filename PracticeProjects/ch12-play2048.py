# 2048 player

'''
2048 is a simple game where you combine tiles by sliding them up, down, left, or right with the arrow keys. 
You can actually get a fairly high score by repeatedly sliding in an up, right, down, and left pattern over 
and over again. Write a program that will open the game at https://gabrielecirulli .github.io/2048/ and keep 
sending up, right, down, and left keystrokes to automatically play the game.
'''

import webbrowser
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Open 2048
browser = webdriver.Firefox()
gameSite = browser.get('https://gabrielecirulli.github.io/2048/')
gameSoup = bs4.BeautifulSoup(gameSite.read(), 'html.parser')

# Get game box
gameElem = browser.find_element_by_class_name('game-container')


# Loop through sending up, right, down left
while True:
    # Detect if the game has ended
    try:
        gameoverElem = browser.find_element_by_class_name(
            'game-message game-over')

        # Print to terminal final score
        scoreElem = gameSoup.select('#score-container')
        print(f'Final score: {scoreElem[0].getText()}')
        break

    except:
        gameElem.send_keys(Keys.UP)
        time.sleep(0.5)
        gameElem.send_keys(Keys.RIGHT)
        time.sleep(0.5)
        gameElem.send_keys(Keys.DOWN)
        time.sleep(0.5)
        gameElem.send_keys(Keys.LEFT)
        time.sleep(0.5)
