from Crypto.Util.number import bytes_to_long
from string import ascii_letters, digits
from itertools import product
from random import choice

envy = 15964117751541664751911609292561171605817137065245052470015254106791836470273
sloth = 65537
anger = 1092785386628944725257603255850106355694639913396799217355695525145936959416

# Generate all possible values of `pride`
charset = ascii_letters + digits
pride_length = 16
pride_candidates = product(charset, repeat=pride_length)

# Try each candidate and check if the result matches the given ciphertext
for pride in pride_candidates:
    pride_str = "".join(pride)
    pride_num = bytes_to_long(pride_str.encode())
    ciphertext = pow(pride_num, sloth, envy)
    print(pride_str)
    if ciphertext == anger:
        print(f"Found the correct value of `pride`: {pride_str}")
        break
else:
    print("Could not find the correct value of `pride`")
