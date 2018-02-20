from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()
driver.get("http://admin.adperfect.com/default.html?chanid=C0A801C90ed8c2129FQXkq2E94FA&pubid=7F0000011b0dd11838YLJHD92B08&pref=wellandtribune") #1


#page 1

driver.find_element_by_xpath('//*[@id="categories"]/div[1]/div/div/div[3]/select').send_keys('Bakery') #Services
#driver.find_element_by_xpath('//*[@id="categories"]/div[2]/div/div/div[3]/select').send_keys('Bakery') #Rentals
#driver.find_element_by_xpath('//*[@id="categories"]/div[3]/div/div/div[3]/select').send_keys('Bakery') #Real Estate
#driver.find_element_by_xpath('//*[@id="categories"]/div[4]/div/div/div[3]/select').send_keys('Bakery') #Buy And Sell
#driver.find_element_by_xpath('//*[@id="categories"]/div[5]/div/div/div[3]/select').send_keys('Bakery') #Garage Sales & Auctions
#driver.find_element_by_xpath('//*[@id="categories"]/div[6]/div/div/div[3]/select').send_keys('Bakery') #Business / Financial
#driver.find_element_by_xpath('//*[@id="categories"]/div[7]/div/div/div[3]/select').send_keys('Bakery') #Orbituaries / Memoriums
#driver.find_element_by_xpath('//*[@id="categories"]/div[8]/div/div/div[3]/select').send_keys('Bakery') #Employment
#driver.find_element_by_xpath('//*[@id="categories"]/div[9]/div/div/div[3]/select').send_keys('Bakery') #Education
#driver.find_element_by_xpath('//*[@id="categories"]/div[10]/div/div/div[3]/select').send_keys('Bakery') #Travel & Entertainment
#driver.find_element_by_xpath('//*[@id="categories"]/div[11]/div/div/div[3]/select').send_keys('Bakery') #Pets & Animals
#driver.find_element_by_xpath('//*[@id="categories"]/div[12]/div/div/div[3]/select').send_keys('Bakery') #Announcements
#driver.find_element_by_xpath('//*[@id="categories"]/div[13]/div/div/div[3]/select').send_keys('Bakery') #Automotive
#driver.find_element_by_xpath('//*[@id="categories"]/div[14]/div/div/div[3]/select').send_keys('Bakery') #Celebrations
#driver.find_element_by_xpath('//*[@id="categories"]/div[15]/div/div/div[3]/select').send_keys('Bakery') #Recreational Vehicle

#page 2

page2 = driver.find_element_by_xpath('//*[@id="packages"]/form') 
radiose = page2.find_element_by_xpath('//*[@id="packageD8DD489B1db0f14519YKkl9F0EBA"]/div[2]')  #change xpath
for radio in radiose.find_elements_by_xpath('//*[@id="packageradioD8DD489B1db0f14519YKkl9F0EBA"]'):   #change xpath
    radio.click()


#page 3

page1 = driver.find_element_by_xpath('//*[@id="ap_C0A801C90ed8c212EFPxk1B144F7"]/fieldset')

title = page1.find_element_by_xpath('//*[@id="ServiceTitle"]')
title.send_keys('Bread')

description = page1.find_element_by_xpath('//*[@id="ap_ServiceDescription"]')
description.send_keys('good, helthy food and sweety')

dropdown1 = page1.find_element_by_xpath('//*[@id="ServicesResidentialCommercial"]')
selectt1 = Select(dropdown1)
selectt1.select_by_value('Residential')


license_dropdown = page1.find_element_by_xpath('//*[@id="ServicesLicensedInsured"]')
selectt2 = Select(license_dropdown)
selectt2.select_by_value('Licensed')

checkboxes = page1.find_element_by_xpath('//*[@id="fieldServicesFreeEstimates"]/div/div/label')
checkboxes.click()

wesitt = page1.find_element_by_xpath('//*[@id="ServiceWebsite"]')
wesitt.send_keys('www.googl.com')

price = page1.find_element_by_xpath('//*[@id="Price"]')
price.send_keys('5600')

#block = page1.find_element_xpath('//*[@id="fieldContactType"]')

#for contact in block.find_elements_by_xpath('//*[@type = "radio"]'):
#    if contact =  Phone Number:
#        contact.click()
#    elif contact = email:
#        contact.click()
#    else conact = both:
#        contact.click()

#block1 = page1.find_element_xpath('//*[@id="fieldWebAdPhone"]')

webelement = page1.find_element_by_xpath('//*[@id="fieldWebAdPhone"]/input[1]')
webelement.send_keys('942')

webelement1 = driver.find_element_by_xpath('//*[@id="fieldWebAdPhone"]/input[2]')
webelement1.send_keys('942')

webelement2 = driver.find_element_by_xpath('//*[@id="fieldWebAdPhone"]/input[3]')
webelement2.send_keys('9425')

e_maill = page1.find_element_by_xpath('//*[@id="WebAdE-mail"]')   
e_maill.send_keys('multimarkettingagency@gmail.com')


address = page1.find_element_by_xpath('//*[@id="MAP_Address"]')
address.send_keys('No.14, vellalar street,Kumbakonam')

city = page1.find_element_by_xpath('//*[@id="MAP_City"]')
city.send_keys('Kumbakonam')


postal_code = page1.find_element_by_xpath('//*[@id="MAP_PostalCode"]')
postal_code.send_keys('612007')

page1.find_element_by_xpath('//*[@id="webad_start_2018-02-10"]/a/div').click()
page1.find_element_by_xpath('//*[@id="stepsubmit"]').click()


#Page4

page4 = driver.find_element_by_xpath('//*[@id="details"]')

form4 = page4.find_element_by_xpath('//*[@id="ap_C0A801C90ed8c212EFoMO1B144F7"]')

contact_first_name = form4.find_element_by_xpath('//*[@id="FirstName"]')
contact_first_name.send_keys('Siva')

contact_last_name = form4.find_element_by_xpath('//*[@id="LastName"]')
contact_last_name.send_keys('Kumar')

webelement11 = page4.find_element_by_xpath('//*[@id="fieldPhoneNumber"]/input[1]')
webelement11.send_keys('942')

webelement12 = driver.find_element_by_xpath('//*[@id="fieldPhoneNumber"]/input[2]')
webelement12.send_keys('942')

webelement22 = driver.find_element_by_xpath('//*[@id="fieldPhoneNumber"]/input[3]')
webelement22.send_keys('9425')

contact_e_mail = form4.find_element_by_xpath('//*[@id="E-mailAddress"]')
contact_e_mail.send_keys('kumar@gmail.com')

contact_e_mails = form4.find_element_by_xpath('//*[@id="EmailConfirm"]')
contact_e_mails.send_keys('kumar@gmail.com')

contact_address = form4.find_element_by_xpath('//*[@id="ContactAddress1"]')
contact_address.send_keys('10A, T.nagar,Chennai')

contact_address2 = form4.find_element_by_xpath('//*[@id="ContactAddress2"]')
contact_address2.send_keys('11/3A, Chrompet, Chennai')

contact_city = form4.find_element_by_xpath('//*[@id="ContactCity"]')
contact_city.send_keys('Chennai')

dropdown3 = page4.find_element_by_xpath('//*[@id="ContactProvince"]')
selectt3 = Select(dropdown3)
selectt3.select_by_value('Prince Edward Island')

contact_postal_code = form4.find_element_by_xpath('//*[@id="PostalCode"]')
contact_postal_code.send_keys('620000')

page4.find_element_by_xpath('//*[@id="stepsubmit"]').click()


