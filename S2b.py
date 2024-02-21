# Define the file paths
input_file_path = r'C:\ChatGPT\dirty.txt'  # Update with the correct file path
output_file_path = r'C:\ChatGPT\CleanHuman.txt'  # Update with the desired output file path

try:
    # Read the input file
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()
except FileNotFoundError:
    print(f"File not found at {input_file_path}. Make sure the file exists.")
    exit(1)

# Initialize a variable to store the cleaned sequence
cleaned_sequence = ""

# Iterate through the lines in the file, skipping FASTA headers, spaces, and hard returns
for line in lines:
    if line.startswith('>'):
        continue  # Skip FASTA headers
    cleaned_sequence += line.strip()  # Remove spaces and hard returns

# Write the cleaned sequence to the output file
try:
    with open(output_file_path, 'w') as output_file:
        output_file.write(cleaned_sequence)
    print(f"Cleaned nucleotide sequence saved to {output_file_path}.")
except Exception as e:
    print(f"An error occurred while writing to {output_file_path}: {str(e)}")
