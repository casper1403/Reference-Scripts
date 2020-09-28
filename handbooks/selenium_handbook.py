
from selenium import webdriver #fedge the friver
from selenium.webdriver.common.keys import Keys #fedge pressing keys
import urllib.request


 #Get the driver for chrome, from map wth path
browser = webdriver.Chrome("C:\chromedriver\chromedriver.exe")

 #Fedge the Link
browser.get("https://www.seleniumhq.org/")

# Find the search bar with id of q
search = browser.find_element_by_id('q')

# Type download in the search bar
search.send_keys("download")

 # press enter
search.send_keys(Keys.ENTER)




search = browser.find_element_by_xpath('//*[@id="ctl00_MainContent_txtuser"]')
search.click()
search.send_keys("info_vandervliet.nl")
search = browser.find_element_by_xpath('//*[@id="ctl00_MainContent_txtPassword"]')
search.click()
search.send_keys('B.v.281247')
button = browser.find_element_by_xpath('//*[@id="ctl00_MainContent_btnConferma"]')
button.click()

browser.get("https://olis.aftersalestools.com/SearchProd.aspx?search=true")

searchbar = browser.find_element_by_id("ctl00_MainContent_txtDescr")
searchbar.click()


test = []

for i in content:
    searchbar = browser.find_element_by_id("ctl00_MainContent_txtDescr")
    searchbar.click()
    searchbar.clear()
    searchbar.send_keys(i)
    searchbar.send_keys(Keys.ENTER)
    time.sleep(1)
    arrow = browser.find_element_by_xpath('//*[@id="ctl00_MainContent_WUCGridSerial1_gridResult_ctl03_imgOpen"]')
    arrow.click()
    time.sleep(1)
    image = browser.find_element_by_xpath('//*[@id="ctl00_MainContent_imgModel"]')
    title = i
    title = title.replace("/","_")
    src = image.get_attribute('src')
    urllib.request.urlretrieve(src, f'{title}.jpg')
    test.append(title)
    browser.execute_script("window.history.go(-1)")
    time.sleep(1)
