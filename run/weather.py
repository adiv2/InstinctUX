from selenium import webdriver
from test.nlp import tag
from selenium.webdriver.common.keys import Keys
import sys
voiceString = sys.argv[1]
tags = tag(voiceString)
keys = tags.keys()
driverPath = "/home/aditya/chromedriver"
# create a new Chrome session

location = ""
if "NNP" in keys:
    location = "in " + list(tags.get("NNP"))[0]

driver = webdriver.Chrome(driverPath)
# driver.implicitly_wait(30)
# driver.maximize_window()

# navigate to the application home page
driver.get("http://www.google.com")
search = driver.find_element_by_name('q')
search.send_keys("weather " + location)
search.send_keys(Keys.RETURN)
