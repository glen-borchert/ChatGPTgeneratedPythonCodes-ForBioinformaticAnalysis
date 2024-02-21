from Bio import SeqIO
import os

def split_sequence_to_fasta(input_filename, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read the nucleotide sequence from the input file
    with open(input_filename, "r") as input_file:
        sequence = input_file.read().strip()

    # Split the sequence into 100 base pair fragments
    fragment_size = 100
    fragments = [sequence[i:i+fragment_size] for i in range(0, len(sequence), fragment_size)]

    # Create the output FASTA file
    output_filename = os.path.join(output_folder, "100bpfragments.fasta")
    with open(output_filename, "w") as output_file:
        # Write each fragment to the FASTA file
        for i, fragment in enumerate(fragments, start=1):
            record_id = f"Fragment_{i}"
            output_file.write(f">{record_id}\n{fragment}\n")

    print(f"Fragmented sequence saved to: {output_filename}")

if __name__ == "__main__":
    # Get the input filename from the user
    input_filename = input("Enter the input file name (containing nucleotide sequence): ")

    # Specify the output folder
    output_folder = r"C:\python\ChatGPTclass"

    try:
        # Split sequence and create FASTA file
        split_sequence_to_fasta(input_filename, output_folder)
    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
