from selenium import webdriver

_driver_path = 'D:\Application\chrome\chromedriver.exe'


def create_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    browser = webdriver.Chrome(executable_path=_driver_path, options=options)
    return browser
