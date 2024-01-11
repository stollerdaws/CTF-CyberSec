def reverse_file_byte_by_byte(input_file_path, output_file_path):
    with open(input_file_path, 'rb') as file:
        data = file.readlines()

    reversed_data = [line[::-1] for line in data]

    with open(output_file_path, 'wb') as file:
        for line in reversed_data:
            file.write(line)

# Replace 'input.bin' with the path to your .bin file
# and 'output.png' with the desired output file name.
reverse_file_byte_by_byte('a.bin', 'output.png')
