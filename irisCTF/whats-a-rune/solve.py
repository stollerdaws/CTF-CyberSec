# Now let's apply the reverse transformation algorithm to this flag
with open('the', 'r') as f:
    transformed_flag = f.read()
def reverse_transformed_flag(transformed_flag):
    original_flag = []
    prev_char = 0

    for char in transformed_flag:
        original_char = chr(ord(char) - prev_char)
        original_flag.append(original_char)
        prev_char = ord(original_char)

    return ''.join(original_flag)

# Use the transformed flag from the file
reversed_flag = reverse_transformed_flag(transformed_flag)
print(reversed_flag)
