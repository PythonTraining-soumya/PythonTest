# two type of waits  - implicit wait and explicit wait
# pause the test for a few seconds using time class(to get the count )
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\soumya balu\\workspace\\New "
                                          "folder\\chromedriver_win32\\chromedriver.exe")
#driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_xpath("//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ber")
products = driver.find_elements_by_xpath("//div[@class='products']/div")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
# item1 = driver.find_element_by_xpath("//h4[text()='Cucumber - 1 Kg']").find_element_by_xpath("//button[text()='ADD TO CART']").click()
# item2 = driver.find_element_by_xpath("//h4[text()='Raspberry - 1/4 Kg']").find_element_by_xpath("//button[text()='ADD TO CART']").click()
# item3 = driver.find_element_by_xpath("//h4[text()='Strawberry - 1/4 Kg']").find_element_by_xpath("//button[text()='ADD TO CART']").click()
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:    #this will click all the add to cart button
    button.click()

driver.find_element_by_xpath("//a[@class='cart-icon']").click()
driver.find_element_by_xpath("//div[@class='action-block']/button").click()
# explicite wait
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "input[@class= 'promoCode']")))
driver.find_element_by_xpath("//input[@class= 'promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//button[@class='promoBtn']").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo")))
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)


#driver.close()