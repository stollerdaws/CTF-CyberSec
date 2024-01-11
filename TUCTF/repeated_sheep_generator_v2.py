import num2words
def generate_repeated_sheep_list(max_count, output_file):
    '''Generate a file with the word 'sheep' repeated up to a specified number, each on a new line.

    Args:
    max_count (int): The maximum number of times 'sheep' is repeated.
    output_file (str): The path to the output file where the wordlist will be saved.'''
    
    word = 'sheep'
    with open(output_file, 'w') as file:
        '''for i in range(1, max_count + 1):
            file.write(word * i + '\n')'''
        for i in range(1, max_count + 1):
            file.write(str(i) + word + '\n')
            file.write(num2words.num2words(i) + word + '\n')
            file.write(num2words.num2words(i) + ' ' + word + '\n')

# Example usage:
generate_repeated_sheep_list(10000, 'sheep_wordlist.txt')  # Generates a file with 'sheep', 'sheepsheep', etc.
