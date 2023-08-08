import base64, math
from CBC import encryptCBC, decryptCBC, encryptECB, decryptECB
from pkcs7 import pkcs7_pad, pkcs7_unpad
from collections import defaultdict

b64str = base64.b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')

key = bytes.fromhex('b6b67c04eeb436681ec0070ab0643d23')

def repeated_blocks(buffer, block_length=16):
    reps = defaultdict(lambda: -1)
    for i in range(0, len(buffer), block_length):
        block = bytes(buffer[i:i + block_length])
        reps[block] += 1
    return sum(reps.values())

def encryptionOracle(buffer):
    buffer = buffer + b64str
    return encryptECB(pkcs7_pad(buffer, 16), key)

def detect():
    checker = encryptionOracle(b'aaaa' * 16)
    i = repeated_blocks(checker, 16)
    if i > 0:
        return "ECB"
    else:
        return "CBC"
    
def findStrSize(oracle):
    ciphLen = len(oracle(b''))
    i = 1
    while True:
        ciph = oracle(b'a' * i)
        if len(ciph) != ciphLen:
            return len(ciph) - 1
        i += 1
    
def blockSize():
    #find block size
    block_size = 0
    base = encryptionOracle(b'')
    for i in range(1, 24):
        checker = encryptionOracle(b'a' * i)
        if base[0:16] == checker[0:16]:
            block_size = i - 1
            break
        base = checker
    return block_size

def attack():
    if detect() == "ECB":
        block_size = blockSize()
        # craft an input block that is exactly 1 byte short
        input = b'a' * (block_size - 1)
        # find the string size
        strSize = findStrSize(encryptionOracle)
        strRound = math.ceil(strSize/block_size) * block_size
        print(f'String size: {strRound}')
        # make a dictionary of all possible last bytes
        unknown = bytearray()
        for j in range(strRound - 1, 0, -1):
            d1 = bytearray(b'a' * j)
            c1 = encryptionOracle(d1)[:strRound]
            for c in range(256):
                #print(f'Checking {bytes(i)}')
                d2 = d1[:] + unknown + bytes([c])
                c2 = encryptionOracle(d2)[:strRound]
                if c1 == c2:
                    print(f'Found a match: {chr(c)}')
                    unknown += bytes([c])
                    break
        return unknown

        
print(attack())