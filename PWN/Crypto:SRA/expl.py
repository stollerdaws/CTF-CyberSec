from pwn import *
from Crypto.Util.number import inverse, long_to_bytes
from string import ascii_letters, digits
from random import choice

sloth = 65537
io = remote("saturn.picoctf.net", 60417)

io.recvuntil("anger =")
anger = int(io.recvline().strip())
print(anger)

io.recvuntil("envy =")
envy = int(io.recvline().strip())
print(envy)

io.recvuntil('>')
#factorize the modulus
phi = (envy * 65537 - 1) // 2
# calculate private key
#totient = (gluttony - 1) * (greed - 1)
envinv = inverse(sloth, phi)
gluttony = (envinv * phi) + 1
greed = envy // gluttony
tot = (gluttony - 1) * (greed - 1)

private_key = inverse(sloth, tot)

pride = pow(anger, private_key, envy * greed)
prideb = long_to_bytes(pride)

print(pride)
#io.recvuntil(">")
io.sendline(prideb)
while(1):
    dat = io.recvline().strip()
    print(dat)
    
