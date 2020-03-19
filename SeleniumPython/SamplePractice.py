# syntax for xpath  "//tagname[@attribute='value]")
# Syntax of xpath regular expression  "//tagname[contains(@attribute, 'value')]"
# syntax for css  "tagname[attribute='value"
# syntax for css regular expression  [attribute* = 'value']
# Syntax to generate css from ID   tagname#ID  eg: input#username
# Syntax to generate css from classname   tagname.classname eg: input.name
# while generating css from classnmae if ther is space , replace the space with .











from selenium import webdriver

#driver = webdriver.Chrome(executable_path="C:\\Users\\soumya balu\\workspace\\New folder\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\\Users\\soumya balu\\workspace\\New "
                                           "folder\\geckodriver-v0.26.0-win64\\geckodriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice")
driver.maximize_window()
print(driver.find_element_by_xpath("//h1[text()='Protractor Tutorial']").text)
print(driver.find_element_by_xpath("//span[text()='by QAClick Academy']").text)
print(driver.find_element_by_xpath("//div[@class='jumbotron']/h5").text)
print(driver.find_element_by_xpath("//div[@class='jumbotron']/h6").text)
driver.find_element_by_name("name").send_keys("jay krish")
driver.find_element_by_name("email").send_keys("abcdg.gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("sfdggbet")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_id("exampleFormControlSelect1").click()
driver.find_element_by_xpath("//select[@id='exampleFormControlSelect1']/option[2]").click()
driver.find_element_by_id("inlineRadio1").click()
driver.find_element_by_name("bday").send_keys("02/03/1988")
print(driver.find_elements_by_tag_name("inlineRadioOptions").__sizeof__())
print(driver.find_element_by_xpath("//p[text()='Copyright © ProtoCommerce 2018']").text)
driver.find_element_by_xpath("//input[@type='submit']").click()
message = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
assert 'success' in message
driver.find_element_by_xpath("//a[text()='Home']").click()
driver.find_element_by_xpath("//a[text()='Shop']").click()
driver.find_element_by_xpath("//h4[@class='card-title']").find_element_by_xpath("//button[@class='btn btn-info']").click()
driver.find_element_by_xpath("//a[text()='Nokia Edge']").find_element_by_xpath("//button[@class='btn btn-info']").click()
driver.find_element_by_xpath("//a[text()='Blackberry']").find_element_by_xpath("//button[@class='btn btn-info']").click()
driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
driver.find_element_by_xpath("//table[@class='table table-hover']/tbody/tr[3]/td[5]/button").click()
driver.find_element_by_id("country").send_keys("ind")







