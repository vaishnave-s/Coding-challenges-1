#GS INTERVIEW TEST DATE - 26.01.20
# You're given a message and a key. You have to either encode or decode it.
# Encode=> 
# message="open"
# key="1234"
# o/p="oppeeennnn"
# Decode=> 
# message="oppeeennnn"
# key="1234"
# o/p="open"
# if the word is "opener", the o/p should be "oppeeennnner"


def secretcode(code,message,key):
  if code == 1: #encoding
    list_m = list(message)
    list_op = []
    # for i in range(len(list_m)):
    if len(message)>=len(key):
    
      for i in range(len(key)):

          n=int(key[i])
          while n>0:
            
            list_op.append(list_m[i]*n)
            n=n-1
            break
      if len(message)>len(key):
        list_op.append(message[len(key):len(message)])
    elif len(message)<len(key):
      for i in range(len(message)):

          n=int(key[i])
          while n>0:
            
            list_op.append(list_m[i]*n)
            n=n-1
            break
  else: #encoding
    list_m = list(message)
    list_split = []
    list_op = []

    strmess = message
    for i in range(len(key)):
          n=int(key[i])
          list_split.append(strmess[:n])
          strmess=strmess[n:]

    for i in list_split:
      list_op.append(i[0])
    list_op.append(strmess)





    

    

  return ''.join(list_op)




print(secretcode(2,"goolden","12"))