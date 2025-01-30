# LEARN PYTHON: FILES
# Writing a JSON File
# 12/13

# Naturally we can use the json library to translate Python objects to JSON as well. This is especially useful in
# instances where you're using a Python library to serve web pages, you would also be able to serve JSON. Let's say we
# had a Python dictioanry we wanted to save as a JSON file:

# turn_to_json = {
#   'eventId': 674189,
#   'dateTime': '2015-02-12T09:23:17.511Z',
#   'chocolate': 'Semi-sweet Dark',
#   'isTomatoAFruit': True
# }

# We'd be able to create a JSON file with that information by doing the following:

# import json
#
# with open('output.json', 'w') as json_file:
#   json.dump(turn_to_json, json_file)

# We import the json module, open up a write-mode file under the variable json_file, and then use the json.dump() method
# to write to the file. json.dump() takes two arguments: first the data object, then the file object you want to save.

# ***INSTRUCTIONS***
# 1. In your workspace, we've put a dictionary called data_payload. We want to save this to a file called data.json.
#    Let's start by importing the json library
# 2. Open a new file object in the variable data_json. The filename should be 'data.json' and the file should be opened
#    in write-mode.
# 3. Call json.dump() with data_payload and data_json to convert our data to JSON and then save it to the file data.json

data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json

with open('data.json', 'w') as data_json:
    json.dump(data_payload, data_json)