from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path=r"C:\Python27\chromedriver.exe")
driver.get("http://www.google.com")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
elem = driver.find_element_by_xpath('//*[@id="lst-ib"]')
elem.clear()
elem.send_keys("virat kohli")

elem.send_keys(Keys.RETURN)
time.sleep(5)
#assert "No results found." not in driver.page_source
driver.close()
print('out')
