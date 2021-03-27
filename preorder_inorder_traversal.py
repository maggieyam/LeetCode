class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:        
        def helper(left, right):
            nonlocal pre_idx
            
            if left >= right: return None
            
            value = preorder[pre_idx]
            root = TreeNode(value)
   
            pre_idx += 1

            root.left = helper(left, index_map[value])        
            root.right = helper(index_map[value] + 1, right)

            return root
        
        pre_idx = 0
        index_map = {val: i for i, val in enumerate(inorder)}
        
        return helper(0, len(inorder))