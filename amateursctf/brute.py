import binascii

# The encrypted hex string
encrypted_hex = "610c6115651072014317463d73127613732c73036102653a6217742b701c61086e1a651d742b69075f2f6c0d69075f2c690e681c5f673604650364023944"

# Convert the encrypted hex string to bytes
encrypted_bytes = binascii.unhexlify(encrypted_hex)

# Iterate through the bytes and perform XOR operations
result = ""
last_byte = None
for i in range(len(encrypted_bytes)):
    if i % 2 == 0:
        # Append the byte to the result
        result += chr(encrypted_bytes[i])
    else:
        # XOR the byte with the last appended byte and append the result
        decrypted_byte = encrypted_bytes[i] ^ last_byte
        result += chr(decrypted_byte)
    last_byte = encrypted_bytes[i]

print("Decrypted text:", result)
