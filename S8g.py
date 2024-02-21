import concurrent.futures
import pandas as pd
import os

def read_excel_and_extract_sequence_names(excel_file):
    # Read the Excel file and extract unique sequence names
    df = pd.read_excel(excel_file, usecols=[0])
    sequence_names = df.iloc[:, 0].unique()
    return sequence_names

def search_and_extract_sequences(fasta_file, sequence_names):
    # Dictionary to store sequence names and sequences
    sequences = {}

    # Open the FASTA file and read it line by line
    with open(fasta_file, "r") as file:
        current_sequence = None
        for line in file:
            if line.startswith(">"):
                current_sequence = line.strip()[1:]
            else:
                if current_sequence in sequence_names:
                    if current_sequence not in sequences:
                        sequences[current_sequence] = ""
                    sequences[current_sequence] += line.strip()

    return sequences

if __name__ == "__main__":
    # Ask the user for the path to the Excel file
    excel_file = input("Enter the path to your Excel file: ")

    # Ask the user for the path to the FASTA file
    fasta_file = input("Enter the path to your FASTA file: ")

    # Read Excel and extract sequence names
    sequence_names = read_excel_and_extract_sequence_names(excel_file)

    # Create the output directory if it doesn't exist
    output_directory = "C:\\ChatGPT"
    os.makedirs(output_directory, exist_ok=True)

    # Search and extract sequences in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        sequence_futures = [executor.submit(search_and_extract_sequences, fasta_file, sequence_names)]

    sequences = sequence_futures[0].result()

    # Write the sequences to the output FASTA file
    output_file = os.path.join(output_directory, f"output_{len(sequences)}.fasta")

    with open(output_file, "w") as output:
        for sequence_name, sequence in sequences.items():
            output.write(f">{sequence_name}\n{sequence}\n")

    print(f"Sequences found and written to: {output_file}")
