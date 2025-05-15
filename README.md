Python Selenium Automation – AJAX Element Tracker (POM Based)

This project is a Selenium-based Python automation script using the Page Object Model (POM) design pattern. It targets dynamic AJAX elements on a live website to continuously fetch and display real-time data, specifically the world population counter from The World Counts.

Project Goal:

Automate interaction with AJAX-based, dynamically updating web elements
Use POM for scalable and maintainable test scripts
Handle continuous data updates using a while loop
Gracefully handle exceptions like missing or invisible elements

Tech Stack:

Language: Python 3.x
Automation: Selenium WebDriver
Design Pattern: Page Object Model
Driver Management: webdriver_manager
Tool: PyCharm
Browser: Google Chrome

Features:

Continuous tracking of AJAX-updating data
Exception handling for NoSuchElementException and ElementNotVisibleException
Modular structure using Page Object Model
Easy to extend for other real-time counters or AJAX elements

Learning Outcome:

Real-time DOM handling with Selenium
Managing AJAX delays using WebDriverWait
Clean architecture using POM
Handling KeyboardInterrupt for stopping continuous execution
