import os

# Get the input file path from the user
input_file_path = input("Enter the path to the input file: ")

# Check if the input file exists
if not os.path.isfile(input_file_path):
    print(f"File not found: {input_file_path}")
else:
    # Read and process the input file
    unique_values = set()
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            value = line.split('\t', 1)[0]  # Extract the value up to the first tab
            unique_values.add(value)

    # Define the output folder
    output_folder = "/Users/meredithshaddix/Documents/CHATGPT"

    # Generate the output file path
    output_file_path = os.path.join(output_folder, f"output_{len(unique_values)}.txt")

    # Write the unique values to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.writelines(sorted(unique_values))

    print(f"Extracted unique values from '{input_file_path}' to '{output_file_path}'")

# Make sure to handle any exceptions that may occur while reading or writing files.
