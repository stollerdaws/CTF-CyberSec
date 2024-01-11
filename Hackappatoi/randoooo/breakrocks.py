from pwn import * 
import time
import ctypes
HOST, PORT = '92.246.89.201', 10001


# Load the C standard library
libc = ctypes.CDLL('libc.so.6')

# Seed the RNG
io = remote(HOST, PORT)
current_time = int(time.time())
libc.srand(current_time)
def get_next_choice():
    return libc.rand() % 3

def choose_winning_option(server_choice):
    # Implement the winning logic based on the game rules
    # 0 - Pizza, 1 - Espresso, 2 - Spaghetti
    if server_choice == 0:  # Server chooses Pizza
        return 'Espresso'
    elif server_choice == 1:  # Server chooses Espresso
        return 'Spaghetti'
    else:  # Server chooses Spaghetti
        return 'Pizza'
    
# Play 10 rounds
for _ in range(10):
    server_choice = get_next_choice()
    winning_choice = choose_winning_option(server_choice)
    io.recvuntil(b'>> ')
    io.sendline(winning_choice)

io.interactive()
io.close()