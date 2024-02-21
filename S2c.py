# Define the input and output file paths
input_file_path = r'C:\chatgptclass\dirty.txt'
output_file_path = r'C:\chatgptclass\clean.txt'

# Define the characters to keep
allowed_characters = {'A', 'G', 'C', 'U', 'T'}

# Function to filter out unwanted characters
def filter_characters(text):
    return ''.join(char for char in text if char in allowed_characters)

# Read the input file and filter the characters
try:
    with open(input_file_path, 'r') as input_file:
        dirty_text = input_file.read()
    clean_text = filter_characters(dirty_text)

    # Write the cleaned text to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(clean_text)
    print("File cleaned and saved successfully!")
except FileNotFoundError:
    print(f"Input file '{input_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
