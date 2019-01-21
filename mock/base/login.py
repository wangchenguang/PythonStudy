def login(url, username, password, browser):
    browser.get(url)
    browser.find_element_by_id('txtUserName2').send_keys(username)
    browser.find_element_by_id('txtPassword2').send_keys(password)
    browser.find_element_by_id('btnLogin2').click()
