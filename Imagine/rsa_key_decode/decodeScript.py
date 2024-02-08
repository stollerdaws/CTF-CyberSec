import base64

def parse_ssh_rsa_key(decoded_key):
    """
    Parses an RSA public key from SSH format and returns the algorithm,
    public exponent, and modulus.
    """
    # Skip the algorithm identifier and its length
    index = 4
    algorithm_length = int.from_bytes(decoded_key[index-4:index], byteorder='big')
    algorithm = decoded_key[index:index+algorithm_length].decode()
    index += algorithm_length

    # Extract the public exponent
    exponent_length = int.from_bytes(decoded_key[index:index+4], byteorder='big')
    index += 4
    public_exponent = int.from_bytes(decoded_key[index:index+exponent_length], byteorder='big')
    index += exponent_length

    # Extract the modulus
    modulus_length = int.from_bytes(decoded_key[index:index+4], byteorder='big')
    index += 4
    modulus = decoded_key[index:index+modulus_length]

    return algorithm, public_exponent, modulus

def main():
    key_file = input("Enter the SSH key file path: ")

    with open(key_file, "r") as file:
        key_data = file.read().strip()

    # Extract the base64 part of the SSH key
    key_parts = key_data.split()
    if len(key_parts) < 2 or key_parts[0] != "ssh-rsa":
        print("Invalid SSH key format.")
        return

    ssh_key_b64 = key_parts[1]
    decoded_key = base64.b64decode(ssh_key_b64)

    algorithm, public_exponent, modulus = parse_ssh_rsa_key(decoded_key)
    modulus_hex = modulus.hex()

    print("Algorithm:", algorithm)
    print("Public Exponent:", public_exponent)
    print("Modulus (Hex):", modulus_hex)
    print("Last 16 Hex Digits of Modulus:", modulus_hex[-16:].lower())

if __name__ == "__main__":
    main()
