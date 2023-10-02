
with open('message.txt', 'r') as f:
    lines = f.readline()

blocks = [lines[i:i+3] for i in range(0, len(lines), 3)]
print(blocks)

def decode_block(block):
    return block[2] + block[0] + block[1]

decblocks = [decode_block(block) for block in blocks]
print(''.join(decblocks))