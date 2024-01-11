from pwn import *

def connect_and_get_flag(length_of_input):
    io = remote('babycha.chal.irisc.tf', 10100)

    # Encrypt arbitrary input of specified length
    io.recvuntil(b'> ')
    io.sendline(b'1')
    io.recvuntil(b'? ')
    io.sendline(b'a' * length_of_input)

    # Encrypt the flag
    io.recvuntil(b'> ')
    io.sendline(b'2')
    encrypted_flag = bytes.fromhex(io.recvline().strip().decode())
    
    io.close()
    return encrypted_flag

# Collect segments of the flag
flag = b''
offset = 0  # Start at the beginning of the flag
for i in range(5):  # Repeat 5 times
    length_of_input = 48 - (i*8)  # Decrease input length by 1 byte each time
    encrypted_flag = connect_and_get_flag(length_of_input)
    
    # Get the next 8 bytes of the flag
    flag_segment = encrypted_flag[offset:offset+8]
    flag += flag_segment
    offset += 8  # Move to the next segment

print(f'Full flag: {flag}')
