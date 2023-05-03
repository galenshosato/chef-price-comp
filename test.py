from selenium import webdriver

driver_location="/usr/bin/chromedriver"
# binary_location ="/usr/bin/google-chrome"

# options = webdriver.ChromeOptions()
# options.binary_location = binary_location

driver = webdriver.Chrome(driver_location)

driver.get("https://www.imdb.com")
print(driver.page_source.encode('utf-8'))

driver.close()
driver.quit()


# email = driver.find_element_by_name("EmailLoginForm[email]")
# password = driver.find_element_by_name("EmailLoginForm[password]")
# email.send_keys('galen.sato@gmail.com')
# password.send_keys('G@!enShoS@to3')
# login_button = driver.find_element_by_id('jsIdNewLoginFormSubmitButton')
# login_button.click()

# import time
# time.sleep(7)
