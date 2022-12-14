import os

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class DriverSteps:

    @property
    def driver_path(self):
        root_dir = os.path.dirname(os.path.abspath("."))
        path = f"{root_dir}/lib/chromedriver"
        print(path)
        return path

    def create_driver_and_open_python_page(self) -> WebDriver:
        driver = webdriver.Chrome(executable_path=self.driver_path)
        driver.get("http://www.python.org")
        return driver
