def xor_decrypt(ciphertext, key):
    plaintext = []
    for i in range(len(ciphertext)):
        plaintext.append(chr(ciphertext[i] ^ ord(key[i % len(key)])))
    return ''.join(plaintext)

hex_string = "0005120f1d111c1a3900003712011637080c0437070c0015"
ciphertext = bytearray.fromhex(hex_string)
key = "fish"

plaintext = xor_decrypt(ciphertext, key)
print(plaintext)
