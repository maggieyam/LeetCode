"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
# 1. traverse to next node until child is not null
# 2. flatten nodes
    # a. Set a pointer at node.next, 
    # b. save the pointer to an array, 
    # c. node.next = child, 
    # d. child = null
# 3. Reapeat untill hits the end.
# 4. pop pointers from the array
    
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        curr = head
        arr = []
        
        while curr:
            while not curr.child and curr.next:
                curr = curr.next
            if not curr.child:
                break
            if curr.next:
                arr.append(curr.next)
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
            curr = curr.next            
                
        while arr:
            nextNode = arr.pop(-1)
            curr.next = nextNode
            nextNode.prev = curr
            while curr.next:
                curr = curr.next
        
        return head
                 