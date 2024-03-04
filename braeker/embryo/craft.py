from pwn import *

io = remote('0.cloud.chals.io', 20922)
with open('solve.asm', 'rb') as f:
    asm_code = f.read()

io.sendline(asm_code)
io.interactive()