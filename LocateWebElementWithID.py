from selenium import webdriver
import time

path ="chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("http://kennethhutw.github.io/demo/Selenium/index.html")

signup = driver.find_element_by_id("signup")
signup.click()
time.sleep(2)
driver.back()
time.sleep(2)


signin = driver.find_element_by_id("signin")
signin.click()
time.sleep(2)

driver.close()
driver.quit()

