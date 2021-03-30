class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        if root.val == targetSum and not root.left and not root.right:
            return [[root.val]]
        
        left = self.pathSum(root.left, targetSum - root.val)
        right = self.pathSum(root.right, targetSum - root.val)
       
        res = []
        if left:
            for arr in left:
                res.append([root.val] + arr)
                
        if right:
            for arr in right:
                res.append([root.val] + arr)
        
        return res