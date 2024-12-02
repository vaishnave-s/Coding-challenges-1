class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        vals=None
        for i in range(1,len(strs)):
            low=0
            high=1
            print(i,strs[i-1],strs[i])
            main =set()
            while low<high and low<= len(strs[i]) and high <= len(strs[i]):
                if strs[i-1][low:high] == strs[i][low:high]:
                    print(strs[i-1][low:high])
                    main.add(strs[i-1][low:high])
                    high+=1
                else:
                    break
            print(main)
            if main != set():
                if not vals:
                    vals=main
                else:
                    vals = vals.intersection(main)
            else:
                return ""
            
        max_val=""
        for i in vals:
            max_val = i if len(i) > len(max_val) else max_val
        return max_val

