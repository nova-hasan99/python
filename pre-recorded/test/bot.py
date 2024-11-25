import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver

def solve_math_challenge(driver):
    """Extract and solve the dynamic math equation."""
    try:
        # Locate the math equation on the page
        equation_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sum-equation"))
        )
        equation = equation_element.text.strip()
        print(f"Found math equation: {equation}")

        # Clean and parse the equation
        equation = equation.replace("=", "").strip()  # Remove the trailing '='
        if "+" in equation:
            num1, num2 = map(int, equation.split("+"))
            solution = num1 + num2
        elif "-" in equation:
            num1, num2 = map(int, equation.split("-"))
            solution = num1 - num2
        else:
            raise ValueError("Unsupported equation format")

        # Fill in the solution
        answer_field = driver.find_element(By.ID, "math_sum-equation_Number")
        answer_field.clear()
        answer_field.send_keys(str(solution))
        print(f"Solved math equation: {equation} = {solution}")
    except Exception as e:
        print(f"Error solving math challenge: {e}")

def simulate_user_interaction(driver, field_id, value):
    """Simulate human-like interaction to fill form fields."""
    field = driver.find_element(By.ID, field_id)
    for char in value:
        field.send_keys(char)
        time.sleep(random.uniform(0.1, 0.4))  # Simulate typing speed

def main():
    driver = setup_driver()
    driver.get("https://pyz88406.infusionsoft.com/app/form/process/dad413f143eea1082a90c180f082a30b")  # Your form URL

    try:
        # Simulate filling form fields
        simulate_user_interaction(driver, "inf_field_FirstName", "John")
        simulate_user_interaction(driver, "inf_field_LastName", "Doe")
        simulate_user_interaction(driver, "inf_field_Email", "test@example.com")
        simulate_user_interaction(driver, "inf_field_Phone1", "+123456789")

        # Solve the math challenge
        solve_math_challenge(driver)

        # Submit the form
        submit_button = driver.find_element(By.ID, "btn-d")
        submit_button.click()
        print("Form submitted successfully.")
    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    main()
