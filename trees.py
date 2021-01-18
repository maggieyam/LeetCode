def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def maxDepthHelper(count, root):
            count1, count2 = count, count           
            if root.left:
                count1 = maxDepthHelper(count + 1, root.left)
            if root.right:
                count2 = maxDepthHelper(count + 1, root.right)
            
            return max(count1, count2)
            
            
        count = 1
        return maxDepthHelper(1, root)

def isValidBST(self, root: TreeNode) -> bool:        
    def isValidBSTHelper(root, low, high):
        if not root:
            return True
        
        if root.val >= high or root.val <= low:
            return False
        
        return isValidBSTHelper(root.left, low, root.val) and isValidBSTHelper(root.right, root.val, high)
    
    return isValidBSTHelper(root, -math.inf, math.inf)