import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("/home/aditya/chromedriver")
browser.get('https://mail.google.com/')

search = browser.find_element_by_xpath('//*[@id="identifierId"]')
search.send_keys("aditya.gholba@sitpune.edu.in")
search.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
time.sleep(3)
search2 = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
search2.send_keys("")
time.sleep(1)
search2.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
time.sleep(7)

