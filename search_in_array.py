class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def isSorted(left, right):
            if left <= right:
                return True
            return False
        
        index = 0
        while len(nums) > 1:
            mid = len(nums) // 2
            if nums[mid] == target:
                return index + mid
            elif nums[mid] < target:
                if (isSorted(nums[mid], nums[-1]) and target > nums[-1]):
                    nums = nums[:mid]                    
                else:
                    index += mid + 1
                    nums = nums[mid + 1:]
                    
            else:
                if (isSorted(nums[0], nums[mid]) and target >= nums[0]) or not isSorted(nums[0], nums[mid]):
                    nums = nums[:mid]
                else:
                    nums = nums[mid + 1:]
                    index += mid + 1
                            
        
        if len(nums) == 1 and nums[0] == target:
            return index
        
        return -1
        