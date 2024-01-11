import bcrypt
from itertools import combinations
from tqdm import tqdm

def generate_and_check_hash(captions, dates, target_hash):
    # Lowercasing the captions
    #captions = [word.lower() for word in captions]

    # Generating combinations of three words from the captions
    word_combinations = list(combinations(captions, 3))

    # Total combinations to process (for progress bar)
    total_combinations = len(word_combinations) * len(dates)
    total_combinations = total_combinations // 2
    # Checking each combination with each date
    for combo in tqdm(word_combinations, total=total_combinations, desc="Processing"):
        for date in dates:
            # Concatenate words with the date
            word = ''.join(combo) + date
            #print(word)
            # Hash the word using bcrypt
            hashed_word = bcrypt.hashpw(word.encode(), bcrypt.gensalt())
            if hashed_word == target_hash:
                return word

    return "No match found"

# Instagram captions
captions = [
    "Italy", "Amsterdam", "Swarovski", "Crystal", "Museum", "Sculptures",
    "Portofino", "Mimosas", "Europe", "Tiramisu", "Starbucks", "Milan",
     'Travel', 'Manhattan', 'Europe', 'London', "Vacation", 'April', 'Elaina'
]

# Important dates formatted as strings
dates = ["04271996", "0481965", '27041996', '08041965']

# The given hash to match against
hash_to_match = b"$2b$04$DkQOnBXHNLw2cnsmSEdM0uyN3NHLUb9I5IIUF3akpLwoy7dlhgyEC"

# Run the function
result = generate_and_check_hash(captions, dates, hash_to_match)
print(result)
