import requests

post_codes_req = requests.get("https://api.postcodes.io/postcodes/pr30sg")

print(post_codes_req)

print(post_codes_req.status_code)
print(post_codes_req.headers)
print(post_codes_req.content)
print(post_codes_req.json())

# Can see how we can take this response and turn it into new files/Python dictionaries.


# Getting confused again with accessing dictionaries, need to practice this more. First bracket tells you
#   that we're trying to get to the "result" dictionary in the json response, "region" says we're trying to get
#   the value of the "region" key.
print(post_codes_req.json()["result"]["region"])


# What is pretty printing? Is that a technical term?
#   print(json.dumps(postcodes_req.json(), indent=4))