class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        biggest = 0
        secondBiggest = 0
        for num in nums:
            if num>biggest:
                secondBiggest = biggest
                biggest = num
            else:
                secondBiggest = max(secondBiggest,num)
        return (secondBiggest-1)*(biggest-1)
