class Solution:
    from collections import defaultdict 
    
    def minSetSize(self, arr: List[int]) -> int:
        def isEven(n):
            return n % 2 == 0
        
        length = len(arr) 
        nums = defaultdict(int)
        
        for num in arr:
            nums[num] += 1
        
        counts = list(nums.values())
        counts.sort()
        
        target = length // 2 if isEven(length) else length // 2 + 1
        
        n = 0
        while target > 0:
            target -= counts.pop(-1)
            n += 1
            
        return n
        