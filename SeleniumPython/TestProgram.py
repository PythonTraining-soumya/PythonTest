import image as image
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\soumya balu\\workspace\\New "
                                          "folder\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.amazon.com")
driver.find_element_by_xpath("//i[@class='a-icon a-icon-next-rounded']").click()

image = driver.find_element_by_xpath("//*[@id='desktop-banner']").click()
