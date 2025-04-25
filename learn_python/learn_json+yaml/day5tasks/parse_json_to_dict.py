import json
import sys

with open("servers.json", "r") as file:
    content = file.read()

    # json.loads is a JSON module method, converts a JSON string to a Python dict
    servers = json.loads(content)
    print(type(servers))

    # Print dictionary key "server1"
    print(servers.get("server1"))

    # Print dictionary key "server2"
    print(servers.get("server2"))

    # Print all the keys and values
    print(servers.values())

    # Print out formatted keys and sub-keys
        # Outer loop that prints the outer keys
    for server_key, server_info in servers.items():
        print(f"Key and value: '{server_key}' = {server_info}")
        # Inner loop that prints the sub keys.
        for record_key, record_info in server_info.items():
            print(f"   Record key and sub value: '{record_key}' = '{record_info}'")


        # Above code works b/c .items() returns all the keys and all the values from a dictionary.
        #   I've told the interpreter to store the outer keys in server_key and outer info in server_info in the outer loop.
        #   Inner loop does the same thing.
