class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            if i == 0 or n not in nums[-i:]:
                perms = self.permuteUnique(nums)
                for perm in perms:
                    res.append([n] + perm)
            nums.append(n)
        return res