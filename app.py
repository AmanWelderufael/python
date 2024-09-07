import json
import yaml

# load YAML from the file
with open('users.yml', 'r') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

# convert the yaml data to JSon
json_data = json.dumps(yaml_data, indent=4)

# Write the json data file into a new file
with open('user.json', 'w') as json_file:
    json_file.write(json_data)

print("YAML data has been converted to JSON and saved as 'users.json'.")


