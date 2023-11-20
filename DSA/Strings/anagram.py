#is anagram
s1 = "fairy tales"
s2 = "rail safety"
def is_anagram(s1,s2):
	ls=[]
	if len(s1)!=len(s2):
		return False
	for i in s1:
		ls.append(i)
	for i in s2:
		if i in ls:
			ls.remove(i)
	if len(ls)==0:
		return True
	else:
		return False

print(is_anagram(s1,s2))