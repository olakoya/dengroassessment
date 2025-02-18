'''
2. Home Page Class
--------------------

a. This class represents the home page of the DenGro website.
b. This HomePage class extends BasePage and provides specific functions for the DenGro home page.
c. It extends BasePage (base_page1), allowing interaction with the DenGro home page.
d. This HomePage class contains methods for verifying text, clicking buttons, navigating to the pricing page, and capturing screenshots.

'''

from base_page1 import BasePage  # This imports the BasePage class, which contains common browser automation methods.
from selenium.webdriver.common.by import By # This imports By, which is used to locate elements (By.ID, By.CLASS_NAME, By.XPATH, etc.).
from selenium.webdriver.support.ui import WebDriverWait # This imports WebDriverWait to allow waiting for elements to appear before interacting with them.
from selenium.webdriver.support import expected_conditions as EC # This imports expected_conditions (EC), which provides conditions like element_to_be_clickable and presence_of_element_located.
from selenium.common.exceptions import TimeoutException, NoSuchElementException # This imports exceptions to handle cases where elements are missing or take too long to load.


class HomePage(BasePage): # This is class definition HomePage of which extends to BasePage, meaning it inherits all its methods.
    def __init__(self, driver): # This is constructor __init__ method.
        super().__init__(driver) # This calls the parent class (BasePage) constructor using super().__init__(driver).
        self.url = "https://dengro.com" # This sets self.url to Dengro’s homepage URL

    def verify_text_presence(self, text): # This method is to verify_text_presence i.e. to check if a given text exists on the page
        try:
            assert text in self.driver.page_source, f"Text '{text}' not found on page {self.url}" # This uses assert to verify the text is in page_source (the entire HTML
            print(f"Test Passed: '{text}' found on {self.url}") # If the text is found, prints success i.e. TEST PASS.
        except AssertionError as e: # If the text is missing, raises an AssertionError
            print(f"Test Failed: {e}") # And it prints failure i.e. TEST FAIL.

    def click_button(self, selector, locator_type="css"): # This method is click_button
        """Click a button using either CSS selector or XPath."""
        try:
            print(f"DEBUG: Checking existence of element -> {selector} (using {locator_type})")
            by_type = By.XPATH if locator_type == "xpath" else By.CSS_SELECTOR # This determines whether to locate the element by CSS or XPath.

            # This first confirms the element **exists** before clicking
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((by_type, selector)) # This waits up to 5 seconds for the button to appear in the DOM.
            )
            print(f"DEBUG: Element found -> {selector} (using {locator_type})")

            # Then, it waits for it to be clickable
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((by_type, selector)) # This waits up to 10 seconds for the button to be clickable.
            )
            button.click()
            print(f"Test Passed: Clicked button -> {selector} (using {locator_type})") # This clicks the button and prints success i.e. TEST PASS.
        except TimeoutException:
            print(f"Test Failed: Element not found or not clickable -> {selector} (using {locator_type})")
        except Exception as e:
            print(f"Test Failed: Unexpected error clicking button -> {selector} (using {locator_type}): {e}") # This handles cases where the button is missing or fails to click of which will result to TEST FAIL.

    def navigate_to_pricing(self, link_xpath): # This method is navigate_to_pricing
        """ This clicks the Pricing link and ensures the page loads."""
        try:
            print(f"Test Debug: Looking for Pricing link using XPath: {link_xpath}")

            # This waits until the button is clickable
            pricing_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, link_xpath)) # This waits up to 10 seconds for the Pricing link to be clickable.
            )
            print("Test Debug: Pricing link found, attempting to click...")

            pricing_link.click()
            print("Test Passed: Clicked on Pricing page link") # This clicks the Pricing link.

            # This waits for a specific element **on the Pricing Page**
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "pricing-panel")) # This waits for a specific element ("pricing-panel") on the Pricing page to confirm it loaded.
                # <- Change this to an element that exists only on the Pricing page
            )
            print("Test Passed: Pricing page loaded successfully")

            # If the Pricing page opens in a new tab, it switches to it
            if len(self.driver.window_handles) > 1:
                self.driver.switch_to.window(self.driver.window_handles[-1])
                print("Test Debug: Switched to new tab") # If the Pricing page opens in a new tab, it switches to that tab.

        except (TimeoutException, NoSuchElementException) as e:
            print(f"Test Failed: Error navigating to Pricing page: {e}") # This handles cases where the Pricing link is missing or the page fails to load.

    def capture_screenshot(self, filename): # This method is capture_screenshot.
        """This captures a screenshot of the current page."""
        try:
            print(f"Camera: Attempting to capture screenshot: {filename}")

            # This verifies we are on the right page before capturing screenshot
            print(f"Current URL: {self.driver.current_url}") # This prints debug information, including the current URL.

            self.driver.save_screenshot(filename)
            print(f"Photo Passed: Screenshot saved: {filename}") # This takes the screenshot and saves it i.e. TEST PASS.
        except Exception as e:
            print(f"Photo Failed: Could not capture screenshot: {e}") # This handles any errors which means TEST FAIL.
