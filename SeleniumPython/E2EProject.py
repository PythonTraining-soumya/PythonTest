from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\soumya balu\\workspace\\New "
                                          "folder\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_link_text("Shop").click()

products = driver.find_elements_by_xpath("//app-card-list[@class='row']/app-card")
print(len(products))  # will give the product count
# "//app-card-list[@class='row']/app-card/div/div/h4/a"  will give the product names
# "//app-card-list[@class='row']/app-card/div/div/h5" will give the prices
# "//app-card-list[@class='row']/app-card/div/div[2]/button"  will gve the add buttons
for product in products:
    productname = product.find_element_by_xpath("div/div/h4/a")  # will iterate and  give each product name
    print(productname.text)
    productprice = product.find_element_by_xpath("div/div/h5")  # will iterate and will give each product price
    print(productprice.text)
    addtocart = product.find_element_by_xpath(
        "div/div[2]/button")  # will iterate through and will give the add to cart button
    print(addtocart.text)
    if productname.text == "Blackberry":
        addtocart.click()
# if you want to add all items in the cart below is the code

# for product in products:
#     productname = product.find_element_by_xpath("div/div/h4/a")  # will iterate and  give each product name
#     print(productname.text)
#     productprice = product.find_element_by_xpath("div/div/h5")  # will iterate and will give each product price
#     print(productprice.text)
#     addtocart = product.find_element_by_xpath("div/div[2]/button")  # will iterate through and will give the add to cart button
#     print(addtocart.text)
#         addtocart.click()
driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()  # will click on the checkout(1)button
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()  # will click on the chekout button
driver.find_element_by_id("country").send_keys("ind")  # inspecting the country box
# adding explicit wait
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))  # waiting till the element is
# located
driver.find_element_by_link_text("India").click()  # will click the country name India
driver.find_element_by_xpath("//input[@class='btn btn-success btn-lg']").click()  # will click the purchase button
# print(driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text)  # will print the
# message
successtext = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
assert "Success! Thank you!" in successtext
driver.get_screenshot_as_file("screen.png")