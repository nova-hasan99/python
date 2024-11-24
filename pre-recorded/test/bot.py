import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import undetected_chromedriver as uc

def setup_driver():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless")  # Enable headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.3")
    
    driver = uc.Chrome(options=options)
    return driver

def auto_submit_form(driver):
    try:
        target_url = "https://www.paxifico.com/bot-protection/"
        driver.get(target_url)
        print(f"Navigated to {target_url}")

        form = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))
        )
        print("Form loaded successfully.")

        inputs = form.find_elements(By.TAG_NAME, "input")
        form_data = {"name": "John Doe", "email": "johndoe@example.com"}

        for input_field in inputs:
            field_name = input_field.get_attribute("name")
            if field_name in form_data:
                input_field.clear()  # Clear any pre-filled values
                input_field.click()
                time.sleep(random.uniform(0.5, 1.5))  # Simulate user typing
                input_field.send_keys(form_data[field_name])
                print(f"Filled '{field_name}' with '{form_data[field_name]}'.")
        
        submit_button = form.find_element(By.TAG_NAME, "button")
        submit_button.click()
        print("Form submitted successfully.")

        # Add random delays to mimic human interaction
        time.sleep(random.uniform(3, 5))

    except TimeoutException:
        print("Error: Timeout while loading the form.")
    except NoSuchElementException as e:
        print(f"Error: Required form element not found. Details: {e}")
    except WebDriverException as e:
        print(f"WebDriver error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        cleanup_driver(driver)

def cleanup_driver(driver):
    try:
        driver.quit()
        print("WebDriver closed.")
    except Exception as e:
        print(f"Error during WebDriver cleanup: {e}")

if __name__ == "__main__":
    driver = setup_driver()
    auto_submit_form(driver)
