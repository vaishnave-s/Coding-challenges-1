"""
Stack Data Structure.
Last in, first out
"""
class Stack():

	def __init__(self):
		self.items = []

	def push(self,item):
		self.items.append(item)
	
	def pop(self):
		last_v=self.items.pop()
		print("{} is removed".format(last_v))
		return last_v
	
	def get_stack(self):
		return self.items
	
	def peek(self):
		return self.items[-1]
	
	def is_empty(self):
		return self.items == []

# st = Stack()
# st.push(1)
# st.push(2)
# st.push(4)
# st.pop()
# print(st.get_stack())
# print(st.peek())
# print(st.is_empty())

