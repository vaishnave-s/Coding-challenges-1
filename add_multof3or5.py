
def add_multiples_3and5(limit):
  s=0

  while(limit!=0):

    if (limit%3 ==0 or limit%5 == 0):
      s = s + limit
      limit=limit-1

    else:

      limit=limit-1
  print(s)
add_multiples_3and5(15)