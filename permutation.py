class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []  
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            remainNums = self.permute(nums)
            for num in remainNums:
                res.append([n] + num)
            nums.append(n)
        return res