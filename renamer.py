import json
import os
import sys

def rename_files(json_path, target_directory):
    # Load the JSON mapping
    try:
        with open(json_path, 'r') as f:
            mapping = json.load(f)
    except FileNotFoundError:
        print(f"Error: {json_path} not found.")
        return

    # Check every file in the folder
    for filename in os.listdir(target_directory):
        if filename in mapping:
            new_name = mapping[filename]
            
            old_path = os.path.join(target_directory, filename)
            new_path = os.path.join(target_directory, new_name)
            
            # Perform the rename
            os.rename(old_path, new_path)
            print(f" Renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python renamer.py <json_file> <directory>")
    else:
        rename_files(sys.argv[1], sys.argv[2])