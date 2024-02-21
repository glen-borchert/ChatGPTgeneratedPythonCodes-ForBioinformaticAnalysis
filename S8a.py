from Bio import SeqIO
import pandas as pd
from multiprocessing import Pool

def process_record(record):
    if record.id in read_names:
        return f">{record.id}\n{record.seq}\n"
    return ""

# Prompt for input file names
reads_file_name = input("Enter the name of the Excel file containing read names: ")
fasta_file_name = input("Enter the name of the FASTA file: ")

# Read the list of read names from the Excel file and convert to plain text
try:
    df = pd.read_excel(reads_file_name, header=None)
    read_names = set(df.iloc[:, 0].astype(str))
    temp_file_name = "temp_read_names.txt"
    with open(temp_file_name, 'w', encoding='utf-8') as f:
        for name in read_names:
            f.write(name + '\n')
except Exception as e:
    print(f"An error occurred while reading the Excel file: {e}")
    exit()

# Iterate through the FASTA file and write the output using multiprocessing
output_file_name = f"output_{len(read_names)}.fasta"
output_count = 0

with open(output_file_name, 'w', encoding='utf-8') as output_fasta, Pool() as pool:
    records = SeqIO.parse(fasta_file_name, "fasta")
    results = pool.map(process_record, records)
    for result in results:
        if result:
            output_fasta.write(result)
            output_count += 1

print(f"Output file {output_file_name} contains {output_count} reads.")

# Remove the temporary text file
import os
if os.path.exists(temp_file_name):
    os.remove(temp_file_name)
