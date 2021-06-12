string = "ccooell"
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
    # return freq

    for k,v in freq.items():
      if v ==1:
        for i in range(0, len(list_str)):
          if k == list_str[i]:
            return k
      
    return "There is no non-repeating value"



        
print(CountFrequency(list_str))
  