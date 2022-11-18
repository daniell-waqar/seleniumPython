import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


url = 'https://instagram.com'
path = Service('/home/waqar/Downloads/chromedriver')
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}              ## Handle alert chrome selenium driver !!!
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options, service=path)

# driver = webdriver.Chrome(service=path)
driver.maximize_window()

driver.get(url)

time.sleep(4)

body = driver.find_element(By.XPATH, '/html/body')

username = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
# user = str(input("Enter the UserName"))
username.send_keys('username')

password = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')

# pa = str(input("Enter the Password"))

password.send_keys('password')

password.send_keys(Keys.ENTER)

time.sleep(4)

adsclose = driver.find_element(By.CSS_SELECTOR, 'button[class="_acan _acao _acas"]')
adsclose.click()
time.sleep(5)

# turnOnNotification = driver.find_element(By.CSS_SELECTOR, 'button[class="_a9-- _a9_0"]')
# turnOnNotification.click()

# time.sleep(5)
search = driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Search"]')
search.click()
searchFor = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Search input"]')
searchFor.send_keys('virat.kohli')
time.sleep(5)
searchFor.send_keys(Keys.ENTER)
time.sleep(2)
searchFor.send_keys(Keys.ENTER)



time.sleep(5)
body1 = driver.find_element(By.XPATH, '/html/body')
time.sleep(4)
body1.send_keys(Keys.PAGE_DOWN)
#body1.send_keys(Keys.ARROW_DOWN)
# body1.send_keys(Keys.PAGE_DOWN)
time.sleep(5)
# data = driver.find_elements(By.CSS_SELECTOR, 'div[class="_ac7v _aang"]')
# print(len(data))


time.sleep(5)
post1 = driver.find_element(By.XPATH, '//*[@id="mount_0_0_Ku"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]')
post1.click()
