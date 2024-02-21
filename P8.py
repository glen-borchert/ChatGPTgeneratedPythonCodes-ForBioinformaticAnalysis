import os
import time
from Bio import SeqIO

# Get the input FASTA file and read list file from the user
fasta_file = input("Enter the path to the FASTA file: ")
read_list_file = input("Enter the path to the text file containing read names: ")

# Check if the input files exist
if not os.path.isfile(fasta_file) or not os.path.isfile(read_list_file):
    print("Input file(s) do not exist.")
else:
    # Define the start time
    start_time = time.time()

    # Read the list of read names
    with open(read_list_file, 'r') as read_list:
        target_reads = set(read_list.read().splitlines())

    # Parse the input FASTA file and extract sequences for the target reads
    sequences = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        if record.id in target_reads:
            sequences.append(record)

    # Determine the output folder
    output_folder = r'C:\python\ChatGPTclass'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Generate the output file path and save the extracted sequences
    output_file = os.path.join(output_folder, f'readsequences_{len(sequences)}.fasta')
    SeqIO.write(sequences, output_file, "fasta")

    print(f"Extracted {len(sequences)} sequences to {output_file}")

    # Measure execution time
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")

