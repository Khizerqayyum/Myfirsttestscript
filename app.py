from sys import executable
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com/")
print(driver.title)

driver.find_element(By.NAME, 'q').send_keys('devigital systems')
driver.implicitly_wait(10)
optionslist = driver.find_elements(By.CSS_SELECTOR, 'ul.G43f7e li span')
print(len(optionslist))
time.sleep(3)
for ele in optionslist:
    print(ele.text)
    if ele.text == 'Devigital Systems':
        ele.click()
        break
else:
    print(" 'Devigital Systems' not found.")

time.sleep(5)
driver.quit()



