from selenium import webdriver
from test.nlp import tag
from selenium.webdriver.common.keys import Keys
from test.clean import clean
import sys
voiceString = sys.argv[1]
driverPath = "/home/aditya/chromedriver"
# create a new Chrome session

voiceString = clean(voiceString)

driver = webdriver.Chrome(driverPath)
# driver.implicitly_wait(30)
# driver.maximize_window()

# navigate to the application home page
driver.get("http://www.google.com")
search = driver.find_element_by_name('q')
search.send_keys(voiceString)
search.send_keys(Keys.RETURN)
