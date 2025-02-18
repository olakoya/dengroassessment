'''
1. Base Page Class
--------------------

a. This class contains common methods and utilities that can be reused across all pages.
b. It handles navigation, element interaction, waiting for elements, clicking accept cookies, and taking screenshots.
c. It ensures better code organisation and reusability when writing Selenium-based automation scripts.

'''

from selenium import webdriver # This imports Selenium’s webdriver, of which allows interaction with web browsers.
from selenium.webdriver.common.by import By # This provides a By class, which helps in locating elements on a webpage (e.g., By.ID, By.CLASS_NAME, By.XPATH).
from selenium.webdriver.support.select import Select # This imports Select to handle dropdown menus.
from selenium.webdriver.common.keys import Keys # This provides keyboard interaction support (e.g., pressing Enter, Tab, Escape).
from selenium.webdriver.support.ui import WebDriverWait # This allows setting a maximum wait time for elements to appear before proceeding.
from selenium.webdriver.support import expected_conditions as EC # This defines conditions that can be used with WebDriverWait, such as waiting for an element to be clickable or present.

class BasePage:
    def __init__(self, driver):  # Constructor __init__ method takes a driver and assigns it to an instance variable (Initialises the class with a driver instance, which represents the browser.)
        self.driver = driver # This assigns the provided driver to an instance variable.

    def open(self, url):  # The purpose of this line is to navigate to a specific URL
        print(f"Opening URL: {url}") # This prints the URL being opened.
        self.driver.get(url) # This helps to navigate to the URL.
        print(f"Page loaded: {self.driver.title}") # This prints the page title to confirm successful navigation.

    def find_element(self, by, value):  # Wrap Selenium’s native method for locating elements on the page
        return self.driver.find_element(by, value) # These parameters by: Specifies the method (e.g., By.ID, By.CLASS_NAME), value: The actual locator value (e.g., "login-button"). Returns: The located element.

    def wait_for_element(self, by, value, timeout=10): # Waits until an element is present before proceeding.
        """ This waits for an element to be present on the page.""" # The parameters are by: Locator type (By.ID, By.CLASS_NAME, etc.). value: The actual identifier. timeout: Maximum wait time (default is 10 seconds).
        return WebDriverWait(self.driver, timeout).until( # Returns: The located element once it appears.
            EC.presence_of_element_located((by, value))
        )

    def click_accept_cookies(self): # This detects and clicks the "Accept Cookies" button if it appears.
        """This clicks the accept cookies button if it appears."""
        try:
            print("Checking for cookie banner...")
            cookie_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                    "body > div.cky-consent-container.cky-box-bottom-left > div > div > div > "
                    "div.cky-notice-btn-wrapper > button.cky-btn.cky-btn-accept")) # This uses WebDriverWait to check for the presence of the cookie consent button.
            )
            print("Cookie banner found, attempting to click...") # If found, clicks the button.
            cookie_button.click()
            print("Cookies accepted successfully!") # If found, print message.
        except Exception as e:
            print("No cookie banner found or already accepted:", e) # If not found within 5 seconds, prints a message indicating it’s already accepted or not present.

    def capture_screenshot(self, filename): # This captures a screenshot of the current webpage.
        """ This captures a screenshot of the current page.""" # The parameter filename specifies the screenshot’s file name.
        try:
            self.driver.save_screenshot(filename) # This calls to take the screenshot.
            print(f"Screenshot saved as {filename}") # This prints a success message if PASS.
        except Exception as e:
            print(f"Failed to capture screenshot: {e}") # If an error occurs, this prints the error message and that's FAIL.
