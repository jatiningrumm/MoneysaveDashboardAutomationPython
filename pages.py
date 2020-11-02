from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains as chains

# Import test data and element locators
from test_data import TestData
from locators import Locators

class BasePage():
    """
        This class will be the parent of other classes
        This class will contain elements and functions that can be used in other classes
    """

    def __init__(self, driver):
        self.driver = driver

    # Function to click an element located
    def click(self, locator):
        WDW(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    # Function to input text into an element
    def enter_text(self, locator, text):
        WDW(self.driver, 10).until(EC.element_to_be_clickable(locator)).send_keys(text)

    # Function to get the text from an element
    def get_text(self, locator):
        return WDW(self.driver, 10).until(EC.visibility_of_element_located(locator)).text

    # Function to check the visibility of an element
    def is_visible(self, locator):
        try:
            element = WDW(self.driver, 30).until(EC.visibility_of_element_located(locator))
            return bool(element)
        except TimeoutException:
            return False

    # Function to check the invisibility of an element
    def is_invisible(self, locator):
        try:
            element = WDW(self.driver, 30).until(EC.invisibility_of_element_located(locator))
            return bool(element)
        except TimeoutException:
            return False

    # Function to hover and click the element
    def hover_to_click(self, locator):
        element = WDW(self.driver, 10).until(EC.presence_of_element_located(locator))
        chains(self.driver).move_to_element(element).click().perform()

    # Function to hover an element then click another element
    def hover_to_click_element(self, locator1, locator2):
        element = WDW(self.driver,10).until(EC.presence_of_element_located(locator1))
        chains(self.driver).move_to_element(element).perform()
        WDW(self.driver, 10).until(EC.visibility_of_element_located(locator2)).click()

class LoginPage(BasePage):
    """
        This is a class for Login page
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL_PRODUCTION)

    # Function to check login success for admin
    def login_admin_success(self):
        self.enter_text(Locators.LOGIN_INPUT_USERNAME, TestData.USERNAME_ADMIN)
        self.enter_text(Locators.LOGIN_INPUT_PASSWORD, TestData.PASSWORD_ADMIN)
        self.click(Locators.LOGIN_BUTTON)
        self.is_visible(Locators.LOGO_DASHBOARD_HEADER)

    # Function to check login success for super admin
    def login_superadmin_success(self):
        self.enter_text(Locators.LOGIN_INPUT_USERNAME, TestData.USERNAME_SUPERADMIN)
        self.enter_text(Locators.LOGIN_INPUT_PASSWORD, TestData.PASSWORD_SUPERADMIN)
        self.click(Locators.LOGIN_BUTTON)
        self.is_visible(Locators.LOGO_DASHBOARD_HEADER)
        self.is_visible(Locators.ADMIN_MANAGEMENT_MENU_SIDE)

    # Function to check login failed with wrong username
    def login_failed_if_wrong_username(self):
        self.enter_text(Locators.LOGIN_INPUT_USERNAME, TestData.WRONG_USERNAME)
        self.enter_text(Locators.LOGIN_INPUT_PASSWORD, TestData.PASSWORD_ADMIN)
        self.click(Locators.LOGIN_BUTTON)
        self.is_visible(Locators.LOGIN_ALERT_TOAST)

    # Function to check login failed with wrong password
    def login_failed_if_wrong_password(self):
        self.enter_text(Locators.LOGIN_INPUT_USERNAME, TestData.USERNAME_ADMIN)
        self.enter_text(Locators.LOGIN_INPUT_PASSWORD, TestData.WRONG_PASSWORD)
        self.click(Locators.LOGIN_BUTTON)
        self.is_visible(Locators.LOGIN_ALERT_TOAST)

    # Function to check login failed with no input
    def login_login_failed_if_no_fill_username_password(self):
        self.click(Locators.LOGIN_BUTTON)
        self.is_visible(Locators.LOGIN_ERROR_ALERT_USERNAME)
        self.is_visible(Locators.LOGIN_ERROR_ALERT_PASSWORD)


class DashboardPage(BasePage):
    """
        This is a class for Dashboard page
    """

    def __init__(self, driver):
        super().__init__(driver)

    # Function to check redirection of Admin Managament page
    def redirect_to_admin_management_page(self):
        self.click(Locators.ADMIN_MANAGEMENT_MENU_SIDE)
        self.is_visible(Locators.ADD_ADMIN_BUTTON)

    # Function to check redirection of 'Atur Pengeluaran' page
    def redirect_to_atur_pengeluaran_page(self):
        self.click(Locators.CASHFLOW_MENU_SIDE)
        self.click(Locators.ATUR_PENGELUARAN_MENU)
        self.is_visible(Locators.ATUR_PENGELUARAN_PAGE_HEADER)

class AdminManagementPage(BasePage):
    """
        This is a class for Admin Management page
        This page can only be accessed by Super Admin
    """

    def __init__(self, driver):
        super().__init__(driver)

    # Function to check add new admin success
    def superadmin_success_add_admin(self):
        self.click(Locators.ADD_ADMIN_BUTTON)
        self.enter_text(Locators.ADD_ADMIN_NAME_INPUT, TestData.NAME_NEW_ADMIN)
        self.enter_text(Locators.ADD_ADMIN_EMAIL_INPUT, TestData.EMAIL_NEW_ADMIN)
        self.enter_text(Locators.ADD_ADMIN_USERNAME_INPUT, TestData.USERNAME_NEW_ADMIN)
        self.enter_text(Locators.ADD_ADMIN_PASSWORD_INPUT, TestData.PASSWORD_NEW_ADMIN)
        self.click(Locators.ADD_ADMIN_SIMPAN_BUTTON)
        self.is_visible(Locators.ADD_ADMIN_BUTTON)

    # Function to check add new admin failed with registered email
    def superadmin_failed_add_admin_if_email_registered(self):
        self.click(Locators.ADD_ADMIN_BUTTON)
        self.enter_text(Locators.ADD_ADMIN_NAME_INPUT, TestData.RANDOM_NAME)
        self.enter_text(Locators.ADD_ADMIN_EMAIL_INPUT, TestData.EMAIL_REGISTERED)
        self.enter_text(Locators.ADD_ADMIN_USERNAME_INPUT, TestData.RANDOM_USERNAME)
        self.enter_text(Locators.ADD_ADMIN_PASSWORD_INPUT, TestData.PASSWORD_NEW_ADMIN)
        self.click(Locators.ADD_ADMIN_SIMPAN_BUTTON)
        self.is_visible(Locators.ALERT_FAILED_ADD_ADMIN)

    # Function to check add new admin failed with registered username
    def superadmin_failed_add_admin_if_username_registered(self):
        self.click(Locators.ADD_ADMIN_BUTTON)
        self.enter_text(Locators.ADD_ADMIN_NAME_INPUT, TestData.RANDOM_NAME)
        self.enter_text(Locators.ADD_ADMIN_EMAIL_INPUT, TestData.RANDOM_EMAIL)
        self.enter_text(Locators.ADD_ADMIN_USERNAME_INPUT, TestData.USERNAME_ADMIN)
        self.enter_text(Locators.ADD_ADMIN_PASSWORD_INPUT, TestData.PASSWORD_NEW_ADMIN)
        self.click(Locators.ADD_ADMIN_SIMPAN_BUTTON)
        self.is_visible(Locators.ALERT_FAILED_ADD_ADMIN)

class AturPengeluaranPage(BasePage):
    """
        This is a class for 'Atur Pengeluaran" page
    """

    def __init__(self, driver):
        super().__init__(driver)

    # Function to check data presence
    def search_data_atur_pengeluaran_found(self):
        self.enter_text(Locators.ATUR_PENGELUARAN_SEARCH_BAR, TestData.ACCOUNT_NUMBER_FOUND)
        self.is_visible(Locators.ATUR_PENGELUARAN_INFORMATION_COUNT_DATA)

    # Function to check no data presence
    def search_data_atur_pengeluaran_not_found(self):
        self.enter_text(Locators.ATUR_PENGELUARAN_SEARCH_BAR, TestData.ACCOUNT_NUMBER_NOT_FOUND)
        self.is_visible(Locators.ATUR_PENGELUARAN_INFORMATION_COUNT_DATA)

