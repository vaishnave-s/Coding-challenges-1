#GS INTERVIEW TEST DATE - 26.01.20
# you will be given a value x and a range y to z.
# the digits in x should not be the same as the digits in x multiplied by iterating over the range y to z. i.e x=2,y=10,z=12
# n=10 => 2*10=20 invalid
# n=11 => 2*11=22 valid
# n=12 => 2*12=24 invalid
import math

def nonrep(x,y,z):
  count=0
  if x < math.pow(10,5) and y < math.pow(10,5) and z < math.pow(10,5):
    for n in range(y,z+1):
      list_n = list(str(n))
      mulxn = x*n
      list_mulxn = list(str(mulxn))

      countlist = []

      for i in range(len(list_mulxn)):

        if list_mulxn[i] not in list_n:
          countlist.append("NF")
      if len(countlist) == len(list_mulxn):
        count+=1
        # print(countlist)
            # countlist.append(list_n)

    return count
  else:
    return "Invalid inputs. Please give a value below 10^5"

print(nonrep(2,20,25))
