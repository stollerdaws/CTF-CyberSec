import binascii
import base64

hexString = input("Enter a hex string\n")
# Convert hex string to bytes
bytes = binascii.unhexlify(hexString)
# Convert from raw bytes to base64 bytes 
base64Dat = base64.b64encode(bytes)
# Decode base64 bytes as base64 string
base64Str = base64Dat.decode()
# Print our encoded string
print(f'Base64 encoded string: {base64Str}\n')