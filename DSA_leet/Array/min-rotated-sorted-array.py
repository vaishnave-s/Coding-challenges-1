class Solution(object):
	def findMin(self, nums):
			"""
			:type nums: List[int]
			:rtype: int
			"""
			def helper(ls,left,right):
					if left == right:
							return ls[left]
					mid = (left+right)//2
					if ls[mid]>ls[right]:
							return helper(ls,mid+1,right)
					else:
							return helper(ls,left,mid)
			return(helper(nums,0,len(nums)-1))
