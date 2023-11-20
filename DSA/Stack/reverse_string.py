from stacks import Stack

def reverse_string(string):
	st = Stack()
	for s in string:
		st.push(s)
	
	val=''
	reversed_str=''
	while not st.is_empty():
		val=st.pop()
		reversed_str=reversed_str+val
	return reversed_str

print(reverse_string("Hello"))

