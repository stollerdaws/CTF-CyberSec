grom pwn import *
#run with python3 pwnr.py DEBUG to see flag
io = remote("ctf.hackucf.org", 10101)

while(1):
   #recieve stream of characters until "value: "
   io.recvuntil("Value: ", timeout=1)
   val = io.recvline()
   io.recvuntil("Repeat: ")
   io.sendline(val)
   while True:
      io.recvuntil("Value: ", timeout=1)
      val = io.recvline()
      io.recvuntil("Repeat: ")
      io.sendline(val)


