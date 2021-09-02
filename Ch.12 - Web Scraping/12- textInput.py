# Text input

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://login.metafilter.com')

userElem = browser.find_element_by_id('user_name')
userElem.send_keys('user name here')

passwordElem = browser.find_element_by_id('user_pass')
passwordElem.send_keys('password')

# This is the same as hitting the "submit" button on that form, and could just have easily been submitted on
# the username field too
passwordElem.submit()
