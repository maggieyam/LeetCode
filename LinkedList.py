
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #edge case: one node
    if not head.next:
        head = None
        return head
    
    #find the length
    length = 0
    curr = head
    while curr:
        length += 1
        if not curr.next:
            break
        curr = curr.next    
    
    if length == n:
        curr = head
        head = head.next
        curr.next = None
        return head
    
    curr = head        
    for i in range(length - n - 1):          
        curr = curr.next

    next = curr.next
    curr.next = next.next
    next.next = None
    
    return head

def reverseList(self, head: ListNode) -> ListNode:
        prev = head
        if not head or not head.next:
            return head
        curr = head.next
        if not curr.next:
            curr.next = head
            head.next = None
            head = curr
            return head
        next_node = curr.next
        curr.next = prev
        head.next = None
        
        while next_node.next:
            prev = curr
            curr = next_node
            next_node = next_node.next
            curr.next = prev
        next_node.next = curr
        head = next_node
        return head

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:      
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val <= l2.val:
            curr1 = l1
            curr2 = l2
        else:
            curr2 = l1
            curr1 = l2
        head = curr1
                   
        while curr1.next:
            prev = curr1.next
            if curr1.val <= curr2.val and prev.val > curr2.val:
                curr1.next = curr2
            if curr2.val < prev.val:
                curr1 = curr2
                curr2 = prev
            else:
                curr1 = prev
        curr1.next = curr2
        return head

if __name__ == '__main__':
    main()
    