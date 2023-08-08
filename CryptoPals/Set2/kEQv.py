from CBC import encryptECB, decryptECB
from pkcs7 import pkcs7_pad, pkcs7_unpad
import math
key = b'YELLOW SUBMARINE'
def blockSize(encryptionOracle):
    #find block size
    block_size = 0
    base = encryptionOracle(b'')
    for i in range(2, 24):
        checker = encryptionOracle(b'a' * i)
        if base[0:16] == checker[0:16]:
            return i - 1
        base = checker
    return -1

def profile_for_bytes(input_bytes=b''):
    email = input_bytes.decode('ascii')
    return profile_for(email)

def parse(string):
    obj = {}
    for kv in string.split("&"):
        kv = kv.split("=")
        obj[kv[0]] = kv[1]
    return obj

def profile_for(email='fpp@bpp.cpm'):
    email = email.replace('&', '').replace('=', '')
    prof =  f'email={email}&uid=10&role=user'
    return encryptECB(pkcs7_pad(bytes(prof, 'ascii'), 16), key)


   
def decryptProfile(prof):
    return parse(pkcs7_unpad(decryptECB(prof, key)).decode('ascii'))

print(profile_for('foo@bar.com'))
print(decryptProfile(profile_for('foo@bar.com')))
print(blockSize(profile_for_bytes))

def attack():
    # we + 6 because of email= at the beginning of the string
    block_size = blockSize(profile_for_bytes) + 6
    # Now we want to the string email=zz&uid=10&role= to be block alighned
    # with no email it is 19 bytes long so we need 17 more
    mandatory = b'email=&uid=10&role='
    remaining = math.ceil(len(mandatory)/block_size) * block_size
    length = remaining - len(mandatory)
    email = b'a' * length
    #craftPref = profile_for(email.decode('ascii'))[0:block_size]
    craftPref = profile_for('aaaaaaaaaaaaa')[0:block_size * 2]
    print(craftPref)
    # now i want to create a ciph with 3 blocks where || means block aligned concat
    # email=zz&uid=10&role=||admin||properly padded end
    mandatory = b'email='
    remaining = math.ceil(len(mandatory)/block_size) * block_size
    length = remaining - len(mandatory)
    craftCiph = b'a' * length
    craftCiph += pkcs7_pad(b'admin', block_size)
    craftPost = profile_for(craftCiph.decode('ascii'))[remaining:remaining + block_size]
    Craft = craftPref + craftPost
    return decryptProfile(Craft)

print(attack())