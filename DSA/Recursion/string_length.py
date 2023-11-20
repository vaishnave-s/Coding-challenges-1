#String length
#Iterative approach
def string_length(text):
	count=0
	for i in text:
		count+=1
	return count

print(string_length("text"))

#Recursive approach

def string_length_rec(text):
	if text == '':
		return 0
	# print(text[1:])
	return 1 + string_length_rec(text[1:])		
	
print(string_length_rec("text"))
		