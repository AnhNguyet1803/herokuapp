# import sys
# sys.path.append(".")

# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# # browser = webdriver.Firefox()

# # browser = webdriver.Firefox(executable_path=r'Drivers\geckodriver.exe')

# browser = webdriver.Chrome(executable_path=r'Drivers\chromedriver.exe')

# browser.get('http://www.python.org')

# search = browser.find_element_by_name("q")
# search.send_keys("python")
# search.send_keys(Keys.RETURN) # hit return after you enter search text
# time.sleep(5) # sleep for 5 seconds so you can see the result

# browser.quit()

import sys
sys.path.append(".")

import logging
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Firefox()

# browser = webdriver.Firefox(executable_path=r'Drivers\geckodriver.exe')

browser = webdriver.Chrome(executable_path=r'Drivers\chromedriver.exe')

browser.get('https://www.saucedemo.com/')

# search = browser.find_element_by_name("q")
# search.send_keys("python")
# search.send_keys(Keys.RETURN) # hit return after you enter search text
txt_username = browser.find_element_by_name('user-name')
txt_username.send_keys('standard')

txt_password = browser.find_element_by_name('password')
txt_password.send_keys('secret_sauce')

btn_login = browser.find_element_by_xpath('//*[@id="login-button"]')
btn_login.click()

# lbl_success = browser.find_element_by_tag_name('h3')
# lbl_failed = browser.find_element_by_tag_name('h3')
#msg = lbl_failed

LABEL_MESSAGE = (By.TAG_NAME, 'h3')

LABEL_MESSAGE.get_text

# print(lbl_failed)
# print(lbl_success.text)

# assert 'You logged into a secure area!' in msg 
time.sleep(5) # sleep for 5 seconds so you can see the result

browser.quit()