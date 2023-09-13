from Crypto.Util.number import long_to_bytes, getPrime, isPrime
from hashlib import sha256

flag = open("flag.txt").read()

def sign(m):
    return sha256(m).hexdigest()

p = getPrime(256)
print(long_to_bytes(p))

def auth(sig, msg):
    #if isPrime(msg):
    #    return "No no no, composites only."
    msg = long_to_bytes(msg)
    print(msg, long_to_bytes(p))

    if sig != sign(msg):
        return "Authentication Failed."
    if msg.startswith(long_to_bytes(p)):
        return f"Welcome admin! Flag is {flag}"
    return "Authentication Successful!"

def menu():
    print("1. Authenticate")
    print("2. Get p")
    print("3. Show source")
    print("4. Quit")
    x = int(input(">>> "))
    if x == 1:
        m = int(input("Enter message as long: "))
        sig = str(input("Enter string as hexstr: "))
        print(auth(sig,m))
    elif x == 2:
        print("The prime is", p)
        print("The signature is", sign(long_to_bytes(p)))
    elif x == 3:
        print("="*80)
        print(open(__file__).read())
        print("="*80)
    elif x == 4:
        exit()

if __name__ == "__main__":
    while True:
        menu()
