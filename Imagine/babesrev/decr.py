lookup = {'':'11','!':'14','"':'17','#':'20','$':'23','%':'26','&':'29',"'":'32','(':'35',')':'38','*':'41','+':'44',',':'47','-':'50','.':'53','/':'56','0':'59','1':'62','2':'65','3':'68','4':'71','5':'74','6':'77','7':'80','8':'83','9':'86',':':'89',';':'92','<':'95','=':'98','>':'1','?':'4','@':'7','A':'10','B':'13','C':'16','D':'19','E':'22','F':'25','G':'28','H':'31','I':'34','J':'37','K':'40','L':'43','M':'46','N':'49','O':'52','P':'55','Q':'58','R':'61','S':'64','T':'67','U':'70','V':'73','W':'76','X':'79','Y':'82','Z':'85','[':'88','\\':'91',']':'94','^':'97','_':'0','`':'3','a':'6','b':'9','c':'12','d':'15','e':'18','f':'21','g':'24','h':'27','i':'30','j':'33','k':'36','l':'39','m':'42','n':'45','o':'48','p':'51','q':'54','r':'57','s':'60','t':'63','u':'66','v':'69','w':'72','x':'75','y':'78','z':'81','{':'84','|':'87','}':'90','~':'93'}

string = '21396248439622427630725957360971978068187168186890'

def decrypt_with_known_end(encrypted_string, lookup, known_start, end_marker):
    decrypted_string = known_start
    # Find the corresponding encrypted part for the known_start
    encrypted_part = ""
    for char in known_start:
        encrypted_part += lookup[char]

    # Start decryption from the end of the known encrypted part
    start_index = encrypted_string.find(encrypted_part) + len(encrypted_part)
    end_index = encrypted_string.find(end_marker)

    while start_index < end_index:
        possibilities = []
        # Check for one and two digit possibilities
        one_digit = encrypted_string[start_index:start_index+1]
        two_digit = encrypted_string[start_index:start_index+2] if start_index+2 <= len(encrypted_string) else ""

        # Find matches in the lookup dictionary
        for key, value in lookup.items():
            if value == one_digit or value == two_digit:
                possibilities.append(key)

        # Handle ambiguities
        if len(possibilities) == 1:
            # If only one match, add it to the decrypted string
            decrypted_string += possibilities[0]
            start_index += len(lookup[possibilities[0]])  # Move ahead by the length of the matched encrypted value
        elif len(possibilities) > 1:
            # If multiple matches, print possibilities and current state of the flag for user to choose
            print(f"Current decrypted flag: {decrypted_string}")
            print(f"Ambiguous possibilities at index {start_index}: {possibilities}")
            choice_index = int(input("Enter the index of the correct character: "))
            decrypted_string += possibilities[choice_index]
            start_index += len(lookup[possibilities[choice_index]])  # Move ahead by the length of the matched encrypted value
        else:
            # If no match found, increment and continue
            start_index += 1

    # Append the last known character '}'
    decrypted_string += '}'
    return decrypted_string

# Known starting part of the flag and the end marker
known_start = "flag{l1ght_w0rk_b4by_3e43e3"
end_marker = '90'

# Decrypt from the known point with the known end
decrypted_flag = decrypt_with_known_end(string, lookup, known_start, end_marker)
print("Final decrypted flag:", decrypted_flag)


