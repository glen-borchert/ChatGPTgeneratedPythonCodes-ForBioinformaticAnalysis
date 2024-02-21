import os

def count_reads_in_fasta(fasta_file):
    try:
        with open(fasta_file, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{fasta_file}' not found.")
        return -1

    read_count = sum(1 for line in lines if line.startswith('>'))
    return read_count

def main():
    # Get user input for the FASTA file
    fasta_file = input("Enter the path to the FASTA file: ")

    # Count the reads in the FASTA file
    read_count = count_reads_in_fasta(fasta_file)

    if read_count == -1:
        return  # Error occurred, exit

    # Extract the filename without extension
    file_name = os.path.splitext(os.path.basename(fasta_file))[0]

    # Create the output folder if it doesn't exist
    output_folder = "C:\\python\\ChatGPTclass"
    os.makedirs(output_folder, exist_ok=True)

    # Create the output file path
    output_file_path = os.path.join(output_folder, f"{file_name}_{read_count}_reads.txt")

    # Write the read count to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(str(read_count))

    print(f"Read count saved to: {output_file_path}")

if __name__ == "__main__":
    main()
