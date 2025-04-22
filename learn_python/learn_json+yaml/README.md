# Comparing JSON and YAML

## JSON:
```json
{
  "name": "John Doe",
  "age": 30,
  "isStudent": false,
  "courses": ["Python", "DevOps"],
  "address": {
    "street": "123 Main St",
    "city": "Anytown"
  }
}
```
* Lists - uses [ ]
* Dictionaries - uses { }
* Commas used inbtwn list and dictionary items to split them up. 
* JSON wraps keys and string values in double quotes


## YAML:
```yaml
name: John Doe
age: 30
isStudent: false
courses:
  - Python
  - DevOps
address:
  street: 123 Main St
  city: Anytown
```
* Lists - start with hyphens
* No double quotes anywhere
* Consistent indenting is very very important. 