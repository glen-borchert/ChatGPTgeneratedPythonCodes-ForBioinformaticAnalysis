import os

def extract_and_copy(input_file, search_file, output_folder):
    # Read the search file and store the strings in a list
    with open(search_file, 'r') as sf:
        search_strings = [line.strip() for line in sf.readlines()]

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the second file for reading
    with open(input_file, 'r') as sf:
        second_file_content = sf.read()

    # Process and extract content for each search string
    for search_string in search_strings:
        start = second_file_content.find(search_string)
        if start != -1:
            start_marker = second_file_content.rfind(">", 0, start)  # Find the nearest ">" before the search_string
            end = second_file_content.find(">", start)
            if end != -1:
                extracted_content = second_file_content[start_marker:end + 1]

                # Create the output file name
                output_filename = f"extracted_{os.path.basename(input_file)}.txt"

                # Write the extracted content to the output file
                output_path = os.path.join(output_folder, output_filename)
                with open(output_path, 'a') as output_file:
                    output_file.write(extracted_content)

if __name__ == "__main__":
    input_file = input("Enter the path to the first file: ")
    search_file = input("Enter the path to the second file: ")
    output_folder = "C:/CHATGPTclass"  # Output folder path

    extract_and_copy(input_file, search_file, output_folder)
