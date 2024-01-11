import re
import os

def extract_includes(file_path):
    # Regex pattern to find include statements
    include_pattern = r'#include "spaghetti/(.*?)"'
    includes = []

    with open(file_path, 'r') as file:
        for line in file:
            matches = re.findall(include_pattern, line)
            if matches:
                includes.extend(matches)

    return includes

def concatenate_files(includes, output_file, base_path):
    with open(output_file, 'w') as outfile:
        for include in includes:
            include_path = os.path.join(base_path, include)
            with open(include_path, 'r') as infile:
                outfile.write(infile.read())
                outfile.write('\n\n')  # Adding a newline for separation

# Main execution
main_file_path = 'noodleNightmare.cpp'  # Replace with the path to your main file
base_path = 'spaghetti'     # Replace with the path to your spaghetti folder
output_file = 'combined_output.txt'        # Output file name

includes = extract_includes(main_file_path)
concatenate_files(includes, output_file, base_path)
