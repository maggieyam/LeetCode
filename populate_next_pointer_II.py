class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        leftmost = root
        
        while leftmost:
            prev = leftmost
            curr, leftmost = None, None
            
            while prev:
                curr, leftmost = self.traverse(curr, leftmost, prev.left)
                curr, leftmost = self.traverse(curr, leftmost, prev.right)
                prev = prev.next
        return root
    
    def traverse(self, curr, leftmost, prev):
        if not prev:
            return curr, leftmost
        
        if leftmost:
            curr.next = prev
            curr = prev
        else:
            leftmost, curr = prev, prev
       
        return curr, leftmost