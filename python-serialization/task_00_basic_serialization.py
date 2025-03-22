import json

def serialize_and_save_to_file(data, filename):
	with open('data.json', 'w') as filename:
		json.dump(data, filename)

def load_and_deserialize(filename):
	with open('data.json', 'r') as filename:
		return json.load(filename)
