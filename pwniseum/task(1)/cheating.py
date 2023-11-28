from pwn import *

io = remote ('62.173.140.174', 17600)

for i in range(99):
    io.recvuntil(b'\t\t')
    size = int(io.recv(4), base=16)
    io.recvuntil(b'Enter the answer => ')
    io.sendline(str(hex(size**3)))

io.recvuntil(b'Enter the answer => ')
io.sendline(b'000000002c010000')
io.interactive()

