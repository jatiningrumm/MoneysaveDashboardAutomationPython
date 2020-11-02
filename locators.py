from selenium.webdriver.common.by import By

class Locators():
    # --- Login Dashboard Locators ---
    LOGIN_INPUT_USERNAME = (By.ID, "normal_login_username")
    LOGIN_INPUT_PASSWORD = (By.ID, "normal_login_password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#normal_login > div:nth-child(6) > div > div > div > button")
    LOGIN_ERROR_ALERT_USERNAME = (By.CSS_SELECTOR, "#normal_login > div:nth-child(2) > div > div.ant-form-item-explain > div")
    LOGIN_ERROR_ALERT_PASSWORD = (By.CSS_SELECTOR, "#normal_login > div:nth-child(4) > div > div.ant-form-item-explain > div")
    LOGIN_ALERT_TOAST = (By.CSS_SELECTOR, "#toast-container")

    # --- Side Menu Page Locators ---
    LOGO_DASHBOARD_HEADER = (By.CSS_SELECTOR, "#__next > main > section > section > aside > div > header > img")
    DASHBOARD_MENU_SIDE = (By.CSS_SELECTOR, "#__next > main > section > section > aside > div > ul > li.ant-menu-item.ant-menu-item-selected > span:nth-child(2) > a")
    ADMIN_MANAGEMENT_MENU_SIDE = (By.CSS_SELECTOR, "#__next > div > main > section > section > aside > div > ul > li:nth-child(2) > span:nth-child(2) > a")
    USER_MANAGEMENT_MENU_SIDE = (By.XPATH, "xpath=//div[@id='__next']/div/main/section/section/aside/div/ul/li[3]/div/span[2]")
    CASHFLOW_MENU_SIDE = (By.XPATH, "//div[@id='__next']/div/main/section/section/aside/div/ul/li[3]/div/span[2]")
    SAVING_MENU_SIDE = (By.LINK_TEXT, "Saving")
    PEMBELIAN_MENU_SIDE = (By.CSS_SELECTOR, "")
    SETTING_MENU_SIDE = (By.CSS_SELECTOR, "")

    # --- Admin Management Side Menu Locators ---
    ADD_ADMIN_BUTTON = (By.CSS_SELECTOR, "#__next > div > main > section > section > section > section > main > div > div > div > div > div.ant-table-title > div > button")
    ADD_ADMIN_NAME_INPUT = (By.ID, "name")
    ADD_ADMIN_EMAIL_INPUT = (By.ID, "email")
    ADD_ADMIN_USERNAME_INPUT = (By.ID, "username")
    ADD_ADMIN_PASSWORD_INPUT = (By.ID, "password")
    ADD_ADMIN_SIMPAN_BUTTON = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]")
    ALERT_FAILED_ADD_ADMIN = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div")

    # --- Cashflow Side Menu Locators ---
    MONITORING_MENU = (By.LINK_TEXT, "Monitoring")
    ATUR_PENGELUARAN_MENU = (By.LINK_TEXT, "Atur Pengeluaran")
    ATUR_PENGELUARAN_PAGE_HEADER = (By.CSS_SELECTOR, "#__next > div > main > section > section > section > section > main > div > div > div > div > div > div.ant-card-meta > div > div")
    ATUR_PENGELUARAN_SEARCH_BAR = (By.CSS_SELECTOR, "#__next > div > main > section > section > section > section > main > div > div > div > div > div > div.ant-row > div:nth-child(1) > div > span > input")
    ATUR_PENGELUARAN_INFORMATION_COUNT_DATA = (By.CSS_SELECTOR, "#__next > div > main > section > section > section > section > main > div > div > div > div > div > div.ant-row > div:nth-child(1) > div > div")
    MONITORING_SEARCH_BAR_TRANSACTION = (By.CSS_SELECTOR, "")
    MONITORING_DATE_BAR_TRANSACTION = (By.CSS_SELECTOR, "")



