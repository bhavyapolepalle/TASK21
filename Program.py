from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver (Make sure to replace 'chromedriver' with the path to your ChromeDriver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("https://www.saucedemo.com/")

    # Display cookies before login
    cookies_before_login = driver.get_cookies()
    print("Cookies before login:")
    for cookie in cookies_before_login:
        print(cookie)

    # Perform login
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    # Wait for login to complete and redirect to the dashboard
    time.sleep(3)

    # Display cookies after login
    cookies_after_login = driver.get_cookies()
    print("\nCookies after login:")
    for cookie in cookies_after_login:
        print(cookie)

    # Perform logout
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()

    # Wait for the menu to open
    time.sleep(1)

    logout_link = driver.find_element(By.ID, "logout_sidebar_link")
    logout_link.click()

    # Wait for logout to complete and redirect to the login page
    time.sleep(3)

    # Verify logout by checking if we are back on the login page
    assert "https://www.saucedemo.com/" in driver.current_url

    print("\nLogged out successfully.")

finally:
    # Close the WebDriver
    driver.quit()