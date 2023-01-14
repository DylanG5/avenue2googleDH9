from selenium import webdriver
import time
DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://nintendo.com')
time.sleep(1000)