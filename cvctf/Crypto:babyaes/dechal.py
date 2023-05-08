import itertools
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad

iv = bytes.fromhex('1df49bc50bc2432bd336b4609f2104f7')
ct = bytes.fromhex('a40c6502436e3a21dd63c1553e4816967a75dfc0c7b90328f00af93f0094ed62')
BS = 16

def brute_force_key():
    for key1 in range(256):
        for key2 in range(256):
            key = pad(bytes([key1, key2]), BS)
            print(f'\n Key: {key}')
            cipher = AES.new(key, AES.MODE_CBC, iv)

            try:
                pt = unpad(cipher.decrypt(ct), BS)
                if pt.startswith(b"cvctf{"):
                    return pt
            except ValueError:
                pass
    return None

decrypted_flag = brute_force_key()

if decrypted_flag is not None:
    print("Decrypted flag:", decrypted_flag)
else:
    print("No flag found.")
