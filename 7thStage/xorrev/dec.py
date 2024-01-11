def generate_key_sequence(seed, length):
    """
    Generates a key sequence for XOR encryption/decryption.
    
    :param seed: The initial seed for key generation.
    :param length: The length of the data to encrypt/decrypt.
    :return: A list containing the key sequence.
    """
    key_sequence = []
    for _ in range(length):
        key_sequence.append(seed & 0xff)  # Append the least significant byte
        # Right shift the seed and conditionally XOR with 0x110
        lsb = seed & 1
        seed >>= 1
        if lsb:
            seed ^= 0x110
    return key_sequence

def decrypt_xor(ciphertext, key_sequence):
    """
    Decrypts the XOR encrypted data using the given key sequence.
    
    :param ciphertext: The encrypted data as a list of byte values.
    :param key_sequence: The key sequence for decryption.
    :return: The decrypted data as a list of byte values.
    """
    return [byte ^ key for byte, key in zip(ciphertext, key_sequence)]

# Example usage
seed = 22887
with open('output.txt', 'rb') as f:
    ciphertext = f.read()
length = len(ciphertext)

# Generate the key sequence
key_sequence = generate_key_sequence(seed, length)

# Decrypt the ciphertext
plaintext = decrypt_xor(ciphertext, key_sequence)
print(''.join(chr(x) for x in plaintext))
