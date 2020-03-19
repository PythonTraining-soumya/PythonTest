
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\soumya balu\\workspace\\New "
                                          "folder\\chromedriver_win32\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/")
print(driver.title)
driver.maximize_window()
driver.find_element_by_xpath("//a[text()='Multiple Windows']").click()
print(driver.current_url)
driver.find_element_by_partial_link_text("Click").click()
childwindow = driver.window_handles[1]   # here all the elements are stored in a list ["parentid", "childid"]
# parentid is stored in 0th index and the first child index is stored in the 1st index
driver.switch_to.window(childwindow)
print(driver.find_element_by_xpath("//div[@class='example']/h3").text)
parentwindow = driver.window_handles[0]
driver.switch_to.window(parentwindow)
print(driver.find_element_by_xpath("//div[@class='example']/h3").text)
driver.quit()