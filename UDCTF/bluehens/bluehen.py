def blue_hens(file_path):
    # Read the file and store each line in a list
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Initialize variables
    register = 0
    counter = 0
    line_num = 1
    flag = ''
    while line_num <= len(lines):
        # Parse the line to determine OPCODE and ARG
        line = lines[line_num - 1].strip().split(' ')
        opcode = line.count('blue')
        arg = line.count('hens')

        # Perform action based on OPCODE
        if opcode == 1:
            register = arg
        elif opcode == 2:
            register += arg
        elif opcode == 3:
            register -= arg
        elif opcode == 4:
            register *= arg
        elif opcode == 5:
            line_num = arg
            continue
        elif opcode == 6:
            line_num -= arg
            continue
        elif opcode == 7:
            line_num += arg
            continue
        elif opcode == 8:
            counter += arg
        elif opcode == 9:
            counter -= arg
        elif opcode == 10:
            if counter == 0:
                line_num += 1
        elif opcode == 11:
            print(chr(register))
            flag += chr(register)

        # Increment the line number
        line_num += 1
        print(flag)

# Test the function
blue_hens('flag.bluehens')
