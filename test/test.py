from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# ChromeDriver এর পাথ নির্ধারণ করুন
CHROMEDRIVER_PATH = './chromedriver-win64/chromedriver.exe'

# আপনার ফেসবুক লগইন তথ্য দিন
FACEBOOK_EMAIL = ''  # আপনার ফেসবুক ইমেল
FACEBOOK_PASSWORD = ''       # আপনার ফেসবুক পাসওয়ার্ড

def login_facebook():
    # Setup ChromeDriver
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)

    # Open Facebook login page
    driver.get('https://www.facebook.com')
    print("Facebook login page loaded.")

    # Enter email address
    email_input = driver.find_element(By.ID, 'email')  # Email field
    email_input.send_keys(FACEBOOK_EMAIL)

    # Enter password
    password_input = driver.find_element(By.ID, 'pass')  # Password field
    password_input.send_keys(FACEBOOK_PASSWORD)

    # Press Login button
    login_button = driver.find_element(By.NAME, 'login')  # Login button
    login_button.click()

    # Wait for some time to let the page load
    time.sleep(5)

    # Print current URL to verify login success
    print("Logged in. Current URL:", driver.current_url)

    # Close browser (Optional)
    # driver.quit()

if __name__ == '__main__':
    login_facebook()
