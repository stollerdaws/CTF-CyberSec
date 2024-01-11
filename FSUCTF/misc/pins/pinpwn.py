import time, pexpect

def check_pin(pin):
    child = pexpect.spawn('./pin_checker')
    child.expect('Please enter your 8-digit PIN code:')
    start_time = time.time()
    child.sendline(pin)
    child.expect(['Access denied.', 'Incorrect length.'])  # Add more expected strings if needed.
    end_time = time.time()
    return end_time - start_time

def find_correct_pin():
    base_pin = ''
    for i in range(8):  # As the pin length is 8
        timings = {}
        for digit in '0123456789':
            pin_try = base_pin + digit + '0' * (7 - len(base_pin))
            duration = check_pin(pin_try)
            timings[digit] = duration
        # Get the digit with the maximum duration
        correct_digit = max(timings, key=timings.get)
        base_pin += correct_digit
        print(f"Guessed so far: {base_pin}")
    return base_pin

print("Starting the attack...")
guessed_pin = find_correct_pin()
print(f"Guessed PIN: {guessed_pin}")

