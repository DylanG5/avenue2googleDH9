from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json

DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
with open('loginInfo.json') as jsonFile:
        data = json.load(jsonFile)


name = []
date = []

def signup():
    driver.get('https://avenue.cllmcmaster.ca/d2l/le/calendar/6605')

    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/d2l-html-block/div/table/tbody/tr[1]/td/p[2]/span/strong/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div/div[1]/ul/li[1]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]').send_keys(data["USERNAME"]+"@mcmaster.ca" + "\n")
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input').send_keys(data["PASSWORD"] + "\n")
    time.sleep(2)

def authen():
    twofactor = True
    while twofactor: 
        try:
            driver.find_element(By.XPATH,'/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input').click()
            twofactor = False
        except:
            twofactor = True

def pullinfo():
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/div[1]/div/ul/li[5]/a').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/a').click()
    time.sleep(1)
    str_num = driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div[2]/form/div/div/div[1]/span[2]/span').text


    num = int(str_num)
    for i in range(num):
        name.append(driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div[2]/form/div/div/ul/li['+str(i+1)+']/div[2]/div/div/div[1]/div[2]').text)
        date.append(driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div[2]/form/div/div/ul/li['+str(i+1)+']/div[2]/div/div/div[2]/div[1]').text)
        print(name[i] + " | " + date[i])
    time.sleep(2)

    count = 0

    for i in date:
        i = i[0:12]
        j = i[i.index(",") + 2: i.index(",") + 6]+'-MM-DD'
        if (i[0:3] == 'Jan'):
            j=j.replace('MM','01')
        elif (i[0:3] == 'Feb'):
            j=j.replace('MM','02')
        elif (i[0:3] == 'Mar'):
            j=j.replace('MM','03')
        elif (i[0:3] == 'Apr'):
            j=j.replace('MM','04')
        elif (i[0:3] == 'May'):
            j=j.replace('MM','05')
        elif (i[0:3] == 'Jun'):
            j=j.replace('MM','06')
        elif (i[0:3] == 'Jul'):
            j=j.replace('MM','07')
        elif (i[0:3] == 'Aug'):
            j=j.replace('MM','08')
        elif (i[0:3] == 'Sep'):
            j=j.replace('MM','09')
        elif (i[0:3] == 'Oct'):
            j=j.replace('MM','10')
        elif (i[0:3] == 'Nov'):
            j=j.replace('MM','11')
        elif (i[0:3] == 'Dec'):
            j=j.replace('MM','12')

        if (i[4:6] == '1,'):
            j=j.replace('DD','01')
        elif (i[4:6] == '2,'):
            j=j.replace('DD','02')
        elif (i[4:6] == '3,'):
            j=j.replace('DD','03')
        elif (i[4:6] == '4,'):
            j=j.replace('DD','04')
        elif (i[4:6] == '5,'):
            j=j.replace('DD','05')
        elif (i[4:6] == '6,'):
            j=j.replace('DD','06')
        elif (i[4:6] == '7,'):
            j=j.replace('DD','07')
        elif (i[4:6] == '8,'):
            j=j.replace('DD','08')
        elif (i[4:6] == '9,'):
            j=j.replace('DD','09')
        else:
            j=j.replace('DD',i[4:6])
        date[count] = j
        
        count+=1
    print(date)
    
def dueDates():
    signup()
    time.sleep(1)
    authen()
    time.sleep(1)
    pullinfo()
    time.sleep(3)
    driver.quit()
    return name,date

