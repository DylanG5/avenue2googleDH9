from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json


DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

with open('C:\\Users\\msbra\\git projects\\avenue2googleDH9\\Credentials.json') as jsonFile:
        data = json.load(jsonFile)

time.sleep(1)

driver.get('https://avenue.mcmaster.ca/?target=\%2Fd2l\%2Fhome')

time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div/div[1]/ul/li[1]/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]').send_keys(data["USERNAME"] + "@mcmaster.ca" + "\n")
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input').send_keys(data["PASSWORD"] + "\n")
time.sleep(20)
date = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/d2l-expand-collapse-content/div/d2l-w2d-work-to-do//d2l-w2d-collections//div/d2l-w2d-list//d2l-list/d2l-w2d-list-item-assignment[1]//d2l-list-item-generic-layout/div[3]/slot[2]/d2l-list-item-content/d2l-w2d-attribute-list/div/span[1]/text()').text()
print(date)
time.sleep(1000000)
driver.quit()

