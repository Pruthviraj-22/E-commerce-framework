from utils.driver_factory import get_driver
from pages.login_page import LoginPage

def test_valid_login():
    driver = get_driver()
    driver.get("https://automationexercise.com")
    login = LoginPage(driver)
    login.click_signup_login()
    login.enter_email("testautomation@gmail.com")
    login.enter_password("test123")
    login.click_login()
    assert "Automation Exercise" in driver.title
    driver.quit()