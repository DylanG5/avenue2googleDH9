from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://avenue.mcmaster.ca/?target=\%2Fd2l\%2Fhome')

time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div/div[1]/ul/li[1]/a').click()
time.sleep(1000000)
driver.quit()
