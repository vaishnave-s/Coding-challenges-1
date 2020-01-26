import array as arr


def  reversingAnArray(start, end, myArray):
    while(start < end):
        myArray[start], myArray[end - 1] = myArray[end - 1], myArray[start]
        start += 1
        end -= 1


myArray = arr.array('i',[4,5,7,9,4])

print('Array before Reversing:',myArray)
reversingAnArray(0, len(myArray), myArray)
print('Array after Reversing:',myArray)
# for i in range (0, len(myArray)): 
#   print (myArray[i], end =" ") _