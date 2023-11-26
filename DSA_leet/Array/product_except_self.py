class Solution(object):
	def productExceptSelf(self, nums):
			"""
			:type nums: List[int]
			:rtype: List[int]
			"""
			res = [1]*len(nums)
			prefix = 1 
			postfix = 1
			#iterate start to end of array
			#eg [1,2,3,4] => res = prefix * array value at i = 
			#[1=1,1*1=1,1*2=2,2*3=6]
			for i in range(len(nums)):
					res[i] = prefix
					prefix *= nums[i]
			#iterate end to start of array
			#eg [1,2,3,4] => res = postfix (prev postfix * array value at i) * result value at i =
			#[24=(12*2)*1,12=(4*3)*1,8=(1*4)*2,6=(1=1)*6]]
			for i in range(len(nums)-1,-1,-1):
					res[i] *= postfix
					postfix *= nums[i]
			return res
