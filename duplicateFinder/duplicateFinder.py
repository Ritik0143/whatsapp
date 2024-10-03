import pandas as pd
import os

def remove_duplicates(main_file, copy_file, output_file):
    # Check if files exist
    if not os.path.exists(main_file):
        raise FileNotFoundError(f"{main_file} does not exist.")
    if not os.path.exists(copy_file):
        raise FileNotFoundError(f"{copy_file} does not exist.")
    
    # Load the CSV files into DataFrames
    main_df = pd.read_csv(main_file)
    copy_df = pd.read_csv(copy_file)

    # Ensure the 'Phone' column exists in both DataFrames
    if 'Phone' not in main_df.columns or 'Phone' not in copy_df.columns:
        raise ValueError("Both CSV files must contain a 'Phone' column")

    # Clean and standardize the 'Phone' column
    main_df['Phone'] = main_df['Phone'].astype(str).str.strip().str.lower()
    copy_df['Phone'] = copy_df['Phone'].astype(str).str.strip().str.lower()

    # Find duplicates based on the 'Phone' column
    duplicate_phones = main_df['Phone'].tolist()
    is_duplicate = copy_df['Phone'].isin(duplicate_phones)
    duplicate_count = is_duplicate.sum()
    
    filtered_copy_df = copy_df[~is_duplicate]

    # Save the filtered copy DataFrame to a new CSV file
    filtered_copy_df.to_csv(output_file, index=False)

    # Print the number of duplicate rows found
    print(f"Number of duplicate rows found and removed: {duplicate_count}")

# Adjust the file paths as needed
main_csv = 'd:/Whatsapp_Automation/duplicateFinder/main.csv'
copy_csv = 'd:/Whatsapp_Automation/duplicateFinder/copy.csv'
output_csv = 'd:/Whatsapp_Automation/duplicateFinder/filtered_copy.csv'

# Call the function
remove_duplicates(main_csv, copy_csv, output_csv)
