from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    signup_login_button = ( By.LINK_TEXT, "Signup / Login" )
    email_input = ( By.XPATH, "//input[@data-qa='login-email']" )
    password_input = ( By.XPATH, "//input[@data-qa='login-password']" )
    login_button = ( By.XPATH, "//button[@data-qa='login-button']" )

    def click_signup_login(self):
        self.driver.find_element( *self.signup_login_button ).click()

    def enter_email(self, email):
        self.driver.find_element( *self.email_input ).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element( *self.password_input ).send_keys(password)

    def click_login(self):
        self.driver.find_element( *self.login_button).click()