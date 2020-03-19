# .clear()code is used to clear data in a particular box
# if you see a tag name with <a the it will be a link
# to find the css of a child from parent  parent css childtagname:nth-child[number]  eg) login:nth-child[2]


from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\soumya balu\\workspace\\New "
                                          "folder\\chromedriver_win32\\chromedriver.exe")
driver.get("https://login.salesforce.com")
print(driver.find_element_by_xpath("//div[@id='usernamegroup']/label").text)
driver.find_element_by_css_selector("input#username").send_keys("abcgd")
print(driver.find_element_by_css_selector("#login_form > label").text)
driver.find_element_by_css_selector("input#password").send_keys("njshxjshx")
driver.find_element_by_css_selector("input#rememberUn").click()
driver.find_element_by_css_selector("input#Login").click()
print(driver.find_element_by_css_selector("div#error").text)
driver.find_element_by_partial_link_text("Forgot").click()
print(driver.find_elements_by_tag_name("a").__sizeof__())
driver.find_element_by_xpath("//a[text()='Cancel']").click()
driver.close()
