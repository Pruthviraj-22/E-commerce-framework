from selenium.webdriver.common.by import By

class SignupPage:

    def __init__(self, driver):
        self.driver = driver
    name_input = (By.XPATH,"//input[@data-qa='signup-name']")
    email_input = (By.XPATH,"//input[@data-qa='signup-email']")
    signup_button = (By.XPATH,"//button[@data-qa='signup-button']")
    gender_radio = (By.ID,"id_gender1")
    password_input = (By.ID,"password")
    day_dropdown = (By.ID,"days")
    month_dropdown = (By.ID,"months")
    year_dropdown = (By.ID,"years")
    first_name = (By.ID,"first_name")
    last_name = (By.ID,"last_name")
    address = (By.ID,"address1")
    state = (By.ID,"state")
    city = (By.ID,"city")
    zipcode = (By.ID,"zipcode")
    mobile_number = (By.ID,"mobile_number")
    create_account_button = (By.XPATH,"//button[@data-qa='create-account']")
    account_created_text = (By.XPATH,"//b[text()='Account Created!']")

    def enter_name(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)
    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)
    def click_signup(self):
        self.driver.find_element(*self.signup_button).click()
    def select_gender(self):
        self.driver.find_element(*self.gender_radio).click()
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)
    def enter_firstname(self, firstname):
        self.driver.find_element(*self.first_name).send_keys(firstname)
    def enter_lastname(self, lastname):
        self.driver.find_element(*self.last_name).send_keys(lastname)
    def enter_address(self, addr):
        self.driver.find_element(*self.address).send_keys(addr)
    def enter_state(self, state):
        self.driver.find_element(*self.state).send_keys(state)
    def enter_city(self, city):
        self.driver.find_element(*self.city).send_keys(city)
    def enter_zipcode(self, zip_code):
        self.driver.find_element(*self.zipcode).send_keys(zip_code)
    def enter_mobile(self, mobile):
        self.driver.find_element(*self.mobile_number).send_keys(mobile)
    def click_create_account(self):
        self.driver.find_element(*self.create_account_button).click()
    def get_account_created_text(self):
        return self.driver.find_element(*self.account_created_text).text