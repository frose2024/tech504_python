import requests

request_bbc = requests.get("https://www.bbc.co.uk/")
print(request_bbc.status_code)
print(request_bbc.content)

"""
import os
# returns our current working directoryworking_directory = os.getcwd()print(f"Current working directory: {working_directory}")

username = os.environ.get('USERNAME') or os.environ.get('USER')
print(f"The current user is: {username}")

cpu_cores = os.cpu_count()
print(f'Total CPU cores: {cpu_cores}')
"""


"""
import sys
# gives us the current paths important to the Python interpreterprint
(f"Current path: {sys.path}")
print(sys.version)
"""

