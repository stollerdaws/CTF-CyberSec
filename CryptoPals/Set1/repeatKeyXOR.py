import binascii
import string

def XOREncode(plain, key):
    plainBytes = bytes(plain, 'ascii')
    keyhex = (bytes(key, 'ascii'))
    ciphertext = bytearray(b ^ keyhex[i % len(keyhex)] for i, b in enumerate(plainBytes))
    return binascii.hexlify(ciphertext).decode()

def XORDecode(ciph, key):
    ciphBytes = binascii.unhexlify(ciph)
    keyBytes = bytes(key, 'ascii')
    plainBytes = bytearray(b ^ keyBytes[i % len(keyBytes)] for i, b in enumerate(ciphBytes))
    return plainBytes.decode('ascii')
'''
plaintext = input("Enter a plaintext to be encrypted\n")
key = input("Enter a key to XOR by\n")
ciph = XOR(plaintext, key)
print(ciph)'''