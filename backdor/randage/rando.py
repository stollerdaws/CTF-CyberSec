from pwn import * 
import ctypes
import time

# Load the C standard library
libc = ctypes.CDLL("libc.so.6")
exe = context.binary = ELF('chal')
# Seed the RNG with the current time, just like the CTF challenge does
current_time = int(time.time())
libc.srand(current_time)
io = remote('34.70.212.151', 8006)
# Define the list of fruits in the order you provided
fruits = ["Apple", "Orange", "Mango", "Banana", "Pineapple", "Watermelon", "Guava", "Kiwi", "Strawberry", "Peach"]

# Function to return the correct fruit name based on the random number
def get_fruit_name(rand_num):
    index = rand_num % 10
    return fruits[index]
for _ in range(50):
    io.recvuntil(b'Your guess : ')
    io.sendline(get_fruit_name(libc.rand()))
io.interactive()