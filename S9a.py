import os

# Function to extract data from a file and store it in a dictionary
def extract_data(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 4:
                key = parts[0]
                value = parts[3]  # Extract value after the third tab
                data[key] = value
    return data

# Function to process the files and generate the output file
def process_files(input_file1, input_file2, output_file):
    data1 = extract_data(input_file1)
    data2 = extract_data(input_file2)

    with open(output_file, 'w') as output:
        for key in data1:
            if key in data2:
                line = f"{key}\t{data1[key]}\t{data2[key]}\n"
                output.write(line)

if __name__ == "__main__":
    input_file1 = input("Enter the path to the first input file: ")
    input_file2 = input("Enter the path to the second input file: ")
    output_folder = "C:\\ChatGPT"
    output_file = os.path.join(output_folder, "same_hits.txt")

    process_files(input_file1, input_file2, output_file)
    print(f"Output file 'same_hits.txt' has been created in {output_folder}")
