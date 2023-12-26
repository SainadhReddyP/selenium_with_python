from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sdetqaportal.blogspot.com/")
print(driver.title)
driver.find_element(By.XPATH, "//a[text()='Demo App']").click()
print(driver.title)
driver.find_element(By.XPATH, "//button[text()='Your Store']").click()
print(driver.title)
driver.find_element(By.ID, "searchQuery").send_keys("Galaxy S22")
driver.find_element(By.XPATH, "//button[text()='Search']").click()
result_ele = driver.find_element(By.XPATH, "//div[@id='resultsContainer']/h3")
result_txt = result_ele.text
print(result_txt)
if result_txt == "Galaxy S22":
    print("Test Passed.")
else:
    print("Test Failed.")
driver.quit()

