from typing import List
class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		prev_map={}
		for i,val in enumerate(nums):
			diff = target-val
			if diff in prev_map:
				return [prev_map[diff],i]
			prev_map[val]=i
		return 

num = [2,7,11,15]
target=9

s = Solution()
print(s.twoSum(num,target))