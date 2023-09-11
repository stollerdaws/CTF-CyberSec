import hashlib

def blake2s_bruteforce(target_hash):
    # Define the alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/\\\" "
    
    # Iterate over each character
    for char in alphabet:
        hashed_value = hashlib.blake2s(char.encode()).hexdigest()
        
        if hashed_value == target_hash:
            return char
    return None

# Provided hash for BLAKE2s
hash_blake2s = "5abf6b1a79dee98ea32a98195c61a667c29a3674e79c82e43f0d19b0efa4b6f7"

matched_char = blake2s_bruteforce(hash_blake2s)

if matched_char:
    print(f"Found match for BLAKE2s: {matched_char}")
else:
    print("Could not find match for BLAKE2s")
