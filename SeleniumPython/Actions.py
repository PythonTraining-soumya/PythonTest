from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\soumya balu\\workspace\\New "
                                          "folder\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.familysearch.org/en/")
action = ActionChains(driver)
action.move_to_element(driver.find_element_by_xpath("//span[text()='More menu items']")).click().perform()
# action.move_to_element(driver.find_element_by_css_selector("#mobileDrawer > div:nth-child(4) > button")).perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
#action.double_click(driver.find_element_by_id("double-click")).perform()
action.move_to_element(driver.find_element_by_id("double-click")).context_click().perform()   # will perform the
# right click actions
action.move_to_element(driver.find_element_by_id("double-click")).double_click().perform()
# print(driver.switch_to.alert.text)
alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
driver.switch_to.alert.accept()


