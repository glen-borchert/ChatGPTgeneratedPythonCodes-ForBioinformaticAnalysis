import os
from Bio import SeqIO

def extract_unmatched_sequences(fasta_file, read_list_file, output_folder):
    # Read the list of read names
    with open(read_list_file, 'r') as read_list:
        target_reads = set(read_list.read().splitlines())

    # Open the output file for unmatched sequences
    output_file = os.path.join(output_folder, f'uniqueseqs_0.fasta')
    output_handle = open(output_file, 'w')

    # Parse the input FASTA file and extract sequences for the target reads
    unmatched_count = 0
    for record in SeqIO.parse(fasta_file, 'fasta'):
        if record.id not in target_reads:
            SeqIO.write(record, output_handle, 'fasta')
            unmatched_count += 1

    # Close the output file
    output_handle.close()

    print(f"Extracted {unmatched_count} unmatched sequences to {output_file}")

if __name__ == "__main__":
    # Get the input FASTA file and read list file from the user
    fasta_file = input("Enter the path to the FASTA file: ")
    read_list_file = input("Enter the path to the text file containing read names: ")

    # Determine the output folder
    output_folder = r'C:\python\ChatGPTclass'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    extract_unmatched_sequences(fasta_file, read_list_file, output_folder)
