import sys
sys.path.insert(0, 'InstinctUX/')
from selenium.webdriver.common.keys import Keys
import test.selenium_helper as chrome
chrome.driver.get('https://mail.google.com/')

search = chrome.driver.find_element_by_xpath('//*[@id="identifierId"]')
search.send_keys("aditya.gholba@sitpune.edu.in")
search.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
chrome.wait_util_visible('//*[@id="password"]/div[1]/div/div[1]/input')
search2 = chrome.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
search2.send_keys("")
chrome.wait_util_visible('//*[@id="passwordNext"]/content/span')
search2.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()


