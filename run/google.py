from selenium.webdriver.common.keys import Keys
from test.nlp import clean
from test.nlp import removeWords
import test.selenium_helper as chrome
import sys
#voiceString = sys.argv[1]
removeAppWords = [" google ", " search ", " find "]  # add empty space around words
voiceString = "google best player "   # Test without calling voice to text
removeWords += removeAppWords
searchQuery = clean(removeWords, voiceString)

# driver.implicitly_wait(30)
# driver.maximize_window()

# navigate to the application home page
chrome.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
chrome.driver.get("http://www.google.com")
search = chrome.driver.find_element_by_name('q')
search.send_keys(searchQuery)
search.send_keys(Keys.RETURN)
