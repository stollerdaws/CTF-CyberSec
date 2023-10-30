import hashlib 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = hashlib.sha256(b"tasciewapeoiu").digest()

with open('flag.enc', 'rb') as f:
    data = f.read()
# Extract the first block of ciphertext.
first_block_ct = data[:AES.block_size]

# The known plaintext.
known_pt = b"UDCTF{"

# Pad the known plaintext to the block size.
known_pt_padded = known_pt.ljust(AES.block_size, b'\0')

# Calculate the IV.
iv = bytes(a ^ b for a, b in zip(first_block_ct, known_pt_padded))

# Separate the ciphertext.
ct = data[AES.block_size:]

# Create the AES cipher object.
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the ciphertext.
pt = cipher.decrypt(ct)

# Unpad the plaintext.
try:
    plaintext = unpad(pt, AES.block_size)
except ValueError:
    # If unpadding fails, just output the decrypted text without unpadding.
    plaintext = pt

print(plaintext)