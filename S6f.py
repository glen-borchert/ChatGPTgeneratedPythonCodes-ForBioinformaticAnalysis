# Ask the user for the input file
input_file = input("Enter the path of the input FASTA file: ")

try:
    with open(input_file, 'r') as file:
        # Read the contents of the input file
        file_contents = file.read()

        # Count the number of '>' characters (FASTA headers)
        header_count = file_contents.count('>')

    # Define the path for the output file
    output_file = r'C:\python\ChatGPTclass\read.txt'

    # Save the count to the output file
    with open(output_file, 'w') as output:
        output.write(f"Number of '>' characters (FASTA headers) in the input file: {header_count}")

    print(f"Header count saved to {output_file}")
except FileNotFoundError:
    print(f"File not found: {input_file}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
