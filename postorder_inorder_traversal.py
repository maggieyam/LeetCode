class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(left, right):
            if left >= right: return None
            
            nonlocal post_idx
            value = postorder[post_idx]
            root = TreeNode(value)
            
            post_idx -= 1
            root.right = helper(inorder_map[value] + 1, right)
            root.left = helper(left, inorder_map[value])
            
            return root
            
        post_idx = len(postorder) - 1
        inorder_map = {val:i for i, val in enumerate(inorder)}

        return helper(0, len(inorder))