# Function to extract lines up to the first tab and remove duplicates
def extract_and_write_lines(input_file):
    # Initialize a set to store unique lines up to the first tab
    unique_lines = set()

    # Read and process the input file
    with open(input_file, 'r') as file:
        for line in file:
            # Extract the content up to the first tab character
            line = line.split('\t')[0]

            # Add the line to the set (automatically removes duplicates)
            unique_lines.add(line)

    # Define the output file name based on the number of unique lines
    output_file_name = f"output_{len(unique_lines)}.txt"

    # Write unique lines to the output file
    with open(output_file_name, 'w') as output_file:
        for line in unique_lines:
            output_file.write(line + '\n')

    print(f"Output file '{output_file_name}' created with {len(unique_lines)} unique lines.")

# Input: Specify the input text file
input_file = input("Enter the path to the input text file: ")

extract_and_write_lines(input_file)
