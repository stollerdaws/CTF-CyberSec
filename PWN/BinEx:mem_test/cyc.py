from pwn import *

ebpval = 0x62616164

offset = cyclic_find(ebpval)

print(offset)
