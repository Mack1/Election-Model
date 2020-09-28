#Got Rate Limited Running this Ver

import time
from selenium import webdriver
#from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# binary = FirefoxBinary("C:/Users/Mack/AppData/Local/Programs/Python/Python38-32/geckodriver-v0.27.0-win64/geckodriver.exe")
# print(binary)
# browser = webdriver.Firefox(firefox_binary=binary)

#WebElement myElement = new WebDriverWait(driver, 20).until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//mat-option[@class='__mat-option mat-option ng-star-inserted' and @role='option'][starts-with(@id,'mat-option-')]/span[@class='mat-option-text']//span[contains(.,'Campaign Details')]")));

options = Options()
options.add_argument("--headless")
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir","/Data")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel")

driver = webdriver.Firefox(options=options, executable_path="C:\\Users\Mack\AppData\Local\Programs\Python\Python38-32\geckodriver-v0.27.0-win64\geckodriver.exe")

urls = ["https://trends.google.com/trends/explore?date=2008-11-04%202012-11-06&geo=US&q=Barack%20Obama,Mitt%20Romney"]

driver.get(urls[0])
selections = ["All categories", "News", "Reference", "Online Communities"]
wait = WebDriverWait(driver, 10)
#catButtonSelect = Select(driver.find_element_by_class_name("hierarchy-select ng-pristine ng-valid" ))
#catButtonSelect.select_by_visible_text(selections[0])

#csvButtonSelect = wait.until(EC.visibility_of_element_located(Select(driver.find_element_by_xpath('.//*[@class="material-icons-extended gray"]'))))

csvButtonSelect = wait.until(EC.visibility_of_element_located(Select(driver.find_element_by_xpath('.//*[@class="logo-container"]'))))

	

