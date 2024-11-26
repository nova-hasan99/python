import requests

def submit_form():
    url = "https://paxifico.com/wp-json/custom-api/v1/get-form-action"  # Form action URL
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Form data to be submitted
    data = {
        "inf_form_xid": "dad413f143eea1082a90c180f082a30b",
        "inf_form_name": "Paxifico - Trigger - Web Form",
        "infusionsoft_version": "1.70.0.736468",
        "inf_field_FirstName": "Test",
        "inf_field_LastName": "User",
        "inf_field_Email": "bot2@example.com",
        "inf_field_Phone1": "+123456789",
        "math_sum-equation_Number": "15",  # Replace with the correct solution if a math challenge is required
        "honeypot": ""  # Honeypot field must be empty for successful submission
    }

    try:
        # Submit the form using POST request
        response = requests.post(url, headers=headers, data=data)
        
        if response.status_code == 200:
            print("Form submitted successfully.")
        else:
            print(f"Failed to submit the form. Status code: {response.status_code}")
            print(f"Response text: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    submit_form()
