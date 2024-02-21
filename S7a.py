# Function to extract values up to the first tab and remove duplicates
def extract_and_remove_duplicates(input_file):
    unique_values = set()

    with open(input_file, 'r') as infile:
        for line in infile:
            # Extract values up to the first tab
            value = line.split('\t')[0]

            # Remove leading and trailing whitespace
            value = value.strip()

            if value not in unique_values:
                unique_values.add(value)

    return list(unique_values)

# Get the user input for the input file
input_file = input("Enter the path to the input file: ")

# Check if the input file exists
try:
    with open(input_file, 'r'):
        pass
except FileNotFoundError:
    print("Input file not found.")
    exit()

# Extract values and remove duplicates
unique_values = extract_and_remove_duplicates(input_file)

# Define the output file name
output_file = f"C:/CHATGPTclass/output_{len(unique_values)}.txt"

# Write the unique values to the output file
with open(output_file, 'w') as outfile:
    outfile.write('\n'.join(unique_values))

print(f"Unique values extracted and written to {output_file}")
