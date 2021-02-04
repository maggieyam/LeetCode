class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def isSubInterval(inner, outer):
            return outer[0] <= inner[0] and inner[1] <= outer[1]
        
        def isOverlapped(left, right):
            return (right[0] > left[0] and left[1] < right[1]) or right[0] == left[1] 
        
        merged = []
        for i, interval in enumerate(intervals):
            if isSubInterval(newInterval, interval):
                return intervals
            
            elif newInterval[1] < interval[0]:
                merged.append(newInterval)
                return merged + intervals[i:]
            
            elif interval[1] < newInterval[0]:
                merged.append(interval)
                
            elif isOverlapped(newInterval, interval) or isOverlapped(interval, newInterval):
                start = min(interval[0], newInterval[0])
                end = max(interval[1], newInterval[1])
                newInterval = [start, end]                 
                
        merged.append(newInterval)
        return merged