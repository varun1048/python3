import os
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://184.95.52.42/examresults/online/report/onlineResult.jsp")

xhtmlpath = '//*[@id="frmOnlineResult"]/table[1]/tbody/tr[2]/td/font/b'
vels = '//*[@id="frmOnlineResult"]/table[1]/tbody/tr[1]/td/div/font[1]/b/u'

os.system('cls')
print(driver.find_element_by_xpath(vels).text)
print(driver.find_element_by_xpath(xhtmlpath).text)
os.system('color 4')

driver.quit()
inner = input("Enter roll number:")
# inner = 19105238

driver = webdriver.Chrome()
driver.get("http://184.95.52.42/examresults/online/report/onlineResult.jsp")

javaScript = f"document.getElementsByClassName('listboxtext')[0].value = '{inner}' "
driver.execute_script(javaScript)
driver.find_element_by_xpath('//*[@id="frmOnlineResult"]/table[2]/tbody/tr[1]/td/table/tbody/tr[1]/td/input[2]').click()

#varun
# print(driver.execute_script("return xmlHttp.responseText"))
# driver.quit()
# print(driver.execute_script("return document.getElementsByClassName('listboxtext')[0].value"))
# javas = "document.getElementsByName('divResult')[0].value"
# help(workplease)
# print(driver.page_source)
# JavascriptExecutor j = (JavascriptExecutor) driver

# xpath= '//*[@id="divResult"]'
# workplease = driver.find_elements_by_xpath(xpath)

# searchbox =  driver.find_element_by_xpath('//*[@id="txtRegisterno"]')
# searchbox.send_keys("19105234")
# searchbutton =  driver.find_element_by_xpath('//*[@id="frmOnlineResult"]/table[2]/tbody/tr[1]/td/table/tbody/tr[1]/td/input[2]')
# searchbutton.click()
# driver.find_element_by_xpath('//*[@id="txtRegisterno"]').send_keys(inner)

# driver.find_element_by_xpath('//*[@id="txtRegisterno"]').send_keys("19105238")
