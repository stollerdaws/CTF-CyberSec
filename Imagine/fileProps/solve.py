import random, os

random.seed(os.stat("stuff.py").st_mtime)
a = str(random.randint(1,10000000000))
b = (os.stat("stuff.py").st_size)*1543424324398769579759769757361544769714143242343241434324324143243424234141432432
output_string = 1059911610212310411111210195121111117951001051001101752368349998856449444821966779711395362671487669506898789255840207854114170710148649
original_string_numeric = str((int(output_string) - int(a[3]) + int(a[4]) - int(a[3:])) ^ b)
print(original_string_numeric)
flag = ''

i = 0
while i < len(original_string_numeric):
    for length in range(3, 0, -1):  # Try lengths 3, 2, and 1
        segment = original_string_numeric[i:i+length]
        
        # Check if the segment is a valid ASCII value (for standard ASCII, use range(32, 128))
        if 0 <= int(segment) <= 255:
            flag += chr(int(segment))
            i += length
            break

print(flag)