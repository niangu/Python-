from selenium import webdriver
import time

fp = webdriver.FirefoxProfile()
fp.set_preference("permissions.default.stylesheet", 2)
fp.set_preference("permissions.default.image", 2)
fp.set_preference("javascript.enabled", False)

driver = webdriver.Firefox(firefox_profile=fp, executable_path=r'/usr/bin/geckodriver')
driver.get("https://zh.airbnb.com/s/%E4%B8%AD%E5%9B%BD%E5%B9%BF%E4%B8%9C%E7%9C%81%E6%B7%B1%E5"
           "%9C%B3%E5%B8%82/homes?refinement_paths%5B%5D=%2Fhomes&query=%E4%B8%AD%E5%9B%BD%E5%"
           "B9%BF%E4%B8%9C%E7%9C%81%E6%B7%B1%E5%9C%B3%E5%B8%82&place_id=ChIJkVLh0Aj0AzQRyYCStw"
           "1V7v0&search_type=UNKNOWN&allow_override%5B%5D=&s_tag=tTa_ytTw")
for i in range(0, 16):
    rent_list = driver.find_elements_by_css_selector('div._gig1e7')
    for eachhouse in rent_list:
        comment1 = eachhouse.find_element_by_css_selector('span._16hhykwk')
        comment = comment1.text
        price1 = eachhouse.find_element_by_css_selector('div._1yarz4r')
        price = price1.text[4:]
        name1 = eachhouse.find_element_by_css_selector('div._1m9t1a27')
        name = name1.text
        #details = eachhouse.find_elements_by_css_selector('span.')
        print(comment, price, name)
    next = driver.find_element_by_css_selector('a._5u96sq')
    next.click()
    time.sleep(5)
    i += 1
driver.quit()

