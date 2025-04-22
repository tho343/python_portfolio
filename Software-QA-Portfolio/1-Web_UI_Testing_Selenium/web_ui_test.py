from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("testuser")
password.send_keys("testpassword")
password.send_keys(Keys.RETURN)

# Verify after login
assert "Welcome" in driver.page_source

driver.quit()