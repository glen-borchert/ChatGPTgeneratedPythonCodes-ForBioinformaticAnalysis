import os

def filter_and_reverse_complement(sequence):
    # Define a dictionary for reverse complement mapping
    complement_dict = {
        'A': 'U',
        'T': 'A',
        'G': 'C',
        'C': 'G',
        'U': 'A'
    }

    # Filter characters and reverse the string
    filtered_sequence = ''.join([char for char in sequence.upper() if char in 'ATCGU'])
    reversed_sequence = filtered_sequence[::-1]

    # Perform reverse complement operations
    complemented_sequence = ''.join([complement_dict.get(char, char) for char in reversed_sequence])
    return complemented_sequence

# Get the input file path from the user
input_file_path = input("Enter the path of the input file: ")

# Check if the specified file exists
if not os.path.isfile(input_file_path):
    print("Error: The specified file does not exist.")
    exit(1)

# Define the output file path
output_folder = r'C:\python\ChatGPTclass'
output_file_path = os.path.join(output_folder, 'reversecomplemented.txt')

# Read the input file
with open(input_file_path, 'r') as input_file:
    input_sequence = input_file.read()

# Filter and reverse complement the sequence
complemented_sequence = filter_and_reverse_complement(input_sequence)

# Write the result to the output file
try:
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    with open(output_file_path, 'w') as output_file:
        output_file.write(complemented_sequence)
    print(f"Reverse complemented sequence has been saved to '{output_file_path}'.")
except IOError:
    print(f"Error writing to '{output_file_path}'. Please make sure the folder exists and is writable.")
