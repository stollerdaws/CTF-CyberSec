from CBC import encryptCBC, decryptCBC, encryptECB, decryptECB
from pkcs7 import pkcs7_pad, pkcs7_unpad

key = bytes.fromhex('b6b67c04eeb436681ec0070ab0643d23')
iv = b'YELLOW SUBMARINE'

def func1(input):
    input = input.replace(';','%3b').replace('=','%3d')
    pender0 = 'comment1=cooking%20MCs;userdata='
    pender1 = ';comment2=%20like%20a%20pound%20of%20bacon'
    return encryptCBC(pkcs7_pad(bytes(pender0 + input + pender1, 'ascii'), 16), key, iv)

def func2(ciph):
    plain = decryptCBC(ciph, key, iv)
    if b';admin=true;' in plain:
        return True
    return False

def attack():
    b1 = 'a' * 16
    b2 = 'XadminXtrueX'
    plain = b1 + b2
    ciph = func1(plain)
    # 'comment1=cooking%20MCs;userdata=' is 32 bytes long
    offset = 32
    # change ciph[offset] to X so the second will be ;
    ciph[offset] = ciph[offset] ^ (ord('X') ^ ord(';'))
    # and so on for = and the other ;
    ciph[offset + 6] = ciph[offset + 6] ^ (ord('X') ^ ord('='))
    ciph[offset + 11] = ciph[offset + 11] ^ (ord('X') ^ ord(';'))
    return func2(ciph)

print(attack())