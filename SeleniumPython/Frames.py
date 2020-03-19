
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\soumya balu\\workspace\\New "
                                          "folder\\chromedriver_win32\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/")
driver.find_element_by_link_text("Frames").click()
driver.find_element_by_link_text("iFrame").click()
linktext = len(driver.find_elements_by_tag_name("a"))
print(linktext)
# if you see tag names like iFrame, frame, Frameset in parent then we can say that the child is in the frames
# use frame id, framename ,frame index to pass the argument
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("i want to automate")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)