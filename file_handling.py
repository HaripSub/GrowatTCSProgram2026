import json
import os

# Ensure data.json exists with valid content
data_file = 'data.json'

# Check if file exists and is not empty
if not os.path.exists(data_file) or os.path.getsize(data_file) == 0:
    print(f"Creating {data_file}...")
    initial_data = {'name': 'Alice', 'age': 25}
    with open(data_file, 'w') as file:
        json.dump(initial_data, file, indent=2)
    print(f"{data_file} created successfully!")

# Now read the JSON file
try:
    with open(data_file, 'r') as file:
        data = json.load(file)
    print(f"Read from {data_file}: {data}")
except json.JSONDecodeError as e:
    print(f"Error reading {data_file}: {e}")
    data = {'name': 'Default', 'age': 0}

# Write to output.json
output_data = {'name': 'Alice', 'age': 25}
with open('output.json', 'w') as file:
    json.dump(output_data, file, indent=2)
print("Wrote to output.json successfully!")

# String to object
json_string = '{"name": "Bob"}'
parsed_data = json.loads(json_string)
print(f"Parsed JSON string: {parsed_data}")

