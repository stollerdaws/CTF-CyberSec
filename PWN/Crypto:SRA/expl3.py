from pwn import *
from Crypto.Util.number import inverse, long_to_bytes
import gmpy2
io = remote("saturn.picoctf.net", 61536)
io.recvuntil("anger = ")
anger = int(io.recvline().strip())
io.recvuntil("envy = ")
envy = int(io.recvline().strip())
sloth = 65537
# factorize the modulus
p = 2


lust = sloth * inverse(envy, sloth) - 1

if lust.bit_length() < 200:
    factors = dict(gmpy2.factor(lust))
    gluttony, greed = factors.keys()
else:
    gluttony = gmpy2ecm.factor(lust, B1=100000, verbose=False)[0]
    greed = lust // gluttony

phi = (gluttony - 1) * (greed - 1)

# calculate private key
d = inverse(sloth, phi)

# decrypt pride
pride = pow(anger, d, gluttony * greed)
prideb = long_to_bytes(pride.decode())
print(prideb)
# send decrypted value to server
io.recvuntil(">")
io.sendline(prideb)

# receive and print response from server
response = io.recvline()
print(response)
