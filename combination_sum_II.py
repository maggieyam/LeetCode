class Solution:    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def findCombination(idx, combSum, combs):
            if combSum == target:
                if combs not in res:
                    res.append(combs)
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if combSum + candidates[i] <= target:
                    findCombination(i + 1, combSum + candidates[i], combs + [candidates[i]])
                else:
                    break
        findCombination(0, 0, [])
        return res
    