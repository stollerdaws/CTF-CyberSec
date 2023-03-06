from pwn import *

io = remote("ctf.hackucf.org", 10102)
flag = False
while(1):
   #recieve stream of characters until "value: "
   io.recvuntil("Value: ", timeout=1)
   
   if flag == False:
      val1 = io.recvline()
      val = val1
      flag = True
   else:
      val = io.recvline()
      print(val)
   if val != b"Repeat: Good job!\n":
      io.sendline(val)
   else:
      io.sendline(val1)
