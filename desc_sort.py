ls = [3,5,7,6]
old_list = list(ls)
new_list = []
while old_list:
  maximum = old_list[0]
  for i in old_list:
    if i > maximum:
      maximum = i
  new_list.append(maximum)
  old_list.remove(maximum)
print(ls)
print(new_list)

# # To find the biggest possible number from the list of numbers
# for i in new_list:
#   print(i,end="")