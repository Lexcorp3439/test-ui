from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class MainPage(BasePage):

    @property
    def donate_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//a[@class='donate-button']")

    @property
    def donation_title(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//h1[@class='entry-title']")

    @property
    def search_input(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//input[@id='id-search-field']")

    @property
    def start_search(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//button[@id='submit']")
