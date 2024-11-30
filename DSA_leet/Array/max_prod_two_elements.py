class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def sorting(arr):
            # print(arr)
            if len(arr)<=1:
                return arr
            
            pivot = arr[len(arr)//2]
            left_half=[x for x in arr if x < pivot]
            right_half=[x for x in arr if x > pivot]
            middle = [x for x in arr if x==pivot]
            return sorting(left_half)+middle+sorting(right_half)
        s = sorting(nums)
        print(s)
        return (s[-1]-1)*(s[-2]-1)
