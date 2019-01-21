from selenium import webdriver
import time

url = 'http://peixun.hongkang-life.com'
driver_path = 'D:\Application\chrome\chromedriver.exe'


options = webdriver.ChromeOptions()
options.add_argument("--incognito")
browser = webdriver.Chrome(executable_path=driver_path, options=options)
browser.get(url)
browser.find_element_by_id('txtUserName2').send_keys("")
browser.find_element_by_id('txtPassword2').send_keys("")
browser.find_element_by_id('btnLogin2').click()
time.sleep(3)
print(browser.page_source)
browser.close()
