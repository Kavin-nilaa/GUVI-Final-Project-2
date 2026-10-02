Project Title
Automated Testing of the Web Application – https://opensource-demo.orangehrmlive.com

Objective
The objective of this project is to automate testing of the HR Management web application by simulating user actions and validating core functionalities. The goal is to ensure that modules such as login, menu accessibility, user management, and logout are functioning as intended.

The automation framework simulates user interactions including:

Logging in with multiple sets of credentials

Navigating menus and validating accessibility

Creating and managing users

Assigning leave and initiating claims

Validating UI content and system responses

Scope
Simulate real-world usage patterns such as form interactions, menu navigation, and authentication validation

Execute tests across multiple browsers to ensure cross-browser compatibility

Cover both positive and negative scenarios

Ensure correctness of UI content, user data, and workflow outcomes

Generate readable test execution reports

Preconditions
Comprehensive test suite with valid and invalid scenarios

Logging of results for each test case

Use of explicit waits for reliable synchronization with UI events

Test Suite
The following test cases are implemented:

Login with multiple credentials – Validate login functionality using structured external data.

Home URL accessibility – Verify that the application home page loads without error.

Login fields presence – Ensure username and password fields are visible and enabled.

Main menu items – Validate visibility and clickability of Admin, PIM, Leave, Time, Recruitment, My Info, Performance, Dashboard.

Create new user and validate login – Add a new user and confirm successful login.

Validate new user in admin list – Search for newly created user in Admin > User Management.

Forgot Password functionality – Verify password reset workflow and confirmation message.

My Info sub-menu items – Validate presence and functionality of Personal Details, Contact Details, Emergency Contacts, etc.

Assign leave – Assign leave to an employee and confirm success message and record update.

Initiate claim request – Submit a claim request and validate confirmation and claim history.

Tech Stack
Language: Python

Framework: Selenium WebDriver

Testing Tool: Pytest

IDE: PyCharm

Utilities: WebDriverWait, Excel/CSV data-driven input

Project Structure
Final Project 2/
│── .venv/                     # Virtual environment
│── Pages/                     # Page Object classes
│   ├── login_page.py
│   ├── home_page.py
│   ├── admin_page.py
│   ├── leave_page.py
│   ├── claim_page.py
│   ├── myinfo_page.py
│   └── base_page.py
│── reports/                   # Test execution reports
│   └── screenshots/
│── Tests/                     # Test cases
│   ├── test_login_page.py
│   ├── test_home_page_main_menu.py
│   ├── test_new_user_login.py
│── Utils/                     # Utilities and setup
│   ├── driver_setup.py
│   ├── excel_util.py
│   └── conftest.py
│── Final Project 2 Test Case.xlsx   # Test case documentation
│── Final Project 2 Test Data.xlsx   # Test data inputs
│── report.html                # Test execution report
│── main.py                    # Entry point
│── README.md                  # Project documentation
