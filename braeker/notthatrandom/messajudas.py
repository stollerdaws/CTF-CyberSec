from pwn import *
import string

# Function to check if a string is printable
def is_printable(s):
    return all(c in string.printable for c in s)

# Known plaintext
known_plaintext = b"brck{"

# Continuously attempt to decrypt the flag
while True:
    # Connect to the service
    conn = remote('0.cloud.chals.io', 26265)

    # Receive the encrypted flag
    encrypted_flag = conn.recv(45)
    #conn.close()

    # Attempt to derive the key by XORing the known plaintext with the encrypted flag
    potential_key = bytes([encrypted_flag[i] ^ known_plaintext[i] for i in range(len(known_plaintext))])

    # Attempt to decrypt the entire flag using the derived key
    decrypted_flag = bytes([encrypted_flag[i] ^ potential_key[i % len(potential_key)] for i in range(len(encrypted_flag))])

    # Check if the decrypted flag is printable
    if is_printable(decrypted_flag.decode('latin-1')):
        print(f"Possible flag: {decrypted_flag}")
