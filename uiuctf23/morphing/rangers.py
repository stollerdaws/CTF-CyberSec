from pwn import *
from Crypto.Util.number import inverse, long_to_bytes

# Establish connection
io = remote('morphing.chal.uiuc.tf', 1337)

# Skip the banner text
io.recvuntil("Public:\n")


# Extract g, p, and A
g = int(io.recvline().decode().strip().split('=')[1].strip())
p = int(io.recvline().decode().strip().split('=')[1].strip())
A = int(io.recvline().decode().strip().split('=')[1].strip())


# Skip the eavesdropped message text
io.recvuntil("Eavesdropped Message:\n")

# Extract c1 and c2
c1 = int(io.recvline().decode().strip().split('=')[1].strip())
c2 = int(io.recvline().decode().strip().split('=')[1].strip())

# Our chosen plaintext is 2
# We can choose any value for k, so let's choose k = 2 as well
k = 2

# Encrypt our chosen plaintext, calculating c1_ and c2_
c1_ = pow(g, k, p)
c2_ = (2 * pow(A, k, p)) % p

# Send our ciphertext to the oracle
io.recvuntil("Give A Ciphertext (c1_, c2_) to the Oracle:\n")
io.sendline(str(c1_))
io.sendline(str(c2_))

# Receive the decrypted message
io.recvuntil("Decryption of You-Know-What:\n")
m = int(io.recvline().decode().strip().split('=')[1].strip())

# Calculate the original message
flag = m // 2

# Convert the integer to bytes
flag_bytes = long_to_bytes(flag)

print(flag_bytes)
