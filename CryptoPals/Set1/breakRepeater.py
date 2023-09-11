import binascii
import base64
from SingleByteXOR import Brutus
from repeatKeyXOR import XORDecode
# Function to calculate the bit difference between = length strings
def hamDist(bytes1, bytes2):
    if len(bytes1) != len(bytes2):
        raise ValueError("Error the input strings must have matching length")
    # Iterate bit by bit checking the difference
    hammingDist = sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(bytes1, bytes2))
    return hammingDist
# Double it to increase the accuracy of the Hamming calc
def quadHam(byte_array, n):
    if len(byte_array) < 4 * n:
        raise ValueError("The input string must be at least 4 times the block size")
    
    # Slice the byte array into 4 blocks
    blocks = [byte_array[i:i+n] for i in range(0, 4 * n, n)]
    # Calculate the average Hamming distance between all pairs of blocks
    total_distance = 0
    num_pairs = 0
    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            total_distance += hamDist(blocks[i], blocks[j])
            num_pairs += 1
    return total_distance / num_pairs

'''f = open('9.txt', 'r')
base64ciph = f.read(); f.close()
#decode the base64 string to bytes
decoded_bytes = base64.b64decode(base64ciph)
# Turn the bytes to a hex string'''
hexStr = '89cb5f6de8a783e9629a2b5e77eb68fa89e5cbeb617be6dab1eeb8f9c85aaec7adfa48a775afacb9c92c'
decoded_bytes = binascii.unhexlify(hexStr)
# Iterate over possible key lengths and determine which is most likely
mindist = 150
bestlen = 0
for guessed_length in range(1, 6):
    currentHamDist = quadHam(decoded_bytes, guessed_length) / guessed_length
    if currentHamDist < mindist:
        mindist = currentHamDist
        bestlen = guessed_length
# Found our match        
print(f'Hamming distances caluclated, key is probably {bestlen} bytes\n')
# split ciphertext in to blocks of size len(key_length)
blocked = [bytearray(decoded_bytes[i:i+bestlen]) for i in range(0, len(decoded_bytes), bestlen)]
# create a first block of every first byte, second of every second byte and so on
# This is because then each of the bytes in each block should be 
# Xored with the same byte given the key length, so check all bytes
# which will be Xored with that byte of the key at once
transposedBlocks = [bytearray() for _ in range(bestlen)]
# Create string to store calculated key
keyGuess = ''
for block in blocked:
    for i in range(bestlen):
        if i < len(block):
            transposedBlocks[i].append(block[i])
for block in transposedBlocks:
    #Use single byte brute force to find best key for all key[index]
    key, plain, score = Brutus(binascii.hexlify(block).decode())
    if key is not None:
        keyGuess += chr(key)
print(f'Calculated the following key: {keyGuess}\n')

plaintext = XORDecode(hexStr, keyGuess)
words = plaintext.split()
neater = ''.join([word + ' ' for word in words])
print(neater)