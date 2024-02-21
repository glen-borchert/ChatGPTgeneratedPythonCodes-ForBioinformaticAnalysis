import os
import time

# Get the input BLAST output file from the user
input_file = input("Enter the path to the BLAST output file: ")

# Check if the input file exists
if not os.path.isfile(input_file):
    print("Input file does not exist.")
else:
    # Read the input file and extract read names
    read_names = []
    with open(input_file, 'r') as f:
        for line in f:
            columns = line.strip().split('\t')
            if len(columns) > 0:
                read_names.append(columns[0])

    # Determine the output folder
    output_folder = r'C:\python\ChatGPTclass'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Generate the output file path and save the extracted read names
    output_file = os.path.join(output_folder, f'extractedreads_{len(read_names)}.txt')
    with open(output_file, 'w') as out_file:
        for read_name in read_names:
            out_file.write(read_name + '\n')

    print(f"Extracted {len(read_names)} read names to {output_file}")
    

