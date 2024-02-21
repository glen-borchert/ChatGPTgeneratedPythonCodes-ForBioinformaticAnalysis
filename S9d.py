def process_files(file1_path, file2_path, output_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(output_path, 'w') as output_file:
        file2_data = {}
        for line in file2:
            parts = line.strip().split('\t')
            name = parts[0]
            value = parts[3]
            file2_data[name] = value
        
        for line in file1:
            parts = line.strip().split('\t')
            name = parts[0]
            value = parts[2]
            
            if name in file2_data:
                output_line = f"{name}\t{value}\t{file2_data[name]}\n"
                output_file.write(output_line)

if __name__ == "__main__":
    file1_path = input("Enter the path of the first file: ")
    file2_path = input("Enter the path of the second file: ")
    output_path = "/Users/isabellaswan/python/same_hits.txt"

    process_files(file1_path, file2_path, output_path)
    print("Output file generated successfully.")

