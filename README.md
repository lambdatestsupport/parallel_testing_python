## Parallel Testing with Pytest and Selenium

### Description

This code is a Python script that demonstrates how to perform parallel testing using Pytest and Selenium. It includes three test cases that run in parallel, each using a different browser and platform configuration provided by LambdaTest. The test cases perform actions such as opening a webpage, entering login credentials, and verifying the page title.

### Dependencies

- Pytest: The code requires the Pytest framework to be installed. You can install it using the following command:

```shell
pip install pytest
```

- Selenium: The code also requires the Selenium library to be installed. You can install it using the following command:

```shell
pip install selenium
```

- Chrome WebDriver: The code uses Chrome WebDriver for testing with Chrome browsers. Make sure you have Chrome WebDriver installed and available in your system's PATH. You can install it using the following command:

```shell
pip install webdriver_manager
```

### Usage

1. Make sure you have installed the necessary dependencies as mentioned above.

2. Update the code with your LambdaTest username, access token, and password. Replace the placeholders in the following lines:

```python
username = "your_username_here"  # Replace with your LambdaTest username
accessToken = "your_access_token_here"  # Replace with your LambdaTest access token
passs = "your_password_here"  # Replace with your LambdaTest account password
```

3. Run the script using the following command:

```shell
pytest script.py
```

### Note

- The code uses the LambdaTest Selenium grid to execute the tests in parallel on remote browsers. Make sure you have a valid LambdaTest account and provide the correct username, access token, and password.

- Each test case is marked with the `@pytest.mark.parallel` decorator, which enables parallel testing for those specific tests.

- The code includes sample capabilities for Chrome and Microsoft Edge browsers on different platforms. You can modify these capabilities to match your desired browser and platform configurations.

- It's important to call `driver.quit()` at the end of each test case to close the browser and release system resources.

### License

This code is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and use it according to your needs.

### Contact

For any questions or suggestions, please feel free to contact [author_name] at [author_email].
