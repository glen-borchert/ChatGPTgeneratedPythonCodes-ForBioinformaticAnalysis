def extract_sequences_from_file(data_file, names_file, output_folder):
    names_to_extract = []

    # Read names from the names file
    with open(names_file, 'r') as names:
        for line in names:
            names_to_extract.append(line.strip())

    sequences = []

    # Read sequences from the data file
    with open(data_file, 'r') as data:
        for line in data:
            columns = line.split()
            if len(columns) >= 1 and columns[0] in names_to_extract:
                sequences.append(line.strip())

    output_file = output_folder + "\\sequence.txt"

    # Save the extracted sequences to a new text file
    with open(output_file, 'w') as output:
        for sequence in sequences:
            output.write(sequence + '\n')

    print(f"Sequences extracted and saved in {output_file}")

# Prompt user for file paths
data_path = input("Enter the path to the data file: ")
names_path = input("Enter the path to the names file: ")

# Define the output folder
output_folder_path = r'C:\CHATGPTclass'

# Call the function to extract sequences
extract_sequences_from_file(data_path, names_path, output_folder_path)
