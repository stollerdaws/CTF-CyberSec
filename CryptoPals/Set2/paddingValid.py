
def validate(buffer):
    if not buffer:
        raise ValueError("The input string is empty")

    pad_length = ord(buffer[-1])  # The value of the last byte gives us the padding length

    # Check that the padding length is valid
    if pad_length > len(buffer) or pad_length <= 0:
        raise ValueError("Invalid padding")

    # Check the validity of the padding
    padding = buffer[-pad_length:]
    if not all(ord(char) == pad_length for char in padding):
        raise ValueError("Invalid padding")

    return buffer[:-pad_length]
