import time
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

# Try seeds around the current time
for i in tqdm.tqdm(range(-1000000, 1000000)):   # increase the range as necessary
    seed = seed_time + i
    srand(seed)

    # Get first random number
    first_num = rand()

    # Then, simulate the random sequence using your known values
    # Replace this with your actual data
    num_sequence = [1620939242, 1615988648, 2031561333, 2065412689, 1828656176]  # the sequence you observed from the generator

    for j, num in enumerate(num_sequence):
        guess = rand()
        if guess != num:
            break   # the seed is incorrect, go to next one
    else:
        print("Seed found:", seed, rand())
        break
else:
    print("Seed not found")
