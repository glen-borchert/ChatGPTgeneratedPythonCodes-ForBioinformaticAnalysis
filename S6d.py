# Function to count the number of '>' characters in a FASTA file
def count_fasta_headers(file_path):
    header_count = 0
    with open(file_path, 'r') as fasta_file:
        for line in fasta_file:
            if line.startswith('>'):
                header_count += 1
    return header_count

# Prompt the user to input the file name
fasta_file_path = input("Enter the path to the FASTA file: ")

header_count = count_fasta_headers(fasta_file_path)
print(f"Number of '>' characters in the FASTA file: {header_count}")
