class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        flattened = [root]
        res = []
        while flattened:
            node = flattened.pop()
            res.append(node)
            if node.right:
                flattened.append(node.right)
            if node.left:                
                flattened.append(node.left)

        for i, node in enumerate(res):
            node.left = None
            if i == len(res) - 1: break
            node.right = res[i + 1]
            
        return root