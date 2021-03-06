# a custom function to simplify syntax for getting with explicit waits

# selenium imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get(driver, by, string):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by, string))
        )
    except:
        driver.quit()
        raise ValueError('element could not be found')

    return element