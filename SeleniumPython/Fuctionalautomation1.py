import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


expectedlist = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
list1 = []
list2 = []
driver = webdriver.Chrome(executable_path="C:\\Users\\soumya balu\\workspace\\New "
                                          "folder\\chromedriver_win32\\chromedriver.exe")
# driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_xpath("//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ber")
# to check how many products are displayed with ber letters
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(count)
assert count == 3
# find the buttons in the displayed in the three products
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
# "//div[@class='product-action']/button/parent::div/parent::div/h4"

for button in buttons:  # this will click all the add to cart button
    list1.append(button.find_element_by_xpath(
        "parent::div/parent::div/h4").text)  # append method will add all the iterated elements to the list
    button.click()

print(list1)
assert expectedlist == list1

driver.find_element_by_xpath("//a[@class='cart-icon']").click()
driver.find_element_by_xpath("//div[@class='action-block']/button").click()
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@class= 'promoCode']")))
veggies = driver.find_elements_by_css_selector("p.product-name")
for veggie in veggies:
    list2.append(veggie.text)

print(list2)

assert list1 == list2

originalAmount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_xpath("//input[@class= 'promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//button[@class='promoBtn']").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
discountAmount = driver.find_element_by_css_selector(".discountAmt").text
assert float(discountAmount) < int(originalAmount)  # to convert string to numbers

print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)
driver.get_screenshot_as_file("screen.png")
Sum = 0
amounts = driver.find_elements_by_xpath("//table[@class='cartTable']/tr/td[5]/p")
for amount in amounts:
    Sum = Sum + int(amount.text)   # as we cannot sum two strings put it in integer
print(Sum)
total = int(driver.find_element_by_xpath("//span[@class='totAmt']").text)  # to assert two string as int put int in
# front
print(total)
assert Sum == total

driver.close()