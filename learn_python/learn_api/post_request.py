import requests
import json

json_body = json.dumps({ "postcodes" : ["pr30sg", "so239jg", "m456gn"]})
headers = {"Content-Type" : "application/json"}

bulk_post_codes_request = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(bulk_post_codes_request)

print(bulk_post_codes_request.json())