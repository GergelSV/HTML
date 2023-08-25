from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.selenium.dev/")
 
print(driver.title)
driver.close()

