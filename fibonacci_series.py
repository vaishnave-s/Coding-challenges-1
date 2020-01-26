def fibonacci(limit):
  a=0
  b=1
  if limit==0:
    print(0)

  elif limit == 1:
    print(a)
  else:
    print(a)
    print(b)
  for i in range(2,limit):
    c=a+b
    a=b
    b=c
    print(c)
fibonacci(0)