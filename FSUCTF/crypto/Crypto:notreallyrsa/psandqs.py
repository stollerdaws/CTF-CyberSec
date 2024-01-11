# given values
p = 3782335750369249076873452958462875461053
q = 9038904185905897571450655864282572131579
e = 65537
n = p * q
et = (p - 1) * (q - 1)
d = pow(e, -1, et)
c = 24369365143578075041744719761042706440623517647517345178446004495680324592679075

# decrypt the ciphertext
decrypted_message_int = pow(c, d, n)

# convert decrypted integer back to bytes
decrypted_message = decrypted_message_int.to_bytes((decrypted_message_int.bit_length() + 7) // 8, 'big')

print(f"Decrypted Message = {decrypted_message}")
