class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        power=0
        s=""
        num = n
        while num:
            bit = num%2
            s=str(bit)+s
            num=num>>1
        if len(s)<32:
            rem=32-len(s)
            print(rem)
            s=(rem*"0")+s
        print(s)
        for i in range(0,len(s)):
            res+=int(s[i])*pow(2,power)
            print(i,s[i],power,res)
            power+=1
        return(res)
            
