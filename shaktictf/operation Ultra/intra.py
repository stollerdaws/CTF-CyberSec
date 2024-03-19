import base64

def reverse_func_2(unk_str2):
    flag_len = len(unk_str2)
    unk_str0 = [''] * flag_len
    j = 0
    
    for i in range(0, flag_len, 4):
        unk_str0[i] = unk_str2[j]
        unk_str0[i + 1] = unk_str2[j + 1]
        j += 2
    
    for i in range(2, flag_len, 4):
        unk_str0[i] = unk_str2[j]
        unk_str0[i + 1] = unk_str2[j + 1]
        j += 2
    
    return ''.join(unk_str0)

def reverse_func_1(unk_str1, unk_str):
    flag_len = len(unk_str1)
    unk_str0 = bytearray(flag_len)
    
    for i in range(flag_len):
        unk_str0[i] = ord(unk_str1[i]) ^ ord(unk_str[i % len(unk_str)])
    
    return unk_str0.decode('utf-8')

unk_str = base64.b64decode("U2hhZG93MjAyNA==".encode('ascii')).decode('ascii')
unk_arr0 = [32, 0, 27, 30, 84, 79, 86, 22, 97, 100, 63, 95, 60, 34, 1, 71, 0, 15, 81, 68, 6, 4, 91, 40, 87, 0, 9, 59, 81, 83, 102, 21]
unk_str2 = ''.join([chr(x) for x in unk_arr0])

# Reverse the transformations
rev_func_2 = reverse_func_2(unk_str2)
rev_func_1 = reverse_func_1(rev_func_2, unk_str)

print(f"Recovered flag: {rev_func_1}")
