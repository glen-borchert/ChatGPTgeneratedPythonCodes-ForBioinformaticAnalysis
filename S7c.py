import os

def extract_and_remove_duplicates(input_file, output_folder):
    unique_values = set()  # Use a set to automatically remove duplicates

    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                value = line.split('\t', 1)[0]  # Split on the first tab
                unique_values.add(value)

    # Generate the output filename based on the number of unique values
    output_filename = f"output_{len(unique_values)}.txt"

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Write the unique values to the output file
    output_path = os.path.join(output_folder, output_filename)
    with open(output_path, 'w') as output_file:
        output_file.write("\n".join(unique_values))

if __name__ == "__main__":
    input_file = input("Enter the path to the input file: ")
    output_folder = "C:/CHATGPTCLASS"  # Output folder path

    extract_and_remove_duplicates(input_file, output_folder)
