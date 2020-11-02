import unittest
from selenium import webdriver

from test_data import TestData
from locators import Locators
from pages import LoginPage, DashboardPage, AdminManagementPage, AturPengeluaranPage

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=TestData.CHROME)
        self.driver.set_window_size(1366, 768) # the default size for dashboard admin
        # self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

class LoginDashboardTest(BaseTest):
    def test_login_superadmin_success(self):
        """
        Test case Login success as a Super Admin
        """

        # create Login page object
        self.loginpage = LoginPage(self.driver)

        # Step 1 - Input username and password as a Super Admin then click Login button
        self.loginpage.login_superadmin_success()

        # create Dashboard page object
        self.dashboardpage = DashboardPage(self.driver)

        # Step 2 - Assertion : Admin Management side menu is visible
        self.dashboardpage.is_visible(Locators.ADMIN_MANAGEMENT_MENU_SIDE)

    def test_login_admin_success(self):
        """
        Test case Login success as an Admin
        """

        # create Login page object
        self.loginpage = LoginPage(self.driver)

        # Step 1 - Input username and password as an admin then click Login button
        self.loginpage.login_admin_success()

        # create Dashboard page object
        self.dashboardpage = DashboardPage(self.driver)

        # Step 2 - Assertion : Admin Management side menu is not visible
        self.dashboardpage.is_invisible(Locators.ADMIN_MANAGEMENT_MENU_SIDE)

    def test_login_failed_wrong_username(self):
        """
        Test case Login failed with wrong username
        """

        # create Login page object
        self.loginpage = LoginPage(self.driver)

        # Step 1 - Input wrong username, input correct password then click Login button
        self.loginpage.login_failed_if_wrong_username()

        # Step 2 - Assertion : Toast alert is visible
        self.loginpage.is_visible(Locators.LOGIN_ALERT_TOAST)

    def test_login_failed_wrong_password(self):
        """
        Test case Login failed with wrong password
        """

        # create Login page object
        self.loginpage = LoginPage(self.driver)

        # Step 1 - Input correct username, input wrong password then click Login button
        self.loginpage.login_failed_if_wrong_password()

        # Step 2 - Assertion : Toast alert is visible
        self.loginpage.is_visible(Locators.LOGIN_ALERT_TOAST)

    def test_login_failed_no_fill_username_password(self):
        """
        Test case Login failed with no input
        """

        # create Login page object
        self.loginpage = LoginPage(self.driver)

        # Step 1 - Fill no username and password, then click Login button
        self.loginpage.login_login_failed_if_no_fill_username_password()

        # Step 2 - Assertion : Alert message is visible
        element_text1 = self.loginpage.get_text(Locators.LOGIN_ERROR_ALERT_USERNAME)
        element_text2 = self.loginpage.get_text(Locators.LOGIN_ERROR_ALERT_PASSWORD)
        self.assertEqual("Mohon masukkan username", element_text1)
        self.assertEqual("Mohon masukkan password", element_text2)

class AdminManagementTest(BaseTest):
    def test_add_admin_success(self):
        """
        Test case Super Admin success add new admin
        """

        # create Login page object
        self.loginpage = LoginPage(self.driver)

        # Step 1 - Login as Super Admin
        self.loginpage.login_superadmin_success()

        # create Dashboard page object
        self.dashboardpage = DashboardPage(self.driver)

        # Step 2 - Click menu admin management
        self.dashboardpage.redirect_to_admin_management_page()

        # create Admin Management page object
        self.adminmanagementpage = AdminManagementPage(self.driver)

        # Step 3 - Click add admin button fill the form with correct requirements
        self.adminmanagementpage.superadmin_success_add_admin()

        # Step 4 - Assertion : Redirected back to Admin Management page
        self.adminmanagementpage.is_visible(Locators.ADD_ADMIN_BUTTON)

    def test_add_admin_failed_email_registered(self):
        """
        Test case Super Admin failed add new admin with registered email
        """

        # create Login page object
        self.loginpage = LoginPage(self.driver)

        # Step 1 - Login as Super Admin
        self.loginpage.login_superadmin_success()

        # create Dashboard page object
        self.dashboardpage = DashboardPage(self.driver)

        # Step 2 - Click menu admin management
        self.dashboardpage.redirect_to_admin_management_page()

        # create Admin Management page object
        self.adminmanagementpage = AdminManagementPage(self.driver)

        # Step 3 - Click add admin button dan fill the form with registered email
        self.adminmanagementpage.superadmin_failed_add_admin_if_email_registered()

        # Step 4 - Assertion : Alert message is visible
        element_text = self.adminmanagementpage.get_text(Locators.ALERT_FAILED_ADD_ADMIN)
        self.assertEqual("Email is already in use!", element_text)

    def test_add_admin_failed_username_registered(self):
        """
        Test case Super Admin failed add new admin with registered username
        """

        # create Login page object
        self.loginpage = LoginPage(self.driver)

        # Step 1 - Login as Super Admin
        self.loginpage.login_superadmin_success()

        # create Dashboard page object
        self.dashboardpage = DashboardPage(self.driver)

        # Step 2 - Click menu admin management
        self.dashboardpage.redirect_to_admin_management_page()

        # create Admin Management page object
        self.adminmanagementpage = AdminManagementPage(self.driver)

        # Step 3 - Click add admin button and fill the form with registered username
        self.adminmanagementpage.superadmin_failed_add_admin_if_username_registered()

        # Step 4 - Assertion : Alert message is visible
        element_text = self.adminmanagementpage.get_text(Locators.ALERT_FAILED_ADD_ADMIN)
        self.assertEqual("Username is already in use!", element_text)

class AturPengeluaranTest(BaseTest):
    def test_search_data_found(self):
        """
        Test case to search data with registered account number
        """

        # create Login page object
        self.loginpage = LoginPage(self.driver)

        # Step 1 - Login
        self.loginpage.login_admin_success()

        # create Dashboard page object
        self.dashboardpage = DashboardPage(self.driver)

        # Step 2 - Click menu Cashflow and choose 'Atur Pengeluaran'
        self.dashboardpage.redirect_to_atur_pengeluaran_page()

        # create 'Atur Pengeluaran' page object
        self.aturpengeluaranpage = AturPengeluaranPage(self.driver)

        # Step 3 - Input registered account number on the search bar
        self.aturpengeluaranpage.search_data_atur_pengeluaran_found()

        # Step 4 - Assertion : The data is presented
        element_text = self.aturpengeluaranpage.get_text(Locators.ATUR_PENGELUARAN_INFORMATION_COUNT_DATA)
        self.assertNotEqual('Menampilkan semua "0 atur pengeluaran"', element_text)

    def test_search_data_not_found(self):
        """
        Test case to search data with unregistered account number
        """

        # create Login page object
        self.loginpage = LoginPage(self.driver)

        # Step 1 - Login
        self.loginpage.login_admin_success()

        # create Dashboard page object
        self.dashboardpage = DashboardPage(self.driver)

        # Step 2 - Click menu Cashflow and choose 'Atur Pengeluaran'
        self.dashboardpage.redirect_to_atur_pengeluaran_page()

        # create 'Atur Pengeluaran' page object
        self.aturpengeluaranpage = AturPengeluaranPage(self.driver)

        # Step 3 - Input unregistered account number on the search bar
        self.aturpengeluaranpage.search_data_atur_pengeluaran_not_found()

        # Step 4 - Assertion : No data is presented
        element_text = self.aturpengeluaranpage.get_text(Locators.ATUR_PENGELUARAN_INFORMATION_COUNT_DATA)
        self.assertEqual('Menampilkan semua "0 atur pengeluaran"', element_text)