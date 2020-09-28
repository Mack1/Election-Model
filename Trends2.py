# import selenium


# el = driver.find_element_by_id('id_of_select')
# for option in el.find_elements_by_tag_name('option'):
#     if option.text == 'The Options I Am Looking For':
#         option.click() # select() in earlier versions of webdriver


#Click button in browser by title

# from selenium import webdriver


# driver = webdriver.Firefox()
# driver.get('url')

# select = Select(driver.find_element_by_id('fruits01'))

# # select by visible text
# select.select_by_visible_text('Banana')

# # select by value 
# select.select_by_value('1')

import time
from selenium import webdriver
#from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# options.add_argument("start-maximized")
# options.add_argument("--headless")
# browser = webdriver.Firefox(firefox_options=options, executable_path="C:\\Utility\\BrowserDrivers\\geckodriver.exe")


# binary = FirefoxBinary("C:/Users/Mack/AppData/Local/Programs/Python/Python38-32/geckodriver-v0.27.0-win64/geckodriver.exe")
# print(binary)
# browser = webdriver.Firefox(firefox_binary=binary)

#WebElement myElement = new WebDriverWait(driver, 20).until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//mat-option[@class='__mat-option mat-option ng-star-inserted' and @role='option'][starts-with(@id,'mat-option-')]/span[@class='mat-option-text']//span[contains(.,'Campaign Details')]")));

options = Options()
options.add_argument("--headless")
options.set_preference("browser.download.folderList",2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir","/Data")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel")

driver = webdriver.Firefox(options=options, executable_path="C:\\Users\Mack\AppData\Local\Programs\Python\Python38-32\geckodriver-v0.27.0-win64\geckodriver.exe")
time.sleep(5)

urls = ["https://www.cnn.com/"]
driver.get(urls[0])
wait = WebDriverWait(driver, 10)
#catButtonSelect = Select(driver.find_element_by_class_name("hierarchy-select ng-pristine ng-valid" ))
#catButtonSelect.select_by_visible_text(selections[0])

#csvButtonSelect = Select(driver.find_element_by_xpath('//*[@title="CSV"]'))

#.//*[@id='username']

myLists = driver.find_elements_by_xpath('.//*[@class="Text-sc-1amvtpj-0-span bcvWKK"]')
#element = Select(myLists[0])
catDrop = [option.get_attribute("innerText") for option in myLists[1:]]


# toggle = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#fldYear a.sbToggle")))
# toggle.click()

# options = [option.get_attribute("innerText") for option in driver.find_elements_by_css_selector("select#ddlYear option")[1:]]
# print(options)



#myLists = driver.find_elements_by_class_name("Text-sc-1amvtpj-0-span bcvWKK")
print(catDrop)


#<span font-weight="bold" data-test="livetv-copy" letter-spacing="1.5px" font-size="12" class="Text-sc-1amvtpj-0-span bcvWKK">Live TV</span>
