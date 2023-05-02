from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://www.python.org")

print(driver.current_url)


# email = driver.find_element_by_name("EmailLoginForm[email]")
# password = driver.find_element_by_name("EmailLoginForm[password]")
# email.send_keys('galen.sato@gmail.com')
# password.send_keys('G@!enShoS@to3')
# login_button = driver.find_element_by_id('jsIdNewLoginFormSubmitButton')
# login_button.click()

# import time
# time.sleep(7)
