from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
user = "aditya"
chromeDriverPath = "chromedriver"
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/home/" + user + "/.config/google-chrome") #Path to your chrome profile
driver = webdriver.Chrome(executable_path=chromeDriverPath, chrome_options=options)


def wait_util_visible(xpath):
    try:
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    finally:
        driver.refresh()