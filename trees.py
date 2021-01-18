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