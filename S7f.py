import os

# Function to extract unique names up to the first tab from each line
def extract_unique_names(input_file, output_folder):
    output_file_path = os.path.join(output_folder, f'output_{os.path.basename(input_file)}.txt')

    unique_names = set()

    with open(input_file, 'r') as input_file:
        for line in input_file:
            name = line.split('\t', 1)[0]  # Extract values up to the first tab
            unique_names.add(name)

    with open(output_file_path, 'w') as output_file:
        for name in unique_names:
            output_file.write(name + '\n')

    return output_file_path

# Prompt the user for the input file path
input_file_path = input("Enter the path to the input file: ")

if os.path.isfile(input_file_path):
    output_folder = "C:\\ChatGPT"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file = extract_unique_names(input_file_path, output_folder)
    num_unique_names = len(open(output_file).readlines())

    print(f'Unique names extracted and saved to {output_file}')
    print(f'Output file contains {num_unique_names} unique names.')
else:
    print('The specified input file does not exist.')
