import base64, math, random
from CBC import encryptCBC, decryptCBC, encryptECB, decryptECB
from pkcs7 import pkcs7_pad, pkcs7_unpad
from collections import defaultdict

key = bytes.fromhex('b6b67c04eeb436681ec0070ab0643d23')
b64str = base64.b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
randBytes = bytes([random.randint(0, 255) for i in range(random.randint(5, 10))])

def encryptionOracle(buffer):
    buffer = randBytes + buffer + b64str
    return encryptECB(pkcs7_pad(buffer, 16), key)

def repeated_blocks(buffer, block_length=16):
    reps = defaultdict(lambda: -1)
    for i in range(0, len(buffer), block_length):
        block = bytes(buffer[i:i + block_length])
        reps[block] += 1
    return sum(reps.values())

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

def blockV2(block1):
    base = encryptionOracle(b'a' * (block1 + 24))
    for i in range(0, 24):
        checker = encryptionOracle(b'a' * (i + block1))
        if base[16:32] == checker[16:32]:
            return i - 1
        base = checker

def attack():
    randLength = blockSize()
    realblock = blockV2(randLength)
    print(f'Block size: {realblock}, Rand length: {randLength}')
    input = b'a' * ((realblock + randLength) - 1)
    strSize = findStrSize(encryptionOracle) - realblock
    strRound = math.ceil(strSize/realblock) * realblock
    print(f'String size: {strRound}')
    prefSize = realblock - randLength
    prefRound = math.ceil(prefSize/realblock) * realblock
    # make a dictionary of all possible last bytes
    unknown = bytearray()
    for j in range(strRound - 1, 0, -1):
        d1 = bytearray(b'a' * (j + prefSize))
        c1 = encryptionOracle(d1)[prefRound:strRound + prefRound] # adjust slicing to skip the first block
        for c in range(256):
            d2 = d1[:] + unknown + bytes([c])
            c2 = encryptionOracle(d2)[prefRound:strRound + prefRound] # adjust slicing to skip the first block
            if c1 == c2:
                print(f'Found a match: {chr(c)}')
                unknown += bytes([c])
                break
    return unknown

print(attack())

# only works for blocks of length 8, will get back to this