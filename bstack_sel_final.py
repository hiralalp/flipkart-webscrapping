from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

driver=webdriver.Chrome(executable_path="chromedriver.exe",options=options)
actions = ActionChains(driver)

try:
    driver.get("https://www.flipkart.com")
    driver.implicitly_wait(5)
    
    pop = driver.find_element_by_class_name('_2AkmmA._29YdH8')
   
    if pop:
        pop.click()
    iphone = driver.find_element_by_class_name('LM6RPg')
    iphone.send_keys("iPhone 8")

    iphone.send_keys(Keys.RETURN)

   
    driver.implicitly_wait(5)

    assured = driver.find_element_by_class_name('_1GEhLw')
    assured.click()
    
    driver.execute_script("window.scrollTo(0, 200);")

    brand = driver.find_element_by_class_name('_4IiNRh _2mtkou')
    brand.click()

    price = Select(driver.find_element_by_class_name('fPjUPw'))
    price.select_by_value('30000')

    driver.implicitly_wait(5)

    products = driver.find_elements_by_class_name('bhgxx2')
    print(products)
    for product in products:
        # get the name of product
        name = product.find_element_by_class_name('_3wU53n').text
        # get the price of product
        price = product.find_element_by_class_name('_1vC4OE._2rQ-NK').text
        link = product.find_element_by_class_name('_31qSD5')
        print(name, price, link)
        products_all.append([name, price, link])
    print(products_all)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
except:
    driver.close()