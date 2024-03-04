import collections

# Frequency mapping for Indonesian letters
indonesian_freq = {
    'A': 20.39, 'N': 9.33, 'E': 8.28, 'I': 7.98, 'T': 5.58, 'K': 5.14,
    'D': 5.00, 'R': 4.64, 'U': 4.62, 'M': 4.21, 'S': 4.15, 'G': 3.66,
    'L': 3.26, 'H': 2.74, 'B': 2.64, 'P': 2.61, 'Y': 1.88, 'O': 1.26,
    'J': 0.87, 'C': 0.76, 'W': 0.48, 'F': 0.21, 'V': 0.18, 'Z': 0.04,
    'X': 0.03, 'É': 0.01, 'Q': 0.01
}
indonesian_bigrams = {
    'AN': 6.24, 'DA': 3.21, 'NG': 3.10, 'KA': 2.41, 'ER': 2.38, 'YA': 2.06,
    'EN': 2.02, 'LA': 1.80, 'ME': 1.78, 'DI': 1.72, 'AK': 1.70, 'AT': 1.69,
    'AR': 1.68, 'TA': 1.55, 'SA': 1.52, 'SE': 1.47, 'AH': 1.45, 'IN': 1.40,
    'GA': 1.32, 'PA': 1.28, 'TU': 1.23, 'RA': 1.22, 'AL': 1.20, 'BE': 1.14,
    'TE': 1.13, 'TI': 1.11, 'BA': 1.10, 'MA': 1.04, 'UN': 1.00, 'AM': 0.99,
    'EM': 0.98, 'EL': 0.95, 'IA': 0.94, 'KE': 0.94, 'HA': 0.92, 'RI': 0.89,
    'NA': 0.86, 'AP': 0.84, 'NT': 0.80, 'UK': 0.79, 'PE': 0.78, 'IK': 0.77,
    'ND': 0.75
}
# Ciphertext
ciphertext = """efe kqkbkx czwkf akfs kdkf qzfskf wzdcjtfk 
ieqku kqk akfs ikxj kck akfs wkak ukikukf :Q lzfqztk 
ukdj kqk qe wefe: bkvim{wzbkdki_ckse_kckukx_ukdj_wjuk_kfkbewew_mtzujzfwe}
"""

# Initial substitution based on 'bkvim' -> 'lactf'
substitution = {
    'b': 'l', 'k': 'a', 'v': 'c', 'i': 't', 'm': 'f',
    'e': 'i', 'f': 'n', ' ': ' ', '{': '{', '}': '}',
    'w': 's', 'c': 'p', 'z': 'e', 'q': 'd', 'x': 'h',
    's': 'g', 'a': 'y', 'd': 'm', '_': '_', 'j': 'u',
    't': 'r', 'u': 'k',
    
}

# Function to calculate the frequency of letters in the ciphertext
def calculate_frequency(text):
    frequency = {}
    for char in text:
        if char.isalpha():  # Consider only alphabetic characters
            char = char.lower()
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    total = sum(frequency.values())
    for char in frequency:
        frequency[char] = (frequency[char] / total) * 100
    return frequency

# Function to decode the ciphertext
def decode(ciphertext, substitution):
    decoded_text = ""
    for char in ciphertext.lower():
        if char in substitution:
            decoded_text += substitution[char]
        else:
            decoded_text += '_'  # Placeholder for undecoded characters
    return decoded_text

# Calculate frequency of letters in the ciphertext
frequency = calculate_frequency(ciphertext)

# Display the frequency of letters in the ciphertext for analysis
print("Ciphertext Letter Frequency:")
for char, freq in sorted(frequency.items(), key=lambda x: x[1], reverse=True):
    print(f"{char}: {freq:.2f}%")


# Compare with Indonesian letter frequencies
print("\nIndonesian Letter Frequencies:")
for char, freq in indonesian_freq.items():
    print(f"{char}: {freq}%")

# Decoding attempt with initial substitution
decoded_message = decode(ciphertext, substitution)
print("\nPartially Decoded Message:")
print(decoded_message)
