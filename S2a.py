def clean_sequence(sequence):
    # Remove all characters except A, U, G, C, T
    cleaned_sequence = ''.join(char for char in sequence if char in 'AUGCT')
    # Replace 'U' with 'T'
    cleaned_sequence = cleaned_sequence.replace('U', 'T')
    return cleaned_sequence

# Prompt the user to enter the input file name
input_file_name = input("Enter the input file name: ")

# Prompt the user to enter the output file name
output_file_name = input("Enter the output file name: ")

try:
    with open(input_file_name, "r") as input_file:
        file_content = input_file.read()

    # Clean the sequence
    cleaned_sequence = clean_sequence(file_content)

    # Write the cleaned sequence to the output file
    with open(output_file_name, "w") as output_file:
        output_file.write(cleaned_sequence)

    print(f"File '{input_file_name}' has been cleaned and saved as '{output_file_name}'.")
except FileNotFoundError:
    print(f"File '{input_file_name}' not found. Please make sure the file exists.")
