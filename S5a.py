import os
import re
from collections import Counter

# Function to extract 20-nucleotide sequences from a text
def extract_20_mer_sequences(text):
    sequences = re.findall(r'[ACGT]{20}', text)
    return sequences

# Function to count occurrences of 20-nucleotide sequences in a file
def count_20_mer_occurrences(input_file, reference_file):
    with open(input_file, 'r') as f:
        input_text = f.read()

    with open(reference_file, 'r') as f:
        reference_text = f.read()

    input_sequences = extract_20_mer_sequences(input_text)
    reference_sequences = extract_20_mer_sequences(reference_text)

    # Count occurrences of each 20-mer sequence in the reference file
    sequence_counts = Counter(reference_sequences)

    return sequence_counts

# Main function
def main():
    # Get user-specified input file
    input_file_path = input("Enter the path to the first file: ")

    if not os.path.exists(input_file_path):
        print("The specified first file does not exist.")
        return

    # Get user-specified reference file
    reference_file_path = input("Enter the path to the second file: ")

    if not os.path.exists(reference_file_path):
        print("The specified second file does not exist.")
        return

    # Count occurrences of 20-mer sequences in the reference file
    sequence_counts = count_20_mer_occurrences(input_file_path, reference_file_path)

    # Save results to a file
    output_folder = "C:\\ChatGPTclass"
    output_file_path = os.path.join(output_folder, "20counts.txt")

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    with open(output_file_path, 'w') as output_file:
        for sequence, count in sequence_counts.items():
            output_file.write(f"{sequence}\t{count}\n")

    print(f"Results saved to {output_file_path}")

if __name__ == "__main__":
    main()
