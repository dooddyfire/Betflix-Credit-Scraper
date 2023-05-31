import datetime
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Fix
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
import schedule
import pandas as pd 
#Insert file name

def scrape_panan(user,pwd):
    url = "https://betflik1188.com/"

    filename = 'Beflix.xlsx'

    #Get bot selenium make sure you can access google chrome
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    #time.sleep(5)

    login_elem = driver.find_element(By.XPATH,'//*[@id="flix-css-j8s74m73"]/div/form/div[1]/label/input')
    login_elem.send_keys(user)

    pwd_elem = driver.find_element(By.XPATH,'//*[@id="flix-css-j8s74m73"]/div/form/div[2]/label/input')
    pwd_elem.send_keys(pwd)

    login_btn = driver.find_element(By.XPATH,'//*[@id="flix-css-j8s74m73"]/div/form/div[3]/div/button')
    login_btn.click()
    time.sleep(5)

    refresh_btn = driver.find_element(By.XPATH,'//*[@id="flix-css-eepbbk6x"]/div/div/div/div[1]/div[2]/button')
    refresh_btn.click()
    time.sleep(5)
    #driver.quit()

    credit = driver.find_element(By.XPATH,'//*[@id="flix-css-eepbbk6x"]/div/div/div/div[1]/div[2]/span').text.strip()
    print(credit)

    return credit



def scrape_all(): 
    filename = "Betflix2.xlsx"
    credit_lis = []
    for user,pwd in zip(user_lis,pwd_lis): 
        
        credit = scrape_panan(user,pwd)
        credit_lis.append(credit)
        time.sleep(5)
    
    df = pd.DataFrame()
    df['user'] = user_lis
    df['credit'] = credit_lis 
    df.to_excel(filename)




#0928093035 // 778800

# username list 
user_lis = ['0802623100','0928093035']

# password list
pwd_lis = ['778899','778899']


# ดึงทุกวันตามเวลาที่กำหนด
#schedule.every().day.at("10:30").do(scrape_all)

#ดึงทุก 30 วินาที 
#schedule.every(30).seconds.do(scrape_all)


"""
while True:
    schedule.run_pending()
    time.sleep(1)
"""

scrape_all()


