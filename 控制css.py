from selenium import webdriver
#限制css加载
fp = webdriver.FirefoxProfile()
fp.set_preference("permissions.default.stylesheet", 2)

#driver = webdriver.Firefox(firefox_profile=fp, executable_path=r'/usr/bin/geckodriver')
#driver.get("http://www.santostang.com/2018/07/04/hello-world/")

#限制图片的加载
#fp = webdriver.FirefoxProfile()
fp.set_preference("permissions.default.image", 2)

#driver = webdriver.Firefox(firefox_profile=fp, executable_path=r'/usr/bin/geckodriver')
#driver.get("http://www.santostang.com/2018/07/04/hello-world/")

#限制JavaScript的执行

#fp = webdriver.FirefoxProfile()
fp.set_preference("javascript.enabled", False)

driver = webdriver.Firefox(firefox_profile=fp, executable_path=r'/usr/bin/geckodriver')
driver.get("http://www.santostang.com/2018/07/04/hello-world/")
