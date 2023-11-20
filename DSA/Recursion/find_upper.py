#Find Uppercase Letter in String
#Iterative approach
def find_upper(text):
	for i in text:
		if i.isupper():
			return i
		else:
			None


print(find_upper("helloworld"))


#Recursive approach
def find_upper_rec(text,ind=0):
	if text[ind].isupper():
		return text[ind]
	if ind==len(text)-1:
		return None
	return find_upper_rec(text,ind+1)

		
print(find_upper_rec("helloWorld"))
