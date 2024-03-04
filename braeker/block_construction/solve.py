def chunk_string(string, chunk_size):
    return [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]

def chunk_list(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

def find_duplicate_blocks(ciphertext):
    seen_blocks = set()
    duplicates = set()
    for block in ciphertext:
        if block in seen_blocks:
            duplicates.add(block)
        else:
            seen_blocks.add(block)
    return duplicates

def main():
    with open('ciphertext', 'r') as fin:
        ciphertext = fin.read().replace('\n', '')

    # Convert to blocks of 64 characters
    blocks_64 = chunk_string(ciphertext, 64)

    # Convert blocks of 64 characters to groups of 100 characters
    groups_100 = chunk_list(blocks_64, 100)

    # Identify blocks where the first 32 characters are the same as the last 32 characters
    for i, group in enumerate(groups_100, start=1):
        for chunk in group:
            if chunk[:32] == chunk[32:]:
                print(chunk)
                break

if __name__ == "__main__":
    main()
