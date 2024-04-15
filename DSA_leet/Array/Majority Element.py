class Solution:
	def majorityElement(self, nums: List[int]) -> int:
			exp_count = int(len(nums)/2)
			hashMap = {}
			for i in nums:
					hashMap[i] =  hashMap.get(i,0)+1
			for k,v in hashMap.items():
					if v>exp_count:
							return k


