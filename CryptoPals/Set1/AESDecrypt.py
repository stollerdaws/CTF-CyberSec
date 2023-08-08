from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

def decrypt(ciph, key):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend) # 0 for decrypt
    decryptor = cipher.decryptor()
    plain = decryptor.update(ciph) + decryptor.finalize()
    return plain
'''
key = 'YELLOW SUBMARINE'
keyBytes = bytes(key, 'ascii')
f = open('7.txt', 'r')
ciphertext = base64.b64decode(f.read()); f.close()
print(decrypt(ciphertext, keyBytes))'''