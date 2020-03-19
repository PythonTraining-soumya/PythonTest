from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\soumya balu\\workspace\\New "
                                          "folder\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
validatetext = 'soumya'
driver.find_element_by_id("name").send_keys(validatetext)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert   # () is not required at the end of alert # recently switch_to_alert has changed to
# switch_to.alert
alerttext =alert.text
assert validatetext in alerttext
print(alerttext)
alert.accept()
driver.find_element_by_id("confirmbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.dismiss()
driver.close()


