class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        curr = root
        leftmost = curr.left
        
        while leftmost:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
                curr = curr.next
            else:
                curr = leftmost
                leftmost = leftmost.left
        
        return root