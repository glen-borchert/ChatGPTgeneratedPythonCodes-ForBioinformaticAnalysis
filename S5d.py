import collections
import docx
from docx import Document
import chardet

# Function to create unique 20-nucleotide sequences with a sliding window
# (no changes to this function)

# Function to count the occurrences of unique sequences in another sequence
# (no changes to this function)

# Prompt the user to enter the input file names
unique_sequence_file = input("Enter the input file name with unique sequences: ")
counting_sequence_file = input("Enter the input file name to count sequences from: ")

# Prompt the user to enter the output Word file name
output_file_name = input("Enter the output Word file name: ")

# Function to detect file encoding
def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
    return result['encoding']

# Detect the encoding for the input files
unique_encoding = detect_encoding(unique_sequence_file)
counting_encoding = detect_encoding(counting_sequence_file)

# Read sequences from the specified files with the detected encodings
with open(unique_sequence_file, "r", encoding=unique_encoding) as unique_file, open(counting_sequence_file, "r", encoding=counting_encoding) as counting_file:
    unique_sequence = unique_file.read()
    counting_sequence = counting_file.read()

# Create a Word document
doc = Document()

# Find unique 20-nucleotide sequences using a sliding window
unique_sequences = find_unique_sequences(unique_sequence, 20)

# Count the occurrences of unique sequences in the counting_sequence
sequence_counter = count_sequence_occurrences(unique_sequences, counting_sequence)

# Save the unique sequences and occurrence counts in the Word document without labels
for sequence in unique_sequences:
    doc.add_paragraph(f"{sequence}: {sequence_counter.get(sequence, 0)}")

# Save the Word document as the specified output file
doc.save(output_file_name)

print(f"Word file '{output_file_name}' has been created with the unique sequence occurrences.")
