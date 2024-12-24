# GUVI Selenium Pytest Automation Project

## Project Overview
This project is designed to automate the testing of the [GUVI](https://www.guvi.in) web application using **Python Selenium** and **Pytest** frameworks. It includes test cases for validating the website's functionality, such as login, sign-up, and navigation, using positive and negative test scenarios.

## Features
- **Automation Framework**: Built using Python Selenium with Pytest.
- **Reusable Components**: Implements the Page Object Model (POM) for better maintainability.
- **Cross-Browser Testing**: Supports multiple browsers (Chrome, Firefox, Edge, etc.).
- **Test Cases**: Covers URL validation, button visibility, navigation, and error handling.

## Project Structure
```
guvi_selenium_automation/
├── tests/
│   ├── test_login.py          # Login-related test cases
│   ├── test_signup.py         # Sign-Up-related test cases
│   ├── test_navigation.py     # Navigation and URL validation test cases
│   ├── __init__.py            # Marks this directory as a Python package
├── pages/
│   ├── base_page.py           # Reusable methods for interacting with web elements
│   ├── login_page.py          # Locators and methods for the Login page
│   ├── signup_page.py         # Locators and methods for the Sign-Up page
│   ├── __init__.py            # Marks this directory as a Python package
├── utils/
│   ├── config.py              # Configuration for URLs, credentials, etc.
│   ├── constants.py           # Constants used across the project
│   ├── helpers.py             # Helper functions (e.g., data generation)
│   ├── __init__.py            # Marks this directory as a Python package
├── drivers/
│   ├── chromedriver.exe       # WebDriver for Chrome (or other browser drivers)
├── requirements.txt           # Python dependencies
├── pytest.ini                 # Pytest configuration file
├── conftest.py                # Shared fixtures for test setup
├── README.md                  # Project documentation
```

## Installation
1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd guvi_selenium_automation
   ```

2. **Set Up Environment**:
   Ensure you have Python 3.8+ installed.

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download WebDriver**:
   - Download the appropriate WebDriver for your browser (e.g., ChromeDriver).
   - Place it in the `drivers/` directory.

## Usage
### Running Tests
Execute the test suite using the following command:
```bash
pytest -v
```

### Example Commands
- Run all tests:
  ```bash
  pytest
  ```
- Run specific test file:
  ```bash
  pytest tests/test_login.py
  ```
- Generate test report:
  ```bash
  pytest --html=report.html
  ```

## Test Cases
### Test Case 1: URL Validity
- **Description**: Verify if the URL is valid and loads correctly.
- **Test File**: `tests/test_navigation.py`

### Test Case 2: Webpage Title
- **Description**: Check if the webpage title matches the expected value.
- **Test File**: `tests/test_navigation.py`

### Test Case 3: Login Button
- **Description**: Ensure the Login button is visible and clickable.
- **Test File**: `tests/test_login.py`

### Test Case 4: Sign-Up Button
- **Description**: Ensure the Sign-Up button is visible and clickable.
- **Test File**: `tests/test_signup.py`

### Test Case 5: Sign-Up Navigation
- **Description**: Verify navigation to the Sign-Up page and logout functionality.
- **Test File**: `tests/test_signup.py`

### Test Case 7: Invalid Login
- **Description**: Test login with invalid credentials and verify the error message.
- **Test File**: `tests/test_login.py`

## Troubleshooting
- **Error**: `ModuleNotFoundError: No module named 'ssl'`
  - **Solution**: Ensure your Python installation includes SSL support. Reinstall Python with the correct options or install the missing `ssl` library.

- **Error**: `WebDriverException`
  - **Solution**: Verify that the WebDriver is compatible with your browser version.

## Contributing
Feel free to submit issues or pull requests to improve this project.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements
- **Selenium**: For providing robust web automation tools.
- **Pytest**: For a powerful and simple testing framework.

---
Happy Coding!

