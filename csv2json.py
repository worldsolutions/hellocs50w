import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Initialize an empty list to store the data
    data = []
    
    # Read the CSV file
    with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
        # Create a CSV reader object that ignores spaces after delimiters
        csv_reader = csv.DictReader(csv_file, skipinitialspace=True)

        # Convert each row to a dictionary and append to data list
        for row in csv_reader:
            # Filter out invalid columns (e.g., from trailing commas)
            clean_row = {k: v for k, v in row.items() if k is not None}
            data.append(clean_row)
    
    # Write to JSON file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        # Write the data to JSON file with proper formatting
        json.dump(data, json_file, indent=4)

# Example usage
csv_file_path = 'ccstests.csv'  # Replace with your CSV file path
json_file_path = 'ccstests.json'  # Replace with your desired JSON file path

try:
    csv_to_json(csv_file_path, json_file_path)
    print(f"Successfully converted {csv_file_path} to {json_file_path}")
except FileNotFoundError:
    print("Error: Input CSV file not found")
except Exception as e:
    print(f"An error occurred: {str(e)}")

