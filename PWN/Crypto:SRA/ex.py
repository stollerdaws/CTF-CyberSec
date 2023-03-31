from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes
from pwn import remote
import gmpy2

def calculate_gluttony_and_greed(envy):
    p = 2
    while envy % p != 0:
        p = gmpy2.next_prime(p)
    q = envy // p
    return p+1, q+1

def main():
    io = remote("saturn.picoctf.net", 65418)
    io.recvline()
    anger = int(io.recvuntil('\r'))
    io.recvuntil("envy =")
    envy = int(io.recvuntil('\r'))
    sloth = 65537
    p = gmpy2.next_prime(int(gmpy2.sqrt(envy)))
    while envy % p != 0:
        p = gmpy2.next_prime(p)
    q = envy // p
    # calculate gluttony and greed
    gluttony = max(p, q)
    greed = min(p, q)
    # calculate phi(n) and d
    phi = (gluttony - 1) * (greed - 1)
    d = inverse(sloth, phi)

    # decrypt pride (the flag)
    flag = pow(anger, d, gluttony * greed)
    flag_bytes = long_to_bytes(flag)
    print(flag_bytes)
    # send flag to server
    io.recvuntil(">")
    io.sendline(flag_bytes)

    # receive and print response from server
    response = io.recvline().decode().strip()
    if "picoCTF" in response:
        print(response)
    else:
        print("Failed to get flag")

if __name__ == "__main__":
    main()
