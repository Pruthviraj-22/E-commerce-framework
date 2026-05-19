import time
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.signup_page import SignupPage


def test_user_registration():
    driver = get_driver()
    driver.get("https://automationexercise.com")
    login = LoginPage(driver)
    login.click_signup_login()
    signup = SignupPage(driver)
    signup.enter_name("Pruthvi")
    signup.enter_email("pruthvi110075@gmail.com")
    signup.click_signup()
    signup.select_gender()
    signup.enter_password("test123")
    signup.enter_firstname("Pruthvi")
    signup.enter_lastname("Raj")
    signup.enter_address("Bangalore")
    signup.enter_state("Karnataka")
    signup.enter_city("Bangalore")
    signup.enter_zipcode("560067")
    signup.enter_mobile("9816003844")
    time.sleep(3)
    signup.click_create_account()

    assert (signup.get_account_created_text() == "ACCOUNT CREATED!")
    driver.quit()