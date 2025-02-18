'''
3. Pricing Page Class
----------------------

a. This class represents the pricing page of the DenGro website.
b. This class interacts with the Pricing Page of DenGro using Selenium of which allows users to:
    i. Select a browser (Chrome or Edge)
    ii. Navigate to the pricing page
    iii. Switch currency in the pricing table
    iv. Verify that the price panel updates after switching currency


'''

from base_page1 import BasePage # This imports the BasePage class, which contains common Selenium methods like open() and find_element().
from selenium import webdriver # This controls browser automation.
from selenium.webdriver.support.ui import WebDriverWait # This waits for elements to appear.
from selenium.webdriver.support import expected_conditions as EC # This defines conditions like element_to_be_clickable().
from selenium.webdriver.common.by import By # This helps locate elements (By.CSS_SELECTOR, By.XPATH, etc.).
import sys # This allows handling command-line arguments.

# This gets browser choice from command line arguments
browser = sys.argv[1] if len(sys.argv) > 1 else "chrome" # This gets the browser name from the command line (sys.argv[1]). If no browser is specified, it defaults to "chrome".

if browser == "chrome":
    options = webdriver.ChromeOptions() # Thus creates Chrome options.
    options.add_argument("--start-maximized") # This maximises the browser window.
    driver = webdriver.Chrome(options=options) # This launches Chrome WebDriver.
elif browser == "edge":
    edge_options = webdriver.EdgeOptions()  # This is also a similar setup for Edge WebDriver just as Chrome.
    edge_options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=edge_options)
else:
    raise ValueError("Unsupported browser!") # This handles errors if the browser is neither Chrome nor Edge.

class PricingPage(BasePage): # This method is defining the PricingPage Class. It also extends BasePage, meaning it inherits common functions like open(url).
    def __init__(self, driver):
        super().__init__(driver) # This calls BasePage’s constructor (super().__init__(driver)).
        self.url = "https://dengro.com/pricing/" # This defines the Pricing Page URL.

    def switch_currency(self, currency_selector, option_selector, price_panel_selector): # The purpose of this is to click the currency dropdown, selects a new currency, and verifies the price panel updates.
        """ This switches currency and verify price panel update."""
        wait = WebDriverWait(self.driver, 10) # This waits up to 10 seconds for the currency dropdown to be clickable.

        # This clicks the dropdown to open it
        currency_dropdown = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, currency_selector)) # This waits for the new currency option to be clickable.
        )
        currency_dropdown.click()
        print("Test Passed: Clicked currency dropdown")

        # This clicks the specific currency option
        currency_option = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, option_selector))  # Passed FIXED
        )
        currency_option.click() # This clicks the currency option.
        print("Test Passed: Selected currency option")


        # This verifies the price panel updates
        price_panel = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, price_panel_selector)) # This waits for the price panel to become visible.
        )
        assert price_panel.is_displayed(), "Test Failed: Currency switch did not update price panel" # It Asserts the panel is displayed to confirm the currency change.
        print("Test Passed: Currency switch successful")

if __name__ == "__main__": # This ensures the script runs only when executed directly (not when imported).
    pricing_page = PricingPage(driver) # This creates a PricingPage instance.
    pricing_page.open(pricing_page.url)  # This navigates to the pricing page i.e. it opens the Pricing Page using open(url).

    # This replaces these with actual CSS selectors from DenGro webpage
    actual_currency_selector = "body > div.wp-site-blocks > div > div > div:nth-child(2) > div > div.block-pricing-table > div > div.pricing-left-align > div.pricing-meta > div > div > div > div > div > div.dengro-drop-option.selected" # The CSS Selector to locate the Currency dropdown (actual_currency_selector).
    actual_option_selector = "body > div.wp-site-blocks > div > div > div:nth-child(2) > div > div.block-pricing-table > div > div.pricing-left-align > div.pricing-meta > div > div > div > div > div > div:nth-child(2)" # The CSS Selector to locate the Currency option (actual_option_selector).
    actual_price_panel_selector = "#pricing-header > div > div:nth-child(1) > a.dengro-primary-btn" # The CSS Selector to locate the Price panel (actual_price_panel_selector).

    pricing_page.switch_currency(actual_currency_selector, actual_option_selector, actual_price_panel_selector) # This calls switch_currency() to Open the dropdown, to Select a new currency, and to Verify the price panel updates.


    # This keeps browser open for debugging i.e 10 seconds after running the script.
    driver.implicitly_wait(10)
    # input("Press Enter to exit and close the browser...") # Pauses execution until the user presses Enter I commented out to avoid manual interaction.

    driver.quit() # This closes the browser when the script finishes.
