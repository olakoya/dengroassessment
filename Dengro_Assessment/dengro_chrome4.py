import time # This provides time-related functions, like sleep() to pause execution.
from selenium import webdriver # This imports Selenium WebDriver, which allows us to automate browser actions.
from home_page2 import HomePage # This imports the HomePage class to interact with elements on the home page.
from pricing_page3 import PricingPage # This imports the PricingPage class to interact with elements on the pricing page.
from base_page1 import BasePage # This imports the BasePage class, which contains shared methods for browser interactions.
from selenium.webdriver.chrome.options import Options # This imports Chrome-specific options for configuring the browser session.


def setup_browser(): # This is the Browser Setup Function
    options = Options() # This function configures and returns a Chrome WebDriver instance
    options.add_argument("--start-maximized") # Full-screen mode
    options.add_argument("--incognito") # Incognito mode
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) # Automation detection disabled
    return webdriver.Chrome(options=options)

def run_tests(): # This is the Main Test Execution Function
    driver = setup_browser() # This initialises Chrome WebDriver and assigns page objects for easy access to methods.

    try:
        base_page = BasePage(driver)
        home_page = HomePage(driver)
        pricing_page = PricingPage(driver)

        # This opens the Home Page Test Cases
        home_page.open("https://dengro.com/")

        # This accepts Cookies if a pop-up appears
        base_page.click_accept_cookies()

        # Test 1: Verify text presence
        home_page.verify_text_presence("DenGro") # This verifies the presence of specific text on the page

        # Test 2: Click a button using an XPath selector
        home_page.click_button("/html/body/div[5]/div/div[1]/div/div/div[1]/a[1]", locator_type="xpath")

        # Test 3: Navigate to pricing page (Added delay)
        time.sleep(3)  # Ensure page is fully loaded before finding the Pricing link i.e. waits 3 seconds to ensure the page loads before finding the Pricing link.
        home_page.navigate_to_pricing("/html/body/div[5]/header/div/div/div/div[1]/nav/div/div/div/div/ul/li[2]/a/span") # This clicks the Pricing link using an XPath selector.

        # Test 4: Switch currency and Verifying Price Panel (Using correct selectors)
        pricing_page.open(pricing_page.url) # This opens the pricing page
        pricing_page.switch_currency(
            "body > div.wp-site-blocks > div > div > div:nth-child(2) > div > div.block-pricing-table > div > div.pricing-left-align > div.pricing-meta > div > div > div > div > div > div.dengro-drop-option.selected",
            "body > div.wp-site-blocks > div > div > div:nth-child(2) > div > div.block-pricing-table > div > div.pricing-left-align > div.pricing-meta > div > div > div > div > div > div:nth-child(2)",
            "#pricing-header > div > div:nth-child(1) > a.dengro-primary-btn"
        ) # This switches currency using three CSS selectors (Currency Dropdown Selector (opens the dropdown menu), Currency Option Selector Currency Option Selector (selects the desired currency), and Price Panel Selector (verifies if the pricing panel updates))

        # Test 5: Capture Screenshot
        try:
            print("Test Debug: Waiting before capturing screenshot...")
            time.sleep(5)  # This will wait few seconds to ensure page is fully loaded i.e. it waits 5 seconds for the page to fully load before capturing a screenshot.
            home_page.capture_screenshot("chrome_home.png") # This calls capture_screenshot() to save the page as chrome_home.png.
            print("Test Passed: Screenshot captured successfully") # i.e. TEST PASS.
        except Exception as e:
            print(f"Test Failed: Could not capture screenshot: {e}") # This handles errors gracefully if the screenshot fails i.e. TEST FAIL.

    finally:
        # This ensures the browser is closed after tests execution
        driver.quit() # The ensures browser closes even if a test fails.

if __name__ == "__main__":
    run_tests() # This ensures the script only runs when executed directly (not when imported).

    # Tester can remove input() for automation runs
    # input("Press Enter to exit and close the browser...") # The input() line is commented out to allow for automation otherwise it will be manually done.

'''
The execution of the above Chrome Suite outputs the below Test Steps:
--------------------------------------------------------------------
1. Launch Chrome in Incognito & Full-Screen Mode
2. Open the DenGro homepage
3. Accept cookies
4. Verify "DenGro" text exists
5. Click a button
6. Navigate to the Pricing page
7. Switch currency & verify price updates
8. Capture a screenshot
9. Close the browser

'''