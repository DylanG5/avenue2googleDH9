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
driver.find_element(By.XPATH,'/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]').send_keys("kugana7@mcmaster.ca" + "\n")
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input').send_keys("Password" + "\n")
time.sleep(2)
twofactor = True
while twofactor: 
    try:
        driver.find_element(By.XPATH,'/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input').click()
        twofactor = False
    except:
        twofactor = True


time.sleep(1000000)
driver.quit()

