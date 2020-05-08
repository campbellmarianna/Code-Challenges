import json

json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, "e":5}'

parsed_json = (json.loads(json_data))
print(json.dumps(parsed_json, indent=4, sort_keys=True))

loaded_json = json.loads(json_data)
for x in loaded_json:
    print("%s: %d" % (x, loaded_json[x]))

# Parse To An Object
class Test(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)

test1 = Test(json_data)
print(test1.a)

# Parse a JSON File
with open('distros.json', 'r') as f:
    distros_dict = json.load(f)

for distro in distros_dict:
    print(distro['Name'])

# It's really not hard to parse JSON in Python. By using the json.load methods, you can convert the JSON into a dictionary. That dictionary can be used as a dictionary, or it can be imported into an object as it's instantiated to transfer data into a new object.

# Exercises
# Create a new Python file an import JSON
# Crate a dictionary in the form of a string to use as JSON
# Use the JSON module to convert your string into a dictionary.
# Write a class to load the data from your string.
# Instantiate an object from your class and print some data from it.
# Create a JSON file with some JSON in it.
# Import your JSON file into Python and iterate over the resulting data.

# Credits
# - https://linuxconfig.org/how-to-parse-data-from-json-into-python
