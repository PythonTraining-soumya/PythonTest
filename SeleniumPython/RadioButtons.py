from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\soumya balu\\workspace\\New "
                                          "folder\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
radiobuttons = driver.find_elements_by_xpath("//input[@name='radioButton']")
#radiobuttons[2].click() can also be used
print(len(radiobuttons))
for radiobutton in radiobuttons:
    print(radiobutton.get_attribute("value"))
    if radiobutton.get_attribute("value")=="radio1": # is used to click only a particular button
        radiobutton.click()
        assert radiobutton.is_selected()
driver.close()
