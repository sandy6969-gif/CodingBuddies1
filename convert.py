import json

# Input file path
input_file_path = 'mem.json'

# Read the first 5 lines of the JSON file
with open(input_file_path, 'r', encoding='utf-8') as json_file:
    # Read the first 5 lines of the file
    first_5_lines = [json_file.readline() for _ in range(5)]

# Join the lines and load as JSON
json_content = ''.join(first_5_lines)
try:
    jsondata = json.loads(json_content)
    print(json.dumps(jsondata, indent=2))  # Print the JSON with indentation
except json.JSONDecodeError as e:
    print(f'Error decoding JSON: {e}')

# Rest of the script for CSV conversion (if needed)
if isinstance(jsondata, list) and all(isinstance(item, dict) for item in jsondata):
    # Continue with the CSV conversion logic
    pass
