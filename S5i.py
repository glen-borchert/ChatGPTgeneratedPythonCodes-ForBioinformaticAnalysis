import os

def get_unique_20mers(filename):
    sequences = set()
    with open(filename, 'r') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            if line.startswith('>'):
                continue
            for i in range(len(line) - 19):
                sequence = line[i:i + 20]
                sequences.add(sequence)
    return sequences

def count_sequences_in_second_file(input_file, output_file, unique_sequences):
    sequence_counts = {}
    with open(input_file, 'r') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            for sequence in unique_sequences:
                count = line.count(sequence)
                if sequence in sequence_counts:
                    sequence_counts[sequence] += count
                else:
                    sequence_counts[sequence] = count

    with open(output_file, 'w') as outfile:
        for sequence, count in sequence_counts.items():
            outfile.write(f'{sequence}\t{count}\n')

if __name__ == "__main__":
    first_file = input("Enter the path to the first file: ")
    second_file = input("Enter the path to the second file: ")
    output_folder = r"C:\python\ChatGPTclass"
    output_file = os.path.join(output_folder, "saltrfcounts.txt")

    unique_sequences = get_unique_20mers(first_file)
    count_sequences_in_second_file(second_file, output_file, unique_sequences)

    print(f"Results saved to {output_file}")
