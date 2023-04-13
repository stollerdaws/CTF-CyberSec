import string
# THis is a brute force script to decrypt this flag
encrypted_flag = "huL{SEp^H6?!"

def reverse_xor(c1, c2):
    return chr(ord(c1) ^ ord(c2))

def brute_force(seed, encrypted_flag):
    flag_len = len(encrypted_flag)
    generated_array = []

    for i in range(flag_len):
        value = (i * 7 + seed) % 126
        generated_array.append(chr(value))

    recovered_flag = ""
    for i in range(flag_len):
        recovered_flag += reverse_xor(encrypted_flag[i], generated_array[i])
    print(recovered_flag)
    if recovered_flag == 'my_arm_hurts':
        return recovered_flag
for seed in range(126):
    flag = brute_force(seed, encrypted_flag)
    if flag is not None:
        print(f"Recovered flag: {flag}")
        break
