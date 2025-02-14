#  Dengro Selenium Automation Assessment

## Below Are Details on How To Install and Run My Dengro Selenium Automation Assessment Using Python Programming Language

This project automates the testing of the **DenGro** website using **Selenium WebDriver** in Chrome and Edge browsers.

## **The Features are:**
1. Open DenGro "https://dengro.com/" homepage
2. Verify text presence
3. Click buttons and navigate to the pricing page
4. Switch currency on the pricing page
5. Capture screenshots on both browsers for testing validation

## **The Prerequisites are:**
Ensure you have the following installed:
- [Python](https://www.python.org/downloads/) (3.8+)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Google Chrome](https://www.google.com/chrome/) and
- [Microsoft Edge](https://www.microsoft.com/en-us/edge)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) and
- [Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## **For Installation:**
1. Clone this repository:
   ```sh
   git clone [https://github.com/olakoya/dengroassessment.git]
   cd dengroassessment
   
2. Create a virtual environment:
   python -m venv .venv
  i. source .venv/bin/activate  # On macOS/Linux
  ii. .venv\Scripts\activate     # On Windows

3. Install dependencies:
   pip install -r requirements.txt
   
## **Running the Tests:**
1. Chrome
Run the tests in Chrome: python dengro_chrome4.py

3. Edge
Run the tests in Edge: python dengro_edge4.py

## **Screenshots:**
The script captures screenshots and saves them as:
1. chrome_home.png

2. edge_home.png

## **Contributing:**
1. Fork the repository
   
2. Create a new branch (git checkout -b feature-branch)
   
3. Make your changes and commit (git commit -m "Description of changes")
   
4. Push the branch (git push origin feature-branch)
   
5. Open a pull request

