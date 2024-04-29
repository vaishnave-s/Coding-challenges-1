class Solution:
	def sortedSquares(self, nums: List[int]) -> List[int]:
			n = len(nums)
			left = 0
			right = n-1
			result = [0]*n
			for i in range(n-1,-1,-1):
					if abs(nums[left])< abs(nums[right]):
							sq = nums[right]
							right-=1
					else:
							sq = nums[left]
							left+=1
					square = sq*sq
					result[i] = square
			return result


num = [-4,-1,0,3,10]

s = Solution()
print(s.sortedSquares(num))