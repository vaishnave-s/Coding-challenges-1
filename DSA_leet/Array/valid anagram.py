from typing import List
class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		if len(s)!=len(t):
			return False
		countS,countT = {},{}
		for i in range(len(s)):
			countS[s[i]] = 1+countS.get(s[i],0)
			countT[t[i]] = 1+countT.get(t[i],0)
		print(countS,countT)
		if countS != countT:
			return False
		return True




s = Solution()
print(s.isAnagram("anagram","nagaram"))