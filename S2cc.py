# Read the input file
input_file_path = '/Users/isabellaswan/python/input.txt'
with open(input_file_path, 'r') as file:
    input_string = file.read()

# Reverse the order of characters
reversed_string = input_string[::-1]

# Replace characters based on the rules
complemented_string = reversed_string.translate(str.maketrans('ATGC', 
'TACG'))

# Write the result to the output file
output_file_path = '/Users/isabellaswan/python/reversecomplemented.txt'
with open(output_file_path, 'w') as file:
    file.write(complemented_string)

print(f"Output written to {output_file_path}")

