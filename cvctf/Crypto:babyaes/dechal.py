import itertools
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad

iv = bytes.fromhex('189b39ae37214d6c2abed9affefbcb0b')
ct = bytes.fromhex('87b3a1774c53d3c32b1925249cc77e4767951cf690e9e65cd5c9b31d2a95340f')
BS = 16

def brute_force_key():
    for key1 in range(256):
        for key2 in range(256):
            key = pad(bytes([key1, key2]), BS)
            print(f'\n Key: {key}')
            cipher = AES.new(key, AES.MODE_CBC, iv)

            try:
                pt = unpad(cipher.decrypt(ct), BS)
                if pt.startswith(b"FSUCTF{"):
                    return pt
            except ValueError:
                pass
    return None

decrypted_flag = brute_force_key()

if decrypted_flag is not None:
    print("Decrypted flag:", decrypted_flag)
else:
    print("No flag found.")
