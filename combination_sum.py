class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:          
        candidates.sort()
        res = []
        def combinationSumHelper(idx, combs, combSum):  
            if combSum == target:                    
                res.append(combs)
                return 
                   
            for i in range(idx, len(candidates)):
                candidate = candidates[i]                                             
                if combSum + candidate <= target:
                    combinationSumHelper(i, combs + [candidate], combSum + candidate)                    
                else:
                    break
                                    
        combinationSumHelper(0, [], 0)
        return res