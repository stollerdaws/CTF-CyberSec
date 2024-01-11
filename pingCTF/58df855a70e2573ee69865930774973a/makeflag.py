def construct_flag():
    # Original string
    original = "Code that overuses }{ GOTO statements ratherzx than_structured programminjg constructqs, resulting in convoluted and unmaintainable programs, is often called spaghetti code. Such code has a complex and tangled control structure, resulting in a program flow that is conceptually like a bowl of spaghetti, twisted and tangled."

    # Indices used in the C++ code
    indices = [63, 71, 34, 66, 20, 71, 5, 51, 71, 15, 51, 128, 7, 2, 51, 255, 6, 3, 34, 51, 56, 1, 2, 3, 51, 71, 15, 51, 3, 7, 15, 71, 3, 13, 51, 5, 1, 51, 13, 3, 7, 2, 51, 71, 34, 51, 7, 15, 15, 3, 32, 128, 93, 276, 19]

    # Constructing the flag
    flag = ''
    for index in indices:
        if index < len(original):
            flag += original[index]
        else:
            flag += ' '  # Assuming spaces for indices out of range

    return flag

# Get the constructed flag
flag = construct_flag()
print("Constructed Flag:", flag)
