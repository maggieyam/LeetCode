class Solution:
    def isValidBST(self, root: TreeNode) -> bool:        
        def isValidBSTHelper(root, low, high):
            if not root:
                return True
            
            if root.val >= high or root.val <= low:
                return False
            
            return isValidBSTHelper(root.left, low, root.val) and isValidBSTHelper(root.right, root.val, high)
        
        return isValidBSTHelper(root, -math.inf, math.inf)