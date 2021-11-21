from selenium import webdriver

# Get the path of the ChromeDriver
chrome_driver_path = "/Users/danielchamorro/Documents/Learning/AutomateWithPython/Selenium/chromedriver"

# Create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)

# Navigate to the application home page
driver.get("http://automated.pythonanywhere.com")

# Get elements by class name
# element = driver.find_elements("animated fadeIn")
element = driver.find_element_by_class_name("animated").text

print(element)
