string = "pneumonoultramicroscopicsilicovolcanoconiosis"
# pneumonoultramicroscopicsilicovolcanoconiosis
list_str = list(string.lower())
def CountFrequency(my_list): 
  
    # Creating an empty dictionary  
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    return freq




        
print(CountFrequency(list_str))
  