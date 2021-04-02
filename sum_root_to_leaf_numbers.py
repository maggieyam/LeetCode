    def sumNumbers(self, root: TreeNode) -> int:        
        values = {}
        sums = 0
        
        def helper(values, root, parent):            
            nonlocal sums 
            
            if not root:
                return None                       
                
            if parent:
                values[root] = values[parent] * 10 + root.val
            else:
                values[root] = root.val
                
            if root.left is None and root.right is None:
                sums += values[root]
                
            helper(values, root.left, root)
            helper(values, root.right, root)
            
        helper(values, root, None)
        return sums