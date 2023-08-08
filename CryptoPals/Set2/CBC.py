from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
from Crypto.Cipher import AES

def pkcs7_pad(data, block_size): # up to pkcs7 standard
    padding_length = block_size - (len(data) % block_size)
    padding = bytes([padding_length]) * padding_length
    turner = data + padding
    return turner

def pkcs7_unpad(data):
    padding_length = data[-1]
    if padding_length > len(data):
        raise ValueError("Invalid padding length")
    
    for i in range(1, padding_length + 1):
        if data[-i] != padding_length:
            raise ValueError("Invalid padding bytes")
    #print(f'\nUnpadded Block: {data[:-padding_length]}')
    return data[:-padding_length]

def encryptECB(buffer, key):
    obj = AES.new(key, AES.MODE_ECB)
    return bytearray(obj.encrypt(bytes(buffer)))

def decryptECB(buffer, key):
    obj = AES.new(key, AES.MODE_ECB)
    return bytearray(obj.decrypt(bytes(buffer)))

def encryptCBC(plain, key, iv):
    plainBlocks = pkcs7_pad(plain, 16)
    ciph = bytearray(len(plainBlocks))
    prev = iv
    for i in range(0, len(plainBlocks), 16):
        block = plainBlocks[i:i+16]
        block = bytes([block[j] ^ prev[j] for j in range(len(block))])
        ciph[i:i+16] = encryptECB(block, key)
        prev = ciph[i:i+16]
    return ciph

def decryptCBC(ciph, key, iv):
    ciphBlocks = ciph
    plain = bytearray(len(ciphBlocks))
    prev = iv
    for i in range(0, len(ciphBlocks), 16):
        block = ciphBlocks[i:i+16]
        plain[i:i+16] = decryptECB(block, key)
        plain[i:i+16] = bytes([plain[i+j] ^ prev[j] for j in range(16)])
        prev = block
    return pkcs7_unpad(plain)
'''
key = 'YELLOW SUBMARINE'
keyBytes = bytes(key, 'ascii')
iv = bytes([0 for i in range(16)])
plain = input('Enter plaintext: ')
plainBytes = bytes(plain, 'ascii')
ciph = encryptCBC(plain, keyBytes, iv)
print(ciph)
print(decryptCBC(ciph, keyBytes, iv))

'''