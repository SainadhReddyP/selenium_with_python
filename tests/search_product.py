from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sdetqaportal.blogspot.com/")
driver.find_element(By.XPATH, "//a[text()='Demo App']").click()
driver.find_element(By.XPATH, "//button[text()='Your Store']").click()
driver.find_element(By.ID, "searchQuery").send_keys("Galaxy S22")
driver.find_element(By.XPATH, "//button[text()='Search']").click()
result_ele = driver.find_element(By.XPATH, "//div[@id='resultsContainer']/h3")
result_txt = result_ele.text
if result_txt == "Galaxy S22":
    print("Test Passed.")
else:
    print("Test Failed.")
