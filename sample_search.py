from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("http://www.wikipedia.org/")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
elem = driver.find_element_by_xpath('//*[@id="searchInput"]')
elem.clear()
elem.send_keys("virat kohli")
elem2 = driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
elem2.click()
#elem.send_keys(Keys.RETURN)
time.sleep(5)

driver.close()
print('out')
