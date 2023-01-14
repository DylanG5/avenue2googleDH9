from selenium import webdriver
import time
DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://avenue.mcmaster.ca/')
email="garned3@mcmaster.ca"
loginButton=driver.find_element("id","login_button")
loginButton.click()
uname = driver.find_element("id", "i0116")