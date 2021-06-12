ls = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []
data_list = list(ls)

while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print(ls)
print(new_list)