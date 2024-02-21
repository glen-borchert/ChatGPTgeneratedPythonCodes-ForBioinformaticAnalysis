def extract_sequences(input_txt_file, input_fasta_file):
    # Create a dictionary to store the headers and sequences from the FASTA file
    fasta_data = {}
    current_header = None
    current_sequence = []

    with open(input_fasta_file, 'r') as fasta_file:
        for line in fasta_file:
            line = line.strip()
            if line.startswith('>'):
                if current_header is not None:
                    fasta_data[current_header] = ''.join(current_sequence)
                current_header = line[1:]
                current_sequence = []
            else:
                current_sequence.append(line)
        if current_header is not None:
            fasta_data[current_header] = ''.join(current_sequence)

    # Determine the output file name based on the input .txt file
    output_file_name = "extracted_" + input_txt_file.split(".")[0] + ".txt"

    # Create the output file and write the matching sequences
    with open(input_txt_file, 'r') as txt_file, open(output_file_name, 'w') as output_file:
        keywords = set(line.strip() for line in txt_file)
        in_matching_sequence = False
        for line in fasta_data:
            if any(keyword in line for keyword in keywords):
                in_matching_sequence = True
                output_file.write('>' + line + '\n' + fasta_data[line] + '\n')
            elif in_matching_sequence and line.startswith('>'):
                in_matching_sequence = False

    print(f"Sequences extracted to {output_file_name}")

# Input: Specify the input .txt and .fasta files
input_txt_file = input("Enter the path to the input .txt file: ")
input_fasta_file = input("Enter the path to the input .fasta file: ")

extract_sequences(input_txt_file, input_fasta_file)
