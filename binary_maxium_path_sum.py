class Solution:
    def maxPathSum(self, root: TreeNode) -> int:  
        def helper(root):
            nonlocal maxSum
            if root is None: 
                return -inf        

            sumL = max(helper(root.left), 0)
            sumR = max(helper(root.right), 0)
            maxSum = max(sumL + sumR + root.val, maxSum)
            return max(sumL,  sumR) + root.val
        
        maxSum = -inf
        helper(root)
        return maxSum