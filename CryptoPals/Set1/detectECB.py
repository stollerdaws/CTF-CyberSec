from AESDecrypt import decrypt
from collections import Counter, defaultdict
#with open('8.txt', 'r') as f:
#    ciphs = f.readlines()

def repeated_blocks(buffer, block_length=16):
    reps = defaultdict(lambda: -1)
    for i in range(0, len(buffer), block_length):
        block = bytes(buffer[i:i + block_length])
        reps[block] += 1
    return sum(reps.values())

def detect_ECB(ciphs, block_size=16):
    mostRepeats = 0
    ECBBoiii = None
    ECBindex = None
    for i, ciph in enumerate(ciphs):
        ciph_bytes = bytes.fromhex(ciph.strip())
        blocks = [ciph_bytes[i:i + block_size] for i in range(0, len(ciph_bytes), block_size)]
        for j, block in enumerate(blocks):
            # use Counter to get a dictionary of byte counts
            byte_counts = Counter(block)
            # get the count of the most common byte
            repeats = byte_counts.most_common(1)[0][1] if byte_counts else 0
            if repeats > 1 and repeats > mostRepeats:
                print(f'New most repeats: {repeats}')
                mostRepeats = repeats
                ECBBoiii = ciph_bytes
                ECBindex = (i, j)
            print(f'Block {j} in Line {i} has {repeats} repeats')
    return ECBindex, ECBBoiii
'''
index, ciph = detect_ECB(ciphs)

if ciph:
    print(f'Found it at index {index}, here she: {ciph}\n')
else:
    print("None detected")    '''