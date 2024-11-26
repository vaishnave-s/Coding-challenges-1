class Solution(object):
	def maxSubArray(self, nums):
			"""
			:type nums: List[int]
			:rtype: int
			"""
			def findBestSubarray(data,left,right,loop):

					if left > right:
							return None
					mid = (left+right)//2
					curr = best_left_sum = best_right_sum = 0
					curr=0
					for i in range(mid-1,left-1,-1):
							curr = curr+nums[i]
							best_left_sum = max(best_left_sum,curr)

					curr=0
					for j in range(mid+1,right+1,1):

							curr = curr+nums[j]
							best_right_sum = max(best_right_sum,curr)
					best_combined_sum = best_right_sum + best_left_sum + nums[mid]
					left_part = findBestSubarray(nums,left,mid-1,"left")
					right_part = findBestSubarray(nums,mid+1,right,"right")
					return max(best_combined_sum,left_part,right_part)
			return findBestSubarray(nums,0,len(nums)-1,"main")