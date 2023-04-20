from AESDecrypt import decrypt

with open('8.txt', 'r') as f:
    ciphs = f.readlines()

def detect_ECB(ciphs, block_size=16):
    mostRepeats = 0
    ECBBoiii = None
    ECBindex = None
    for i, ciph in enumerate(ciphs):
        ciph_bytes = bytes.fromhex(ciph.strip())
        blocks = [ciph_bytes[i:i + block_size] for i in range(0, len(ciph_bytes), block_size)]
# This is checking if a block repeats, the odds naturally are 1/2^128
# So if we have a repeat, it's there on purpose or incredibly unlucky
        repeats = 0
        for block in set(blocks): #Use set to eliminate duplicates
            count = blocks.count(block)
            if count > 1:
                repeats += count - 1 # -1 to only count repetitions
        if repeats > mostRepeats:
            mostRepeats = repeats
            ECBBoiii = ciph_bytes
            ECBindex = i
    return ECBindex, ECBBoiii

index, ciph = detect_ECB(ciphs)

if ciph:
    print(f'Found it at index {index}, here she: {ciph}\n')
else:
    print("None detected")    