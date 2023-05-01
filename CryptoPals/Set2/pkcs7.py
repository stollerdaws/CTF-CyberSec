def pkcs7_pad(data, block_size): # up to pkcs7 standard
    padding_length = block_size - (len(data) % block_size)
    padding = bytes([padding_length]) * padding_length
    print(f'\nPadded Block: {data + padding}')
    return data + padding

def pkcs7_unpad(data):
    padding_length = data[-1]
    if padding_length > len(data):
        raise ValueError("Invalid padding length")
    
    for i in range(1, padding_length + 1):
        if data[-i] != padding_length:
            raise ValueError("Invalid padding bytes")
    print(f'\nUnpadded Block: {data[:-padding_length]}')
    return data[:-padding_length]


data = input("Input some data to pad\n")
blockSize = int(input("input the block size\n"))

padded = pkcs7_pad(bytes(data, 'ascii'), blockSize)
unpadded = pkcs7_unpad(padded)

print(f'Padded Block: {padded}\nUnpadded Block : {unpadded}')