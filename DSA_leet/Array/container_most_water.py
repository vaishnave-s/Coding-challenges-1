class Solution:
    def maxArea(self, height: List[int]) -> int:
        low=0
        high = len(height)-1
        max_area=0
        while low<high:
            # print(height[low],height[high])
            area = (high-low)*min(height[high],height[low])
            max_area=max(max_area,area)
            if height[low]>height[high]:
                high-=1
            else:
                low+=1
        return(max_area)
