import itertools
import hashlib

# The target SHA-256 hash we're looking for, in hexadecimal format
target_hash = '4546af8bf66d0f1d13713d85d952f5de689e91092b23ed1634c984d3b8e960b3'

# Function to check if the hash of a given input matches the target hash
def check_hash(input_string):
    # Encode the input string to bytes, compute its SHA-256 hash, and convert the hash to a hexadecimal string
    hash_hex = hashlib.sha256(input_string.encode('utf-8')).hexdigest()
    # Compare the computed hash with the target hash
    return hash_hex == target_hash

# Generate all possible 8-character strings consisting of 'd' and 'p'
for combination in itertools.product('dp', repeat=8):
    # Join the tuple of characters into a string
    test_string = ''.join(combination)
    # Check if the hash of this string matches the target hash
    if check_hash(test_string):
        print(f"Found matching string: {test_string}")
        break
else:
    print("No matching string found.")
