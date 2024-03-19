import json
import base64
import random, math
from Crypto.Util.number import bytes_to_long, long_to_bytes, isPrime
import hashlib
from Crypto.Util.number import bytes_to_long, isPrime

# Replicate the hash_string_sha256 function
def hash_string_sha256(message):
    message_bytes = message.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(message_bytes)
    hashed_message = sha256_hash.digest()
    return int.from_bytes(hashed_message, byteorder='big')

# Replicate the generate_signature function
def generate_signature(message, private_key):
    n, d = private_key
    hashed_message = hash_string_sha256(message)
    signature = pow(hashed_message, d, n)
    return signature

# Replicate the generate_key function
def generate_key(username):
    length = lambda x: len(bin(x)[2:])
    s = bytes_to_long(username.encode())
    random.seed(s)
    e = 0x1001
    phi = 0
    while math.gcd(phi, e) != 1:
        n = 1
        factors = []
        while length(n) < 2048:
            temp_n = random.getrandbits(48)
            if isPrime(temp_n):
                n *= temp_n
                factors.append(temp_n)
        phi = 1
        for f in factors:
            phi *= (f - 1)
    d = pow(e, -1, phi)
    print(f"Generated key for {username}: n={n}, e={e}, d={d}")
    return (n, e), (n, d)

# Add a function to verify the signature
def verify_signature(message, public_key, signature):
    n, e = public_key
    hashed_message = hash_string_sha256(message)
    recovered_hash = pow(signature, e, n)
    return hashed_message == recovered_hash

# Username to exploit
username = "allen"

# Generate the public/private key pair
public_key, private_key = generate_key(username)

# Construct the message with the subscription status set to True
message = str({username: [True]})
encoded_message = base64.b64encode(message.encode()).decode()

# Generate the signature
signature = generate_signature(message, private_key)

# Verify the signature locally
if verify_signature(message, public_key, signature):
    print("Signature is valid.")
else:
    print("Signature is invalid.")

# Construct the URL with the forged signature and message
url = f"http://localhost:5000/news?token={signature}&message={encoded_message}"

print(f"URL to access the news page as a subscribed user: {url}")
