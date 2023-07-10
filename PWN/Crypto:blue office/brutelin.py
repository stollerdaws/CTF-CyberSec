import binascii

def reseed(s):
	return s * 214013 + 2531011

def decrypt(s, enc):
    assert s <= 2**32
    c, d = 0, s
    dec, l = b'', len(enc)
    while c < l:
        d = reseed(d)
        dec += (enc[c] ^ ((d >> 16) & 0xff)).to_bytes(1, 'big')
        c += 1
    return dec

def decrypt_initial(s, enc):
    c, d = 0, s
    dec, l = b'', len(enc)
    while c < l:
        d = reseed(d)
        dec += (enc[c] ^ ((d >> 16) & 0xff)).to_bytes(1, 'big')
        c += 1
    return dec

# Convert the given output to bytes.
enc_given = binascii.unhexlify('b0cb631639f8a5ab20ff7385926383f89a71bbc4ed2d57142e05f39d434fce')

# Known beginning of the flag
known_flag_start = b'CCTF{'

# Iterate through all possible 32-bit seed values
for possible_seed in range(2**32):
    # Only decrypt the first 5 characters
    decrypted_start = decrypt_initial(possible_seed, enc_given[:5])
    if decrypted_start == known_flag_start:
        print(f"Found the seed: {possible_seed}")
        seed = possible_seed
        break
if seed:
     # Decrypt the message
    decrypted_message = decrypt(seed, enc_given)

    # Print out the decrypted message.
    print(f'The decrypted flag is: {decrypted_message.decode()}')
