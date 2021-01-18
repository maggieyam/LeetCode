
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


if __name__ == '__main__':
    main()
    