import time # This is used to add delays in execution (time.sleep()).
from selenium import webdriver # This imports Selenium WebDriver to automate browser interactions.
from home_page2 import HomePage # This imports HomePage class, which contains methods to interact with the home page.
from pricing_page3 import PricingPage # This imports PricingPage class, which contains methods for the pricing page.
from base_page1 import BasePage # This imports BasePage class, which contains common browser interaction methods.
from selenium.webdriver.edge.options import Options # This imports Edge-specific options to configure the browser.


def setup_browser(): # This is the Browser Setup Function
    options = Options()
    options.add_argument("--start-maximized") # Full-screen mode
    options.add_argument("--inprivate")  # Edge equivalent of incognito. This is to prevent cache/cookies from being stored.
    return webdriver.Edge(options=options)


def run_tests(): # This is the Main Test Execution Function, and it initialises Edge WebDriver and assigns page objects for interacting with the website.

    driver = setup_browser()
    try:
        base_page = BasePage(driver)
        home_page = HomePage(driver)
        pricing_page = PricingPage(driver)

        # This opens Home Page Test Cases
        home_page.open("https://dengro.com/") # This opens the Home Page.

        # This accepts Cookies if prompted.
        base_page.click_accept_cookies()

        # Test 1: Verify text presence
        home_page.verify_text_presence("DenGro") # This verifies the presence of text "DenGro".

        # Test 2: Click a button
        home_page.click_button("#hero-item-1 > div.col.content > a.hero-btn.dengro-primary-btn") # This clicks a button on the home page using a CSS selector.

        # Test 3: Navigate to pricing page (Added delay)
        time.sleep(3)  # Ensure homepage is fully loaded before finding the Pricing link i.e. it waits 3 seconds for the page to load.
        home_page.navigate_to_pricing("/html/body/div[5]/header/div/div/div/div[1]/nav/div/div/div/div/ul/li[2]/a/span") # This clicks the Pricing link using an XPath selector.

        # Test 4: Switch currency and & Verifying Price Panel (Using correct selectors)
        pricing_page.open(pricing_page.url) # This oOpens the pricing page.
        pricing_page.switch_currency(
            "body > div.wp-site-blocks > div > div > div:nth-child(2) > div > div.block-pricing-table > div > div.pricing-left-align > div.pricing-meta > div > div > div > div > div > div.dengro-drop-option.selected",
            "body > div.wp-site-blocks > div > div > div:nth-child(2) > div > div.block-pricing-table > div > div.pricing-left-align > div.pricing-meta > div > div > div > div > div > div:nth-child(2)",
            "#pricing-header > div > div:nth-child(1) > a.dengro-primary-btn"
        ) # # This switches currency using three CSS selectors (Currency Dropdown Selector (opens the dropdown menu), Currency Option Selector Currency Option Selector (selects the desired currency), and Price Panel Selector (verifies if the pricing panel updates))

        # Test 5: Capture Screenshot
        try:
            print("Test Debug: Waiting before capturing screenshot...")
            time.sleep(5)  # This will wait for page to fully load i.e. it waits 5 seconds for the page to fully load before capturing a screenshot.
            home_page.capture_screenshot("edge_home.png") # This captures a screenshot and saves it as "edge_home.png".
            print("Test Passed: Screenshot captured successfully") # i.e. TEST PASS.
        except Exception as e:
            print(f"Test Failed: Could not capture screenshot: {e}") # This handles errors gracefully if the screenshot fails i.e. TEST FAIL.

    except Exception as e:
        print(f"Test execution encountered an error: {e}") # This catches any errors during test execution and prints an error message.

    finally:
        # This closes the browser when tests are complete
        driver.quit() # The ensures browser closes even if a test fails.


if __name__ == "__main__":
    run_tests() # This ensures the script only runs when executed directly (not when imported).

    # Tester can remove input() for automation runs
    # input("Press Enter to exit and close the browser...") # The input() line is commented out to allow for automation otherwise it will be manually done.

'''
The execution of the above Edge Suite outputs the below Test Steps:
--------------------------------------------------------------------
1. Launch Edge in InPrivate & Full-Screen Mode
2. Open the DenGro homepage
3. Accept cookies if prompted
4. Verify "DenGro" text is present
5. Click a button on the homepage
6. Navigate to the Pricing page
7. Switch currency & verify price updates
8. Capture a screenshot
9. Close the browser

'''