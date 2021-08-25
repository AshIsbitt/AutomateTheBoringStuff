# Special characters

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Safari()
browser.get('https://inventwithpython.com')

htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)                # Scrolls to end
htmlElem.send_keys(Keys.HOME)               # Scrolls to top

browser.refresh()
