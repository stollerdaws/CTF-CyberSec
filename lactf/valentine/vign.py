def char_to_num(char):
    """Convert character to number (0-25), ignoring case."""
    return ord(char.upper()) - ord('A')

def num_to_char(num):
    """Convert number (0-25) back to uppercase character."""
    return chr(num + ord('A'))

def extract_key_segment(plaintext, ciphertext):
    """Extract the key segment from the known plaintext and its corresponding ciphertext."""
    key_segment = ''
    for p_char, c_char in zip(plaintext, ciphertext):
        if p_char.isalpha() and c_char.isalpha():
            p_num = char_to_num(p_char)
            c_num = char_to_num(c_char)
            k_num = (c_num - p_num) % 26
            key_segment += num_to_char(k_num)
    return key_segment

def extend_key(key_segment, key_length):
    """Extend the key segment to the specified key length."""
    extended_key = key_segment * (key_length // len(key_segment)) + key_segment[:key_length % len(key_segment)]
    return extended_key

def decrypt_vigenere(ciphertext, key):
    """Decrypt the ciphertext using the Vigenère cipher and the given key."""
    plaintext = ''
    key_index = 0
    for c in ciphertext:
        if c.isalpha():
            c_num = char_to_num(c)
            k_num = char_to_num(key[key_index % len(key)])
            p_num = (c_num - k_num) % 26
            plaintext += num_to_char(p_num)
            key_index += 1
        else:
            plaintext += c
    return plaintext

# Load the ciphertext and known plaintext
ciphertext_path = "ct.txt"
plaintext_path = "intro.txt"
with open(ciphertext_path, 'r') as file:
    ciphertext = file.read().strip()
with open(plaintext_path, 'r') as file:
    known_plaintext = file.read().strip()

# Extract the key segment using the known plaintext and corresponding ciphertext part
key_segment = extract_key_segment(known_plaintext, ciphertext)

# Extend the key to the specified length (161 characters in this case)
key_length = 161
extended_key = extend_key(key_segment, key_length)

# Decrypt the ciphertext with the extended key
decrypted_plaintext = decrypt_vigenere(ciphertext, extended_key)

# Output the key segment, extended key, and the decrypted plaintext
print(f"Partial Key: {key_segment}")
print(f"Extended Key: {extended_key}... [Total Length: {len(extended_key)}]")
print("Decrypted Plaintext:", decrypted_plaintext, "...")


