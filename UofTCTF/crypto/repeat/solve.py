# Encrypted flag in hexadecimal
encrypted_flag_hex = "982a9290d6d4bf88957586bbdcda8681de33c796c691bb9fde1a83d582c886988375838aead0e8c7dc2bc3d7cd97a4"
encrypted_flag_bytes = bytes.fromhex(encrypted_flag_hex)

# Known plaintext
known_plaintext = "uoftctf{"

# XOR the known plaintext with the encrypted flag to get the key bytes
key_bytes = [encrypted_flag_bytes[i] ^ ord(known_plaintext[i]) for i in range(len(known_plaintext))]

# Repeat the key to match the length of the encrypted flag
full_key = (key_bytes * (len(encrypted_flag_bytes) // len(key_bytes) + 1))[:len(encrypted_flag_bytes)]

# Decrypt the flag
decrypted_flag_bytes = bytes([encrypted_flag_bytes[i] ^ full_key[i] for i in range(len(encrypted_flag_bytes))])
decrypted_flag = decrypted_flag_bytes.decode()

print(decrypted_flag)
