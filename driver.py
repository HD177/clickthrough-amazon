from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
search_box.send_keys('science fiction books')

# Press the Enter key to search
search_box.send_keys(Keys.ENTER)

# Wait for the first result to appear
wait = WebDriverWait(driver, 10)
first_result = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@data-index='6']")))

# Click on the first result
first_result.click()

# Wait for 3 seconds
time.sleep(3)

# Take a screenshot of the page
screenshot = driver.get_screenshot_as_png()
timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
file_name = f"screenshot-{timestamp}.png"
driver.save_screenshot(file_name)

# Go back to the results page
driver.back()

# Wait for the second result to appear
second_result = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@data-index='7']")))

# Click on the second result
second_result.click()

# # Find the search input box and enter 'Video games'
# first_result = driver.find_element(By.ID, 'search_result_6')
# first_result.click()

# Set the name of the screenshot file
screenshot_name = "Screenshot"

# Take a screenshot of the page
screenshot = driver.get_screenshot_as_png()
timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
file_name = f"screenshot-{timestamp}.png"
driver.save_screenshot(file_name)

# Save the screenshot to a local file
with open(screenshot_name, 'wb') as file:
    file.write(screenshot)

# Close the driver
driver.close()