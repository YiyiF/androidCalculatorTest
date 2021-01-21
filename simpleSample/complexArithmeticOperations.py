# /usr/bin/env python3

from appium import webdriver

caps = {
    "platformName": "Android",
    "productName": "emulator-5554",
    # "avd": "Pixel_2_API_28_v9.0",
    "appPackage": "com.android.calculator2",
    "appActivity": "com.android.calculator2.Calculator",
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

# numbers
num1 = driver.find_element_by_id("com.android.calculator2:id/digit_1")
num2 = driver.find_element_by_id("com.android.calculator2:id/digit_2")
num3 = driver.find_element_by_id("com.android.calculator2:id/digit_3")

# operators
op_plus = driver.find_element_by_accessibility_id("plus")
op_minus = driver.find_element_by_accessibility_id("minus")
op_mul = driver.find_element_by_accessibility_id("multiply")
op_div = driver.find_element_by_accessibility_id("divide")

# common
op_equal = driver.find_element_by_accessibility_id("equals")

# result field
result = driver.find_element_by_id("com.android.calculator2:id/result")

num1.click()
op_plus.click()
num3.click()
op_equal.click()
op_mul.click()
num2.click()
op_equal.click()
op_minus.click()
num1.click()
op_equal.click()
op_div.click()
num2.click()
op_equal.click()

resultPython = ((1 + 3) * 2 - 1) / 2
print('Result thru python: ', resultPython)
print('Result thru appium: ', result.text)
assert resultPython == float(result.text), "Results are not equal btw python and appium."

driver.quit()
