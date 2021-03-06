# python imports

# local imports
from src.webscraper.scraper.veracross.auth import auth_veracross
from src.webscraper.scraper.veracross.driver import generate_driver
from config import SELENIUM_TYPE

# selenium imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def ensure_veracross(username, password):

    TYPE = SELENIUM_TYPE
    driver = generate_driver(TYPE)
    print(f"Running {TYPE} browser\n")

    try:
        print("Authenticating veracross...\n")
        driver = auth_veracross(driver, username, password)
    except:
        raise ValueError("Probably didn't enter username or password correctly")

    try:
        driver.get("https://portals.veracross.com/hackley/student")
        driver.find_element(By.ID, "username")
        return False
    except:
        return True
