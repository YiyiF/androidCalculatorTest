# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["productName"] = "emulator-5554"
caps["avd"] = "Pixel_2_API_28_v9.0"
caps["appPackage"] = "com.android.calculator2"
caps["appActivity"] = "com.android.calculator2.Calculator"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element_by_id("com.android.calculator2:id/digit_2")
el1.click()
el2 = driver.find_element_by_accessibility_id("plus")
el2.click()
el3 = driver.find_element_by_id("com.android.calculator2:id/digit_3")
el3.click()
el4 = driver.find_element_by_accessibility_id("equals")
el4.click()

driver.quit()