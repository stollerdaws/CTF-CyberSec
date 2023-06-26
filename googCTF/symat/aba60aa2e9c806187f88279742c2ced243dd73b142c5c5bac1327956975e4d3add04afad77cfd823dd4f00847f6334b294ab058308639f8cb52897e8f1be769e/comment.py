from PIL import Image
import binascii

def binstr_to_hexstr(binstr):
    hexstr = hex(int(binstr, 2))[2:]  # Remove '0x' from the start
    return hexstr

def pixel_bit(t1, t2):
    return str(t2[2] - t1[2])

encoded_image = Image.open("./symatrix.png")

x_len, y_len = encoded_image.size
nx_len = x_len // 2  # Original width of the image

encoded_matrix = encoded_image.load()

binary_string = ""

for i in range(y_len):
    for j in range(nx_len):
        left_pixel = encoded_matrix[j, i]
        right_pixel = encoded_matrix[x_len - j - 1, i]  # Corresponding pixel in the mirrored image
        
        # Check if the pixel has been altered
        if left_pixel != right_pixel:
            binary_string += pixel_bit(left_pixel, right_pixel)

# Convert the binary string to hexadecimal
hexstr = binstr_to_hexstr(binary_string)

# Convert the hexadecimal string to bytes
bytes_data = binascii.unhexlify(hexstr)

print(bytes_data)