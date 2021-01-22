class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLowestIndex(idx, indices):
            while(nums[idx] == target and (indices[0] == -1 or idx <= indices[0])):
                indices[0] = idx
                idx -= 1
                if idx < 0: 
                    break           
        
        def findHighestIndex(idx, indices):
            while nums[idx] == target and idx >= indices[1]:
                indices[1] = idx
                idx += 1                  
                if idx >= len(nums):
                    break
                        
        
        def searchHelper(subNums, target, indices, offset):
            mid = len(subNums) // 2
            if not subNums:
                return

            if subNums[mid] > target: 
                searchHelper(subNums[:mid], target, indices, offset) 
            elif subNums[mid] < target:                
                searchHelper(subNums[mid + 1:], target, indices, offset + mid + 1)                 
            else:                
                findLowestIndex(mid + offset, indices)     
                findHighestIndex(mid + offset, indices)
        
        indices = [-1, -1]
        searchHelper(nums, target, indices, 0)
        return indices