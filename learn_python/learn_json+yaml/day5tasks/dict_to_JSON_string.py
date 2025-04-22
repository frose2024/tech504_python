# Goal is to convert a specific Python dictionary into a JSON-formatted string

# Import the dictionary in question.
import servers_dictionary

import os
import json
import sys


# Based on what the user inputs as the first argument, execute either of the below options

# Function that contains the JSON string code.
def dict_to_json_string():
    target = servers_dictionary.servers_dict
    print(target)


# Function that contains the JSON file code.
def dict_to_json_file():
    target = servers_dictionary.servers_dict

    f = open("JSONfile.json", "w")
    json.dump(target, f)
    f.close()


# What does this nonsense looking line do? Tells Python to only run this block of code if this file is the main script, not an import.
    # Importing a script that's based on command line arguments is likely to end in tears.
if __name__ == "__main__":

    if len(sys.argv) <= 1:
        print("You need to specify which version you want to run - string or file.")

    elif sys.argv[1] == "string":
        dict_to_json_string()

    elif sys.argv[1] == "file":
        dict_to_json_file()

