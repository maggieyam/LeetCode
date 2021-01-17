def nextPermutation(nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        #less than two ele
        if len(nums) < 2: 
            return nums
        
        # first strict descending number        
        last = len(nums) - 1
        idx = 0
        for i in range(last, -1, -1):
            if i == 0:
                return nums[::-1]
            else:
                if nums[i] > nums[i - 1]:
                    idx = i
                    break
          
        # the next greater number
        next = nums[idx] 
        curr = nums[idx - 1]
        idx1 = idx
        idx2 = idx - 1
        for i in range(idx, len(nums)):
            if nums[i] > curr and nums[i] < next:
                next = nums[i]
                idx1 = i
        
        # swap 
        nums[idx2], nums[idx1] = nums[idx1], nums[idx2]
        
        # reverse
        nums = nums[:idx2 + 1] + nums[idx:][::-1]
        return nums

def main():
    nums = nextPermutation([6,5,4,3,2,1])
    print(nums)

if __name__ == "__main__":
    main()