#Count consonents in string
#Iterative approach
def count_consonents(text):
    vowels = 'aeiou'
    count = 0
    for i in text:
        if i not in vowels:
            count += 1
    return count


print(count_consonents("hello"))


#Recursive approach
def count_consonents_rec(text, ind=0):
    vowels = 'aeiou'
    if text == '':
        return 0
    if text[0].lower() not in vowels and text[0].isalpha():
        return 1 + count_consonents_rec(text[1:])
    else:
        return count_consonents_rec(text[1:])


print(count_consonents_rec("hello"))
