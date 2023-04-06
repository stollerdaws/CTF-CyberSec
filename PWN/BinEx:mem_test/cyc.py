from pwn import *

ebpval = 0x61617161

offset = cyclic_find(ebpval)

print(offset)
