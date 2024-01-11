import codecs

# Arrays containing parts of the flag
f = ['r3st', '4s_a', 'b3_c', 'm4tt', 'l3t_']
l = ['4ll0', '30_1', '7t3_', 'jkin', 'p1ck']
a = ['5_th', '3_4n', '1t_1', '00p5', '1n_1']
g = ['p1_7', '3_w0', 't0g3', '00_k', 'n0th']
s = ['ear5', 'k!1!', '1n6!', '33p5', 'rd_!']

# Indexes based on correct timing
indexes = [3, 1, 0, 1, 4]

# Constructing the flag
flag = ''
for index, array in zip(indexes, [f, l, a, g, s]):
    flag += array[index]
flag = 'upgs{' + flag + '}'

# Decoding the flag using ROT13
decoded_flag = codecs.encode(flag, 'rot13')
decoded_flag
