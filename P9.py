import os

# Input file paths specified by the user
first_file_path = input("Enter the path of the first file: ")
second_file_path = input("Enter the path of the second file: ")

# Output file path
output_file_path = r'C:\python\ChatGPTclass\samehits.txt'

# Check if the input files exist
if not os.path.exists(first_file_path) or not os.path.exists(second_file_path):
    print("Input file(s) not found. Please make sure the file paths are correct.")
else:
    # Create a dictionary to store values from the second file
    second_file_values = {}

    # Read the second file and store values in the dictionary
    with open(second_file_path, 'r') as second_file:
        for line in second_file:
            parts = line.split('\t')
            if len(parts) >= 4:
                name = parts[0]
                value = parts[3]
                second_file_values[name] = value

    # Open the input files and the output file
    with open(first_file_path, 'r') as first_file, open(output_file_path, 'w') as output_file:
        # Iterate through the lines in the first file
        for line in first_file:
            parts = line.split('\t')
            if len(parts) >= 4:
                name = parts[0]
                value = parts[3]

                # Check if the name exists in the second file
                if name in second_file_values:
                    second_value = second_file_values[name]

                    # Write the output line to the file
                    output_line = f"{name}\t{value}\t{second_value}\n"
                    output_file.write(output_line)

    print(f"Results have been saved to {output_file_path}")
