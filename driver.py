from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime


# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Set the size of the browser window
driver.set_window_size(1366, 945)

# Go to the Amazon website
driver.get('https://www.amazon.com.au')

# Find the search input box and enter 'Video games'
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
search_box.send_keys('Video games')

# Press the Enter key to search
search_box.send_keys(Keys.ENTER)

# Wait for the results to load
time.sleep(5)

# Set the name of the screenshot file
screenshot_name = "Screenshot"

# Take a screenshot of the page
screenshot = driver.get_screenshot_as_png()

# Save the screenshot to a local file
with open(screenshot_name, 'wb') as file:
    file.write(screenshot)

# Close the driver
driver.close()