from Set2.CBC import encryptCBC, decryptCBC
import random, base64

block_size = 16
strings = [
    'MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=',
    'MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=',
    'MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==',
    'MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==',
    'MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl',
    'MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==',
    'MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==',
    'MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=',
    'MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=',
    'MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93'
]

def genKey():
    return bytes([random.randint(0, 255) for i in range(16)])

key = genKey()

def pkcs7_pad(data, block_size): # up to pkcs7 standard
    padding_length = block_size - (len(data) % block_size)
    padding = bytes([padding_length]) * padding_length
    turner = data + padding
    return turner

def encryptionOracle():
    iv = genKey()
    buffer = pkcs7_pad(base64.b64decode(random.choice(strings)), block_size)
    return encryptCBC(buffer, key, iv), iv

def func2(ciph, iv):
    ciph = decryptCBC(ciph, key, iv)
    pad_length = ciph[-1] # The value of the last byte gives us the padding length

    # Check that the padding length is valid
    if pad_length > len(ciph) or pad_length <= 0:
        return False

    # Check the validity of the padding
    padding = ciph[-pad_length:]
    if not all(char == pad_length for char in padding):
        return False

    return True

def attack():
    ciph, iv = encryptionOracle()
    bytearray(iv)[-1] = 100
    print(func2(ciph, iv))

    

attack()
    