from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

def delete_reads(fasta_file, reads_to_delete_file, output_file):
    # Read the reads to delete from the text file
    with open(reads_to_delete_file, 'r') as reads_handle:
        reads_to_delete = set(line.strip() for line in 
reads_handle.readlines())

    # Create a new FASTA file without the specified reads
    output_path = f"/Users/isabellaswan/python/{output_file}.fasta"
    with open(output_path, 'w') as output_handle:
        for record in SeqIO.parse(fasta_file, 'fasta'):
            if record.id not in reads_to_delete:
                SeqIO.write(record, output_handle, 'fasta')

    print(f"New FASTA file created: {output_path}")

# Get user input for the files
fasta_file_path = input("Enter the path to the original FASTA file: ")
reads_to_delete_file_path = input("Enter the path to the text file with reads to delete: ")
output_file_name = "P22_Ominus_deleted_unknowns"

# Call the function to delete reads and create a new FASTA file
delete_reads(fasta_file_path, reads_to_delete_file_path, output_file_name)

