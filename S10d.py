def remove_reads(source_file, remove_file, output_folder):
    # Read reads from the source file
    with open(source_file, 'r') as source_file:
        source_reads = source_file.read().splitlines()

    # Read reads to be removed from the remove file
    with open(remove_file, 'r') as remove_file:
        remove_reads = remove_file.read().splitlines()

    # Remove specified reads
    remaining_reads = [read for read in source_reads if read not in remove_reads]

    # Create a new file with the remaining reads
    output_file_path = os.path.join(output_folder, 'newreads.txt')
    with open(output_file_path, 'w') as output_file:
        output_file.write('\n'.join(remaining_reads))

    print(f"New reads saved to: {output_file_path}")

if __name__ == "__main__":
    import os

    # Get file paths from the user
    source_file = input("Enter the path of the source file: ")
    remove_file = input("Enter the path of the file containing reads to be removed: ")

    # Make sure the files exist
    if not os.path.isfile(source_file) or not os.path.isfile(remove_file):
        print("One or more specified files do not exist. Please check the file paths.")
    else:
        output_folder = r'C:\chatgptclass'
        remove_reads(source_file, remove_file, output_folder)
