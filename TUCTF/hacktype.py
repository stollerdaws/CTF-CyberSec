from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Open the browser using the default location of the driver
driver = webdriver.Chrome()

# Open the specified website
driver.get('https://hacker-typer.tuctf.com/')

try:
    # Wait for the page elements to load initially
    time.sleep(1)

    for _ in range(180):
        # Find the element that contains the word to type
        word_to_type = driver.find_element(By.CSS_SELECTOR, 'strong[name="word-title"]').text
        # Find the input field, clear it, type the word, and submit
        input_field = driver.find_element(By.NAME, 'word')
        input_field.clear()
        input_field.send_keys(word_to_type)
        input_field.send_keys(Keys.RETURN)

        # Wait a short time to allow the page to update
        time.sleep(0.2)  # Adjust this delay as needed

    print(driver.page_source)
finally:
    # Close the browser
    driver.quit()
