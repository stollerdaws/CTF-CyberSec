from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long
import hashlib

# Establish connection
io = remote('group-projection.chal.uiuc.tf', 1337)

# Skip the banner text
io.recvuntil("Public:\n")

k = 2

# Extract g, p, and A
g = int(io.recvline().decode().strip().split('=')[1].strip())
p = int(io.recvline().decode().strip().split('=')[1].strip())
A = int(io.recvline().decode().strip().split('=')[1].strip())


# Skip the eavesdropped message text
io.recvuntil("Choose k = ")
io.sendline(b'2')

# Extract c1 and c2
io.recvuntil(';)\n')
modulus = int(io.recvline().decode().strip().split('=')[1].strip())

Ak = pow(A, k, p)

# For each possible value of B in the small subgroup
for b in [1, p-1]:

    # Calculate S
    S = pow(Ak, b, p)
    
    # Generate key from S
    key = hashlib.md5(long_to_bytes(S)).digest()
    
    # Create AES cipher with the key
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Convert c from integer to bytes
    c_bytes = long_to_bytes(c)
    
    # Attempt to decrypt c
    try:
        plaintext = unpad(cipher.decrypt(c_bytes), 16)
        print("Possible plaintext:", plaintext)
    except:
        # If padding is incorrect, ignore and continue with the next value
        pass
