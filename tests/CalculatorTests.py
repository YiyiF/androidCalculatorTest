import unittest
from pageobjects.Calc import Calculator
from webdriver import Driver


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def test_plus(self):
        calculator = Calculator(self.driver)
        calculator.plusdo(1, 2)

    def test_multiply(self):
        calculator = Calculator(self.driver)
        calculator.multiplydo(2, 3)

    def tearDown(self):
        self.driver.instance.quit()
