from itertools import cycle

def xor(a, b):
    return bytes(i ^ j for i, j in zip(a, cycle(b)))

# Known PNG header bytes
key = [137, 80, 78, 71, 13, 10, 26, 10]

# Read the encoded file
with open('enc.txt', 'rb') as file:
    enc = file.read()

# Decrypt the content
dec = xor(enc, key)

# Write the decrypted content back to a new PNG file
with open('decrypted.png', 'wb') as file:
    file.write(dec)

print("Decryption complete. The file has been saved as decrypted.png.")
