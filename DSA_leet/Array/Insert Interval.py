class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        allIntervals=intervals
        allIntervals.append(newInterval)
        allIntervals.sort()
        stack = [allIntervals[0]]
        for i in range(1,len(allIntervals)):
            if stack[-1][-1]>=allIntervals[i][0]:
                stack[-1][-1] = max(stack[-1][-1],allIntervals[i][1])
            else:
                stack.append(allIntervals[i])
        return(stack)
