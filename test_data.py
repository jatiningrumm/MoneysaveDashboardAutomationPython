# import fake data library
from faker import Faker
fake = Faker()

class TestData():
    # --- Driver Path ---
    CHROME = r"C:\Users\Lenovo\Documents\DashboardMoneysaveAutomationProject\Driver\chromedriver.exe"

    # --- URL & Credentials ---
    BASE_URL = "https://semut-dashboard.vercel.app/"
    BASE_URL_PRODUCTION = "https://moneysave-admin.vercel.app/"
    BASE_URL_LOCAL = "localhost:3000"

    # --- Login Credentials ---
    USERNAME_SUPERADMIN = "bukandimas"
    PASSWORD_SUPERADMIN = "dimasdimas"
    USERNAME_ADMIN = "ocha"
    PASSWORD_ADMIN =  "tetehocha"
    WRONG_USERNAME = "iniadminmoneysave"
    WRONG_PASSWORD = "12345687"

    # --- Admin Management ---
    RANDOM_NAME = fake.first_name()
    RANDOM_EMAIL = fake.ascii_email()
    RANDOM_USERNAME = fake.user_name()
    NAME_NEW_ADMIN = "denaneer"
    USERNAME_NEW_ADMIN = "operatordena"
    EMAIL_NEW_ADMIN = "denaneer@yopmail.com"
    PASSWORD_NEW_ADMIN = "denadena"
    EMAIL_REGISTERED = "tetehocha@yopmail.com"

    # --- Atur Pengeluaran ---
    ACCOUNT_NUMBER_FOUND = "081221811878"
    ACCOUNT_NUMBER_NOT_FOUND = "334213444"

