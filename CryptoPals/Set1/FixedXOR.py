import binascii

def fXOR(s1, s2):
    ciphertext = bytearray()
    b1 = binascii.unhexlify(s1)
    b2 = binascii.unhexlify(s2)
    if(len(s1) != len(s2)):
        raise ValueError("Input strings must be the same length")
    
    for a, b in zip(b1, b2):
        ciphertext.append(a ^ b)
    hex_result = binascii.hexlify(ciphertext).decode()    
    return hex_result

# Always performing operations on raw bytes
input1 = input("Enter the first hex string\n")

input2 = input("Enter second hex string\n")
bytes2 = binascii.unhexlify(input2)

ciph = fXOR(input1, input2)

print(f'The XOR encoded string is:\n{ciph}')