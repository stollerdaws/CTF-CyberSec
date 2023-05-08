import binascii
from langdetect import detect_langs
import string
from collections import Counter
# Dict containing the frequency of english letters to check if a string
# is english
English_frequency = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 'f': 0.02228, 'g': 0.02015,
    'h': 0.06094, 'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749,
    'o': 0.07507, 'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056, 'u': 0.02758,
    'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974, 'z': 0.00074
}
# counts occurances of letters and returns the distributions of each character
def checkFreq(str):
    str = str.lower()
    letters = [char for char in str if char in string.ascii_lowercase]
    letter_count = Counter(letters)
    total = sum(letter_count.values())
    # Calculate the frequency distributiion
    freq_dist = {char: count / total for char, count in letter_count.items()}
    return freq_dist
# Determines how similar the frequency of the plaintext is to english
def Freq_sim(freq1, freq2):
    similarity = sum(abs(freq1.get(char, 0) - freq2.get(char, 0)) for char in string.ascii_lowercase)
    return 1 - (similarity / 2)
# sets a threshhold and ultimately decides if text is or is not english
def is_english(text, freq, threshhold=0.65):
    textFreq = checkFreq(text)
    similarity = Freq_sim(textFreq, freq)
    return similarity > threshhold
# Perform single byte xor
def XOR(hex, key):
    bytes1 = bytes.fromhex(hex)
    plainHex = bytearray(b ^ key for b in bytes1)
    return plainHex.decode('utf-8', errors='ignore')
# Try XOR on every possible single ascii character (1-255)
def Brutus(hex):
    mostSimilar = 0
    topKey = None
    topPlain = None

    for key in range(256):
        plaintext = XOR(hex, key)
        print(f'\nPlain: {plaintext}')
        if is_english(plaintext, English_frequency):
            score = Freq_sim(checkFreq(plaintext), English_frequency)
            if score > mostSimilar:
                mostSimilar = score
                topKey = key
                topPlain = plaintext
    return topKey, topPlain, mostSimilar            

scores = []
f = open('4.txt', 'r')
for line in f.read():
    key, mess, score = Brutus(line)

    if key is not None:
        languages = detect_langs(mess)
        for lang in languages:
            if lang.lang == 'en' and lang.prob >= .99:
                scores.append((key, mess, score))
for score in scores:    
    print(f'Probable English found! Key: {score[0]}\n Plaintext: {score[1]}, Score: {score[2]}')

#target_string = input("Enter your encoded hex string\n")
#key, mess = Brutus(target_string)
#print(f'Recovered English! Key: {key}\n Plaintext: {mess}')