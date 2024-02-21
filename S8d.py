import os

# Get the paths of the input files from the user
input_file_path = input("Enter the path to the first input file: ")
second_file_path = input("Enter the path to the second input file: ")

# Check if both input files exist
if not os.path.isfile(input_file_path) or not os.path.isfile(second_file_path):
    print("One or both of the input files do not exist.")
else:
    # Define the output folder
    output_folder = "/Users/meredithshaddix/Documents/CHATGPT"

    # Create the output file name
    output_file_name = f"extracted_{os.path.basename(input_file_path)}"
    output_file_path = os.path.join(output_folder, output_file_name)

    # Function to extract text and write to the output file
    def extract_text(text):
        with open(output_file_path, 'a') as output_file:
            output_file.write(text)

    # Variables to control chunk size and storage
    chunk_size = 100000  # Set the chunk size to control memory usage
    buffer = ''

    with open(second_file_path, 'r') as second_file:
        for line in second_file:
            buffer += line
            if '>' in buffer and buffer.count('>') > 1:
                parts = buffer.split('>')
                if len(parts) >= 3:
                    extract_text('>' + parts[1])  # Append the extracted text to the output file
                buffer = ''.join(parts[2:])

    # Process the remaining data in the buffer
    if buffer.strip():
        extract_text(buffer)

    print(f"Extracted data from '{second_file_path}' to '{output_file_path}'")

# Make sure to handle any exceptions that may occur while reading or writing files.
