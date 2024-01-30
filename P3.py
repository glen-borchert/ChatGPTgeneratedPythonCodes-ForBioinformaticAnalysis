import os
import random

# Define the file paths
input_file_path = r"C:\ChatGPTclass\peak.txt"
output_file_path = r"C:\ChatGPTclass\scrambled.txt"

# Check if the input file exists
if not os.path.exists(input_file_path):
    print(f"Input file '{input_file_path}' not found.")
else:
    # Read the content from the input file
    with open(input_file_path, "r") as input_file:
        input_text = input_file.read()

    # Convert the input string into a list of characters
    char_list = list(input_text)

    # Shuffle the characters randomly
    random.shuffle(char_list)

    # Create the output directory if it doesn't exist
    output_directory = os.path.dirname(output_file_path)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Write the shuffled string to the output file
    with open(output_file_path, "w") as output_file:
        output_file.write("".join(char_list))

    print(f"Shuffled string saved to '{output_file_path}'.")
