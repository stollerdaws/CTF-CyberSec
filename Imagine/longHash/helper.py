from Crypto.Util.number import long_to_bytes, bytes_to_long, isPrime
from hashlib import sha256


def sign(m):
    return sha256(m).hexdigest()

f = int(input("Enter message to sign: "))
f = long_to_bytes(f)
print(f)
g = f + b'admin'
print(g)
h = bytes_to_long(g)
print(h)
sig = sign(long_to_bytes(h))
print(sig)
