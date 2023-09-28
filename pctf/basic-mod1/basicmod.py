with open('message.txt', 'r') as f:
    nums = f.read().split()
chars = []
'''Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.'''
def trans(val):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
    return alphabet[val]

for i, num in enumerate(nums):
    nums[i] = int(num)
    nums[i] = nums[i] % 37
    chars.append(trans(nums[i]))

print(''.join(chars))
