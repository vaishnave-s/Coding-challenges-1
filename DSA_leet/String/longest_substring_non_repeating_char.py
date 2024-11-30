class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxL = 0
        start=0
        char_set = set()
        for end in range(len(s)):
            while s[end] in char_set:
                char_set.remove(s[start])
                start+=1
            char_set.add(s[end])
            maxL=max(maxL,end-start+1)
        return maxL
