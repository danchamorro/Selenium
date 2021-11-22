from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def login_user():
    # Create a new instance of the Chrome driver with the service
    service = Service(
        "../Selenium/chromedriver")
    service.start()
    driver = webdriver.Remote(service.service_url)
    # Navigate to the application home page
    driver.get("http://automated.pythonanywhere.com/login/")

    # Find the username field and enter the username
    driver.find_element(By.ID, "id_username").send_keys("automated")
    # Sleep for 2 seconds to allow the username to be entered
    time.sleep(2)
    # Find the password field and enter the password
    driver.find_element(By.ID, "id_password").send_keys("automatedautomated")
    # Press the enter key using the Keys class
    driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
    # Print url to verify login
    print(driver.current_url)


login_user()
