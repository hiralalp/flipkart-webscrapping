from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import requests






options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver=webdriver.Chrome(executable_path="chromedriver.exe",options=options)
driver.maximize_window()

driver.get("https://www.flipkart.com/")

time.sleep(5)

driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button").click()

driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").send_keys("iphone 8")
driver.find_element(By.CLASS_NAME,"vh79eN").send_keys(Keys.ENTER)

driver.implicitly_wait(5)


price = Select(driver.find_element_by_class_name('fPjUPw'))
price.select_by_value('30000')

time.sleep(5)



assured = driver.find_element_by_class_name('_2rIV_l')
assured.click()
time.sleep(5)



driver.execute_script("window.scrollTo(0, 200);")




brand = driver.find_element_by_class_name('_1GEhLw')
brand.click()

time.sleep(5)



page_source=driver.page_source

soup=BeautifulSoup(page_source,"html.parser")

first_page_mobiles = soup.find_all('div', class_='_1UoZlX')
for i in first_page_mobiles:
	price = i.find('div', class_='_1vC4OE _2rQ-NK')
	name=i.find('div',class_='_3wU53n')


	print(price.text," ",name.text)
	driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

time.sleep(2)
driver.quit()