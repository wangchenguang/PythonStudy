from mock.base import login, create_browser
import time

username = ''
password = ''
login_url = 'http://peixun.hongkang-life.com'
browser = create_browser()
login(login_url, username, password, browser)
time.sleep(2)
print(browser.page_source)
# 关闭
browser.close()
