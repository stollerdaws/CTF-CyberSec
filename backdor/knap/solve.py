import hashlib
from Crypto.Cipher import AES
from itertools import combinations

# Function to try all combinations of numbers to match the sum
def find_subset(numbers, target_sun):
    for r in range(len(numbers) + 1):
        for subset in combinations(numbers, r):
            if sum(subset) == target_sun:
                return subset
    return None

ciphertext = 0xaf95a58f4fbab33cd98f2bfcdcd19a101c04232ac6e8f7e9b705b942be9707b66ac0e62ed38f14046d1cd86b133ebda9

numbers = [600848253359, 617370603129, 506919465064, 218995773533, 831016169202, 501743312177, 15915022145, 902217876313, 16106924577, 339484425400, 372255158657, 612977795139, 755932592051, 188931588244, 266379866558, 661628157071, 428027838199, 929094803770, 917715204448, 103431741147, 549163664804, 398306592361, 442876575930, 641158284784, 492384131229, 524027495955, 232203211652, 213223394430, 322608432478, 721091079509, 518513918024, 397397503488, 62846154328, 725196249396, 443022485079, 547194537747, 348150826751, 522851553238, 421636467374, 12712949979]
target_sum = 7929089016814

# Find the subset of numbers that add up to the sum
subset = find_subset(numbers, target_sum)

# Reconstruct the secret key
secret_bits = [1 if num in subset else 0 for num in numbers]
secret_key = int("".join(map(str, secret_bits)), 2)

# Hash the reconstructed secret to get the AES key
key = hashlib.sha256(secret_key.to_bytes((secret_key.bit_length() + 7) // 8, 'big')).digest()[:16]

# Decrypt the ciphertext
cipher = AES.new(key, AES.MODE_ECB)
decrypted_flag = cipher.decrypt(ciphertext).rstrip(b'\x00')

print(decrypted_flag)
