import random
from string import printable
from datetime import datetime, timedelta

# Function to shuffle printable characters with a given seed
def shuffle_printable(seed):
    rand_printable = list(printable)
    random.seed(seed)
    random.shuffle(rand_printable)
    return rand_printable

# Convert timestamp to range of seeds
timestamp_str = "2024-02-21 08:37:16-05:00"
timestamp_format = "%Y-%m-%d %H:%M:%S%z"
target_datetime = datetime.strptime(timestamp_str, timestamp_format)
target_timestamp = target_datetime.timestamp()
shuffed = shuffle_printable(target_timestamp)

def read_ciphertexts(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Read ciphertexts from file
file_name = "cip3"
ciphertexts = read_ciphertexts(file_name)
ciph2 = []
for i in ciphertexts:
    ciph2.append(i[-32:])


mapping = {}
for i, ciphertext in enumerate(ciph2):
    mapping[ciphertext] = shuffed[i]

theboys = [
    '5d4459eec1d2ea2b5551cb7966cbf547',
    '063acd9c86ea3b2fc0464c7d0cb7caa0',
    'e8ba2d31a732ee57df13d1ed2713d413',
    '641bfdc8cc12ad1ca3f31163b12bef14',
    '3fbc591a8bef465777e5a414188e3255',
    'a37d42d159681bc62dbb1076b8c24e8c',
    '850a9009f1e228f3210c129c6bc6db45',
    '6469b2befed662d68f0b770826e65c9e',
    '7eb11b0ed8852fd46970758f9ab2c722',
    'b72a0588e8efdd03963cbd387da67d69',
    'df3707b43e46e75cb2e14bfb40bdd5ec',
    'ea84779dcc775bf688676dd5d05c746e',
    '57f46e7af83542018917eab9ecbfb79b',
    'b72a0588e8efdd03963cbd387da67d69',
    '850a9009f1e228f3210c129c6bc6db45',
    '5003f729cba465f7919950f456df53a9',
]
flag = ''
for i in theboys:
    if i in mapping:
        flag += mapping[i]
print(flag)