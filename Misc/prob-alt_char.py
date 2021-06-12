# Given 2 strings A and B, return a string in which characters from A and B are filled alternatively in order same as in original strings beginning with a character from A, example A = “Hello”, B= “Bye” then output should be “HBeylelo”. (|A|,|B|<25000)

A="Hello"
B="Bye"
if len(A)>len(B):
  g=A
  s=B
else:
  g=B
  s=A

ls = []
for i in range(0,len(s)):
  ls.append(g[i])
  ls.append(s[i])

for i in range(len(s),len(g)):
  ls.append(g[i])
print(ls)
