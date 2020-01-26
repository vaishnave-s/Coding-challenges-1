pos = 0
l = [1,23,4,7]
n = 1
def binary_search(lis,num):
  #ALWAYS START WITH SORTED LIST
  lis.sort()
  print("The sorted list is ",lis)
  lb = 0
  ub = len(lis)-1
  while lb <= ub:
    mb = (lb + ub)//2
    if lis[mb]==num:
      globals()['pos']=mb
      return True
    elif lis[mb]>num:
      ub=mb-1
    else:
      lb=mb+1
  return False
if binary_search(l,n):
  print("Found at index:",pos)
else:
  print("Not found")