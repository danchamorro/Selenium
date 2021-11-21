from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def get_driver():
    # Create a new instance of the Chrome driver with the service
    service = Service(
        "/Users/danielchamorro/Documents/Learning/AutomateWithPython/Selenium/chromedriver")
    service.start()
    driver = webdriver.Remote(service.service_url)
    # Navigate to the application home page
    driver.get("http://automated.pythonanywhere.com")

    # Get elements by class name
    element = driver.find_element(By.CLASS_NAME, "animated").text
    driver.quit()
    return(element)


print(get_driver())
