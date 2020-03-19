from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\soumya balu\\workspace\\New "
                                          "folder\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(len(checkboxes))  # count of the checkboxes in the page

for checkbox in checkboxes:
    print(checkbox.get_attribute("value"))

    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()  # will tell us whether the checkboxes are selected or not


#print(driver.find_element_by_id("displayed-text").is_displayed())
assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
#print(driver.find_element_by_id("displayed-text").is_displayed())
assert not driver.find_element_by_id("displayed-text").is_displayed()  # use negation not after assert if you want to verify false
driver.close()
# interview question
# there are 100 checkboxes write a simple program to click on all the 100 checkboxes
# checkboxes = driver.find_elements_by_xpath("//input[@type-'checkbox']")
# print(len(checkboxes))
# for checkbox in checkboxes:
# checkbox.click()  # this for loop will help to click on all the check boxes
# print(checkbox.is_selected())  # will tell us whether that check boxes is selected or not
# ansewr like this : will find the generic locator which will extract all the check boxes into a list
# and will iterate and will use clickmethod
# checkbox.click()  # this for loop will help to click on all the check boxes
# print(checkbox.is_selected())  # will tell us whether that check boxes is selected or not
