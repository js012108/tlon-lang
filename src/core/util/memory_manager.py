from src._common._structures import *

class MemoryManager:
	"""docstring for MemoryManager"""

	memory_stack = None

	def __init__(self):
		self.memory_stack = []
		main_mem = Memory('MAIN')
		self.memory_stack.append(main_mem)

	def exists(self, name):
		i = len(self.memory_stack) - 1
		while i >= 0:
			memory = self.get_memory(i)
			if memory.exists(name):
				return True
			i -= 1

		return False

	def find(self, name):
		i = len(self.memory_stack) - 1
		while i >= 0:
			memory = self.get_memory(i)
			if memory.exists(name):
				return memory.find(name)
			i -= 1

		return None

	def assign(self, name, value):
		item = self.find(name)

		if item is not None:
			item.value = value
		else:
			if len(name) == 1:
				local_mem = self.memory_stack[-1]
				name = str(name[0])
				item = Variable(name, 'any', value)
				local_mem.assign(name, item)
			else:
				parent = self.find(name[:len(name) - 1])
				child_name = name[-1]
				item = Variable(child_name, 'any', value)

				if type(value) is Variable:
					item = value

				parent.value[child_name] = item

	def get_memory(self, index):
		if index < 0 or index >= len(self.memory_stack):
			raise Exception('Index not valid.')

		return self.memory_stack[index]

	def add_memory(self, name, params = {}):
		if type(params) is not dict:
			raise Exception('Error: typeof \'params\' is not dict')

		local_memory = Memory(name, params)

		self.memory_stack.append(local_memory)

		return local_memory

	def pop_memory(self):
		return self.memory_stack.pop()

	def peek_memory(self):
		return self.memory_stack[-1]

	def size(self):
		return len(self.memory_stack)