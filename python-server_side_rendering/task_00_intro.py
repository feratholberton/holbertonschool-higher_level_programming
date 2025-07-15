import os

def generate_invitations(template, attendees):
	# Check types
	if not isinstance(template, str):
		print(f'Error: {type(template).__name__}.')
		return
	if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
		print('Error: not a dictionary')
		return
	
	# Check for empty
	if not template.strip():
		print('Template is empty')
		return
	if not attendees:
		print('No data provided')
		return

	# Write files
	for idx, attendee in enumerate(attendees, start=1):
		filled_template = template

		for placeholder in ['name', 'event_title', 'event_date', 'event_location']:
			value = attendee.get(placeholder)
			filled_template = filled_template.replace(
				f'{{{placeholder}}}', str(value) if value else 'N/A'
			)

		filename = f'output_{idx}.txt'
		try:
			with open(filename, 'w', encoding='utf-8') as file:
				file.write(filled_template)
			print(f'Generated: {filename}')
		except Exception as exception:
			print(f'Failed to write {filename}: {exception}')