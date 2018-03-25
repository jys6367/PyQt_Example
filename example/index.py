
import requests

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("C:\DEV\MyCrawler/chromedriver")

driver.implicitly_wait(3)

driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys('MY_ID')

driver.find_element_by_xpath("//*[@id='frmNIDLogin']/fieldset/input").click()
driver.find_element_by_name('pw').send_keys('MY_PW')
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser');

[print(a) for a in soup]