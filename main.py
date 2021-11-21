from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Create a new instance of the Chrome driver with the service
service = Service(
    "/Users/danielchamorro/Documents/Learning/AutomateWithPython/Selenium/chromedriver")
service.start()
driver = webdriver.Remote(service.service_url)

# Navigate to the application home page
driver.get("http://automated.pythonanywhere.com")

# Get elements by class name
# element = driver.find_elements("animated fadeIn")
element = driver.find_element_by_class_name("animated").text

print(element)
