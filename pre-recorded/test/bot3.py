import requests

def submit_form():
    # Form action URL
    url = "https://designyourlifecentre.activehosted.com/proc.php"
    
    # Headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Form data to be submitted
    data = {
        "u": "100",
        "f": "2",
        "s": "",  # Leave empty
        "c": "0",
        "m": "0",
        "act": "sub",
        "v": "2",
        "or": "c1428372876b2c9475a4981733d6046f",
        "firstname": "mirza2",  # Replace with the first name
        "email": "mirza.doe@example.com",  # Replace with the email address
        "g-recaptcha-response": "",  # Replace with a valid reCAPTCHA token
    }

    try:
        # Submit the form using a POST request
        response = requests.post(url, headers=headers, data=data)

        # Check response
        if response.status_code == 200:
            print("Form submitted successfully.")
        else:
            print(f"Failed to submit the form. Status code: {response.status_code}")
            print(f"Response text: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    submit_form()
