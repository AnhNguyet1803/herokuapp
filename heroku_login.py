import sys
sys.path.append(".")

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# browser = webdriver.Firefox()

# browser = webdriver.Firefox(executable_path=r'Drivers\geckodriver.exe')

browser = webdriver.Chrome(executable_path=r'Drivers\chromedriver.exe')

browser.get('https://the-internet.herokuapp.com/login')

login_form = browser.find_element_by_id('login')

##### element by name
txt_username = browser.find_element_by_name('username')
txt_username.send_keys('tomsmith')

txt_password = browser.find_element_by_name('password')
txt_password.send_keys('SuperSecretPassword!')

btn_login = browser.find_element_by_xpath('//button[contains(text(), Login)]')
btn_login.click()

lbl_success = browser.find_element_by_id('flash')
msg = lbl_success.text
print(msg)
# print(lbl_success.text)

assert 'You logged into a secure area!' in msg 

# login = browser.find_elements_by_name('')
# login.click()

##### element by id
# username = browser.find_element_by_id('username')
# username.send_keys("nguyetpa")

# password = browser.find_element_by_id('password')
# password.send_keys('123456')

# login = browser.find_elements_by_id('')
# login.click()

##### element by xPath
# cusername = browser.find_element_by_xpath('//*[@id="username"]')
# cusername.send_keys("nguyetpa")

# password = browser.find_element_by_xpath('//*[@id="password"]')
# password.send_keys("123456")

# clogin = browser.find_element_by_xpath('//*[@id="login"]/button')
# login.click()

##### element by tag name
# heading = browser.find_element_by_tag_name('h2')

##### element by class name
# classname = browser.find_element_by_class_name('example')

##### element by CSS selectors
# cssname = browser.find_element_by_css_selector('input#username')
# cssname = browser.find_element_by_css_selector('[name="username"]')
# cssname.send_keys("nguyetpa")

# csspass = browser.find_element_by_css_selector('input#password')
# csspass = browser.find_element_by_css_selector('[name="password"]')
# csspass.send_keys("123456")

# csslogin = browser.find_element_by_css_selector('button.radius')
# csslogin.click()

time.sleep(5) # sleep for 5 seconds so you can see the result

browser.quit()