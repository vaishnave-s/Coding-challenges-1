# Find the 1st repeated word in a string. 
string = "Ravi had been saying that he had been there."
ls = string.split(' ')
ls2=[]
def repeat(ls):
  for i in range(len(ls)):
    if ls[i] not in ls2:
      ls2.append(ls[i])
    else:
      return ls[i]
print(repeat(ls))
