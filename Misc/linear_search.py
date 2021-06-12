l = [5,6,8,9,10]
num=10

def search(lis,number):
  counter = 0
  while counter < len(lis):
    if lis[counter]==number:
      # print(list[counter])
      print("Found here")
      return True;
      counter = counter + 1
  return False;




# search(l,num)
if search(l,num):
  print("Found")
else:
  print("Not found")