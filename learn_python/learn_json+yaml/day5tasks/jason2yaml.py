import json
import os
import sys
import yaml

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json> <target_file.yaml>")

# Convert the JSON to YAML
yaml_data = yaml.dump(source_content, default_flow_style=False)

# Saving the YAML to a new file, or just printing it if no file name given.

# Check target file name was specified
if len(sys.argv) < 3:
    print(yaml_data)
else:
    target_file_path = sys.argv[2]

# Check that given file name doesn't already exist. Done using os.path.exists
    if os.path.exists(target_file_path):
        print("Error, that file already exists.")

# Using "with" and "as" syntax b/c that opens and closes the file for you.
with open(target_file_path, "w") as target_file:
    target_file.write(yaml_data)
print(f"YAML successfully written to {target_file_path}")



