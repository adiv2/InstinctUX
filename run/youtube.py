import sys
sys.path.insert(0, 'InstinctUX/')
from selenium.webdriver.common.keys import Keys
from test.nlp import clean
from test.nlp import removeWords
import test.selenium_helper as chrome
import sys
voiceString = sys.argv[1]
removeAppWords = [" youtube ", " play ", " on "]  # add empty space around words
#voiceString = "play beatles on youtube"   # Test without calling voice to text

removeWords += removeAppWords
searchQuery = clean(removeWords, voiceString)
print(searchQuery)

# navigate to the application home page
chrome.driver.get("http://www.youtube.com")
search = chrome.driver.find_element_by_xpath('//*[@id="search"]')
search.send_keys(searchQuery)
search.send_keys(Keys.RETURN)
chrome.wait_util_visible('//*[@id="video-title"]')
clickVid = chrome.driver.find_element_by_xpath('//*[@id="video-title"]')
clickVid.click()
