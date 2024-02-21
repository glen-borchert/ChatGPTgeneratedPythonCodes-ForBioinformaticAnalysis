def remove_fasta_headers(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            lines = input_file.readlines()

        sequence = ""
        for line in lines:
            line = line.strip()  # Remove leading and trailing whitespace

            # Skip lines starting with '>' as they are FASTA headers
            if not line.startswith('>'):
                sequence += line

        # Remove any spaces or hard returns
        sequence = sequence.replace(" ", "").replace("\n", "")

        with open(output_filename, 'w') as output_file:
            output_file.write(sequence)

        print(f"Sequence with headers removed saved to {output_filename}")

    except FileNotFoundError:
        print(f"File not found: {input_filename}")

if __name__ == '__main__':
    input_filename = input("Enter the input filename: ")
    output_filename = input("Enter the output filename: ")

    remove_fasta_headers(input_filename, output_filename)
