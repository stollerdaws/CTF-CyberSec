from Crypto.Util.number import *

with open('message.txt', 'r') as f:
    nums = f.read().split()
chars = []
'''Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.'''
def trans(val):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
    return alphabet[val - 1]

for i, num in enumerate(nums):
    nums[i] = int(num)
    nums[i] = inverse(nums[i] % 41, 41)
    chars.append(trans(nums[i]))

print(''.join(chars))