import base64

# Decode the ciphertext from base64
ciphertext = base64.b64decode('LEs2fVVxNDMfNHEtcx80cB8nczQfJhVkDHI/Ew==')

# Known parts of the key, with a placeholder for the 6th byte
known_key = bytearray([ord('J'), ord('&'), ord(';'), ord('0'), ord('I'), ord('$'), ord('n')])

# Function to decrypt
def decrypt(ciphertext, key):
    key_len = len(key)
    flag_len = len(ciphertext)
    output = bytearray(flag_len)

    for i in range(flag_len - key_len + 1):
        for j in range(key_len):
            output[i + j] ^= ciphertext[i + j] ^ key[j]

    return output

# Brute force the 6th byte of the key
for sixth_byte in range(256):
    trial_key = bytearray(known_key)
    trial_key[5] = sixth_byte  # Set the 6th byte

    decrypted_data = decrypt(ciphertext, trial_key)

    if decrypted_data.startswith(b"flag{"):
        print(f"Found Key: {trial_key}")
        print(f"Decrypted Data: {decrypted_data.decode(errors='ignore')}")

# Decrypted Data: flag{1k l@k.r,@ k/@x,k@ yJq
# Decrypted Data: flag{ . t   s_t1m 3 _   t0_g3 t _   f\nHU n }