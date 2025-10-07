import pandas as pd
import io
import sys


# Ask for filename
df, input_file_name = None, ""
while not input_file_name:
    input_file_name = input("Please enter INPUT CSV filename: ").strip()

if input_file_name:
    # Attempt to read the file
    try:
        df = pd.read_csv(input_file_name)
        print(f"-- Data loaded from {input_file_name} --")
    except FileNotFoundError:
        print(f"Warning: File not found")
        sys.exit()
    except Exception as e:
        print(f"Warning: Error reading file ({e})")
        sys.exit()
    
# print(df.to_string())
# print("-" * 40)

# Find rows where the 'SummitCode' column starts with "W0C"
filter_mask = df['SummitCode'].str.startswith('W0C', na=False)

df_cleaned = df[filter_mask]

output_file_name = f"{input_file_name.split('.')[0]}_cleaned.csv"

df_cleaned.to_csv(output_file_name, index=False)

print("Cleaning complete")
