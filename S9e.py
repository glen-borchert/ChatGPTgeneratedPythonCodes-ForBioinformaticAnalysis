def find_and_copy_values(input_file1, input_file2, output_file):
    # Create a dictionary to store values from the second file
    values_from_file2 = {}
    with open(input_file2, 'r') as file2:
        for line in file2:
            parts = line.strip().split('\t')
            if len(parts) >= 4:
                key = parts[0]
                value = parts[3]
                values_from_file2[key] = value

    # Create the output file and write matching lines with values
    with open(input_file1, 'r') as file1, open(output_file, 'w') as output:
        for line in file1:
            parts = line.strip().split('\t')
            if len(parts) > 0:
                key = parts[0]
                if key in values_from_file2:
                    value1 = parts[3]
                    value2 = values_from_file2[key]
                    output.write(f"{key}\t{value1}\t{value2}\n")

if __name__ == "__main__":
    input_file1 = input("Enter the first input file name: ")
    input_file2 = input("Enter the second input file name: ")
    output_file = "same_hits.txt"

    find_and_copy_values(input_file1, input_file2, output_file)
    print(f"Output has been saved to {output_file}")
