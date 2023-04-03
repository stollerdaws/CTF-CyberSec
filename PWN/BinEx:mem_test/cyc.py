from pwn import *

ebpval = 0x61616761

offset = cyclic_find(ebpval)

print(offset)
