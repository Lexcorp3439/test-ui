from steps.driver_steps import DriverSteps
from steps.main_page_steps import MainPageSteps


def main_page(driver) -> MainPageSteps:
    return MainPageSteps(driver=driver)


def driver_steps() -> DriverSteps:
    return DriverSteps()
