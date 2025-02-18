'''
The Exercise
--------------

1. Goal

Build an automated browser suite to test the functionality of the dengro.com website.

Requirements:
-------------

a. Use any testing tool of your choice.
b. Use any strongly typed programming language of your choice.
c. Your project must check the functionality in 2 major browsers.
d. Your project must test the 5 different pieces of functionality listed below

i. Assert that a piece of text appears on a given page
ii. Assert clicking a button does some functionality
iii. Assert clicking a link navigates correctly
iv. Assert that the pricing page allows users to change their currency https://dengro.com/pricing and that the pricing panels reflect that
v. Capture a screenshot of any page

2. Guide

a. You should focus not only on the functionality of your code but also the cleanliness.
b. The code should be easy to read and follow good coding practices.
c. Please spend no more than 2-3 hours on this.

3. Submission

a. Complete your project preferably by close of play Mon 10th or latest by 1pm Tue 11th Feb
b. Submit via a source code control tool, such as a GitHub repository.
c. Include a README.md describing how to install and run your project.

'''

'''
Answer
------

To rewrite the code I will be using the Page Object Model (POM), as I need to create separate classes for each page or component of 
the application. 

This approach will improve code readability, maintainability, and reusability. 

'''

'''
Below are different files that will be created for the refactored code using POM:
----------------------------------------------------------------------------------

1. Base Page Class

2. Home Page Class

3. Pricing Page Class

4. i. DenGro Chrome Suite

4. ii. DenGro Edge Suite

'''

'''
How It Works?
-------------

BasePage: Provides reusable methods for interacting with the browser.

HomePage: Implements actions specific to the home page, such as verifying text, clicking buttons, and navigating to other pages.

PricingPage: Implements actions specific to the pricing page, such as switching currency.

Test Suite: Initialises the browser, creates instances of the page classes, and runs the tests.

'''

'''
Benefits of Page Object Model
-------------------------------

Reusability: Common methods are reused across pages.

Maintainability: Changes to a page's structure only require updates in the corresponding page class.

Readability: Tests are more readable and focused on user actions.

Scalability: Easy to add new pages or tests without duplicating code.

'''