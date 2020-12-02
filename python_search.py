import sys
sys.path.append(".")

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Firefox()

# browser = webdriver.Firefox(executable_path=r'Drivers\geckodriver.exe')

browser = webdriver.Chrome(executable_path=r'Drivers\chromedriver.exe')

browser.get('http://www.python.org')

search = browser.find_element_by_name("q")
search.send_keys("python")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the result

browser.quit()