import random
from CBC import encryptCBC, decryptCBC, encryptECB, decryptECB
from pkcs7 import pkcs7_pad, pkcs7_unpad
import sys
sys.path.insert(1, '../Set1')
from detectECB import repeated_blocks
# write a function to generate 16 random bytes
def genKey():
    return bytes([random.randint(0, 255) for i in range(16)])

#write a function that enrypts data under an unknown key (generate a key and encrypt)
def encryptionOracle(buffer):
    key = genKey()
    iv = genKey()
    randomBytes = bytes([random.randint(0, 255) for i in range(random.randint(5, 10))])
    buffer = randomBytes + buffer + randomBytes
    choice = random.randint(0, 1)
    if choice == 0:
        #print('ECB')
        return encryptECB(pkcs7_pad(buffer, 16), key)
    else:
        #print('CBC')
        return encryptCBC(buffer, key, iv)
    

def detect(buffer):
    checker = encryptionOracle(buffer)
    print(f'Checker: {checker.hex()}')
    i = repeated_blocks(checker, 16)
    if i > 0:
        return "ECB"
    else:
        return "CBC"

boop = input('Enter plaintext: ')
print(detect(bytes(boop, 'ascii')))