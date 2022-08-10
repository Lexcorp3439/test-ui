from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver

import steps


# def test_donation_button():
#     driver = open_python_page()
#     main_page = MainPage(driver)
#
#     assert main_page.donate_button.text == "Donate", "Donation button text is not Donate"
#     main_page.donate_button.click()
#     assert main_page.donation_title.is_displayed(), "Donation title not visible"
#     assert main_page.donation_title.text == "Donation for the PSF", "Donation title text is not valid"


def test_search_input():
    search_text = "hello"

    driver = steps.driver_steps().create_driver_and_open_python_page()
    steps.main_page(driver).search(search_text=search_text)
