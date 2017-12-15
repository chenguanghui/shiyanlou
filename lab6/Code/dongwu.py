class Dog(object):
	"""docstring for Dog"""
	def __init__(self, name):
		self._name = name
	def get_name(self):
		return self._name
	def set_name(self, value):
		self._name = value
	def bark(self):
		print(self.get_name() + 'is marking sound wang wang wang...')

class Cat(object):
	"""docstring for Cat"""
	def __init__(self, name):
		self._name = name
	def get_name(self):
		return self._name
	def set_name(self, value):
		self._name = value
	def mew(self):
		print(self.get_name() + 'is marking sound miu miu miu...')