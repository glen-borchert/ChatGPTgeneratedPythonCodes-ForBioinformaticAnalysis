import pandas as pd

# Input file paths provided by the user
input_file1 = input("Enter the path of the first Excel file: ")
input_file2 = input("Enter the path of the second Excel file: ")

# Read both Excel files into dataframes
df1 = pd.read_excel(input_file1, sheet_name="Sheet1")
df2 = pd.read_excel(input_file2, sheet_name="Sheet1")

# Extract the names and values from the first and fourth columns of both dataframes
names_df1 = df1.iloc[:, 0]
values_df1 = df1.iloc[:, 3]
names_df2 = df2.iloc[:, 0]
values_df2 = df2.iloc[:, 3]

# Find the names that match in both dataframes
matching_names = names_df1[names_df1.isin(names_df2)].tolist()

# Create a new dataframe with matched names and corresponding values from both files
result_df = pd.DataFrame({
    'Name': matching_names,
    'Value from File 1': [values_df1[names_df1 == name].values[0] for name in matching_names],
    'Value from File 2': [values_df2[names_df2 == name].values[0] for name in matching_names]
})

# Output file path
output_file = "C:\\CHATGPTclass\\same_hits.txt"

# Write the result dataframe to the output file
result_df.to_csv(output_file, sep='\t', index=False)

print(f"Output saved to {output_file}")
