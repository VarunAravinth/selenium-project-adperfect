from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from filereader import a
import time

#file_in = open('sample.txt','r') 
#a=file_in.readlines()
#print(type(a))
#a = ['sample','sample2']
c=[]
for e in a[:]:
    c.append(e.strip())
    
print('from mainfile')
for f in c[:]:
    
    driver = webdriver.Chrome(executable_path=r"C:\Python27\chromedriver.exe")
    driver.get("http://www.google.com")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
    elem = driver.find_element_by_xpath('//*[@id="lst-ib"]')
    elem.clear()
    elem.send_keys(f)
    
    elem.send_keys(Keys.RETURN)
#driver.implicitly_wait(5)
    print('before closing driver')
    time.sleep(5)
#assert "No results found." not in driver.page_source
    driver.close()
    time.sleep(5)
print('out')
#file_in.close()
