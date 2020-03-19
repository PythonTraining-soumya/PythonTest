# Javascript DOM can access any element on the web page same as like selenium does
# selenium have a method to execute Javascript code





from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\soumya balu\\workspace\\New "
                                          "folder\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_xpath("//div[@class='form-group']/input").send_keys("abcd")
# if anything enterd into the boxes by selenium script wont be retrieved using text in the console only the elements
# in the webpage can be get by using text method
print(driver.find_element_by_xpath("//div[@class='form-group']/input").get_attribute("value"))  # this one way which
# we can print the text which we entered in the box
# we can use one more method to get the value we entered in the box that is shown below using javascript
# to get the value enterd in a box
print(driver.execute_script('return document.getElementsByName("name")[0].value'))
# to click on a webelement using javascript
driver.execute_script('document.getElementsByTagName("a")[2].click()')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
