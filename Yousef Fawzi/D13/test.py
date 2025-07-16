from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

# Set up Firefox options
options = webdriver.FirefoxOptions()
options.add_argument('--headless')  # Run in headless mode

# Start the browser
service = Service(executable_path='/usr/local/bin/geckodriver')
driver = webdriver.Firefox(service=service, options=options)

# Go to Google
driver.get("https://www.google.com ")

# Wait a bit for the page to load
time.sleep(2)

# Find the Google Search button by class name
search_button = driver.find_element(By.CLASS_NAME, 'o3j99 LLD4me yr19Zb LS8OJ')

# Get the 'value' attribute of the button
button_text = search_button.get_attribute('value')

# Print it out
print("Button Text:", button_text)

# Close the browser
driver.quit()