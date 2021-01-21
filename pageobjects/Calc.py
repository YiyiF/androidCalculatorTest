from webdriver import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy

"""
Expected conditions >> Indicate the value for the expected condition.
    EC.visibility_of_element_located，Need to find the element and it is visible.
    EC.presence_of_element_located，Find the element whatever it is visible.
WebDriverWait >> Waiting for some specific element to be reachable and may also receive a timeout value.
MobileBy >> Indicate in a mobile context that can use specific content to find elements.
    find_element_by_ios_uiautomation
    find_elements_by_ios_uiautomation
    find_element_by_android_uiautomator
    find_elements_by_android_uiautomator
    find_element_by_accessibility_id
    find_elements_by_accessibility_id
"""


class Calculator:
    def __init__(self, driver):
        self.driver = driver
        self.result = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ID, 'com.android.calculator2:id/result'
        )))
        self.plus = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, 'plus'
        )))
        self.div = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, 'divide'
        )))
        self.multiply = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, 'multiply'
        )))
        self.minus = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, 'minus'
        )))
        self.number = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ID, 'com.android.calculator2:id/formula'
        )))

    def clicknumber(self, num):
        _num = str(num)
        self.driver.instance.find_element(MobileBy.ID, 'com.android.calculator2:id/digit_' + _num).click()
        assert _num in self.number.text, 'Result is different from input.'

    def plusdo(self, num1, num2):
        self.clicknumber(num1)
        self.plus.click()
        self.clicknumber(num2)

        result = sum((num1, num2))
        calcResult = int(self.result.text)

        assert result == calcResult, 'Result is different from python.'

    def multiplydo(self, num1, num2):
        self.clicknumber(num1)
        self.multiply.click()
        self.clicknumber(num2)

        result = num1 * num2
        calcResult = int(self.result.text)

        assert result == calcResult, 'Result is different from python.'

