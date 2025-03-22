import pickle

class CustomObject:
	def __init__(self, name:str, age:int, is_student:bool):
		self.name = name
		self.age = age
		self.is_student = is_student

	def display(self):
		print(f'Name: {self.name}')
		print(f'Age: {self.age}')
		print(f'Is student: {self.is_student}')

	def serialize(self, filename):
		try:
			with open(filename, 'wb') as file:
				pickle.dump(self, file)
		except Exception as exception:
			print(f'Serialization error: {exception}')

	@classmethod
	def deserialize(cls, filename):
		try:
			with open(filename, 'rb') as file:
				obj = pickle.load(file)
				if isinstance(obj, cls):
					return obj
				else:
					print('Not a CustomObject')
					return None
		except (FileNotFoundError, pickle.UnpicklingError, EOFError) as error:
			print(f'Deserialization error: {error}')
			return None