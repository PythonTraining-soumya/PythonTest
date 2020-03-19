# here we will study how to invoke the browser and hit our first program
# so first : before stating automation we have to invoke the browser
# always make sure that you have added selenium libraries root to the project
# for that you have to go left down side and click interpreter settings and select our local root directory
# after that while writing webdriver make sure all must be in small letters
# while selecting the browser select the one with capital letters

from selenium import webdriver
# we are invoking Chrome browser
# abd creating object of the Chrome class ie driver
# every browser has an executable file (.exe file)
driver = webdriver.Chrome(executable_path="C:\\Users\\soumya balu\\workspace\\New "
                                          "folder\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element_by_link_text("About").click()
driver.back()
driver.find_element_by_link_text("Store").click()
driver.back()
driver.find_element_by_name("q").send_keys("selenium")
driver.get("https://rahulshettyacademy.com//AutomationPractice")
driver.minimize_window()
driver.refresh()
driver.close()






