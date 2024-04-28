from typing import List

class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
			swap_index = 0
			for i in range(len(nums)):
					if nums[i] != 0:
							nums[swap_index],nums[i] = nums[i],nums[swap_index]
							swap_index+=1
			return nums

arr = [1,0,3,0,12]

s = Solution()
print(s.moveZeroes(arr))