import csv
import json

def convert_csv_to_json(csv_filename):
	try:
		with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
			reader = csv.DictReader(csv_file)
			data = list(reader)

		with open('data.json', mode='w', encoding='utf-8') as json_file:
			json.dump(data, json_file, indent=2)

		return True
	
	except FileNotFoundError:
		print(f'Error: {csv_filename} not found.')
		return False
	except Exception as exception:
		print(f'Unexpected error: {exception}')
		return False