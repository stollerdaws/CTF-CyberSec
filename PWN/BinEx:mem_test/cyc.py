from pwn import *

ebpval = 0x61616164

offset = cyclic_find(ebpval)

print(offset)
