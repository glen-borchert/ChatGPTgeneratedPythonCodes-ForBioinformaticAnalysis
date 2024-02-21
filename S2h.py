# Define the file paths
input_file_path = r'C:\ChatGPT\Dirty.txt'  # Update with the correct file path
output_file_path = r'C:\ChatGPT\Clean.txt'  # Update with the desired output file path

try:
    # Read the input file
    with open(input_file_path, 'r') as input_file:
        dirty_text = input_file.read()
except FileNotFoundError:
    print(f"File not found at {input_file_path}. Make sure the file exists.")
    exit(1)

# Remove numbers, spaces, and hard returns
clean_text = ''.join(char for char in dirty_text if not char.isdigit() and char != ' ' and char != '\n')

# Write the cleaned text to the output file
try:
    with open(output_file_path, 'w') as output_file:
        output_file.write(clean_text)
    print(f"Cleaned text saved to {output_file_path}.")
except Exception as e:
    print(f"An error occurred while writing to {output_file_path}: {str(e)}")
