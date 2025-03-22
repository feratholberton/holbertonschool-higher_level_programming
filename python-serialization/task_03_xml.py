import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
	try:
		root = ET.Element('data')
		for key, value in dictionary.items():
			child = ET.SubElement(root, key)
			child.text = str(value)

		tree = ET.Element(root)
		tree.write(filename, encoding='utf-8', xml_declaration=True)
	except Exception as exception:
		print(f'Serialization error: {exception}')

def deserialize_from_xml(filename):
	try:
		tree = ET.parse(filename)
		root = tree.getroot()

		data = {}
		for child in root:
			data[child.tag] = child.text

		return data

	except (ET.ParseError, FileNotFoundError) as exception:
		print(f'Deserialization error: {exception}')
		return None