import json
from pathlib import Path

# reading the complete content of json file
def parse_json_file_and_read_data(json_path):
    print(json_path)
    if Path(json_path).exists():
        try:
            with open(json_path, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Invalid JSON format.")
            
    
