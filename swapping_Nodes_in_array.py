class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        
        curr = head
        back = head
        front = head
        count = 1
        while curr.next:
            curr = curr.next 
            count += 1
            if count > k:
                back = back.next
            else:
                front = front.next
                
        temp = front.val
        front.val = back.val
        back.val= temp
        
        return head